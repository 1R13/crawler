import requests
from UrlObj import Url
import sys
from colored import stylize, fg
import UrlObj


def web_scrape(url: Url, limit: str, *search:str):

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
            if search and line.__contains__(search):
                url.flag = 5

        return urls     # returns all found URLs as objects
    except requests.exceptions.ConnectionError:
        url.flag = 3  # marks unreachable urls
        return False


class Session:

    def get_url(self, name: str, dic: list):
        for u in dic:
            if u.name == name:
                return u
        return False

    def get_args(self):
        # goes through the option dictionary and sets variables according to their presence in the parameter
        try:
            for f in self.flags:
                if sys.argv.__contains__(f) and type(self.flags[f]) != bool:
                    try:
                        self.flags[f] = int(sys.argv[sys.argv.index(f) + 1])
                    except ValueError:
                        self.flags[f] = sys.argv[sys.argv.index(f) + 1]
                elif sys.argv.__contains__(f) and type(self.flags[f]) == bool:
                    self.flags[f] = not self.flags[f]
        except Exception as e:
            print(e)

    # Sets self.flags for dic entries

    flags = {
        "-l": 2,  # level
        "-u": "https://www.google.com",  # root URL
        "-r": "google",  # restrain string
        "-s": None,  # search string
        "-nR": False,  # no Recursion
        "-h": False,  # hyper refs
        "-v": False,    # Verbose
        "-x": None
    }

    def __init__(self):
        self.get_args()
        self.root: UrlObj.Url = UrlObj.Url(self.flags["-u"])
        self.depth: int = self.flags["-l"]
        self.restrain: str = self.flags["-r"]
        self.found = []
        self.searched = []
        self.search_hits = []

        print("Set up session attributes…")
        print("Following settings:\n", self.flags)

    def display_findings(self):
        if len(self.found) > 0: print("Displaying findings :\n")
        for u in self.found:
            if any(x in u.name for x in (".jpg", ".jpeg", ".png", ".gif", ".ico")):
                print(stylize("Found : %s" % u.name, fg("cyan_1")))
            elif u.name.__contains__(".pdf"):
                print(stylize("Found : %s" % u.name, fg("green_1")))
            elif any(x in u.name for x in (".css", ".js", ".php")):
                print(stylize("Found : %s" % u.name, fg("yellow_1")))
            elif u.name.__contains__(".txt"):
                print(stylize("Found : %s" % u.name, fg("red_1")))
            else:
                print("Found : %s" % u.name)
        for u in self.search_hits:
            print(stylize("Hit on : %s" % u.name, fg("red_1")))
        print("Found %i URLs on %i sites." % (len(self.found), len(self.searched)))

    def scrape_loop(self):
        print("Starting scraping…") if self.flags["-v"] else None
        print("Excluding : ", )
        try:
            level = 0
            todo1 = []
            todo2 = []
            todo1.append(self.root)
            while level <= self.depth:
                for u in todo1:  # TODO redo src
                    result = web_scrape(u, self.restrain)
                    if result:
                        for r in result:
                            if not self.get_url(r.name, self.found):
                                if self.flags["-x"] is None or not r.name.__contains__(self.flags["-x"]):
                                    if not any(ext in r.name for ext in(".jpg", ".gif", ".png", ".jpeg", ".mp3", ".mp4")):
                                        todo2.append(r)         # adds new urls for the next while loop
                                    self.found.append(r)
                                if self.flags["-s"] and r.name.__contains__(self.flags["-s"]):
                                    self.search_hits.append(r)

                    else:
                        u.flag = 3
                        if self.flags["-v"]: print("Couldn't reach %s" % u.name)
                    self.searched.append(u)

                    if self.flags["-v"]: print("Finished %s" % u.name)
                todo1 = todo2
                todo2 = []
                level += 1

                level += 1
        except Exception as e:
            print("scrape_loop :\n", e) if self.flags["-v"] else None
