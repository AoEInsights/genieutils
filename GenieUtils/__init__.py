import os
from collections import namedtuple
import enum
from io import BytesIO
from typing import Generator

from GenieUtils.slp import SLP
from PIL import Image
import numpy as np

from . import DatFile, lang, smx
from .colors import PaletteConfig
from .smx import SMX


class UnknownValueMixin(enum.Enum):
    @classmethod
    def _missing_(cls, value):
        return cls.UNKNOWN


class UnitType(UnknownValueMixin, enum.IntEnum):
    EYE_CANDY = 10
    TREE_AOK = 15
    ANIMATED = 20
    DOPPELGANGER = 25
    MOVING = 30
    ACTOR = 40
    SUPERCLASS = 50
    PROJECTILE = 60
    COMBATANT = 70
    BUILDING = 80
    TREE_AOE = 90

    UNKNOWN = -1


Unit = namedtuple("Unit", ("id", "type", "name", "icon", "graphic", "dying_graphic", "walking_graphic", "attacking_graphic", "raw"))
Graphic = namedtuple("Graphic", ("id", "file_name", "first_frame", "frame_count", "frame_duration", "raw"))


class GenieUtils(object):
    def __init__(self, resource_dir,
                 dataset_file="_common/dat/empires2_x2_p1.dat",
                 dataset_game_version=DatFile.GV_C15,
                 palette_config_file="_common/palettes/palettes.conf",
                 graphics_dir="_common/drs/graphics",
                 strings_file="en/strings/key-value/key-value-strings-utf8.txt",
                 buildings_icons_file="_common/drs/interface/50706.slp",  # see https://www.voobly.com/forum/thread/234428
                 interface_buttons_icons_file="_common/drs/interface/50721.slp",  # see https://www.voobly.com/forum/thread/234428
                 technologies_icons_file="_common/drs/interface/50729.slp",  # see https://www.voobly.com/forum/thread/234428
                 units_icons_file="_common/drs/interface/50730.slp"  # see https://www.voobly.com/forum/thread/234428
                 ):

        # /home/kevin/.local/share/Steam/steamapps/common/AoE2DE/widgetui/textures/ingame/units

        self.resource_dir = resource_dir
        self.graphics_dir = graphics_dir
        self.buildings_icons_file = buildings_icons_file
        self.interface_buttons_icons_file = interface_buttons_icons_file
        self.technologies_icons_file = technologies_icons_file
        self.units_icons_file = units_icons_file

        self.dataset = DatFile.DatFile()
        self.dataset.setGameVersion(dataset_game_version)
        self.dataset.load(os.path.join(resource_dir, dataset_file))

        self.palette_config = PaletteConfig(os.path.join(resource_dir, palette_config_file))

        self.strings = lang.load_txt(os.path.join(resource_dir, strings_file))

    def _create_unit(self, u: DatFile.Unit) -> Unit:
        graphic_id = u.StandingGraphic[0]

        return Unit(u.ID, UnitType(u.Type), self.strings.get(u.LanguageDLLName, u.Name), u.IconID, self.graphic(graphic_id),
                    self.graphic(u.DyingGraphic), self.graphic(u.DeadFish.WalkingGraphic),
                    self.graphic(u.Type50.AttackGraphic), raw=u)

    def units(self, filter_types=None) -> Generator[Unit, None, None]:
        gaia_civ = list(self.dataset.Civs)[0]

        for u in gaia_civ.Units:
            unit = self._create_unit(u)

            if not filter_types or unit.type in filter_types:
                yield unit

    def unit(self, unit_id) -> Unit:
        gaia_civ = list(self.dataset.Civs)[0]
        units = list(gaia_civ.Units)

        unit = units[unit_id]

        return self._create_unit(unit)

    def _create_graphic(self, g: DatFile.Graphic) -> Graphic:
        return Graphic(g.ID, g.FileName, g.FirstFrame, g.FrameCount, g.FrameDuration, raw=g)

    def graphic(self, graphic_id) -> Graphic:
        graphic = list(self.dataset.Graphics)[graphic_id]

        return self._create_graphic(graphic)

    @property
    def graphics(self) -> Generator[Graphic, None, None]:
        for g in self.dataset.Graphics:
            yield self._create_graphic(g)

    def get_smx(self, graphic: Graphic):
        return SMX.from_file(os.path.join(self.resource_dir, self.graphics_dir, "{}.smx".format(graphic.file_name)))

    def get_unit_icon(self, icon, format: str = "png"):
        image = Image.open(os.path.join(self.resource_dir, "../widgetui/textures/ingame/units/{}_50730.DDS".format(str(icon).zfill(3))))
        image_arr = np.array(image)
        image_arr = image_arr[:,:,::-1]

        idx = np.argwhere(image_arr[:, :, 3] < 255)
        image_arr[idx[:, 0], idx[:, 1], 3] = 255

        image = Image.fromarray(image_arr, "RGBA")

        buf = BytesIO()
        image.save(buf, format=format)
        buf.seek(0)

        return buf

    def get_unit_icon_mask(self, icon, format: str = "png"):
        image = Image.open(os.path.join(self.resource_dir, "../widgetui/textures/ingame/units/{}_50730.DDS".format(str(icon).zfill(3))))
        original_image_arr = np.array(image)
        original_image_arr = original_image_arr[:,:,::-1]

        idx = np.argwhere(original_image_arr[:, :, 3] < 255)

        mask_arr = np.zeros_like(original_image_arr, dtype=np.uint8)
        mask_arr[:, :, :] = (255, 255, 255, 255)
        mask_arr[idx[:, 0], idx[:, 1]] = (0, 0, 0, 255)

        image = Image.fromarray(mask_arr, "RGBA")

        buf = BytesIO()
        image.save(buf, format=format)
        buf.seek(0)

        return buf

    def get_image(self, graphic: Graphic, format: str = "png"):
        smx_file = SMX.from_file(os.path.join(self.resource_dir, self.graphics_dir, "{}.smx".format(graphic.file_name)))
        frame = smx_file.main_frames[graphic.first_frame]

        picture_data = frame.get_picture_data(self.palette_config.get_palette(frame.get_palette_number()))

        image = Image.fromarray(picture_data, "RGBA")

        buf = BytesIO()
        image.save(buf, format=format)
        buf.seek(0)

        return buf, frame.get_hotspot()

    def get_animation_image(self, graphic: Graphic, loop: int = 0, format: str = "png"):
        smx_file = SMX.from_file(os.path.join(self.resource_dir, self.graphics_dir, "{}.smx".format(graphic.file_name)))

        images = list()

        max_w0 = max_w1 = max_h0 = max_h1 = 0

        frame_picture_data = list()

        for frame_id in range(graphic.first_frame, graphic.first_frame + graphic.frame_count):
            frame = smx_file.main_frames[frame_id]
            picture_data = frame.get_picture_data(self.palette_config.get_palette(frame.get_palette_number()))

            frame_picture_data.append((frame, picture_data))

            cx, cy = frame.get_hotspot()
            height, width = picture_data.shape[:2]

            w0 = cx
            w1 = width - cx
            h0 = cy
            h1 = height - cy

            max_w0 = max([max_w0, w0])
            max_w1 = max([max_w1, w1])
            max_h0 = max([max_h0, h0])
            max_h1 = max([max_h1, h1])

        frame_height = max_h0 + max_h1
        frame_width = max_w0 + max_w1

        for frame, picture_data in frame_picture_data:
            img_frame = np.zeros((frame_height, frame_width, 4), dtype=picture_data.dtype)
            cx, cy = frame.get_hotspot()
            height, width = picture_data.shape[:2]

            w0 = cx
            w1 = width - cx
            h0 = cy
            h1 = height - cy

            img_frame[
                max_h0 - h0 : max_h0 + h1,
                max_w0 - w0 : max_w0 + w1,
                :] = picture_data

            images.append(
                Image.fromarray(
                    img_frame,
                    "RGBA"
                )
            )

        buf = BytesIO()
        images[0].save(buf, format=format, save_all=True, append_images=images[1:], optimize=True,
                       duration=graphic.frame_duration * 1000, loop=loop)

        buf.seek(0)

        return buf, (max_w0, max_h0)
