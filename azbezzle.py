import os
import sys
from bs4 import BeautifulSoup
import requests
import urllib.request as urlreq
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="The URL you want to analyze.")
parser.add_argument("--id", help="Your Amazon Associate ID")
args = parser.parse_args()

if args.id:
    AFF_TAG = args.id
else:
    AFF_TAG = input("What is your Amazon Affiliate tag? ")

PAGE_URL = args.url

#PAGE_URL = input("What is the URL you want to check? ")

def links(url):
    html = requests.get(url).content
    bsObj = BeautifulSoup(html, features='lxml')

    links = bsObj.findAll('a')
    finalLinks = []
    amt_of_links = len(links)
    the_index = 0
    for link in links:
        percent_done = round(the_index / amt_of_links * 100)
        os.system('clear')
        print(str(percent_done) + "% done checking links")
        link = str(link.attrs['href'])
        if "amazon." in link:
            finalLinks.append(link)
        elif "amzn.to" in link:
            req = urlreq.Request(
                link,
                data=None,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )
            truelink = urlreq.urlopen(req)
            fullURL = truelink.url
            finalLinks.append(fullURL)
        the_index += 1
    return finalLinks

def get_unowned_links(links):
    the_links = []
    for link in links:
        if str(AFF_TAG) not in str(link):
            the_links.append(link)
    return the_links

azon_links_on_page = links(PAGE_URL)
unowned_links = get_unowned_links(azon_links_on_page)

if len(unowned_links) == 0:
    print("Hurray! You own all of the links")
else:
    print("Here are unowned links on the URL you provided:")
    for link in unowned_links:
        print("* " + link)
