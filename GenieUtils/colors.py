import logging
import os


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
            return ColorPalette(os.path.join(self.basename, self.palettes[palette_id]))

        raise FileNotFoundError


class ColorPalette(object):
    """
    Roughly based on https://github.com/SFTtech/openage/blob/master/openage/convert/value_object/read/media/colortable.py
    """

    def __init__(self, path):
        with open(path, "rb") as file:
            data = file.read().decode("ascii")
            lines = data.split("\r\n")

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
                raise Exception("read %d palette entries "
                                "but expected %d. (palette: %s)" % (
                                    len(self.palette), entry_count, path))

    def __getitem__(self, index):
        return self.palette[index]

    def __len__(self):
        return len(self.palette)

    def __repr__(self):
        return "ColorTable<%d entries>" % len(self.palette)

    def __str__(self):
        return "%s\n%s" % (repr(self), self.palette)
