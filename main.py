import datetime

import src


root = input("Enter your root URL : ") or "https://www.google.com"
level = int(input("Enter the max depth to search : ") or 1)
restrain = input("Enter restrain on which urls shall be searched : ") or "google"
term = input("Enter a search term if you desire : ") or None

session = src.WebScraper(root, level, restrain)
if term:
    session.search_term = term


def test():
    return src.WebScraper("https://google.com/", 2, "google.com")


session.start()
session.scrape_loop()

for url in session.found_urls:
    if url.__contains__(session.restrain):
        print("Found :", url)
for url in session.found_urls:
    if not url.__contains__(session.restrain):
        print("Found :", url)

for url in session.search_hits:
    print("Found string on :", url)

for url in session.unreachable:
    print("Couldn't reach :", url)

finished = datetime.datetime.now() - session.time_start
print("\nFinished in", str(finished).split(".")[0])
print(len(session.search_hits), "websites found containing", session.search_term, ".")
print("Found", len(session.found_urls) + len(session.unreachable), "urls on", session.searched, "sites.")
print(len(session.unreachable), "are unreachable.")
print("Finished at level", session.step, "from", session.level)

input()
