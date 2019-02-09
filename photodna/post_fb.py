import cv2
import os,glob
from collections import defaultdict
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import boto3
import logging
from io import BytesIO
import base64
import numpy as np
from photodna.configigi import IDIOTSKII_KEY,SUCHII_KEY
import string
from random import *

os.chdir('/var/www/html/backend/photoDNA/photodna')

def do_post_shit(jason):
    characteristics = jason
    if characteristics['shareOrientation']:
        podlozhka = cv2.imread('gay_krug.jpg', cv2.IMREAD_UNCHANGED)
    else:
        podlozhka = cv2.imread('prosto_krug.jpg', cv2.IMREAD_UNCHANGED)

    for i in range(podlozhka.shape[0]):
        for j in range(podlozhka.shape[1]):
            temp = podlozhka[i, j][0]
            podlozhka[i, j][0] = podlozhka[i, j][2]
            podlozhka[i, j][2] = temp



    # the_list_v = (characteristics['data']['nationality'][0]['confidence'], characteristics['data']['nationality'][1]['confidence'],
    #               characteristics['data']['nationality'][2]['confidence'])

    d_n = defaultdict(int)

    the_flag = characteristics['shareCountry']['name']
    d_n[the_flag] = characteristics['shareCountry']['confidence']

    if (characteristics['data']['nationality'][0]['confidence'] == d_n[the_flag]):
        if (characteristics['data']['nationality'][1]['confidence'] > characteristics['data']['nationality'][2][
            'confidence']):
            flag2 = characteristics['data']['nationality'][1]['name']
            flag3 = characteristics['data']['nationality'][2]['name']
            d_n[flag2] = characteristics['data']['nationality'][1]['confidence']
            d_n[flag3] = characteristics['data']['nationality'][2]['confidence']
        else:
            flag2 = characteristics['data']['nationality'][2]['name']
            flag3 = characteristics['data']['nationality'][1]['name']
            d_n[flag2] = characteristics['data']['nationality'][2]['confidence']
            d_n[flag3] = characteristics['data']['nationality'][1]['confidence']

    else:
        if (characteristics['data']['nationality'][1]['confidence'] == d_n[the_flag]):
            if (characteristics['data']['nationality'][0]['confidence'] > characteristics['data']['nationality'][2][
                'confidence']):
                flag2 = characteristics['data']['nationality'][0]['name']
                flag3 = characteristics['data']['nationality'][2]['name']
                d_n[flag2] = characteristics['data']['nationality'][0]['confidence']
                d_n[flag3] = characteristics['data']['nationality'][2]['confidence']
            else:
                flag2 = characteristics['data']['nationality'][2]['name']
                flag3 = characteristics['data']['nationality'][0]['name']
                d_n[flag2] = characteristics['data']['nationality'][2]['confidence']
                d_n[flag3] = characteristics['data']['nationality'][0]['confidence']
        else:
            if (characteristics['data']['nationality'][1]['confidence'] > characteristics['data']['nationality'][0][
                'confidence']):
                flag2 = characteristics['data']['nationality'][1]['name']
                flag3 = characteristics['data']['nationality'][0]['name']
                d_n[flag2] = characteristics['data']['nationality'][1]['confidence']
                d_n[flag3] = characteristics['data']['nationality'][0]['confidence']
            else:
                flag2 = characteristics['data']['nationality'][0]['name']
                flag3 = characteristics['data']['nationality'][1]['name']
                d_n[flag2] = characteristics['data']['nationality'][0]['confidence']
                d_n[flag3] = characteristics['data']['nationality'][1]['confidence']

    # root = os.getcwd()

    if (characteristics['data']['gender'] == 'male'):
        sex = cv2.imread('/var/www/html/backend/photoDNA/photodna/for_posting/orientation_gender_age/mars.png', 1)
        if characteristics['shareOrientation']:
            podlozhka = put_element_overlay(458, 1020, sex, podlozhka)
        else:
            podlozhka = put_element_overlay(422, 860, sex, podlozhka)
    else:
        sex = cv2.imread('/var/www/html/backend/photoDNA/photodna/for_posting/orientation_gender_age/venus.png', 1)
        if characteristics['shareOrientation']:
            podlozhka = put_element_overlay(458, 1020, sex, podlozhka)
        else:
            podlozhka = put_element_overlay(422, 860, sex, podlozhka)

    # image = string_to_image(characteristics['img'].split(',', 1)[1])
    image = cv2.imread(characteristics['imgURL'], 1)

    # 618/630-коэффициент

    vis_shir = float(image.shape[0] / image.shape[1])
    if (vis_shir > 630 / 618):
        # образаем высоту (то кесть ширину)
        # ЗДЕСЬ ШИРИНА ЭТО ВЫСОТА И НАОБОРОТ
        the_chop = int((image.shape[0] - image.shape[1] * 630 / 618) / 2)
        crop_img = image[the_chop:image.shape[0] - the_chop, :]
        # 0 428 флаг; 190 111 - размеры его 428+190=618
    else:
        the_chop = int((image.shape[1] - image.shape[0] * 618 / 630) / 2)
        crop_img = image[:, the_chop:image.shape[1] - the_chop]

    res_shir = 618
    res_vis = 630
    flg1 = 0
    flg2 = 428
    new = cv2.resize(crop_img, (res_shir, res_vis), interpolation=cv2.INTER_AREA)

    # the_filter = cv2.imread('/var/www/html/backend/photoDNA/photodna/for_posting/picture/filter.png', cv2.IMREAD_UNCHANGED)

    # podlozhka = put_picture_and_filter(int((630 - new.shape[0]) / 2), int((618 - new.shape[1]) / 2), the_filter, new,
    #                                    podlozhka)

    podlozhka = put_element_overlay(0, 0, new, podlozhka)
    os.chdir(os.getcwd() + "/for_posting/flags/")
    #index_list = []
    for file in glob.glob("*.png"):
        if (file[:-4] == the_flag):
            true_flag = cv2.imread("/var/www/html/backend/photoDNA/photodna/for_posting/flags/" + file, 1)
            resized = cv2.resize(true_flag, (190, 111), interpolation=cv2.INTER_AREA)
            podlozhka = put_element_overlay(flg1, flg2, resized, podlozhka)

    c_png = cv2.imread("/var/www/html/backend/photoDNA/photodna/circle.png", 1)
    os.chdir('/var/www/html/backend/photoDNA/photodna')

    podlozhka = put_element_overlay(36, 804, c_png, podlozhka)

    img = Image.fromarray(podlozhka)

    draw = ImageDraw.Draw(img)

    font1 = ImageFont.truetype("Roboto-Medium.ttf", 70)

    font6 = ImageFont.truetype("Roboto-Medium.ttf", 20)

    font7 = ImageFont.truetype("Roboto-Medium.ttf", 25)

    font8 = ImageFont.truetype("Roboto-Medium.ttf", 25)

    draw.text((843, 70), str(d_n[the_flag]), (154, 154, 160), font=font1)
    if characteristics['shareOrientation']:
        draw.text((865, 427), str(characteristics['data']['straight']) + '%', '#D63796', font=font6)
        draw.text((865, 463), str(characteristics['data']['gay']) + '%', '#D63796', font=font6)

    if characteristics['shareOrientation']:
        draw.text((1016, 421), str(characteristics['data']['age']), '#D63796', font=font7)
    else:
        draw.text((1011, 425), str(characteristics['data']['age']), '#D63796', font=font7)


    draw.text((1058, 321), str(d_n[flag2]) + '%', '#C0C0C0', font=font8)
    draw.text((1058, 358), str(d_n[flag3]) + '%', '#C0C0C0', font=font8)
    font2 = ImageFont.truetype("Roboto-Medium.ttf", 50)
    draw.text((927, 81), "%", (154, 154, 160), font=font2)

    text1_x = 898
    text1_y = 150
    text2_x = 788
    text2_y = 332
    text3_x = 788
    text3_y = 368

    if (len(the_flag) < 9):
        font3 = ImageFont.truetype("Roboto-Medium.ttf", 35)
    else:
        if (len(the_flag) < 12):
            font3 = ImageFont.truetype("Roboto-Medium.ttf", 25)
        else:
            font3 = ImageFont.truetype("Roboto-Medium.ttf", 20)

    if (len(flag2) < 9) and (len(flag3) < 9):
        font5 = ImageFont.truetype("Roboto-Medium.ttf", 20)
    else:
        font5 = ImageFont.truetype("Roboto-Medium.ttf", 14)

    text_size = draw.textsize(the_flag, font=font3)
    x = text1_x - (text_size[0] / 2)
    draw.text((x, text1_y), the_flag, font=font3, fill=(120, 120, 120))

    text_size = draw.textsize(flag2, font=font5)
    x = text2_x - (text_size[0] / 2)
    draw.text((x, text2_y), flag2, font=font5, fill='#969696')

    text_size = draw.textsize(flag3, font=font5)
    x = text3_x - (text_size[0] / 2)
    draw.text((x, text3_y), flag3, font=font5, fill='#969696')

    allchar = string.ascii_letters + string.digits
    rand_file_name = "".join(choice(allchar) for x in range(68))

    img.save('/var/www/html/backend/photoDNA/photodna/for_posting/' + rand_file_name + '.png')

    session = boto3.Session(
        aws_access_key_id=SUCHII_KEY,
        aws_secret_access_key=IDIOTSKII_KEY,
    )
    s3 = session.client('s3')

    with open('/var/www/html/backend/photoDNA/photodna/for_posting/' + rand_file_name + '.png', 'rb') as data:
        s3.upload_fileobj(data, 'storage.ws.pho.to', 'photohack/stckrs/' + rand_file_name + '.png', ExtraArgs={'ContentType': 'image/png'})

    if os.path.exists('/var/www/html/backend/photoDNA/photodna/for_posting/' + rand_file_name + '.png'):
        os.remove('/var/www/html/backend/photoDNA/photodna/for_posting/' + rand_file_name + '.png')
    else:
        print("The file does not exist")
    return 'https://storage.ws.pho.to/photohack/stckrs/' + rand_file_name + '.png'


