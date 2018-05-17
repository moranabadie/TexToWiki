import os

def compileHTML(sub, dir_path):
    file = sub.file_link
    newHTMLNAME = file.replace(".tex", ".html").replace(" ", "_")
    code = "pandoc -s -c css.css -A footer.html \"" + file +"\" -o \"" +newHTMLNAME + "\""
    sub.htmlLink = newHTMLNAME
    os.system(code)
    