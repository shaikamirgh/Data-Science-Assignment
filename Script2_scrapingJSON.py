import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def scrape_linkedin(search_text):
    with open('cookies.json', 'r') as file:
        cookies = json.load(file)
    session = requests.Session()
    session.cookies.update(cookies)
    

    search_url = f"https://www.linkedin.com/search/results/people/?keywords={search_text}&origin=SWITCH_SEARCH_VERTICAL&sid=%40%2Co"
    print(search_url)

    # Make the request to LinkedIn and get the HTML content
    response = session.get(search_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)

    # Extract relevant information from the search results
        
    code_tag = soup.find('code', {"id":"bpr-guid-2887896"} )
    print(code_tag)
    if code_tag:
        # Extract the JSON string and load it into a Python dictionary
        json_data = json.loads(code_tag.get_text())
        with open('linkedin_scrape.json', 'w') as file:
            json.dump(json_data, file)

    search_results = []
    for item in soup.find_all('li', class_='search-result'):
        name = item.find('span', class_='actor-name').text.strip()
        connection_details = item.find('span', class_='dist-value').text.strip()
        job_title = item.find('p', class_='subline-level-1').text.strip()

        search_results.append({
            "Name": name,
            "Connection Details": connection_details,
            "Job Title": job_title
        })

    return search_results

def main():
    # Get input search text
    search_text = "Bob" #input("Enter the search text: ")

    # Scrape LinkedIn search results
    results = scrape_linkedin(search_text)[:10]  # Limit to the first 10 results

    # Create a DataFrame from the scraped data
    df = pd.DataFrame(results)

    # Save the DataFrame to an Excel file
    df.to_excel(f"{search_text}_linkedin_results.xlsx", index=False)
    print("Results saved to Excel file.")

if __name__ == "__main__":
    main()
