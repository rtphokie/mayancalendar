import math
import os

from PIL import Image, ImageDraw


class block(object):

    def __init__(self, size=1, name="test", cachedir='cache'):
        os.makedirs(cachedir, exist_ok=True)
        self.cachedir = cachedir
        if size == 1:
            filename = "glyphs/block.png"
        else:
            filename = "glyphs/block_double.png"
        block = Image.open(filename).convert("RGBA")
        self.width, self.height = block.size
        if size < 1:
            block = block.resize((self.width * size, self.height))
        if size > 2:
            block = block.resize((self.width * (size / 2), self.height))
        self.block = block
        self.img = block.copy()
        self.name = name
        self.draw = ImageDraw.Draw(self.block)
        self.draw.rounded_rectangle((0, 0, self.width, self.height), fill=None, outline="#000", width=2, radius=7)

    def overlay(self, glyphname, cnt=None):
        overlay = Image.open(f"glyphs/{glyphname}.png").convert("RGBA")
        overlay = overlay.resize((self.width - 7, self.height - 7))
        glyph_width, glyph_height = overlay.size
        glyph_long_side = max([glyph_height, glyph_width])
        stroke = int(round(max([glyph_width, glyph_height]) / 75))

        _, _, col_cnt = self.tally_layout(cnt)
        pip_size, gutter_width, column_width = self.tally_sizing(glyph_height, stroke=stroke)

        # place right glyph
        offset = gutter_width + (col_cnt * column_width)
        overlay = overlay.resize((glyph_width - offset, glyph_height), resample=Image.Resampling.NEAREST)
        self.img = self.block.copy()
        self.img.paste(overlay, (offset, gutter_width), mask=overlay)

        # draw pips, always in the leftmost tally column
        if cnt == 0:
            zero = Image.open(f"glyphs/zero.png").convert("RGBA")
            zero = zero.resize(((column_width * col_cnt) - gutter_width, glyph_height))
            self.img.paste(zero, (gutter_width, gutter_width), mask=zero)
        else:
            self.draw_pips(cnt, glyph_long_side, stroke)
            self.draw_bars(cnt, glyph_long_side, stroke)

    def draw_bars(self, cnt, glyph_height, stroke):
        pip_cnt, bar_cnt, _ = self.tally_layout(cnt)
        pip_size, gutter_width, column_width = self.tally_sizing(glyph_height, stroke=stroke)
        draw = ImageDraw.Draw(self.img)

        if pip_cnt == 0:
            first_bar_column = 0
        else:
            first_bar_column = 1
        for n in range(bar_cnt):
            x = (column_width * (n + first_bar_column)) + gutter_width
            y = gutter_width
            draw.rounded_rectangle((x, y,
                                    x + pip_size[0], glyph_height-(gutter_width*2)),
                                   fill=None, outline="#000", width=2, radius=7)

    def draw_pips(self, cnt, glyph_height, stroke, color='#000'):
        # draw first column of circles representing remainder of cnt divided by 5
        pip_cnt, _, _ = self.tally_layout(cnt)
        print(f"{cnt} {pip_cnt} {'-' * 20}")
        if 0 < pip_cnt < 5:
            pip_size, gutter, column_width = self.tally_sizing(glyph_height, stroke=stroke)
            draw = ImageDraw.Draw(self.img)

            offset = gutter
            pip_height = pip_size[1]
            if pip_cnt == 4:
                pip_height = math.floor(pip_size[1] * .85)
            else:
                pip_height = pip_size[1]
                if pip_cnt == 1:
                    pip_height = math.floor(pip_size[1] * 1.25)
                    offset += math.floor((glyph_height / 2) - (pip_height / 2))
                elif pip_cnt == 2:
                    offset += math.floor((glyph_height / 3) - (pip_height / 2))
                elif pip_cnt == 3:
                    offset += math.floor(pip_height/4)

            start = offset
            end = self.height - offset
            step = pip_height + gutter

            for y in range(start, end, step):
                draw.rounded_rectangle((gutter, y, column_width, y + pip_height),
                                       fill=None, outline=color, width=2, radius=7)

    def tally_sizing(self, glyph_height, stroke=2):
        gutter_width = int(stroke * 2)
        pip_length = round(glyph_height / 4)

        pip_size = [math.floor(glyph_height / 10), pip_length]
        column_width = gutter_width + pip_size[0]
        return pip_size, gutter_width, column_width

    def tally_layout(self, cnt):
        if cnt is None:
            # no tally, e.g. the capstone
            pip_cnt, bar_cnt, tally_columns = 0, 0, 0
        else:
            pip_cnt = cnt % 5
            bar_cnt = int((cnt - pip_cnt) / 5)
            if cnt == 0:
                tally_columns = 3  # enough room for zero glyph
            else:
                if pip_cnt > 0:
                    tally_columns = bar_cnt + 1  # count of 5 unit bars and remainder
                else:
                    tally_columns = bar_cnt
        return pip_cnt, bar_cnt, tally_columns

    def __del__(self):
        self.img.save(f'cache/{self.name}.png')


def tile(name, cnt):
    uut = block(size=1, name=f'{cnt:02d}_{name}')
    uut.overlay(name, cnt=cnt)
    return (uut.img)
