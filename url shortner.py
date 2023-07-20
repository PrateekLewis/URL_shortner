import requests

def shorten_link(full_link, link_name):
    # API details
    API_KEY = '4da73951b61344cbba443b080acfef83d1c16'
    BASE_URL = 'https://cutt.ly/api/api.php'

    # Prepare the payload for the API request
    payload = {'key' : API_KEY, 'short' : full_link, 'name' : link_name}

    # Send the API request to the Cutt.ly service
    response = requests.get(BASE_URL, params=payload)
    data = response.json()

    print('')

    try:
        # Check if the API returned a valid response with the shortened link
        if 'url' in data and 'title' in data['url'] and 'shortLink' in data['url']:
            title = data['url']['title']
            short_link = data['url']['shortLink']

            print('Title:', title)
            print('Link:', short_link)
        else:
            # If the API response does not contain the expected data, print an error message
            print('Error: Unable to shorten the link.')
    except:
        # Handle any exceptions that may occur during the API response parsing
        status = data['url']['status']
        print('Error Status:', status)

# User input for the long URL and custom name
link = input('Enter a link: >> ')
name = input('Give your link a name (optional): >> ')

# Call the function to generate the shortened link
shorten_link(link, name)
