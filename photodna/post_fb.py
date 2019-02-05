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

os.chdir('/var/www/html/backend/photoDNA/photodna')

def do_post_shit(jason):
    logging.error('DoOING POSTING SHITTING')
    logging.error(os.getcwd())
    logging.error(str(os.listdir(os.getcwd())))
    podlozhka = cv2.imread('gay_krug.png', cv2.IMREAD_UNCHANGED)
    for i in range(podlozhka.shape[0]):
        for j in range(podlozhka.shape[1]):
            temp = podlozhka[i, j][0]
            podlozhka[i, j][0] = podlozhka[i, j][2]
            podlozhka[i, j][2] = temp
    # im = Image.open('gay_krug.png')
    # podlozhka = np.array(im)
    # podlozhka = podlozhka[:, :, ::-1].copy()
    # podlozhka = pil_image_to_cv(im)
    logging.error('PROCHITAL')
    # json_data = open('data.json').read()

    characteristics = jason
    logging.error(characteristics['data']['nationality'][0]['confidence'])
    the_list_v = (characteristics['data']['nationality'][0]['confidence'], characteristics['data']['nationality'][1]['confidence'],
                  characteristics['data']['nationality'][2]['confidence'])

    d_n = defaultdict(int)
    if (characteristics['data']['nationality'][0]['confidence'] == max(the_list_v)):
        the_flag = characteristics['data']['nationality'][0]['name']
        d_n[the_flag] = characteristics['data']['nationality'][0]['confidence']
        if (characteristics['data']['nationality'][1]['confidence'] > characteristics['data']['nationality'][2]['confidence']):
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
        if (characteristics['data']['nationality'][1]['confidence'] == max(the_list_v)):
            the_flag = characteristics['data']['nationality'][1]['name']
            d_n[the_flag] = characteristics['data']['nationality'][1]['confidence']
            if (characteristics['data']['nationality'][0]['confidence'] > characteristics['data']['nationality'][2]['confidence']):
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
            the_flag = characteristics['data']['nationality'][2]['name']
            d_n[the_flag] = characteristics['data']['nationality'][2]['confidence']
            if (characteristics['data']['nationality'][1]['confidence'] > characteristics['data']['nationality'][0]['confidence']):
                flag2 = characteristics['data']['nationality'][1]['name']
                flag3 = characteristics['data']['nationality'][0]['name']
                d_n[flag2] = characteristics['data']['nationality'][0]['confidence']
                d_n[flag3] = characteristics['data']['nationality'][1]['confidence']
            else:
                flag2 = characteristics['data']['nationality'][1]['name']
                flag3 = characteristics['data']['nationality'][0]['name']
                d_n[flag2] = characteristics['data']['nationality'][1]['confidence']
                d_n[flag3] = characteristics['data']['nationality'][0]['confidence']

    root = os.getcwd()
    logging.error(root)
    # os.path.join(root, 'for')
    if (characteristics['data']['gender'] == 'male'):
        # sexim = Image.open(os.path.join('for_posting','orientation_gender_age','mars.png'))
        # sex = pil_image_to_cv(sexim)
        # sex = cv2.imread(root + '/for_posting/orientation_gender_age/mars.png', 1)
        sex = cv2.imread('/var/www/html/backend/photoDNA/photodna/for_posting/orientation_gender_age/mars.png', 1)
        podlozhka = put_element_overlay(458, 1020, sex, podlozhka)
    else:
        # sex = cv2.imread(root + '/for_posting/orientation_gender_age/venus.png', 1)
        sex = cv2.imread('/var/www/html/backend/photoDNA/photodna/for_posting/orientation_gender_age/venus.png', 1)
        # sexim = Image.open(os.path.join('for_posting', 'orientation_gender_age', 'venus.png'))
        # sex = pil_image_to_cv(sexim)
        podlozhka = put_element_overlay(458, 1020, sex, podlozhka)

    # image = cv2.imread(root + "/irish.jpg", 0)
    logging.error(len(characteristics['img']))
    image = string_to_image(characteristics['img'].split(',', 1)[1])

    '''
    618/630-коэффициент



    '''

    vis_shir = float(image.shape[0] / image.shape[1])
    logging.error(vis_shir)
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
    logging.error('Before resize')
    new = cv2.resize(crop_img, (res_shir, res_vis), interpolation=cv2.INTER_AREA)
    # new = Image.fromarray(crop_img)
    # new = new.resize((res_shir, res_vis))
    # new = pil_image_to_cv(new)


    logging.error('Resize ready')
    # the_filter = cv2.imread(root + '/for_posting/picture/filter.png', cv2.IMREAD_UNCHANGED)
    # the_filter_im = Image.open(os.path.join('for_posting', 'picture', 'filter.png'))
    # the_filter = pil_image_to_cv(the_filter_im)
    the_filter = cv2.imread('/var/www/html/backend/photoDNA/photodna/for_posting/picture/filter.png', cv2.IMREAD_UNCHANGED)
    logging.error('Filter read')

    # logging.error(the_filter.shape, podlozhka.shape, new.shape)
    logging.error(str(the_filter.shape) + ' - filter')
    logging.error(str(podlozhka.shape) + ' - podlozhka')
    logging.error(str(new.shape) + ' - new')
    podlozhka = put_picture_and_filter(int((630 - new.shape[0]) / 2), int((618 - new.shape[1]) / 2), the_filter, new,
                                       podlozhka)

    os.chdir(os.getcwd() + "/for_posting/flags/")
    logging.error(os.getcwd())
    index_list = []
    for file in glob.glob("*.png"):
        if (file[:-4] == the_flag):
            # true_flag = cv2.imread(root + "/for_posting/flags/" + file, 1)
            # true_flag_im = Image.open(os.path.join(root, 'for_posting', 'flags', file))
            # true_flag = pil_image_to_cv(true_flag_im)
            true_flag = cv2.imread("/var/www/html/backend/photoDNA/photodna/for_posting/flags/" + file, 1)
            resized = cv2.resize(true_flag, (190, 111), interpolation=cv2.INTER_AREA)
            podlozhka = put_element_overlay(flg1, flg2, resized, podlozhka)

    c_png = cv2.imread("/var/www/html/backend/photoDNA/photodna/circle.png", 1)
    os.chdir('/var/www/html/backend/photoDNA/photodna')
    # c_png_im = Image.open('circle.png')
    # c_png = pil_image_to_cv(c_png_im)
    logging.error('Circle read')
    podlozhka = put_element_overlay(36, 804, c_png, podlozhka)

    # cv2.imwrite(root + '/for_posting/post.png', podlozhka)
    img = Image.fromarray(podlozhka)
    logging.error('imgigig')
    # img = Image.open(root + '/for_posting/post.png')
    # os.remove(root + '/for_posting/post.png')
    draw = ImageDraw.Draw(img)

    # os.chdir(root)

    font1 = ImageFont.truetype("Roboto-Medium.ttf", 70)

    font6 = ImageFont.truetype("Roboto-Medium.ttf", 20)

    font7 = ImageFont.truetype("Roboto-Medium.ttf", 25)

    font8 = ImageFont.truetype("Roboto-Medium.ttf", 25)
    logging.error('Ya prochital fonts')

    draw.text((843, 70), str(d_n[the_flag]), (154, 154, 160), font=font1)

    draw.text((865, 427), str(characteristics['data']['straight']) + '%', '#D63796', font=font6)
    draw.text((865, 463), str(characteristics['data']['gay']) + '%', '#D63796', font=font6)
    draw.text((1016, 421), str(characteristics['data']['age']), '#D63796', font=font7)

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
    #root + '/for_posting/final.png'
    img.save('/var/www/html/backend/photoDNA/photodna/for_posting/final.png')
    # with open('/var/www/html/backend/photoDNA/photodna/for_posting/final.png', 'w') as fi:
    #     img.save(fi)
    # img.save('/var/www/html/backend/photoDNA/photodna/for_posting/final.png', format='PNG')
    # img.tobytes()
    logging.error('I saved!')
    session = boto3.Session(
        aws_access_key_id=SUCHII_KEY,
        aws_secret_access_key=IDIOTSKII_KEY,
    )
    s3 = session.client('s3')

    #'/for_posting/final.png'
    with open('/var/www/html/backend/photoDNA/photodna/for_posting/final.png', 'rb') as data:
        s3.upload_fileobj(data, 'storage.ws.pho.to', 'photohack/stckrs/final-test-9.png')
    # potim v amazon + return url
    return 'http://storage.ws.pho.to/photohack/stckrs/final-test-9.png'


