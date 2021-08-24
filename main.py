import src
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
    print(u)

print(50*"-", "\n", len(Searched), "unique urls searched,", target, "levels searched,", len(Todo) + len(Todo2), "URLs open, took", finished - started)

# print(hits, "successful search hits.")

