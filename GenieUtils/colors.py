import logging
import math
import os

from PIL import Image, ImageDraw


logger = logging.getLogger(__name__)


class PaletteConfig(object):
    def __init__(self, path, palette_overrides={50500: 0}):
        self.palettes = dict()
        self.palette_overrides = palette_overrides
        self.basename = os.path.dirname(path)

        with open(path, "rb") as file:
            data = file.read()

        lines = data.decode('ascii').split('\r\n')

        for line in lines:
            if line.startswith("//"):
                continue

            entry = line.split(",")

            if len(entry) != 2:
                continue

            palette_id, filename = entry

            self.palettes[int(palette_id)] = filename

    def get_palette(self, palette_id):
        palette_id = self.palette_overrides.get(palette_id, palette_id)

        if palette_id in self.palettes:
            return ColorPalette.from_file(os.path.join(self.basename, self.palettes[palette_id]))

        raise FileNotFoundError


class ColorPalette(object):
    name_struct = "palette_color"
    name_struct_file = "color"
    struct_description = "indexed color storage."

    __slots__ = ('header', 'version', 'palette')

    def __init__(self, data):
        super().__init__()

        if isinstance(data, list) or isinstance(data, tuple):
            self.fill_from_array(data)
        else:
            self.fill(data)

    @classmethod
    def from_file(cls, path):
        with open(path, "rb") as file:
            return cls(file.read())

    def fill_from_array(self, ar):
        self.palette = [tuple(e) for e in ar]

    def fill(self, data):
        # split all lines of the input data
        # \r\n windows windows windows baby
        lines = data.decode('ascii').split('\r\n')

        self.header = lines[0]
        self.version = lines[1]

        # check for palette header
        if not (self.header == "JASC-PAL" or self.header == "JASC-PALX"):
            raise Exception("No palette header 'JASC-PAL' or 'JASC-PALX' found, "
                            "instead: %r" % self.header)

        if self.version != "0100":
            raise Exception("palette version mismatch, got %s" % self.version)

        entry_count = int(lines[2])

        entry_start = 3
        if lines[3].startswith("$ALPHA"):
            # TODO: Definitive Editions have palettes with fixed alpha
            entry_start = 4

        self.palette = []

        # data entries from 'entry_start' to n
        for line in lines[entry_start:]:
            # skip comments and empty lines
            if not line or line.startswith("#"):
                continue

            # one entry looks like "13 37 42",
            # "red green blue"
            # => red 13, 37 green and 42 blue.
            # DE1 and DE2 have a fourth value, but it seems unused
            self.palette.append(tuple(int(val) for val in line.split()))

        if len(self.palette) != entry_count:
            raise Exception("read a %d palette entries "
                            "but expected %d." % (
                                len(self.palette), entry_count))

    def __getitem__(self, index):
        return self.palette[index]

    def __len__(self):
        return len(self.palette)

    def __repr__(self):
        return "ColorTable<%d entries>" % len(self.palette)

    def __str__(self):
        return "%s\n%s" % (repr(self), self.palette)

    def gen_image(self, draw_text=True, squaresize=100):
        """
        writes this color table (palette) to a png image.
        """

        imgside_length = math.ceil(math.sqrt(len(self.palette)))
        imgsize = imgside_length * squaresize

        logger.debug("generating palette image with size %dx%d", imgsize, imgsize)

        palette_image = Image.new('RGBA', (imgsize, imgsize),
                                  (255, 255, 255, 0))
        draw = ImageDraw.ImageDraw(palette_image)

        # dirty, i know...
        text_padlength = len(str(len(self.palette)))
        text_format = "%%0%dd" % (text_padlength)

        drawn = 0

        # squaresize 1 means draw single pixels
        if squaresize == 1:
            for y in range(imgside_length):
                for x in range(imgside_length):
                    if drawn < len(self.palette):
                        r, g, b, a = self.palette[drawn]
                        draw.point((x, y), fill=(r, g, b, a))
                        drawn = drawn + 1

        # draw nice squares with given side length
        elif squaresize > 1:
            for y in range(imgside_length):
                for x in range(imgside_length):
                    if drawn < len(self.palette):
                        sx = x * squaresize - 1
                        sy = y * squaresize - 1
                        ex = sx + squaresize - 1
                        ey = sy + squaresize
                        r, g, b, a = self.palette[drawn]
                        # begin top-left, go clockwise:
                        vertices = [(sx, sy), (ex, sy), (ex, ey), (sx, ey)]
                        draw.polygon(vertices, fill=(r, g, b, a))

                        if draw_text and squaresize > 40:
                            # draw the color id
                            # insert current color id into string
                            ctext = text_format % drawn
                            tcolor = (255 - r, 255 - b, 255 - g, 255)

                            # draw the text
                            # TODO: use customsized font
                            draw.text((sx + 3, sy + 1), ctext,
                                      fill=tcolor, font=None)

                        drawn = drawn + 1

        else:
            raise Exception("fak u, no negative values for squaresize pls.")

        return palette_image

    def save_visualization(self, fileobj):
        self.gen_image().save(fileobj, 'png')
