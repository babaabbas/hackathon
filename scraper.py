import requests
from bs4 import BeautifulSoup


def get_text_from_url(url):
    # Fetch the content of the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from the parsed HTML
    text = soup.get_text(separator='\n', strip=True)

    return text


if __name__ == "__main__":
    url = 'https://www.alkimi.org/how-it-works'
    text = get_text_from_url(url)
    print(text)
