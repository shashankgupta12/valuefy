# valuefy/valuefy.py

URL = 'https://medium.com/'


def write_to_file(file_name, url):

    """This function writes the received url to the received file name."""

    with open(file_name, 'a') as myfile:
        myfile.write('{}\n'.format(url))


def format_internal_url(url):

    """This function formats an internal path to a valid URL."""

    url = url.split('"')[-2]

    if not url.startswith('https:'):
        url = (
            'https://medium.com{}'.format(url) if not url.startswith('//medium.com')
            else 'https:{}'.format(url))

    return url


def extract_page_html(url):

    """This function makes a request to the passed url and extracts its html."""

    from urllib.request import Request, urlopen

    request_headers = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url, headers=request_headers)
    page = urlopen(req).read()

    return page
    