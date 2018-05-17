import os

from Parser.FindFolderName import find_folder


def compileHTML(sub, dir_path):
    file = sub.file_link
    newHTMLNAME = file.replace(".tex", ".html").replace(" ", "_")
    code = "pandoc -s -c css.css -A footer.html \"" + file +"\" -o \"" +newHTMLNAME + "\""
    sub.htmlLink = newHTMLNAME
    os.system(code)
def compileRootHTML(dir_path, filename):
    
    filename = dir_path + "/" + filename
    [_, file] = find_folder(filename)
    new_path = dir_path + "/compiled/pages" + file.replace(".tex",".html")
    code = "pandoc -s -c css.css -A footer.html \"" + \
    filename +"\" -o \"" + new_path + "\""
    os.system(code)
    return new_path