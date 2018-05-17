import os

def compileHTML(file, dir_path, name):
    
    os.system("pandoc -s -c css.css -A footer.html " + file +" -o "+ dir_path + "/compiled/pages/" + name.replace(".tex", "")+ ".html")
    