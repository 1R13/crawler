import requests
import datetime


class WebScraper:

    # Initializes Session with provided parameters
    def __init__(self, root_url, level: int, restrain: str):
        self.search_hits = []
        self.found_urls = []
        self.root_url = root_url
        self.level = level
        self.time_start = datetime.datetime.now()
        self.restrain = restrain
        self.step = 0
        self.todo1 = []
        self.todo2 = []
        self.search_term = None

    # Searches a string for http and https urls and returns them
    def get_urls_from_line(self, line):

        urls = []

        i = line.find("http")
        e = i
        while line.find("http", i) != -1 and e <= len(line) and i <= len(line):  # finds first pattern match
            i = line.find("http", i)  # and sets end of string
            e = i  # further by scanning it
            try:  # for escape characters
                while not "\" <>(){}\'[]*;\\".__contains__(line[e]):
                    e += 1
            except Exception as err:
                print(err)
            u = line[i:e]
            if not urls.__contains__(u) and not u.__contains__("\/") and not u.__contains__("https?") \
                    and u.__contains__(".") and u.__contains__("://"):
                urls.append(u)
            i = e
        return urls

    def start(self):
        try:
            r = requests.get(self.root_url)
            print("Received url_source.")

            for line in r.text.splitlines():    # Iterates line by line through source_code
                if line.__contains__("http"):
                    urls = self.get_urls_from_line(line)
                    for url in urls:
                        if not self.found_urls.__contains__(url):   # Adds new urls to found and todo1 list
                            self.found_urls.append(url)
                            # print(url)
                            if url.__contains__(self.restrain):
                                self.todo1.append(url)

                try:
                    if line.__contains__(self.search_term) and not self.search_hits.__contains__(self.root_url):
                        print(line)
                        self.search_hits.append(self.root_url)
                except TypeError:
                    if False:
                        print("No search term set.")

        except requests.exceptions.ConnectionError:
            print("Cant connect to given url.")

    def scrape_loop(self):
        while self.step < self.level:
            for url in self.todo1:

                r = requests.get(url)
                for line in r.text.splitlines():

                    if line.__contains__("http"):

                        urls = self.get_urls_from_line(line)
                        for u in urls:
                            if not self.found_urls.__contains__(u):
                                self.found_urls.append(u)
                                # print(url)
                                if not self.todo1.__contains__(u) and not self.todo2.__contains__(u) and \
                                        u.__contains__(self.restrain):
                                    self.todo2.append(u)

                    try:
                        if line.__contains__(self.search_term) and not self.search_hits.__contains__(url):
                            self.search_hits.append(url)
                            if len(line) < 200:
                                print(line)
                    except TypeError:
                        if False:
                            print("No search term set.")
                self.todo1.remove(url)
            self.todo1 += self.todo2
            self.todo2 = []
            self.step += 1


"""class Hit:

    def __init__(self, url, line):
        self.url = url
        self.line = line
"""