from PIL import Image, ImageEnhance, ImageFilter
import os

path = "C:/Users/harsh/Harsha/python/Images"
pathOut = 'C:/Users/harsh/Harsha/python/editedImages'

if not os.path.isdir(f'{pathOut}'):
    os.mkdir(f'{pathOut}')

for filename in os.listdir(path):
    print(f'{path}/{filename}')
    img = Image.open(f'{path}/{filename}')

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(90)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f'{pathOut}/{clean_name}_edited.jpg')

