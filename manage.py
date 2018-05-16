from Parser.InputReader import inputReader

import os 
from HTMLCoverter.compileHTML import compileHTML
def _findFolder(stri):
    i = len(stri) - 1
    while i > 0 and stri[i] != "/":
        i -= 1
    return stri[:i]
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = dir_path + "/"+ filename
        with open(filepath, 'r') as myfile:
            data=myfile.read()
            
            l = inputReader(data, _findFolder(filepath))
            for tex in l:
                compileHTML(tex, dir_path)
        
        
