import requests
import urllib.parse
import json

# Your existing code to formulate the LinkedIn URL
SearchName = "Amir"
linkedin_url = "https://www.linkedin.com/search/results/people/?keywords=" + SearchName + "&origin=SWITCH_SEARCH_VERTICAL&sid=%40%2Co"
linkedin_url = urllib.parse.quote(linkedin_url, safe='')
url = "https://api.lix-it.com/v1/li/linkedin/search/people?url=" + linkedin_url

# Headers with authorization token
headers = {
  'Authorization': "Qz9opBFXKURQh97JBniRdFY8NmkKI4lHypNhUNreKuvCtWcnnWVJBeS89ZSG"
}

# Making the GET request
response = requests.get(url, headers=headers)

# Extracting JSON data from the response
data = response.json()

# Print the JSON data (optional, for verification)
print(data)

# Saving the JSON data to a file
with open('linkedin_data.json', 'w') as file:
    json.dump(data, file)
