import subprocess
import os

path = "base.html"


def insert(path, title):
    content_path =  "blog/" + title + ".md"
    with open(path, "r") as b:
        base = b.read()
        content = subprocess.run(["pandoc",  "-f", "markdown", "-t", "html", content_path], capture_output=True, text=True).stdout
        print(content_path)
        base = base.replace("yuhuu", content)
        page = open("../public/" + title + ".html", "w")
        page.write(base)
        page.close()
        #print(base)

def create_pages():
    list = os.listdir("blog")
    for file in list:
        insert(path, os.path.splitext(file)[0])

create_pages()

