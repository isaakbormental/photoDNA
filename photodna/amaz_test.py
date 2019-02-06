import boto3
from io import StringIO
# s3 = boto3.client('s3')
#
# with open('imaga.jpg', 'rb') as data:
#     response = s3.upload_fileobj(data, 'storage.ws.pho.to', 'photohack/stckrs/testiks.png', ExtraArgs={'ContentType': 'image/png'})
#
#
# print(response)
#
base_img = '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'
import base64
from PIL import Image
import cv2
from io import StringIO, BytesIO
import numpy as np
#
#
# def readb64(base64_string):
#     sbuf = StringIO()
#     sbuf.write(base64.b64decode(base64_string))
#     pimg = Image.open(sbuf)
#     return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)
#
# def stringToImage(base64_string):
#     imgdata = base64.b64decode(base64_string)
#     cvimg = Image.open(BytesIO(imgdata))
#     open_cv_image = np.array(cvimg)
#     return open_cv_image[:, :, ::-1].copy()
# #
# #
# cvimg = Image.fromarray(stringToImage(base_img))
# # cvimg.show()
#
# response = s3.upload_fileobj(cvimg.tobytes(), 'storage.ws.pho.to', 'photohack/stckrs/test_tak.png')
# # cv2.imshow('image',stringToImage(base_img))
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# def pil_image_to_cv(pil_image):
#     podlozhka = np.array(pil_image)
#     for i in range(podlozhka.shape[0]):
#         for j in range(podlozhka.shape[1]):
#             podlozhka[i][j][0] = 255 - podlozhka[i][j][0]
#             podlozhka[i][j][1] = 255 - podlozhka[i][j][1]
#             podlozhka[i][j][2] = 255 - podlozhka[i][j][2]
#     return podlozhka[:, :, ::-1].copy()
#
# # im = Image.open('gay_krug.png')
# # podlozhka = pil_image_to_cv(im)
#
# podlozhka = cv2.imread('gay_krug.png', cv2.IMREAD_UNCHANGED)
# cv2.imshow('image',podlozhka)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import json
url = 'poshel_nahui'
didi = dict()
didi['link'] = url
resp = json.dumps(didi)
print(json.loads(resp))
print(type(json.loads(resp)))

# def string_to_image(base64_string):
#
#     imgdata = base64.b64decode(base64_string)
#     cvimg = Image.open(BytesIO(imgdata))
#     open_cv_image = np.array(cvimg)
#     return open_cv_image[:, :, ::-1].copy()
#
# pdlozhka  = string_to_image(base_img)
# cv2.imshow('image',pdlozhka)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import string
from random import *

allchar = string.ascii_letters + string.digits
rand_file_name = "".join(choice(allchar) for x in range(68))

print (rand_file_name)


################ Тестим цвета
import cv2
import os,glob
from collections import defaultdict
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
import base64
import numpy as np
import string
from random import *


