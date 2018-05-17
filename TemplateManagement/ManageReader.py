def clickJSReplacement(dir_path, links):
    fileName = dir_path + "/compiled/js/click.js"
    with open(fileName , 'r') as myfile:
        data=myfile.read()
        newD = data.replace("TOREPLACE", _linkManager(links))
        with open(fileName,'w') as f:
            f.write(newD)
            f.close()
def _linkManager(links):
    first = True
    rep = ""
    inde = 1
    for link in links:
        if first:
            first = False
            rep += """
            if (to == """ + str(inde) + """) {
                return "pages""" + link +"""\"
            }
            """
        else:
            rep += """
            elif (to == """ + str(inde) + """) {
                return "pages""" + link +"""\"
            }
            """
        inde += 1   
    return rep