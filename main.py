import src


root = input("Enter your root URL : ")
level = int(input("Enter the max depth to seach : "))
restrain = input("Enter restrain on which urls shall be searched : ")
term = input("Enter a serach term if you desire : ") or None

session = src.WebScraper(root, level, restrain)
if term:
    session.search_term = term


def test():
    return src.WebScraper("https://google.com/", 2, "google.com")


session.start()
session.scrape_loop()

for url in session.found_urls:
    if url.__contains__(session.restrain):
        print(url)
for url in session.found_urls:
    if not url.__contains__(session.restrain):
        print(url)

for url in session.search_hits:
    print(url)

for url in session.unreachable:
    print("Couldn't reach :", url)

