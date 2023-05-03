import requests
import json


# Make a GET request to the API URL
response = requests.get("https://programming-quotesapi.vercel.app/api/random")

# Check if the request was successful
if response.status_code == 200:
    # If it was, get the quote from the response JSON
    data = response.json()
    # Print the quote to the console
    print(data)
else:
    # If the request was not successful, print an error message
    print(f"Error: {response.status_code}")
