import requests
import csv
import logging

def get_linkedin_data(first_name, last_name, access_token):
    try:
        url = f"https://api.linkedin.com/v2/people/(first_name:{first_name},last_name:{last_name})"
        headers = {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        logging.error("Error occurred in API call", exc_info=True)
        return None


def main():
    access_token = "ACCESS_TOKEN"
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    data = get_linkedin_data(first_name, last_name, access_token)
    if data:
        print(data)

if __name__ == "__main__":
    main()
