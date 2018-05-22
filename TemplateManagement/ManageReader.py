def clickJSReplacement(dir_path, chapters, new_path):
    file_name = dir_path + "/compiled/js/click.js"
    with open(file_name , 'r') as myfile:
        data=myfile.read()
        new_d = data.replace("TOREPLACE", _link_manager(chapters)).replace("NAMECORE", new_path)
        new_d = new_d.replace("TRPLPA", _link_manager_2(chapters))
        with open(file_name,'w') as f:
            f.write(new_d)
            f.close()
def _link_manager(chapters):
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
def _link_manager_2(chapters):
    rep = ""
    inde = 1
    for chap in chapters:
        for sub in chap.list:
            rep += """
            else if (to == """ + str(inde) + """) {
                return \"""" + sub.name +"""\"
            }
            """

            sub.index = inde
            inde += 1  
    
    return rep