def put_element_overlay(position_h,position_w,elelment,podlozhka):
    for i in range(elelment.shape[0]):
        for j in range(elelment.shape[1]):
            if ((elelment[i, j][0]==0) and(elelment[i, j][1]==0)and (elelment[i, j][2] == 0)):
                podlozhka[position_h + i, position_w + j][0] = 255
                podlozhka[position_h + i, position_w + j][1] = 255
                podlozhka[position_h + i, position_w + j][2] = 255
            else:
                podlozhka[position_h+i, position_w+ j][0] = elelment[i, j][2]
                podlozhka[position_h+i, position_w+ j][1] = elelment[i, j][1]
                podlozhka[position_h+i, position_w+ j][2] = elelment[i, j][0]
                # podlozhka[position_h + i, position_w + j][3]=255
    return podlozhka

def put_element_transperency_shit(position_h,position_w,elelment,podlozhka):
    for i in range(elelment.shape[0]):
        for j in range(elelment.shape[1]):
            if ((elelment[i, j][0]==0) and(elelment[i, j][1]==0)and (elelment[i, j][2] == 0)):
                podlozhka[position_h + i, position_w + j][0] = 255
                podlozhka[position_h + i, position_w + j][1] = 255
                podlozhka[position_h + i, position_w + j][2] = 255
            else:
                podlozhka[position_h+i, position_w+ j][0] = elelment[i, j][2]
                podlozhka[position_h+i, position_w+ j][1] = elelment[i, j][1]
                podlozhka[position_h+i, position_w+ j][2] = elelment[i, j][0]
                # podlozhka[position_h + i, position_w + j][3] = elelment[i, j][3]
    return podlozhka


