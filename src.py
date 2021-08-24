import requests


class Src:

    def web_scrape(url, limit: str):

        hoopla_counter = 0

        try:
            r = requests.get(url)

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
                            # print(err)
                            hoopla_counter += 1
                        u = line[i:e]
                        if not urls.__contains__(u) and not u.__contains__("\/") and not u.__contains__("https?") \
                                and u.__contains__(".") and u.__contains__("://") and u.__contains__(limit):
                            urls.append(u)
                        i = e

            return urls     # returns all found URLs
        except requests.exceptions.ConnectionError:
            return []

