import json
import random
import math
import textwrap

import os
from twilio.rest import Client
from PIL import Image, ImageDraw, ImageFont

with open("list.json") as list:
    dictionary = json.load(list)

cat_item = []
selection = []
paths = []
tdl = []

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
        return '\n'.join(lines), len(lines)



#####

for key in get_keys(dictionary):
    selection.append(key)

for item in selection:
    sp = item.split("->")
    tdl.append(sp[-1])
    paths.append(sp)


####

hi = get_len()-1


selected = random.randint(0, len(cat_item)-1)
print(selected)
ttp = cat_item[selected][1]

char_len = len(ttp)
width = 828
height = 1792

im = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(im)

#font_size = int((height / char_len))
font_size = 1000
font = ImageFont.truetype("Arial.ttf", font_size)


text = ttp
while font_size > 1:
  if font.getlength(text) < width*.6:
    break
  font_size -= 1
  font = font.font_variant(size=font_size)

print(font_size)
print(width/font_size)
print((width/font_size))
text, text_l = get_wrapped_text(text, font, line_length=((10*font_size)))
print(text_l)

if text_l == 2:
    font = font.font_variant(size=font_size*1.33)

elif text_l > 2:
    font = font.font_variant(size=font_size*text_l)

draw.multiline_text((width / 2, height / 2), text, font=font, fill="black", anchor="mm")
im.save("static/out.png")

print(selection)

account_sid = 'AC92725fde0df1a6f6e72c2a0d05e2873f'
auth_token = 'c83fe16b493490afbeeb5ecd3f05c2fe'
client = Client(account_sid, auth_token)

def message_handler():
    print('got here')

def send_mms():
    #account_sid = os.environ['AC92725fde0df1a6f6e72c2a0d05e2873f']
    #auth_token = os.environ['c83fe16b493490afbeeb5ecd3f05c2fe']
    

    message = client.messages \
        .create(
            body='Test 1',
            media_url='https://raw.githubusercontent.com/dianephan/flask_upload_photos/main/UPLOADS/DRAW_THE_OWL_MEME.png',
            from_='+18333962867',
            to='+15756445190'
        )

    print(message.sid)


messages = client.messages.list(
    from_='+15756445190',
    to="+18333962867"
)

curr_items = len(messages)

def check_messages():
    messages = client.messages.list(
        from_='+15756445190',
        to="+18333962867"
    )

    if len(messages) > curr_items:
        message_handler("out.png")
        send_mms()
        curr_items = len(messages)


test = check_messages()
print(test)


