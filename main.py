import src

# TODO somehow working, find out why




def __main__():
    try:
        print("Creating session…")
        s = src.Session()
        s.scrape_loop()
        s.display_findings()
        # initiate scrape_loop

    except Exception as e:
        print("Main : \n", e)
        # pass


__main__()

