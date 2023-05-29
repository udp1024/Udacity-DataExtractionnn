# Command file to setup CLI for interactive coding in Python for musicbrainz.py app
# python3
# exec(open("JSON/command-line-setup.py").read())

import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}

def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    """
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print("requesting", r.url)
    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()

def query_by_name(url, params, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    """
    params["query"] = "artist:" + name
    return query_site(url, params)

def pretty_print(data, indent=4):
    """
    After we get our output, we can use this function to format it to be more
    readable.
    """
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    else:
        print(data)

results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")

artistCount = 0
itemcount = len(results['artists'])
# for i in range(itemcount):
#     if (results['artists'][i]['name'] == "Queen") and (results['artists'][i]['type'] == 'Group'):
#         print(i, results['artists'][i]['name'], 'id',results['artists'][i]['id'])
#         #artistCount += 1
#         print(i)


i=0
for i in range(itemcount):
    print(results['artists'][i]['name'], results['artists'][i]['type'])
    if (results['artists'][i]['name'] == "One Direction") and (results['artists'][i]['type'] == "Group"):
        print(json.dumps(results["artists"][i]["life-span"]["begin"]))
        break

# numofAliases=len(results['artists'][i]['aliases'])
# j=0
# for j in range(numofAliases):
#     if (results['artists'][i]['aliases'][j]['locale'] == "es"):
#         print(i, j, "es")
#         results['artists'][i]['aliases'][j]['name']
#         break


# print(artistCount)
# print(json.dumps(results, indent=4))
# OneDdatafile = open("OneD-data.json", "w")
# OneDdatafile.write(json.dumps(results, indent=4))
# OneDdatafile.close()
