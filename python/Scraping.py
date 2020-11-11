from io import open
a = open("a.html","r")
b=open("b.txt","w")
text=a.read()
b.write(text[text.find("ind") : text.find("ind") + 10])
a.close()
b.close()