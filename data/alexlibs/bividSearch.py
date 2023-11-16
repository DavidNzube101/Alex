import webbrowser

def normalSearch(query, search_engine="google"):
    query = query.replace(" ", "+")
    
    if search_engine == "google":
        url = f"https://www.google.com/search?q={query}"
    elif search_engine == "bing":
        url = f"https://www.bing.com/search?q={query}"
    elif search_engine == "duckduckgo":
        url = f"https://duckduckgo.com/?q={query}"
    else:
        raise ValueError("Unsupported search engine")
    
    webbrowser.open(url)

# search_query = input_text

# Choose a search engine: "google", "bing", or "duckduckgo"
search_engine = "google"

def howToSearch(query):
	query = query.replace(" ", "+")
	url = f"https://www.youtube.com/results?search_query={query}"
	webbrowser.open(url)
# normalSearch(search_query, search_engine)