def search_google(term):
    try:
        print(f"Searched for {term.replace(' ','+')}\n Results: https://www.google.com/search?q={term.replace(' ','+')}")
    except TypeError:
        print("Term is a required argument, that is missing")

search_google(term="None")
