import random
import os
import uuid
from PIL import Image, ImageDraw

# python -m pip install --upgrade pip   ,  python -m pip install --upgrade pillow

def get_filename():
    dir_path=os.path.split(os.path.dirname(os.path.abspath(__file__)))[-2]
    image_path = os.path.join(dir_path, "generative_art/images/")
    print("path == ",image_path)
    return image_path

def draw_image():
    run_id = uuid.uuid1()
    
    print(f'Processing run_id: {run_id}')
    
    image = Image.new('RGB', (2000, 2000))
    width, height = image.size
    
    rectangle_width = 100
    rectangle_height = 100
    
    number_of_squares = random.randint(10, 550)
    
    draw_image = ImageDraw.Draw(image)
    for i in range(number_of_squares):
        rectangle_x = random.randint(0, width)
        rectangle_y = random.randint(0, height)
    
        rectangle_shape = [
            (rectangle_x, rectangle_y),
            (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
        draw_image.rectangle(
            rectangle_shape,
            fill=(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
        )
    path = get_filename()
    image.save(f'{path}/{run_id}.png')
    
if __name__ == '__main__':
        draw_image()

"""
import urllib.request
import os
import random
from PIL import Image, ImageOps, ImageDraw, ImageFont
# pip install Pillow

# download
def dl_image():
  img_url = "https://source.unsplash.com/random/2560x1080"
  img_name = os.path.basename(img_url)
  urllib.request.urlretrieve(img_url,img_name + '.jpg') # save pic in folder
  print('Download image {}'.format(img_name + '.jpg'))
  
# resize
def resize_ig_image():
	image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'2560x1080.jpg')
	im = Image.open(image_file)
	out = im.resize((1080,1080))
	# save resize image
	out.save('resize_output.png')

# crop
def crop_ig_image():
	image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'2560x1080.jpg')
	im = Image.open(image_file)
	out = im.crop((1,3,1080,1080))
	# save resize image
	out.save('crop_output.png')


#  pillow_crop_max_square from the centre of an image
def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def pillow_crop_max_square():    
    image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'2560x1080.jpg')
    pil_img = Image.open(image_file)
    im_new = crop_center(pil_img, min(pil_img.size), min(pil_img.size))
    im_new.save('crop_max_square.jpg', quality=95)



# https://pillow.readthedocs.io
# Example: Draw Multiline Text
def write_to_image():
   #from PIL import Image, ImageDraw, ImageFont

   # create an image
   out = Image.new("RGB", (150, 100), (255, 255, 255))

   # get a font
   fnt = ImageFont.truetype("FreeMono.ttf", 40)
   # get a drawing context
   d = ImageDraw.Draw(out)

   # draw multiline text
   d.multiline_text((10,10), "Hello\nWorld", font=fnt, fill=(0, 0, 0))

   out.show()

# changing colour
def greyscale_ig_image():
	image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'crop_max_square.jpg')
	im = Image.open(image_file)
	out = ImageOps.grayscale(im)
	# save resize image
	out.save('greyscale.png',"PNG")

def get_qoute():
	qoute_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'qoute.txt')
	f = open(qoute_file,'r')
	txt = f.read()
	lines = txt.split('\n.\n')
	text_out = random.choice(lines)
	print(text_out)
	return text_out
def wrap_by_word(s,n):
	'''returns a string \\n is inserted between every n words '''
	a = s.split()
	ret = ''
	for i in range(0, len(a),n):
		ret += ' '.join(a[i:i+n]) + '\n'
	return ret	

def text_overlay_ig(qoutation):
	image_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),'greyscale.png')
	im = Image.open(image_file).convert("RGBA")

	draw = ImageDraw.Draw(im)
	font = ImageFont.truetype('FreeMono.ttf',size=60)
	font_author = ImageFont.truetype('FreeMono.ttf',size=30)

	(qoute,author) = qoutation.split('--')
	qoute = wrap_by_word(qoute, 4)

	(x,y) = (50,100)
	color = 'rgb(206, 0, 240)'
	# draw the massage on the background
	draw.text((x, y), qoute, fill=color, font=font)

	(x,y) = (50,1000)
	color = 'rgb(255, 255, 255)'
	# draw the massage on the background
	draw.text((x, y), author, fill=color, font=font_author)
	im.save('text_overlay.png')


dl_image()
#resize_ig_image()
#crop_ig_image()
pillow_crop_max_square()
#write_to_image()
greyscale_ig_image()
qoutation = get_qoute()
text_overlay_ig(qoutation)
"""        



"""                                                                         original
import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

image = Image.new('RGB', (2000, 2000))
width, height = image.size

rectangle_width = 100
rectangle_height = 100

number_of_squares = random.randint(10, 550)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    rectangle_x = random.randint(0, width)
    rectangle_y = random.randint(0, height)

    rectangle_shape = [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )

image.save(f'./output/{run_id}.png')
 
"""