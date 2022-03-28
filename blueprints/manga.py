from flask import Blueprint, render_template, Flask, request
import json
import requests

manga = Blueprint('manga', __name__)

@manga.route('/manga')
def man():
    man = request.args.get('man')
    cate = request.args.get('cate')

    if (not man) and (not cate):
        url = "https://kitsu.io/api/edge/manga?page[limit]=20&page[offset]=0&sort=-startDate"
    elif cate and (not man):
        url = "https://kitsu.io/api/edge/manga?page[limit]=20&page[offset]=0&sort=-startDate&filter[categories]={}".format(cate)
    elif man and (not cate):
        url = "https://kitsu.io/api/edge/manga?page[limit]=20&page[offset]=0&filter[text]={}".format(man)
    else:
        url = "https://kitsu.io/api/edge/manga?page[limit]=20&page[offset]=0&filter[text]={0}&filter[categories]={1}".format(man, cate)
    

    manga = get_manga(url)

    return render_template("manga.html", manga = manga)


def get_manga(url):
    headers = {
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
    }

    data = requests.get(url, headers=headers).json()
    manga = list()

    for i in range(len(data['data'])):
        slug = data['data'][i]['attributes']['slug']
        name = data['data'][i]['attributes']['canonicalTitle']
        urlImg = data['data'][i]['attributes']['posterImage']['small']
        synopsis = data['data'][i]['attributes']['synopsis']
        synopsis = data['data'][i]['attributes']['synopsis']

        manga.append({"slug":slug, "name":name, "urlImg":urlImg, "synopsis":synopsis})
            
    return manga