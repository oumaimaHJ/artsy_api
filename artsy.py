import requests
import json
#Connect to the Artsy API
client_id = '325a19edc13ec7f6d3ee'
client_secret = '1e277ff8db2a932477061f4ecbed0d18'


r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })


j = json.loads(r.text)


token = j["token"]

headers = {"X-Xapp-Token": token}
#Web scrapping to the Artists
di = {}
# create a dictionary where we will write the name and year of birth of the artists. For example, id = 52f16a0e8b3b81a5b3000022
# id.txt where the id of the artists is stored. Then we will add id to url and get json and pull data from it
with open('id.txt', 'r') as f:
    for line in f:
        id = str(line.rstrip())
        url = "https://api.artsy.net/api/artists/"
        result = requests.get(url+id, headers=headers)
        result.encoding = 'utf-8'
        data = result.json()
        # print(data)
        birthday = data['birthday']
        name = data["sortable_name"]
        di[name] = birthday
# sorting the years of birth and names received
di_list = list(di.items())
# sorted first by year, then by name
di_list.sort(key=lambda i: (i[1], i[0])) 
# if we want to write the result to a file
with open('artists.txt', 'w', encoding="UTF-8") as d:
    for i in di_list:
        # print(i[0], ':', i[1])
        d.write(i[0])
        d.write('\n')

