#-*- coding: utf-8 -*-
import json

import sys,io,os
import django


sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doecoproject.settings")
django.setup()

from doeco_app.models import Ecospot

def parsing():

    with open('static/data.json') as json_file:
        json_data = json.load(json_file)

    post = []

    for i in range(10):
        post.append({
            "GRP_NM" : json_data['Nfcogzenvrn'][i]["GRP_NM"],
            "REFINE_LOTNO_ADDR" : json_data['Nfcogzenvrn'][i]["REFINE_LOTNO_ADDR"],
            "REFINE_WGS84_LOGT" : json_data['Nfcogzenvrn'][i]["REFINE_WGS84_LOGT"],
            "REFINE_WGS84_LAT" : json_data['Nfcogzenvrn'][i]["REFINE_WGS84_LAT"]

        })

    return post


if __name__ == '__main__':
    post = parsing()

    for i in range(len(post)):
        Ecospot(
            name=post[i][ "GRP_NM"],
            location=post[i]["REFINE_LOTNO_ADDR"],
            latitude=post[i]["REFINE_WGS84_LOGT"],
            longitude=post[i]["REFINE_WGS84_LAT"]
        ).save()