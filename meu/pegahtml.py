import requests

def get_html(url):
    """
    Gets html text for the given url
    """
    response = requests.get(url)
    return response.text  # Converts the response into text and return it