def html_sizer(chapters, dir_path, filename):
    filename = dir_path + "/" + filename
    files = [filename]
    for chapter in chapters:
        for sub in chapter.list:
            files.append(sub.htmlLink)
    
    for file_name in files:
       
        with open(file_name , 'r') as myfile:
            data=myfile.read()
            new_d = _replace_with(data)
            with open(file_name,'w') as f:
                f.write(new_d)
                f.close()
            
    
def _replace_with(data):
    return data.replace("<body>", \
"""<body style="width:99%;height:100%;padding:0px;">
    <div id="fullbody" style="padding:0px;width:100%;">""")\
    .replace("</body>", \
"""</div>
<script>
new SimpleBar($('#fullbody')[0]);
</script>
</body>""")
            
    