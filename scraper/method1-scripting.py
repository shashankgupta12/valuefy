# valuefy/method1-scripting.py
# Creates a file named method1.txt containing a list of internal URLs

from valuefy import URL, extract_page_html, format_internal_url, write_to_file
import re


def internal_url_scraper(url, set_of_urls, list_of_urls):

    """
    This function extracts and appends unique internal URLS to the master list,
    so that the iteration continues as long as there are internal URLS.
    """

    for url in list_of_urls:

        try:
            page = extract_page_html(url)
            html_body = page.decode().split('head><body')[-1]

        except:
            pass

        for _url in re.findall('href=".*?"', html_body):

            _url = format_internal_url(_url)
            if _url not in set_of_urls:

                set_of_urls.add(_url)
                write_to_file('method1.txt', _url)
                print(_url)

                if 'medium.com' in _url:
                    list_of_urls.append(_url)

        if len(list_of_urls) > 1000:
            break

if __name__ == '__main__':

    set_of_urls = {URL}
    list_of_urls = [URL]
    internal_url_scraper(URL, set_of_urls, list_of_urls)
