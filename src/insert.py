
path = ""


with open(path, r) as content_file:
    


path = "src/base.html"

with open(path, "r+") as base:
    pos = 0
    while(True):
        line = base.readLine()
        if line.startswith('<body>'):
            break    
        if (line == ""):
            return
    base.seek(i + 1)
    rem = base.read()


