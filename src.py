import requests
from UrlObj import Url


def web_scrape(url: Url, limit: str):

    try:
        r = requests.get(url.name)

        # print(r.text)
        urls = []

        for line in r.text.splitlines():    # iterates through html request line by line

            if line.__contains__("http"):
                i = line.find("http")
                e = i
                while line.find("http", i) != -1 and e <= len(line) and i <= len(line): # finds first pattern match
                    i = line.find("http", i)                                            # and sets end of string
                    e = i                                                               # further by scanning it
                    try:                                                                # for escape characters
                        while not "\" <>(){}\'[]*;\\".__contains__(line[e]):
                            e += 1
                    except Exception as err:
                        pass
                    u = line[i:e]
                    if not urls.__contains__(u) and not u.__contains__("\/") and not u.__contains__("https?") \
                            and u.__contains__(".") and u.__contains__("://") and u.__contains__(limit):
                        urls.append(Url(u))
                    i = e

        return urls     # returns all found URLs as objects
    except requests.exceptions.ConnectionError:
        url.flag = 3  # marks unreachable urls
        return False

