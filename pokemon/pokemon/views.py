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
            dict1={}
            for i in range(l):
                lst.append(a[i]["name"])
                # #bonus
                # resource_url=a[i]["url"]
                # url1=resource_url
                # response = requests.get(url1)
                # if response.status_code==200:
                #     newdata=json.loads(response.text)
                #     typ=newdata["types"][0]["type"]["name"]
                #     print("Pokemon Type=",typ)
                #     dict1(a[i]["name"],newdata["types"][0]["type"]["name"])

                # else: print("Error occured")
            return [lst]


        else:
            return ("An error occurred querying the API")

    return HttpResponse(query("http://pokeapi.co/api/v2/pokemon/"))
