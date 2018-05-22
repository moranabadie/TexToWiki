from Parser.ChapterReader import UNICSTARTNAME, UNICSTARTNAMEEND, \
    UNICSTARTNAMEEND2, LINKEDUNICSTARTNAME, LINKEDUNICSTARTNAMEEND, \
    LINKEDUNICSTARTNAMEEND2


def html_sizer(chapters, dir_path, filename, links):
    filename = dir_path + "/" + filename
    files = [filename]
    for chapter in chapters:
        for sub in chapter.list:
            files.append(sub.htmlLink)
    
    for file_name in files:
        
        with open(file_name , 'r') as myfile:
            data=myfile.read()
            new_d = _replace_with(data, links)
            with open(file_name,'w') as f:
                f.write(new_d)
                f.close()
            
    
def _replace_with(data, links):
    return link_manager(data.replace("<body>", \
"""<body style="width:99%;height:100%;padding:0px;">
    <div id="fullbody" style="padding:0px 1% 0px 1%;width:98%;height:100%;">""")\
    .replace("</body>", \
"""</div>
<script>
var simpleBz =new SimpleBar($('#fullbody')[0]);

</script>
</body>""").replace("<a", '<a target="_blank" '), links)
    
def link_manager(data, links):
    data = link_manager_aux(data, 0, links)
    return link_manager_aux(data, 1, links)
def link_manager_aux(data, ii, links):
    if ii == 0:
        li = data.split(UNICSTARTNAME)
    else:
        li = data.split(LINKEDUNICSTARTNAME)
    first = True
    data = ""
    for i in li:
        if first:
            data += i
            first = False
        else:
            
            if ii == 0:
                data += '<a class="liketext" id="'
                lii = i.split(UNICSTARTNAMEEND)
            else:
                
                data += '<font class="button fakelink" link="#'
                lii = i.split(LINKEDUNICSTARTNAMEEND)
            first2 = True
            for l in lii:
                if first2:
                    first2 = False
                    link = links.look_for(l)
                    data += l +'" to="'+str(link.chapter)+'">'
                else:
                    data += l
    if ii == 0:
        return data.replace(UNICSTARTNAMEEND2, "</a>")
    else:
        return data.replace(LINKEDUNICSTARTNAMEEND2, "</font>")
    
    
            
    