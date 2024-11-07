with open("about.txt", "r+") as file:
    content = file.read()
    global new
    new = content.replace("[Your Name]", input(str("what's your name please? ")))
    with open("abouut.txt", "+a") as file2:
        file2.write(new)