def put_picture_and_filter(position_h,position_w,filter,image,podlozhka):
    for i in range (image.shape[0]):
        for j in range (image.shape[1]):
            ########### Remove later ######################
            # podlozhka[position_h+i, position_w+ j][0] = filter[i,j][2]
            # podlozhka[position_h+i, position_w+ j][1] = filter[i,j][1]
            # podlozhka[position_h+i, position_w+ j][2] = filter[i,j][0]
            # podlozhka[position_h + i, position_w + j][3] = 255 - int((0.299*image[i,j][2] + 0.587*image[i,j][1] + 0.114* image[i,j][0]))

            norm_red = filter[i, j][0] / 255
            norm_green = filter[i, j][1] / 255
            norm_blue = filter[i, j][2] / 255
            norm_transparency = 1 - int(
                (0.299 * image[i, j][0] + 0.587 * image[i, j][1] + 0.114 * image[i, j][2])) / 255
            # 0.299 0.587 0.114
            # 0.2126 0.7152 0.0722
            # 0.2627 0.6780 0.0593
            podlozhka[position_h + i, position_w + j][0] = int(
                255 * ((1 - norm_transparency) * norm_red + int(norm_transparency * image[i, j][0] / 255)))
            podlozhka[position_h + i, position_w + j][1] = int(
                255 * ((1 - norm_transparency) * norm_green + int(norm_transparency * image[i, j][1] / 255)))
            podlozhka[position_h + i, position_w + j][2] = int(
                255 * ((1 - norm_transparency) * norm_blue + int(norm_transparency * image[i, j][2] / 255)))

    return podlozhka


def string_to_image(base64_string):
    imgdata = base64.b64decode(base64_string)
    cvimg = Image.open(BytesIO(imgdata))
    open_cv_image = np.array(cvimg)
    return open_cv_image[:, :, ::-1].copy()


def pil_image_to_cv(pil_image):
    podlozhka = np.array(pil_image)
    return podlozhka[:, :, ::-1].copy()