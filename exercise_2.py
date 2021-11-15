def wildcard(bstring):
    if "?" not in bstring:
        print(bstring)
    else:
        wildcard(bstring.replace("?","1",1))
        wildcard(bstring.replace("?","0",1))
wildcard("1?0?1")