def do_post_shit(baseimg):

    podlozhka = cv2.imread('gay_krug.jpg', cv2.IMREAD_UNCHANGED)
    for i in range(podlozhka.shape[0]):
        for j in range(podlozhka.shape[1]):
            temp = podlozhka[i, j][0]
            podlozhka[i, j][0] = podlozhka[i, j][2]
            podlozhka[i, j][2] = temp

    nat1 = 'Uzbek'
    nat2 = 'Ru'
    nat3 = 'Ukrop'
    conf1 = 0.85
    conf2 = 0.62
    conf3 = 0.34

    the_list_v = (conf2, conf3, conf1)

    d_n = defaultdict(int)
    if (conf1 == max(the_list_v)):
        the_flag = nat1
        d_n[the_flag] = conf1
        if (conf2 > conf3):
            flag2 = nat2
            flag3 = nat3
            d_n[flag2] = conf2
            d_n[flag3] = conf3
        else:
            flag2 = nat3
            flag3 = nat2
            d_n[flag2] = conf3
            d_n[flag3] = conf2

    else:
        if (conf2 == max(the_list_v)):
            the_flag = nat2
            d_n[the_flag] = conf2
            if (conf1 > conf3):
                flag2 = nat1
                flag3 = nat3
                d_n[flag2] = conf1
                d_n[flag3] = conf3
            else:
                flag2 = nat3
                flag3 = nat1
                d_n[flag2] = conf3
                d_n[flag3] = conf1
        else:
            the_flag = nat3
            d_n[the_flag] = conf3
            if (conf2 > conf1):
                flag2 = nat2
                flag3 = nat1
                d_n[flag2] = conf2
                d_n[flag3] = conf1
            else:
                flag2 = nat1
                flag3 = nat2
                d_n[flag2] = conf1
                d_n[flag3] = conf2
    pol = 'male'
    root = os.getcwd()
    if (pol == 'male'):
        sex = cv2.imread('D:\\Education\\Hackathones\\photohack\\pravoslavnaya_papka\\photoDNA\\photodna\\for_posting\\orientation_gender_age\\mars.png', 1)
        podlozhka = put_element_overlay(458, 1020, sex, podlozhka)
    else:
        sex = cv2.imread('D:\\Education\\Hackathones\\photohack\\pravoslavnaya_papka\\photoDNA\\photodna\\for_posting\\orientation_gender_age\\venus.png', 1)
        podlozhka = put_element_overlay(458, 1020, sex, podlozhka)

    image = string_to_image(baseimg)

    vis_shir = float(image.shape[0] / image.shape[1])

    if vis_shir > 630 / 618:
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
    # new = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
    the_filter = cv2.imread('D:\\Education\\Hackathones\\photohack\\pravoslavnaya_papka\\photoDNA\\photodna\\for_posting\\picture\\filter.png', cv2.IMREAD_UNCHANGED)

    podlozhka = put_picture_and_filter(int((630 - new.shape[0]) / 2), int((618 - new.shape[1]) / 2), the_filter, new,
                                       podlozhka)

    os.chdir(os.getcwd() + "\\for_posting\\flags\\")

    for file in glob.glob("*.png"):
        if (file[:-4] == the_flag):
            # true_flag = cv2.imread(root + "/for_posting/flags/" + file, 1)
            # true_flag_im = Image.open(os.path.join(root, 'for_posting', 'flags', file))
            # true_flag = pil_image_to_cv(true_flag_im)
            true_flag = cv2.imread("D:\\Education\\Hackathones\\photohack\\pravoslavnaya_papka\\photoDNA\\photodna\\for_posting\\flags\\" + file, 1)
            resized = cv2.resize(true_flag, (190, 111), interpolation=cv2.INTER_AREA)
            podlozhka = put_element_overlay(flg1, flg2, resized, podlozhka)

    c_png = cv2.imread("D:\\Education\\Hackathones\\photohack\\pravoslavnaya_papka\\photoDNA\\photodna\\circle.png", 1)
    os.chdir('D:\\Education\\Hackathones\\photohack\\pravoslavnaya_papka\\photoDNA\\photodna')

    podlozhka = put_element_overlay(36, 804, c_png, podlozhka)

    img = Image.fromarray(podlozhka)

    draw = ImageDraw.Draw(img)

    font1 = ImageFont.truetype("Roboto-Medium.ttf", 70)

    font6 = ImageFont.truetype("Roboto-Medium.ttf", 20)

    font7 = ImageFont.truetype("Roboto-Medium.ttf", 25)

    font8 = ImageFont.truetype("Roboto-Medium.ttf", 25)

    draw.text((843, 70), str(d_n[the_flag]), (154, 154, 160), font=font1)
    gay = 200
    straight = 5
    age = 44
    draw.text((865, 427), str(straight) + '%', '#D63796', font=font6)
    draw.text((865, 463), str(gay) + '%', '#D63796', font=font6)
    draw.text((1016, 421), str(age), '#D63796', font=font7)

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

    if len(the_flag) < 9:
        font3 = ImageFont.truetype("Roboto-Medium.ttf", 35)
    else:
        if len(the_flag) < 12:
            font3 = ImageFont.truetype("Roboto-Medium.ttf", 25)
        else:
            font3 = ImageFont.truetype("Roboto-Medium.ttf", 20)

    if len(flag2) < 9 and len(flag3) < 9:
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
    img = img.convert('RGB')
    # img.save('/var/www/html/backend/photoDNA/photodna/for_posting/' + rand_file_name + '.png')

    return img


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

            norm_red = filter[i, j][0] / 255
            norm_green = filter[i, j][1] / 255
            norm_blue = filter[i, j][2] / 255
            norm_img_red = image[i, j][0] / 255
            norm_img_greed = image[i, j][1] / 255
            norm_transparency = 1 - int(
                (0.299 * image[i, j][2] + 0.587 * image[i, j][1] + 0.114 * image[i, j][0])) / 255

            podlozhka[position_h + i, position_w + j][0] = int(
                255 * ((1 - norm_transparency) * norm_blue + int(norm_transparency * norm_img_red)))
            podlozhka[position_h + i, position_w + j][1] = int(
                255 * ((1 - norm_transparency) * norm_green + int(norm_transparency * norm_img_greed)))
            podlozhka[position_h + i, position_w + j][2] = int(
                255 * ((1 - norm_transparency) * norm_red + int(norm_transparency * image[i, j][2] / 255)))

            # Target.R = ((1 - Source.A) * BGColor.R) + (Source.A * Source.R)
            # Target.G = ((1 - Source.A) * BGColor.G) + (Source.A * Source.G)
            # Target.B = ((1 - Source.A) * BGColor.B) + (Source.A * Source.B)
            # print(image.shape)


            # norm_transparency = 1 - int((0.299 * image[i, j][2] + 0.587 * image[i, j][1] + 0.114 * image[i, j][0])) / 255
            # podlozhka[position_h + i, position_w + j][0] = int(((1 - norm_transparency) * filter[i, j][0]) + int(norm_transparency * image[i, j][0]))
            # podlozhka[position_h + i, position_w + j][1] = int(((1 - norm_transparency) * filter[i, j][1]) + int(norm_transparency * image[i, j][1]))
            # podlozhka[position_h + i, position_w + j][2] = int(((1 - norm_transparency) * filter[i, j][2]) + int(norm_transparency * image[i, j][2]))

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


imag = do_post_shit(base_img)
imag.show()


