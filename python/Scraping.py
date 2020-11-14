import os
a = open("a.html","r")
b=open("b.txt","w")
text=a.read()
b.write(text[text.find("ind") : text.find("ind") + 10] + os.linesep)
b.write(text[text.find("cat") : text.find("cat") + 13] + os.linesep)
b.write(text[text.find("Gam") : text.find("Gam") + 9] + os.linesep)
a.close()
b.close()