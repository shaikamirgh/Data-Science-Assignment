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
    print(soup)
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))
    # Extract relevant information from the search results
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
    search_text = input("Enter the search text: ")

    # Scrape LinkedIn search results
    results = scrape_linkedin(search_text)[:10]  # Limit to the first 10 results

    # Create a DataFrame from the scraped data
    df = pd.DataFrame(results)

    # Save the DataFrame to an Excel file
    df.to_excel(f"{search_text}_linkedin_results.xlsx", index=False)
    print("Results saved to Excel file.")

if __name__ == "__main__":
    main()
