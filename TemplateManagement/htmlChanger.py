from Utility.RomanNumber import write_roman, write_upper


def doc_replacement(dir_path, chapters):
    file_name = dir_path + "/compiled/doc.html"
    with open(file_name , 'r') as myfile:
        data=myfile.read()
        new_d = data.replace("TOREPLACE", _link_manager(chapters))
        with open(file_name,'w') as f:
            
            f.write(new_d)
            f.close()
def _link_manager(chapters):
    rep = ""
 
    index_chap = 1
    
    for chap in chapters:
        rep += """<button class="accordion">""" + write_roman(index_chap)+""". """+chap.info.name + """</button>
<div class="panel">\n"""
        index_sub = 0
        for sub in chap.list:
            rep += '    <button class="button" to="'+ str(sub.index)+ '">'\
             + write_upper(index_sub)+ '. '+sub.name+ '</button>\n'
            index_sub += 1
        index_chap += 1
        rep += "</div>"
   
    return rep
