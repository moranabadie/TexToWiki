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
    first = True
    for sub in lis:
        
        if first:
            first = False
            pref = sub
        else:
            name_finder = sub.split("}")
            
            if len(name_finder) > 1:
                name_chap = name_finder[0]
                chapter_names.append(name_chap)
                roman_index = write_roman(index) + ". " 
                title_index =  roman_index + write_upper(index_chap)+". "
                chapter_content.append(\
                    sub_replace(\
                                "\\chapter{" + \
                                roman_index + name_chapter + "}" + pref +\
                                "\\section{" + \
                                title_index + sub, title_index, links, global_index))
                index_chap += 1
                global_index += 1
                pref = ""
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
    stri = ref_manager(stri, links)
    stri = links.commands + stri
    new_command_manager(stri, links)
    return sub_replace_links_aux(stri, links, global_index, 1)
def new_command_manager(stri, links):
    l = stri.split("\\newcommand")
    first = True
    for i in l:
        if first:
            first = False
        else:
            command = "\\newcommand" 
            nb = 0
            first_c = True
            for cha in i: 
                command += cha
                if cha == "{":
                    nb += 1
                if cha == "}":
                    if nb == 1:
                        if first_c:
                            first_c = False
                            nb -= 1
                        else:
                            break
                    else:
                        nb -= 1
            links.add_command(command)
def ref_manager(stri, links):
   
    l = stri.split("\\begin{figure}")
    first = True
    new_str = ''
    for i in l:
        if first:
            first = False
            new_str = i
        else:
            new_str += "\\begin{figure}"
            l2 = i.split("\\end{figure}")
            first7 = True
            for kk in l2:
                if first7:
                    first7 = False
                    
                    if "\\begin{minipage}" in kk:
                        l2 = kk.split("\\begin{minipage}")
                        first2 = True
                        for j in l2:
                            if first2:
                                first2 = False
                            else:
                                l3 = j.split("}")
                                kk = kk.replace("\\begin{minipage}" + l3[0] + '}', "")
                        
                    kk = kk.replace("\\end{minipage}", "") 
                    l2= kk.split("\\label{")
                    
                    
                    first2 = True
                    for j in l2:
                        if first2:
                            new_str +=j
                            first2 = False
                        else:
                            new_str += "\\label{"
                            l3= j.split("}")
                            first3 = True
                            for k in l3:
                                if first3:
                                    first3 = False
                                    new_str += links.get_nb_fig(k)
                                else:
                                    new_str += "}" + k
                else:
                    new_str += "\\end{figure}" + kk
                  
            
    return new_str
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