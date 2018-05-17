def clickJSReplacement(dir_path, chapters, new_path):
    fileName = dir_path + "/compiled/js/click.js"
    with open(fileName , 'r') as myfile:
        data=myfile.read()
        newD = data.replace("TOREPLACE", _linkManager(chapters)).replace("NAMECORE", new_path)
        with open(fileName,'w') as f:
            f.write(newD)
            f.close()
def _linkManager(chapters):
    rep = ""
    inde = 1
    for chap in chapters:
        for sub in chap.list:
            rep += """
            else if (to == """ + str(inde) + """) {
                return \"""" + sub.htmlLink +"""\"
            }
            """

            sub.index = inde
            inde += 1  
    
    return rep