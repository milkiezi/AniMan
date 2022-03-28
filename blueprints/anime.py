from flask import Blueprint, render_template, Flask, request
import json
import requests

anime = Blueprint('anime', __name__)

@anime.route('/anime')
def animes():
    ani = request.args.get('ani')
    cate = request.args.get('cate')

    if (not ani) and (not cate):
        url = "https://kitsu.io/api/edge/anime?page[limit]=20&page[offset]=0&sort=-startDate"
    elif cate and (not ani):
        url = "https://kitsu.io/api/edge/anime?page[limit]=20&page[offset]=0&sort=-startDate&filter[categories]={}".format(cate)
    elif ani and (not cate):
        url = "https://kitsu.io/api/edge/anime?page[limit]=20&page[offset]=0&filter[text]={}".format(ani)
    else:
        url = "https://kitsu.io/api/edge/anime?page[limit]=20&page[offset]=0&filter[text]={0}&filter[categories]={1}".format(ani, cate)
    

    anime = get_anime(url)

    return render_template("anime.html", anime = anime)


def get_anime(url):
    headers = {
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
    }

    data = requests.get(url, headers=headers).json()
    anime = list()

    for i in range(len(data['data'])):
        slug = data['data'][i]['attributes']['slug']
        name = data['data'][i]['attributes']['canonicalTitle']
        urlImg = data['data'][i]['attributes']['posterImage']['small']
        synopsis = data['data'][i]['attributes']['synopsis']

        anime.append({"slug":slug, "name":name, "urlImg":urlImg, "synopsis":synopsis})
            
    return anime