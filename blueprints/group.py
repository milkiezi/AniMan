from flask import Blueprint, render_template
import json
import requests

group = Blueprint('group', __name__)

@group.route('/group')
def gro():
    url = "https://kitsu.io/api/edge/groups?filter[category]=anime-manga&filter[privacy]=open&sort=-membersCount"
    headers = {
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
    }
    data = requests.get(url, headers=headers).json()
    group = list()

    for i in range(len(data['data'])):
        createdAt = data['data'][i]['attributes']['createdAt']
        slug = data['data'][i]['attributes']['slug']
        about = data['data'][i]['attributes']['about']
        membersCount = data['data'][i]['attributes']['membersCount']
        name = data['data'][i]['attributes']['name']
        avatar = data['data'][i]['attributes']['avatar']['medium']
        
        group.append({"createdAt":createdAt, "slug":slug, "about":about, "membersCount":membersCount, "name":name, "avatar":avatar})

    return render_template("group.html", group = group)