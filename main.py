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

"""for u in session.found_urls:
    if u.__contains__("google.com"):
        print(u)
for u in session.found_urls:
    if not u.__contains__("google.com"):
        print(u)
"""
for url in session.search_hits:
    print(url)
