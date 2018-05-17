def chapterReader(stri):
    subL = stri.split("% SUB ")
    chapterNames = []
    chapterContent = []
    for sub in subL:
        if sub != "":
            nameFinder = sub.split("\n")
            if len(nameFinder) > 1:
                nameChap = nameFinder[0]
                chapterNames.append(nameChap)
                
                chapterContent.append(sub[len(nameChap):])
                
    return  [chapterNames, chapterContent]
                