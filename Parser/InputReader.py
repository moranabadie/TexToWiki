def inputReader(data, dir_path):
    le = len(data)
    l = _substring_indexes("\input", data)
    rep = []
    for i in l:
        
        while i < le and data[i] != "{":
            i += 1
        j = i
        while j < le and data[j] != "}":
            j += 1
        newFile = dir_path + "/"+ data[i+1:j] +".tex"
        rep.append(newFile)
    return rep
            
    

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
    