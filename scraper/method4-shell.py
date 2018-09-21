# valuefy/method4-shell.py
# Creates a file named method4.txt containing a list of internal URLs

from subprocess import check_output, CalledProcessError
from valuefy import URL, write_to_file

set_of_urls = set()


def run_command(url):

    """
    This is a recursive function which runs the 'lynx' shell command
    for a URL and returns the standard output as a list.
    """

    command = 'lynx -dump -listonly "{}" | grep -o "https:.*"' \
              '| sort -u | grep -vwE "(osd.xml|plus.google.com)"'.format(url)
    std_out = check_output(command, shell=True)

    return std_out.decode().split('\n')


def internal_url_scraper(url):

    """
    This function recursively calls itself for each unique URL returned
    by the run_command() function.
    """

    global set_of_urls

    # stopping condition
    if len(set_of_urls) > 100:
        return

    try:
        urls = run_command(url)
        for _url in urls:

            if _url not in set_of_urls:

                set_of_urls.add(_url)
                write_to_file('method4.txt', _url)

                if 'medium.com' in _url:
                    internal_url_scraper(_url)

    except CalledProcessError:
        pass

if __name__ == '__main__':

    internal_url_scraper(URL)
