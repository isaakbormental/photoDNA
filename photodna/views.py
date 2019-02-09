from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from photodna.beface_adapter import get_analysis
from photodna.pricessing_photo import process
from django.views.generic import View
from django.conf import settings
import os
import json
from photodna.post_fb import do_post_shit
import logging
import random

def photoload(request):
    # index = urllib.request.urlopen('file:../djangoback\static\index.html').read()
    # index = urllib.request.urlopen('file:').read()
    # return HttpResponse(index)
    return render(request, 'photodna\index.html')

@csrf_exempt
def generate_amazon_post(request):
    jsonka = json.loads(request.body.decode('utf-8'))
    # logging.error(jsonka)
    url = do_post_shit(jsonka)
    didi = dict()
    didi['link'] = url
    resp = json.dumps(didi)
    # resp = json.dumps('{' + '"link":' + '"' + url + '"' + '}')
    # logging.error(resp)
    return HttpResponse(resp, content_type="application/json")

@csrf_exempt
def process_image(request):
    content = request.body

    content = json.loads(content.decode('utf-8'))

    # print(content['img'].split(',', 1)[1])
    # encoded_image = content['img'].split(',', 1)[1]
    encoded_image = content['imgUrl']
    # results = json.dumps(get_analysis(encoded_image))
    # results = get_analysis(encoded_image)
    results = process(encoded_image)
    # print(results)
    return HttpResponse(results, content_type="application/json")


class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            ran = random.randint(0, 1)
            # if ran == 0:
            with open(os.path.join(settings.REACT_APP_DIR, 'v1', 'index.html')) as f:
                return HttpResponse(f.read())
            # elif ran == 1:
            #     with open(os.path.join(settings.SECOND_REACT_APP_DIR, 'index.html')) as f:
            #         return HttpResponse(f.read())

        except FileNotFoundError:
            logging.exception('Production build of app not found')
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )