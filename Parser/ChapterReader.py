def chapter_reader(stri):
    lis = stri.split("% SUB ")
    chapter_names = []
    chapter_content = []
    for sub in lis:
        if sub != "":
            name_finder = sub.split("\n")
            if len(name_finder) > 1:
                name_chap = name_finder[0]
                chapter_names.append(name_chap)
                
                chapter_content.append(sub[len(name_chap):])
                
                
    return  [chapter_names, chapter_content]
                