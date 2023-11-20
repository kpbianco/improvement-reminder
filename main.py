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
sel_dict = {}
paths = []
tdl = []

#####
def get_keys(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, dict):
            for subkey in get_keys(value):
                yield key + '->' + subkey
        cat_item.append(key)
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

ttp = cat_item[selected]

char_len = len(ttp)
width = 828
height = 1792

im = Image.open("./template/sisy_f.png")
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

font_size1f=font_size
text, text_l = get_wrapped_text(text, font, line_length=((10*font_size)))


if text_l == 2:
    font = font.font_variant(size=font_size*1.33)

elif text_l > 2:
    font = font.font_variant(size=font_size*text_l)

draw.multiline_text((width / 2, height / 2.66), text, font=font, fill="black", anchor="mm")

chosen_path = lookup_path(ttp)
chosen_path = "->".join(chosen_path[:-1])
cp_len = len(chosen_path)

fl_final = font_size

# font_size = 1000
font2 = ImageFont.truetype("Arial.ttf", font_size1f*.66)
# while font_size > 1:
#   if font2.getlength(text) < width*.6:
#     break
#   font_size -= 1
#   font2 = font2.font_variant(size=font_size)



# print(font_size)
t2_ll = 10*font_size1f
text2, text_l2 = get_wrapped_text(chosen_path, font2, line_length=t2_ll)

# # font_size2 = 1
# while font_size1f:
#     # iterate until the text size is just larger than the criteria
#     font_size1f -= 1
#     font2 = font2.font_variant(size=font_size)

# print(str(t2_ll) + ":1")
# print(str(cp_len) + ":2")
# print('font size 2: ' + str(font_size))
#font2 = font2.font_variant(size=(t2_ll // cp_len) * height/font_size // font_size)

print(str(text_l2) + ":" + str(cp_len))
font_size2f=font_size1f*(1.33 * text_l2)*.33
print(str(font_size1f) + ":" + str(font_size2f) + ":" + str(20- (20 *(1/(font_size1f*0.66)))) + ":" + str(fl_final))


font2 = font2.font_variant(size=20- (20 *(1/(font_size1f*0.66))))
draw.multiline_text((width / 2, height-(height*0.1)), text=text2, font=font2, fill="black", anchor="mm" )
im.save("static/out.png")




# account_sid = 123
# auth_token = 123
# client = Client(account_sid, auth_token)

# def message_handler():
#     print('got here')

# def send_mms():

    

#     message = client.messages \
#         .create(
#             body='New Challenge',
#             media_url='https://raw.githubusercontent.com/dianephan/flask_upload_photos/main/UPLOADS/DRAW_THE_OWL_MEME.png',
#             from_='+',
#             to='+'
#         )

#     print(message.sid)


# messages = client.messages.list(
#     from_='+',
#     to="+"
# )

# curr_items = len(messages)

# def check_messages():
#     messages = client.messages.list(
#         from_='+',
#         to="+"
#     )

#     if len(messages) > curr_items:
#         message_handler("out.png")
#         send_mms()
#         curr_items = len(messages)


# test = check_messages()
# print(test)


