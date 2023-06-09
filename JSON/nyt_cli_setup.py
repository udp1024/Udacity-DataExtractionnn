# Command file to setup CLI for interactive coding in Python for nytimes.py app
# python3
# exec(open("JSON/nyt_cli_setup.py").read())

import json
import codecs
import requests
from dotenv import load_dotenv
import os

load_dotenv("JSON/.env")

URL_MAIN = "http://api.nytimes.com/svc/"
URL_POPULAR = URL_MAIN + "mostpopular/v2/"
API_KEY = { "popular": os.getenv("api_key_nyt"),
            "article": os.getenv("api_key_nyt")}

def query_site(url, target, offset):
    # This will set up the query with the API key and offset
    # Web services often use offset paramter to return data in small chunks
    # NYTimes returns 20 articles per request, if you want the next 20
    # You have to provide the offset parameter
    if API_KEY["popular"] == "" or API_KEY["article"] == "":
        print("You need to register for NYTimes Developer account to run this program.")
        print("See Intructor notes for information")
        return False
    #params = {"api-key": API_KEY[target], "offset": offset}
    params = {"api-key": API_KEY[target]}
    r = requests.get(url, params = params)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()

    
def get_popular(url, kind, days, section="all-sections", offset=0):
    # This function will construct the query according to the requirements of the site
    # and return the data, or print an error message if called incorrectly
    if days not in [1,7,30]:
        print("Time period can be 1,7, 30 days only")
        return False
    if kind not in ["viewed", "shared", "emailed"]:
        print("kind can be only one of viewed/shared/emailed")
        return False

    #url += "most{0}/{1}/{2}.json".format(kind, section, days)
    url += "{0}/{1}.json".format(kind, days)
    data = query_site(url, "popular", offset)

    return data

def save_file(kind, period):
    # This will process all results, by calling the API repeatedly with supplied offset value,
    # combine the data and then write all results in a file.
    data = get_popular(URL_POPULAR, "viewed", 1)
    num_results = data["num_results"]

    #full_data = []
    with codecs.open("popular-{0}-{1}.json".format(kind, period), encoding='utf-8', mode='w') as v:
        # for offset in range(0, num_results, 20):        
        #     data = get_popular(URL_POPULAR, kind, period, offset=offset)
        #     full_data += data["results"]
        
        # v.write(json.dumps(full_data, indent=2))
        v.write(json.dumps(data, indent=2))

def get_from_file(kind, period):
    filename = "popular-{0}-{1}.json".format(kind, period)
    with open(filename, "r") as f:
        return json.loads(f.read())
    
def article_overview(kind, period):
    data = get_from_file(kind, period)
    titles = []
    urls =[]
    # YOUR CODE HERE

    return (titles, urls)

def article_overview(kind, period):
    data = get_from_file(kind, period)
    titles = []
    urls =[]
    # YOUR CODE HERE
    with open("popular-{0}-{1}.json".format(kind,period), encoding='utf-8', mode='r') as w:
        data = json.load(w)

    for idxResult in range(data['num_results']):
        titles.append({ 'title': data['results'][idxResult]['title'], 'section': data['results'][idxResult]['section'] })
        for idxMedia in range(len(data['results'][idxResult]['media']['media-metadata'])):
            if data['results'][idxResult]['media']['media-metadata'][idxMedia] == 'Standard Thumbnail'
            urls.append({ 'url': data['results'][idxResult]['title']})

    return (titles, urls)

titles, urls = article_overview("viewed", 1)
save_file("viewed",1)
titles, urls = article_overview("viewed", 1)

