
path = "base.html"
title = "getting-started"
content_path =  title + ".md"

def insert(path, content_path):
    with open(path, "r") as b:
        base = b.read()
        with open(content_path, "r") as content:  
            base = base.replace("yuhuu", content.read())
        page = open("./" + title + ".html", "w")
        page.write(base)
        page.close()
        print(base)
insert(path, content_path)

