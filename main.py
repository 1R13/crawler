import src
import UrlObj
import sys
import datetime
from colored import stylize, fg


class Session:

    def get_url(self, name: str, dic: list):
        for u in dic:
            if u.name == name:
                return u
        return False

    def get_args(self):

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
        "-l": 0,  # level
        "-u": "https://www.google.com",  # root URL
        "-r": "google",  # restrain string
        "-s": None,  # search string
        "-nR": False,  # no Recursion
        "-h": False,  # hyper refs
        "-v": False    # Verbose
    }

    def __init__(self):
        self.get_args()
        self.root: UrlObj.Url = UrlObj.Url(self.flags["-u"])
        self.depth: int = self.flags["-l"]
        self.restrain: str = self.flags["-r"]
        self.found = []
        self.searched = []

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
        print("Found %i URLs on %i sites." % (len(self.found), len(self.searched)))


# TODO somehow working, find out why

def scrape_loop(session: Session):
    print("Starting scraping…") if session.flags["-v"] else None
    try:
        level = 0
        todo1 = []
        todo2 = []
        todo1.append(session.root)
        while level <= session.depth:
            for u in todo1:     # TODO redo src
                result = src.web_scrape(u, session.restrain)
                if result:
                    for r in result:
                        if not session.get_url(r.name, session.found):
                            todo2.append(r)
                            session.found.append(r)
                else:
                    u.flag = 3
                    if session.flags["-v"]: print("Couldn't reach %s" % u.name)
                session.searched.append(u)

                if session.flags["-v"]: print("Finished %s" % u.name)
            todo1 = todo2
            todo2 = []
            level += 1

            level += 1
    except Exception as e:
        print("scrape_loop :\n", e) if session.flags["-v"] else None


def __main__():
    try:
        print("Creating session…")
        s = Session()
        scrape_loop(s)
        s.display_findings()
        # initiate scrape_loop

    except Exception as e:
        print("Main : \n", e)
        # pass


__main__()


"""import src
import datetime


Todo = []
Todo2 = []

Found = []

Searched = []
# URLS = []

target = int(input("How many levels for searching? :"))
level = 1

Todo.append(input("Enter first URL i.e. https://www.google.com : "))
limit = input("Limit to URLs containing : ") or "."
started = datetime.datetime.now()
# lives = int(input("How many levels ? "))

while level <= target:
    Todo2 = []
    for url in Todo:
        try:
            Found = src.Src.web_scrape(url, limit)
        except Exception as err:
            print("\n", err, "at", url)
        for u in Found:
            if not Todo.__contains__(u) and not Searched.__contains__(u) and not Todo2.__contains__(u):
                Todo2.append(u)
                # print(lives)
        Searched.append(url)
        print("Finished ", url)
        print(len(Searched), "Websites searched,", len(Todo)
              , "Websites on todo,", len(Todo2), "on todo2,", "at level", level
              , "/", target, "[" + str(datetime.datetime.now() - started) + "]", end="\r")
        Todo.remove(url)
    Todo += Todo2
    level += 1
    # print("\n", len(Todo), "items on todo list.")
finished = datetime.datetime.now()

for u in Found:
    print("Found :", u)

for u in Todo2:
    print("To be searched :", u)

print(75*"-", "\n", len(Searched), "unique urls searched,", len(Found), "urls found,", target, "levels searched,", len(Todo) + len(Todo2), "URLs open, took", finished - started)

# print(hits, "successful search hits.")

"""