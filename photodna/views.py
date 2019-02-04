from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from photodna.beface_adapter import get_analysis
from django.views.generic import View
from django.conf import settings
import logging
import os
import json


def photoload(request):
    # index = urllib.request.urlopen('file:../djangoback\static\index.html').read()
    # index = urllib.request.urlopen('file:').read()
    # return HttpResponse(index)
    return render(request, 'photodna\index.html')


@csrf_exempt
def process_image(request):
    content = request.body
    # print(content)
    print('_____________________')
    content = json.loads(content.decode('utf-8'))

    # print(content['img'].split(',', 1)[1])
    encoded_image = content['img'].split(',', 1)[1]
    # return get_analysis(encoded_image)
    # return HttpResponse('<h2>prinyal</h2>')
    # results = json.dumps(get_analysis(encoded_image))
    results = get_analysis(encoded_image)
    print(results)
    print(type(results))
    return HttpResponse(results, content_type="application/json")


class FrontendAppView(View):
    """
    Serves the compiled frontend entry point (only works if you have run `yarn
    run build`).
    """

    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP_DIR, 'index.html')) as f:
                return HttpResponse(f.read())
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