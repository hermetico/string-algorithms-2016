from border_array import border_array as ba

def search_naive(x,pat):
    print ("do nothing")

def search_kmp(x,pat):
    print ("do nothing")

def search_ba(x, pat):
    ba.BA_search(x,pat )


if __name__ == "__main__":
    x = "abbacbbbababacabbbba"
    pat = "bbba"

    search_naive(x,pat)
    search_kmp(x,pat)
    search_ba(x,pat)



