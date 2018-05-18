from Utility.RomanNumber import write_upper, write_roman
UNICSTARTNAME = "AZERTYUUIOIPONBBLDFJKDFJSDFKJDFKSDFKDFJQLSXKWX"
UNICSTARTNAMEEND = "XWCµWXCKJESRLKZERKFDKSJFKSDJFKSDJCCCVKXCWJVKJSDFKSDEFKZEJRZFJIDSJ"
UNICSTARTNAMEEND2 = "TYKBVGVBN?EZNIQSNXCXNJCWXCJZDNCNXCCXJDNSkiwkllwjx"

LINKEDUNICSTARTNAME = "RTKEJGF?NSCVXCWOVZNDQSCOICWCNWXCJIJI"
LINKEDUNICSTARTNAMEEND = "AZKIRTNCVXIEZBNDSVCJVNXDFEO"
LINKEDUNICSTARTNAMEEND2 = "4654df35s4dfsdflksjdfkhsbdfshdfA"
def chapter_reader(stri, index, name_chapter, links, global_index):
   
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
                                title_index + sub, title_index, links, global_index))
                index_chap += 1
                global_index += 1
    return  [chapter_names, chapter_content, global_index]

def sub_replace(stri, title_index, links, global_index):
    
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
    
    return sub_replace_links(stri, links, global_index)
def sub_replace_links(stri, links, global_index):
    stri = sub_replace_links_aux(stri, links, global_index, 0)
    return sub_replace_links_aux(stri, links, global_index, 1)
def sub_replace_links_aux(stri, links, global_index, mode_aux):
    
    stri = stri + " "
    if mode_aux == 0:
        lis = stri.split("\\hypertarget{")
    else:
        lis = stri.split("\\hyperlink{")

    stri = ""
    first = True
    for sub in lis:
        if first:
            stri += sub
            first = False
        else:
            n = len(sub)
            
            name = ""
            mode = 0
            content = ""
            
            for i in range(n):
                cha = sub[i]
                if mode == 0:
                    if cha == "}":
                        mode = 1
                 
                    else:
                        name += cha
                elif mode == 1:
                    if cha == "{":
                        mode = 2
                        nb = 0
                elif mode == 2:
                    if cha == "{":
                        nb += 1
                        content += cha
                    elif cha == "}":
                        if nb == 0:
                            
                            break
                        else:
                            nb -= 1
                            content += cha
                    else:
                        content += cha
                        
            
            if mode_aux == 0:
                links.add(name, global_index)
                stri += UNICSTARTNAME +name+ UNICSTARTNAMEEND + content +UNICSTARTNAMEEND2 + sub[i+1:]
            else:
                stri += LINKEDUNICSTARTNAME +name+\
                 LINKEDUNICSTARTNAMEEND + content +LINKEDUNICSTARTNAMEEND2 + sub[i+1:]
  
    return stri