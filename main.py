import json
import random
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

with open("list.json") as list:
    dictionary = json.load(list)

cat_item = []
selection = []
paths = []

#####
def get_keys(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for subkey in get_keys(value):
                yield key + '->' + subkey
        elif isinstance(value, str):
            cat_item.append((key, value))
            yield value
        else:
            yield key

def lookup_path(value):
    for item in paths:
        if item[-1] == value:
            return item

def pop_path(value):
    paths.pop(paths.index(lookup_path(value)))

def get_len():
    return len(paths)

def get_wrapped_text(text: str, font: ImageFont.ImageFont,
                     line_length: int):
        lines = ['']
        for word in text.split():
            line = f'{lines[-1]} {word}'.strip()
            if font.getlength(line) <= line_length:
                lines[-1] = line
            else:
                lines.append(word)
        return '\n'.join(lines)



#####

for key in get_keys(dictionary):
    selection.append(key)

for item in selection:
    sp = item.split("->")
    paths.append(sp)


####

hi = get_len()-1


selected = random.randint(0, hi)
ttp = paths[hi][-1]
ttp = "the quick brown fox jumped over the yellow dog"



char_len = len(ttp)
width = 828
height = 1792

im = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(im)

print(char_len)

font_size = int((height / char_len))
font = ImageFont.truetype("Arial.ttf", font_size)
print(font_size)
ttp = get_wrapped_text(ttp, font, line_length=660)
text = ttp


while font_size > 1:
  if font.getlength(text) < width:
    break
  font_size -= 1
  font = font.font_variant(size=font_size)

draw.multiline_text((width / 2, height / 2), text, font=font, fill="black", anchor="mm")
im.save("out.png")




