# valuefy/method3-threads.py
# Creates a file named method3.txt containing a list of internal URLs

from valuefy import URL, extract_page_html, format_internal_url, write_to_file
from threading import Thread, Lock
import re

set_of_urls = set()
connection_count = 0


def manage_connection_count(url):

    """
    This function maintains concurrent connection count to 5. It acquires
    and releases lock, and treats connection request as a critical section.
    """

    global connection_count
    lock = Lock()

    while (connection_count > 5):
        pass

    try:
        lock.acquire()
        connection_count += 1
        page = extract_page_html(url)

    except ValueError:
        pass

    finally:
        connection_count -= 1
        lock.release()

    return page


def internal_url_scraper(url):

    """
    This function recursively creates a new thread for each internal URL
    and calls itself inside that thread.
    """

    global set_of_urls

    page = manage_connection_count(url)
    html_body = page.decode().split('head><body')[-1]

    for _url in re.findall('href=".*?"', html_body):

        _url = format_internal_url(_url)
        if _url not in set_of_urls:

            set_of_urls.add(_url)
            write_to_file('method3.txt', _url)

            if 'medium.com' in _url:
                thread = Thread(target=internal_url_scraper, args=(_url,))
                thread.start()

if __name__ == '__main__':

    internal_url_scraper(URL)
