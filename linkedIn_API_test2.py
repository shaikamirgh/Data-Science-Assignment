import requests
import urllib.parse

SearchName= "Amir"

linkedin_url = "https://www.linkedin.com/search/results/people/?keywords="+SearchName+"&origin=SWITCH_SEARCH_VERTICAL&sid=%40%2Co"
print(linkedin_url)
# https://www.linkedin.com/search/results/people/?keywords=Amir&origin=SWITCH_SEARCH_VERTICAL&sid=%40%2Co
# encode the URL
linkedin_url = urllib.parse.quote(linkedin_url, safe='')

url = "https://api.lix-it.com/v1/li/linkedin/search/people?url=" + linkedin_url


payload={}
headers = {
  'Authorization': "Qz9opBFXKURQh97JBniRdFY8NmkKI4lHypNhUNreKuvCtWcnnWVJBeS89ZSG"
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())

#Qz9opBFXKURQh97JBniRdFY8NmkKI4lHypNhUNreKuvCtWcnnWVJBeS89ZSG