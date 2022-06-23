print("""
D O R K  S E A R C H ! 
    ---------
@alpernae (IG/TW)\n
""")


# Check for errors!
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
# Search for google dork!
def search_dork():
    query = input("Enter your dork: ")
 
    for s in search(query, tld="co.in", num=3000, stop=5000, pause=10):
        print("\n" + s)

search_dork()



