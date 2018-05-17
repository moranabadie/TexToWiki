def clickJSReplacement(dir_path, chapters):
    fileName = dir_path + "/compiled/js/click.js"
    with open(fileName , 'r') as myfile:
        data=myfile.read()
        newD = data.replace("TOREPLACE", _linkManager(chapters))
        with open(fileName,'w') as f:
            f.write(newD)
            f.close()
def _linkManager(chapters):
    first = True
    rep = ""
    inde = 0
    for chap in chapters:
        for sub in chap.list:
            if first:
                first = False
                rep += """
                if (to == """ + str(inde) + """) {
                    return \"""" + sub.htmlLink +"""\"
                }
                """
            else:
                rep += """
                else if (to == """ + str(inde) + """) {
                    return \"""" + sub.htmlLink +"""\"
                }
                """
            sub.index = inde
            inde += 1  
    
    return rep