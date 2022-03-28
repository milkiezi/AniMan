from flask import Blueprint, render_template, Flask, request
import json
import requests

home = Blueprint('home', __name__)

@home.route('/')
def index():
    urlAni = "https://kitsu.io/api/edge/trending/anime"
    urlMan = "https://kitsu.io/api/edge/trending/manga"
    headers = {
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
    }
    dataAni = requests.get(urlAni, headers=headers).json()
    dataMan = requests.get(urlMan, headers=headers).json()

    topanime = list()
    topmanga = list()

    for i in range(0,8):
        slugAni = dataAni['data'][i]['attributes']['slug']
        nameAni = dataAni['data'][i]['attributes']['titles']['en']
        urlImgAni = dataAni['data'][i]['attributes']['posterImage']['small']
        popularAni = dataAni['data'][i]['attributes']['popularityRank']
        ratingAni = dataAni['data'][i]['attributes']['ratingRank']

        topanime.append({"slug":slugAni, "name":nameAni, "urlImg":urlImgAni, "popular":popularAni, "rating":ratingAni})


        slugMan = dataMan['data'][i]['attributes']['slug']
        nameMan = dataMan['data'][i]['attributes']['titles']['en']
        urlImgMan = dataMan['data'][i]['attributes']['posterImage']['small']
        popularMan = dataMan['data'][i]['attributes']['popularityRank']
        ratingMan = dataMan['data'][i]['attributes']['ratingRank']

        topmanga.append({"slug":slugMan, "name":nameMan, "urlImg":urlImgMan, "popular":popularMan, "rating":ratingMan})
            
    return render_template("home.html", topanime=topanime, topmanga=topmanga)