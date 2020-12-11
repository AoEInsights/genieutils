import os
from io import BytesIO
from typing import Generator

from GenieUtils.slp import SLP
from PIL import Image
import numpy as np

from . import DatFile, lang, smx
from .colors import PaletteConfig
from .enums import UnitType, ResourceType
from .smx import SMX


class Graphic(object):
    def __init__(self, genie_utils: 'GenieUtils', g: DatFile.Graphic):
        self.genie_utils = genie_utils

        self.id = g.ID
        self.file_name = g.FileName
        self.first_frame = g.FirstFrame
        self.frame_count = g.FrameCount
        self.frame_duration = g.FrameDuration
        self.raw = g

    @property
    def smx(self):
        return SMX.from_file(os.path.join(self.genie_utils.resource_dir, self.genie_utils.graphics_dir, "{}.smx".format(self.file_name)))

    def get_image(self, format: str = "png"):
        frame = self.smx.main_frames[self.first_frame]

        picture_data = frame.get_picture_data(self.genie_utils.palette_config.get_palette(frame.get_palette_number()))

        image = Image.fromarray(picture_data, "RGBA")

        buf = BytesIO()
        image.save(buf, format=format)
        buf.seek(0)

        return buf

    def get_animation_image(self, loop: int = 0, format: str = "png"):
        smx_file = self.smx

        images = list()

        max_w0 = max_w1 = max_h0 = max_h1 = 0

        frame_picture_data = list()

        for frame_id in range(self.first_frame, self.first_frame + self.frame_count):
            frame = smx_file.main_frames[frame_id]
            picture_data = frame.get_picture_data(self.genie_utils.palette_config.get_palette(frame.get_palette_number()))

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

            img_frame[max_h0 - h0: max_h0 + h1, max_w0 - w0: max_w0 + w1, :] = picture_data

            images.append(
                Image.fromarray(
                    img_frame,
                    "RGBA"
                )
            )

        buf = BytesIO()
        images[0].save(buf, format=format, save_all=True, append_images=images[1:], optimize=True,
                       duration=self.frame_duration * 1000, loop=loop)

        buf.seek(0)

        return buf


class Unit(object):
    def __init__(self, genie_utils: 'GenieUtils', u: DatFile.Unit):
        self.genie_utils = genie_utils

        self.id = u.ID
        self.type = UnitType(u.Type)
        self.name = genie_utils.strings.get(u.LanguageDLLName, u.Name)
        self.icon = u.IconID
        self.graphic = genie_utils.graphic(u.StandingGraphic[0])
        self.dying_graphic = genie_utils.graphic(u.DyingGraphic)
        self.undead_graphic = genie_utils.graphic(u.UndeadGraphic)
        self.undead_mode = bool(u.UndeadMode)
        self.walking_graphic = genie_utils.graphic(u.DeadFish.WalkingGraphic)
        self.attacking_graphic = genie_utils.graphic(u.Type50.AttackGraphic)
        self.hit_points = u.HitPoints
        self.line_of_sight = u.LineOfSight
        self.garrison_capacity = u.GarrisonCapacity
        self.class_type = u.Class
        self.collision_size = u.CollisionSize
        self.dead_unit_id = u.DeadUnitID
        self.blood_unit_id = u.BloodUnitID
        self.resource_decay = u.ResourceDecay
        self.outline_size = u.OutlineSize
        self.speed = u.Speed
        self.raw = u

    @property
    def _icon_dds(self):
        return Image.open(os.path.join(self.genie_utils.resource_dir, "../widgetui/textures/ingame/units/{}_50730.DDS".format(str(self.icon).zfill(3))))

    def get_icon(self, format: str = "png"):
        image = self._icon_dds

        image_arr = np.array(image)
        image_arr = image_arr[:,:,::-1]

        idx = np.argwhere(image_arr[:, :, 3] < 255)
        image_arr[idx[:, 0], idx[:, 1], 3] = 255

        image = Image.fromarray(image_arr, "RGBA")

        buf = BytesIO()
        image.save(buf, format=format)
        buf.seek(0)

        return buf

    def get_icon_mask(self, format: str = "png"):
        image = self._icon_dds

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

    def __repr__(self):
        return f"<Unit '{self.name}' ({self.id})>"


