import os

from Parser.ChapterReader import chapter_reader
from Parser.FindFolderName import find_folder
from Utility.Chapter import Chapter
from Utility.UnicID import UnicID


def input_reader(data, dir_path, folder):
    le = len(data)
    l = _substring_indexes("\input", data)
    rep = []
    unic_id = UnicID()
    index = 1
    for i in l:
        
        while i < le and data[i] != "{":
            i += 1
        j = i
        while j < le and data[j] != "}":
            j += 1
        name_file = data[i+1:j]
        new_file = folder + "/"+ name_file +".tex"
        [_, chap_name] = find_folder(new_file)
        
        
        
        with open(new_file, 'r') as myfile:
           
            data=myfile.read()
            name_chapter, data  = _name_finder(data, new_file)
            chapter = Chapter(name_chapter)
            rep.append(chapter)
            
            [chapter_names, chapter_content] = chapter_reader(data, index, name_chapter)
            _write_chapters(dir_path, chapter_names, chapter_content, unic_id, chapter, chap_name)
            
        index += 1
    return rep
def _name_finder(data, new_file):
    lis = data.split("\\chapter{")
    if len(lis) > 1:
        
        lis = lis[1].split("}")
        
        
        if len(lis) > 1:
            name_chapter = lis[0]
            data = data.replace("\\chapter{"+name_chapter+"}","")
        else:
            return new_file.replace(".tex", "").replace("/", "")
    else:
        return new_file.replace(".tex", "").replace("/", "")
    
    return name_chapter, data 
def _write_chapters(dir_path, chapter_names, chapter_content, unic_id, chapter_object, chap_name):
    index = 0
    for chapter in chapter_names:
       
        chapter_conten = chapter_content[index]

        folder_name = dir_path + "/compiled/pages" + chap_name.replace(".tex","") + "/"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        file_link =  folder_name + chapter + "__"  + str(unic_id.get()) + ".tex"
        with open(file_link,'w') as f:
            f.write(chapter_conten)
            f.close()
   
           
            chapter_object.add(chapter, file_link)
        index += 1
def _substring_indexes(substring, string):
    """ 
    Generate indices of where substring begins in string

    >>> list(find_substring('me', "The cat says meow, meow"))
    [13, 19]
    """
    last_found = -1  # Begin at -1 so the next position to search from is 0
    while True:
        # Find next index of substring, by starting after its last known position
        last_found = string.find(substring, last_found + 1)
        if last_found == -1:  
            break  # All occurrences have been found
        yield last_found
    