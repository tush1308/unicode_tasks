from django.http.response import HttpResponse
import requests 
import json


def index(request):
    def query(url):
        # url = "http://pokeapi.co/api/v2/pokemon/"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            a=data['results']
            l=len(a)
            lst=[]
            
            for i in range(l):
                lst.append(a[i]["name"])
            return [lst]


        else:
            return ("An error occurred querying the API")

    return HttpResponse(query("http://pokeapi.co/api/v2/pokemon/"))
