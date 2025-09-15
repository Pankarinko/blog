import subprocess

path = "base.html"
title = "getting-started"
content_path =  title + ".md"

def insert(path, content_path):
    with open(path, "r") as b:
        base = b.read()
        content = subprocess.run(["pandoc", "-f", "markdown", "-t", "html", content_path], capture_output=True, text=True).stdout
        print(content)
        base = base.replace("yuhuu", content)
        page = open("./" + title + ".html", "w")
        page.write(base)
        page.close()
        print(base)
insert(path, content_path)

