import os
archivo = "Mi nave"
direccion = r"C:\Users\Toni\Desktop\\"
file = open(direccion + archivo + ".html", "w")
file.write("<!DOCTYPE html>" + os.linesep)
file.write("<html lang=\"en\">" + os.linesep)
file.write("<head>" + os.linesep)
file.write("    <meta charset=\"UTF-8\">" + os.linesep)
file.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">" + os.linesep)
file.write("    <title>Document</title>" + os.linesep)
file.write("</head>" + os.linesep)
file.write("<body>" + os.linesep)
file.write("</body>" + os.linesep)
file.write("</html>" + os.linesep)
file.close()