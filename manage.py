from distutils.dir_util import copy_tree
import os 

from HTMLCoverter.compileHTML import compileHTML
from Parser.FindFolderName import find_folder
from Parser.InputReader import input_reader


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
            [folder, file] = find_folder(filepath)
            copy_tree(dir_path + "/template/", dir_path + "/compiled/")
            chapters = input_reader(data, dir_path, folder)
            
            for chapter in chapters:
                for sub in chapter.list:
                    compileHTML(sub, dir_path)
                 
            #clickJSReplacement(dir_path, links)
            
        
        