class Civ(object):
    def __init__(self, genie_utils: 'GenieUtils', id, c: DatFile.Civ):
        self.genie_utils = genie_utils

        self.id = id
        self.name = c.Name
        self.name2 = c.Name2
        self.tech_tree_id = c.TechTreeID
        self.team_bonus_id = c.TeamBonusID
        self.icon_set = c.IconSet
        self.raw = c

        # performance improvements
        self.__units = list(c.Units)

    @property
    def units(self):
        for u in self.__units:
            unit = Unit(self.genie_utils, u)

            yield unit

    def unit(self, id):
        return list(self.units)[id]

    def techs(self):
        for tech in self.genie_utils.techs():
            if tech.civ is None or tech.civ == self:
                yield tech

    def __repr__(self):
        return f"<Civ '{self.name}'>"


class Cost(object):
    def __init__(self, resource_usage: DatFile.ResearchResourceCost):
        self.resource_type = ResourceType(resource_usage.Type)
        self.amount = resource_usage.Amount
        self.paid = bool(resource_usage.Flag)
        self.raw = resource_usage

    def __repr__(self):
        return f"<Cost '{str(self.resource_type)}': '{self.amount}' [Paid: {self.paid}]>"


class Tech(object):
    def __init__(self, genie_utils: 'GenieUtils', t: DatFile.Tech):
        self.required_techs = t.RequiredTechs
        self.required_tech_count = t.RequiredTechCount
        self.civ = genie_utils.civ(t.Civ) if t.Civ != -1 else None
        self.full_tech_mode = bool(t.FullTechMode)
        self.research_location = t.ResearchLocation
        self.research_time = t.ResearchTime
        self.effect_id = t.EffectID
        self.type = t.Type
        self.icon_id = t.IconID
        self.button_id = t.ButtonID
        self.help = genie_utils.strings.get(t.LanguageDLLHelp, "")
        self.tech_tree = genie_utils.strings.get(t.LanguageDLLTechTree, "")
        self.name = genie_utils.strings.get(t.LanguageDLLName, t.Name)
        self.description = genie_utils.strings.get(t.LanguageDLLDescription, "")
        self.name2 = t.Name2
        self.repeatable = bool(t.Repeatable)
        self.cost = [Cost(r) for r in t.ResourceCosts if r.Type != -1]
        self.raw = t


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

        self.resource_dir = resource_dir
        self.graphics_dir = graphics_dir
        self.buildings_icons_file = buildings_icons_file
        self.interface_buttons_icons_file = interface_buttons_icons_file
        self.technologies_icons_file = technologies_icons_file
        self.units_icons_file = units_icons_file

        self.dataset = DatFile.DatFile()
        self.dataset.setGameVersion(dataset_game_version)
        self.dataset.load(os.path.join(resource_dir, dataset_file))

        # performance improvements
        self.civs = [Civ(self, id, c) for id, c in enumerate(self.dataset.Civs)]
        self.__graphics = list(self.dataset.Graphics)
        self.__techs = list(self.dataset.Techs)

        self.palette_config = PaletteConfig(os.path.join(resource_dir, palette_config_file))

        self.strings = lang.load_txt(os.path.join(resource_dir, strings_file))

    @property
    def gaia_civ(self):
        return self.civs[0]

    def civ(self, id):
        return self.civs[id]

    def units(self, filter_types=None) -> Generator[Unit, None, None]:
        for unit in self.gaia_civ.units:
            if not filter_types or unit.type in filter_types:
                yield unit

    def unit(self, unit_id) -> Unit:
        return self.gaia_civ.unit(unit_id)

    def graphic(self, graphic_id) -> Graphic:
        graphic = self.__graphics[graphic_id]

        return Graphic(self, graphic)

    def graphics(self) -> Generator[Graphic, None, None]:
        for g in self.__graphics:
            yield Graphic(self, g)

    def techs(self):
        for t in self.__techs:
            yield Tech(self, t)
