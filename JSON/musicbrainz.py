"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""
import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"


# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
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


def main():
    """
    Below is an example investigation to help you get started in your
    exploration. Modify the function calls and indexing below to answer the
    questions on the next quiz.

    1. How many bands named "First Aid Kit"?
    2. Begin-Area Name for Queen?
    3. Spanish Alias for Beatles?
    4. Nirvana disambiguation?
    5. When was one direction formed?

    HINT: Note how the output we get from the site is a multi-level JSON
    document, so try making print statements to step through the structure one
    level at a time or copy the output to a separate output file. Experimenting
    and iteration will be key to understand the structure of the data!
    """

    # Query for information in the database about bands named Nirvana
    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    pretty_print(results)

    # Isolate information from the 4th band returned (index 3)
    print("\nARTIST:")
    pretty_print(results["artists"][3])

    # Query for releases from that band using the artist_id
    artist_id = results["artists"][3]["id"]
    artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
    releases = artist_data["releases"]

    # Print information about releases from the selected band
    print("\nONE RELEASE:")
    pretty_print(releases[0], indent=2)

    release_titles = [r["title"] for r in releases]
    print("\nALL TITLES:")
    for t in release_titles:
        print(t)

if __name__ == '__main__':
    main()

# 1. How many bands named "First Aid Kit"?
    # results['artists'][0].keys()
    # print(results['artists'][0]["name"])
    # len(results['artists'])
    artistCount = 0
    itemcount = len(results['artists'])
    for i in range(itemcount):
        if results['artists'][i]['name'] == "First Aid Kit":
            print(i, results['artists'][i]['name'], 'id',results['artists'][i]['id'])
            artistCount += 1


    print(artistCount)

# 2. Begin-Area Name for Queen?
    # print(results["artists"][0]["begin-area"]["name"])
i=0
for i in range(itemcount):
    print(results['artists'][i]['name'], results['artists'][i]['type'])
    if (results['artists'][i]['name'] == "Queen") and (results['artists'][i]['type'] == "Group"):
        print(i, results['artists'][i]['begin-area']['name'])
        break

# 3. Spanish Alias for Beatles?
i=0
for i in range(itemcount):
    print(results['artists'][i]['name'], results['artists'][i]['type'])
    if (results['artists'][i]['name'] == "The Beatles") and (results['artists'][i]['type'] == "Group"):
        print(i)
        break

numofAliases=len(results['artists'][i]['aliases'])
j=0
for j in range(numofAliases):
    if (results['artists'][i]['aliases'][j]['locale'] == "es"):
        print(i, j, "es")
        results['artists'][i]['aliases'][j]['name']
        break
    
# 4. Nirvana disambiguation?
    # results["artists"][0]["disambiguation"]
    # >>> '90s US grunge band'
i=0
for i in range(itemcount):
    print(results['artists'][i]['name'], results['artists'][i]['type'])
    if (results['artists'][i]['name'] == "Nirvana") and (results['artists'][i]['type'] == "Group"):
        print(json.dumps(results["artists"][i]["disambiguation"]))
        break

# 5. When was one direction formed?
# # Q4 
i=0
for i in range(itemcount):
    print(results['artists'][i]['name'], results['artists'][i]['type'])
    if (results['artists'][i]['name'] == "One Direction") and (results['artists'][i]['type'] == "Group"):
        print(json.dumps(results["artists"][i]["life-span"]["begin"]))
        break
"2010-07-23"



