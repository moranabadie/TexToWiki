from distutils.dir_util import copy_tree
import os 

from HTMLCoverter.compileHTML import compileHTML
from Parser.InputReader import inputReader
from TemplateManagement.ManageReader import clickJSReplacement


def _findFolder(stri):
    i = len(stri) - 1
    while i > 0 and stri[i] != "/":
        i -= 1
    return [stri[:i], stri[i:]]
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        dir_path = os.path.dirname(os.path.realpath(__file__))
        filepath = dir_path + "/"+ filename
        with open(filepath, 'r') as myfile:
            if not os.path.exists(dir_path + "/compiled/"):
                os.makedirs(dir_path + "/compiled/")
            os.system("rm -rf " + dir_path + "/compiled/*")
            
            data=myfile.read()
            [folder, file] = _findFolder(filepath)
            l = inputReader(data, folder)
            copy_tree(dir_path + "/template/", dir_path + "/compiled/")
            links = []
            links.append(file.replace(".tex",'.html'))
            compileHTML(filepath, dir_path, file)
            for tex in l:
                [_, file] = _findFolder(tex)
                compileHTML(tex, dir_path, file)
                links.append(file.replace(".tex",'.html'))
            clickJSReplacement(dir_path, links)
            
        
        
