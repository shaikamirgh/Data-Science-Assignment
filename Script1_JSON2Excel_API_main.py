import pandas as pd
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
#
# Making the GET request
response = requests.get(url, headers=headers)

# Extracting JSON data from the response
data = response.json()

# Print the JSON data (optional, for verification)
print(data)

# Saving the JSON data to a file
with open('linkedin_data.json', 'w') as file:
    json.dump(data, file)

# Assuming 'data' is your JSON response
elements = data["response"]["elements"]
extracted_data = []

for element in elements:
    items = element.get("items", [])
    for item in items:
        entity_result = item.get("itemUnion", {}).get("entityResult", {})
        if entity_result:
            name = entity_result.get("title", {}).get("text", "")
            position = entity_result.get("primarySubtitle", {}).get("text", "")
            location = entity_result.get("secondarySubtitle", {}).get("text", "")
            connection_details = entity_result.get("badgeText", {}).get("text", "")
            summary = entity_result.get("summary", {}).get("text", "")
            profile_url = entity_result.get("navigationUrl", "")
            image_attribute = entity_result.get("image", {}).get("attributes", [{}])[0]
            profile_image_url = image_attribute.get("detailDataUnion", {}).get("nonEntityProfilePicture", {}).get("vectorImage", {}).get("artifacts", [{}])[0].get("fileIdentifyingUrlPathSegment", "")

            extracted_data.append({
                "Name": name,
                "Position": position,
                "Location": location,
                "Connection Details": connection_details,
                "Summary": summary,
                "Profile URL": profile_url,
                "Profile Image URL": profile_image_url
            })

df = pd.DataFrame(extracted_data)
df.to_excel("linkedin_profiles.xlsx", index=False)
