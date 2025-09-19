import subprocess
import os

path = "base.html"


def insert(path, title):
    content_path =  "blog/" + title + ".md"
    subprocess.run(["pandoc", "--template=base.template", "--highlight-style=zenburn", content_path, "-o", "../docs/" + title + ".html"])

def create_pages():
    list = os.listdir("blog")
    for file in list:
        insert(path, os.path.splitext(file)[0])

create_pages()