def put_element_overlay(position_h,position_w,elelment,podlozhka):
    logging.error('Put_elemet_overlay')
    for i in range(elelment.shape[0]):
        for j in range(elelment.shape[1]):
            # if(i<2 and j<2):
            #     logging.error(podlozhka[i][j])
            if ((elelment[i, j][0]==0) and(elelment[i, j][1]==0)and (elelment[i, j][2] == 0)):
                podlozhka[position_h + i, position_w + j][0] = 255
                podlozhka[position_h + i, position_w + j][1] = 255
                podlozhka[position_h + i, position_w + j][2] = 255
            else:
                podlozhka[position_h+i, position_w+ j][0] = elelment[i, j][2]
                podlozhka[position_h+i, position_w+ j][1] = elelment[i, j][1]
                podlozhka[position_h+i, position_w+ j][2] = elelment[i, j][0]
                podlozhka[position_h + i, position_w + j][3]=255
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
                podlozhka[position_h + i, position_w + j][3] = elelment[i, j][3]
    return podlozhka

def put_picture_and_filter(position_h,position_w,filter,image,podlozhka):
    for i in range (image.shape[0]):
        for j in range (image.shape[1]):
            podlozhka[position_h+i, position_w+ j][0] = 255 - filter[i,j][2]
            podlozhka[position_h+i, position_w+ j][1] = 255 - filter[i,j][1]
            podlozhka[position_h+i, position_w+ j][2] = 255 - filter[i,j][0]
            podlozhka[position_h + i, position_w + j][3] = 255 - int((image[i,j][0] + image[i,j][1] + image[i,j][2])/3)
    return podlozhka


def string_to_image(base64_string):
    imgdata = base64.b64decode(base64_string)
    cvimg = Image.open(BytesIO(imgdata))
    open_cv_image = np.array(cvimg)
    return open_cv_image[:, :, ::-1].copy()


def pil_image_to_cv(pil_image):
    podlozhka = np.array(pil_image)
    return podlozhka[:, :, ::-1].copy()