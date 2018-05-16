import os

def compileHTML(file, dir_path):
    if not os.path.exists(dir_path + "/compiled/"):
        os.makedirs(dir_path + "/compiled/")
    os.system("pandoc -s -c css.css -A footer.html " + file +" -o "+ dir_path + "/compiled/final.html")
    