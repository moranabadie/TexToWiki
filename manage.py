from distutils.dir_util import copy_tree
import os 

from HTMLCoverter.HTMLSizer import html_sizer
from HTMLCoverter.compileHTML import compile_html, compile_root
from Parser.FindFolderName import find_folder
from Parser.InputReader import input_reader
from TemplateManagement.ManageReader import clickJSReplacement
from TemplateManagement.htmlChanger import doc_replacement
from Utility.Links import Links
import sys

if __name__ == "__main__":
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
            path = folder + "/Figures/"
            links = Links()
            try:
                copy_tree(path, dir_path + "/compiled/Figures/")
            except:
                print(path+ " not found")
            chapters = input_reader(data, dir_path, folder, links)
            
            for chapter in chapters:
                for sub in chapter.list:
                    compile_html(sub, dir_path)
            new_path = compile_root(dir_path, filename, folder)    
            clickJSReplacement(dir_path, chapters, new_path)
            doc_replacement(dir_path, chapters)
            html_sizer(chapters, dir_path, filename, links)
        
        
