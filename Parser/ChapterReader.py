from Utility.RomanNumber import write_upper, write_roman


def chapter_reader(stri, index, name_chapter):
   
    lis = stri.split("\\section{")
    chapter_names = []
    chapter_content = []
    index_chap = 0
    for sub in lis:
        if sub != "":
            name_finder = sub.split("}")
            if len(name_finder) > 1:
                name_chap = name_finder[0]
                chapter_names.append(name_chap)
                
                chapter_content.append(\
                    sub_replace(\
                                "\\chapter{" + \
                                write_roman(index) + ". "+name_chapter + "}" +\
                                "\\section{" + \
                                write_roman(index) + ". " + \
                                write_upper(index_chap)+". " + sub))
                index_chap += 1
                
    return  [chapter_names, chapter_content]

def sub_replace(stri):
    
    stri = stri + " "
    lis = stri.split("\\subsection{")
    indexx = 0
    stri = ""
    first = True
    for sub in lis:
        if first:
            stri += sub
            first = False
        else:
            first = False
            stri += "\\subsection{" + write_upper(indexx).lower()+". " + sub
            indexx += 1
    
    return stri