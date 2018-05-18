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
                roman_index = write_roman(index) + ". " 
                title_index =  roman_index + write_upper(index_chap)+". "
                chapter_content.append(\
                    sub_replace(\
                                "\\chapter{" + \
                                roman_index + name_chapter + "}" +\
                                "\\section{" + \
                                title_index + sub, title_index))
                index_chap += 1
                
    return  [chapter_names, chapter_content]

def sub_replace(stri, title_index):
    
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
            stri += "\\subsection{" + title_index + write_upper(indexx).lower()+". " + sub
            indexx += 1
    
    return stri