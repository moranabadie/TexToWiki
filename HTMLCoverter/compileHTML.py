import os

def compileHTML(sub, dir_path):
    file = sub.file_link
    code = "pandoc -s -c css.css -A footer.html \"" + file +"\" -o \"" +file.replace(".tex", "")+ ".html\""
    print(code)
    os.system(code)
    