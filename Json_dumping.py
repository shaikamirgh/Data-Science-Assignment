import requests
import urllib.parse
import json
import os

from dotenv import load_dotenv
load_dotenv()

MY_AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
print(MY_AUTH_TOKEN)

# Your existing code to formulate the LinkedIn URL
SearchName = "Amir"
linkedin_url = "https://www.linkedin.com/search/results/people/?keywords=" + SearchName + "&origin=SWITCH_SEARCH_VERTICAL&sid=%40%2Co"
linkedin_url = urllib.parse.quote(linkedin_url, safe='')
url = "https://api.lix-it.com/v1/li/linkedin/search/people?url=" + linkedin_url

# Headers with authorization token
headers = {
  'Authorization': MY_AUTH_TOKEN
}

# Making the GET request
response = requests.get(url, headers=headers)

# Extracting JSON data from the response
data = response.json()

# Print the JSON data (optional, for verification)
print(data)

# Saving the JSON data to a file
with open('Linkedin_Data_Dump.json', 'w') as file:
    json.dump(data, file)
