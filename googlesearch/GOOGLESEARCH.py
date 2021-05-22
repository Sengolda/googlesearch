import urllib3

def search_google(query):

    querystring = urllib3.request.urlencode({
        'q': query
        })

    full_url = 'https://www.google.com/search?{}'.format(querystring)

    print(full_url)
