# valuefy/method2-recursion.py
# Creates a file named method2.txt containing a list of internal URLs

from valuefy import URL, extract_page_html, format_internal_url, write_to_file
import re

set_of_urls = set()


def internal_url_scraper(url):

    """This function recursively calls itself for each unique URL"""

    global set_of_urls

    # stopping condition
    if len(set_of_urls) > 100:
        return

    try:
        page = extract_page_html(url)
        html_body = page.decode().split('head><body')[-1]

    except ValueError:
        return

    for _url in re.findall('href=".*?"', html_body):

        _url = format_internal_url(_url)
        if _url not in set_of_urls:

            set_of_urls.add(_url)
            write_to_file('method2.txt', _url)

            if 'medium.com' in _url:
                internal_url_scraper(_url)

if __name__ == '__main__':

    internal_url_scraper(URL)
