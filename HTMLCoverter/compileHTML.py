import os
from time import strftime, gmtime

from Parser.FindFolderName import find_folder


def compile_html(sub, dir_path):
    file = sub.file_link
    new_name = file.replace(".tex", ".html")
    code = "pandoc -s \"" + file +"\" -o \"" +new_name + "\""
    sub.htmlLink = new_name
    os.system(code)
def compile_root(dir_path, filename, folder):
    filename = dir_path + "/" + filename
    [_, file] = find_folder(filename)
    """
    
    
    new_path_tex = filename.replace(".tex","_supr.tex")
    with open(filename , 'r') as myfile:
        data=myfile.read()
        ne = data.replace("\input","%\input")
        with open(new_path_tex,'w') as f:
            f.write(ne)
            f.close()
    
    
    code = "cd \"" + folder + "\" && r |  htlatex "+  new_path_tex + ""
   
    os.system(code)
    copyfile(new_path_tex.replace(".tex",".html"), new_path)
    copyfile(new_path_tex.replace(".tex",".css"), new_path.replace(".html","_supr.css"))
    """
    new_path = dir_path + "/compiled/pages" + file.replace(".tex",".html")
    code = "pandoc -s \"" + filename +"\" -o \"" +new_path + "\""
    os.system(code)
    with open(new_path , 'r') as myfile:
        data=myfile.read()
        new_d = data.replace("</body>", "<font class=\"time\">" + strftime("%a, %d %b %Y %H:%M:%S", gmtime()) + "</font></body>")
        with open(new_path,'w') as f:
            f.write(new_d)
            f.close()
    return new_path