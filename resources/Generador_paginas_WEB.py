import os

#{'nombre':'', 'marca':'', 'archivo':'', 'gama':'', 'color':'', 'img_dir':'', 'img_alt':'', 'capacidad':0, 'caracteristicas':[]}
#{'nombre':'', 'marca':'', 'archivo':'', 'gama':'', 'color':'', 'img_dir':'', 'img_alt':'', 'capacidad':0, 'caracteristicas':[]}



def crearPagina(nombre, marca, archivo, gama, color, img_dir, img_alt, capacidad, caracteristicas):
    direccion = r".\client-side\transports\\"
    file = open(direccion + archivo + ".html", "w", encoding="utf-8")
    file.write("<!DOCTYPE html>" + os.linesep)
    file.write("<html lang=\"en\">" + os.linesep)
    file.write("<head>" + os.linesep)
    file.write("        <link rel=\"icon\" type=\"image/png\" href=\"links/img/2_logo.png\"/>" + os.linesep)
    file.write("        <link type=\"text/css\" rel=\"stylesheet\" href=\"transports.css\" media=\"screen\"/>" + os.linesep)
    file.write("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">" + os.linesep)
    file.write("        <meta charset=\"utf-8\" />" + os.linesep)
    file.write("        <title>" + nombre + "</title>" + os.linesep)
    file.write("</head>" + os.linesep)
    file.write("<body>" + os.linesep)
    file.write("        <div class=\"banner\">" + os.linesep)
    file.write("            <div class=title_text>" + os.linesep)
    file.write("                <h1 style=\"font-size:50px\">Servicios  Intergalácticos</h1>" + os.linesep)
    file.write("                <!--<button id=\"button\">Escoger Transporte</button>-->" + os.linesep)
    file.write("            </div>" + os.linesep)
    file.write("        </div>" + os.linesep)
    file.write("        <div class=\"menu\">" + os.linesep)
    file.write("            <a href=\"../index.html\">Inicio</a>" + os.linesep)
    file.write("            <a href=\"../catalogo.html\">Gammas</a>" + os.linesep)
    file.write("            <a href=\"../contacto.html\">Contactos</a>" + os.linesep)
    file.write("        </div>" + os.linesep)
    file.write("        <div class = \"content\" style=\"color:yellow\">" + os.linesep)
    file.write("            <h3>" + nombre + " - " + marca + "</h3>" + os.linesep)
    if gama == "Alta":
        file.write("            <p>Gama: " + gama + " (Tasa: 50§)</p>" + os.linesep)
    elif gama == "Media":
        file.write("            <p>Gama: " + gama + " (Tasa: 25§)</p>" + os.linesep)
    elif gama == "Baja":
        file.write("            <p>Gama: " + gama + " (Tasa: 15§)</p>" + os.linesep)
    else:
        pass
    file.write("            <p>Color: " + color +"</p>" + os.linesep)
    file.write("            <img class=\"img\" alt=\"" + img_alt + "\" src=\"" + img_dir + "\">" + os.linesep)
    file.write("            <h2>Numero de plazas: <b>" + str(capacidad) + "</b></p>" + os.linesep)
    file.write("                <h3>Características:</h3>" + os.linesep)
    file.write("            <!--Características-->" + os.linesep)
    file.write("            <div class=\"caracteristicas\">" + os.linesep)
    for car in caracteristicas:
        file.write("                <p>" + car + "</p>" + os.linesep)

    file.write("            </div>" + os.linesep)
    file.write("        </div>" + os.linesep)
    file.write("        <footer>" + os.linesep)
    file.write("            © Diseño realizado por Antoni Pizarro & Pau Llinàs 2020. Todos los derechos reservados" + os.linesep)
    file.write("        </footer>" + os.linesep)
    file.write("</body>" + os.linesep)
    file.write("</html>")
    file.close()


#Lista de diccionarios

nave = [
    {'nombre':'Crucero de Alderaan', 'marca':'Rebelión', 'archivo':'crucero-alderaan', 'gama':'Alta', 'color':'Blanco', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/databank_alderaancruiser_01_169_c60ce268.jpeg?region=184%2C22%2C1281%2C721&width=768', 'img_alt':'Crucero de Alderaan', 'capacidad':20, 'caracteristicas':["Escudos", "Turbo laser", "Hipervelocidad", "Puerto", "Puente de mando"]},
    {'nombre':'T-70 X-Wing', 'marca':'Resistencia', 'archivo':'t70-xwing', 'gama':'Baja', 'color':'Gris', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/resistance-x-wing_9433981f.jpeg?region=0%2C0%2C1560%2C878&width=768', 'img_alt':'X-Wing de la Resistencia', 'capacidad':2, 'caracteristicas':["Hipervelocidad", "Patas extensibles", "Cabina"]},
    {'nombre':'V-Wing', 'marca':'República', 'archivo':'v-wing', 'gama':'Baja', 'color':'Blanco', 'img_dir':'https://static.wikia.nocookie.net/starwars/images/a/a9/V-wing_BF2.png/revision/latest?cb=20170825000555', 'img_alt':'V-Wing de la República', 'capacidad':1, 'caracteristicas':["Torpedos", "Cabina", "Hipervelocidad"]},
    {'nombre':'Y-Wing', 'marca':'República', 'archivo':'y-wing', 'gama':'Baja', 'color':'Blanco', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/resistance-ywing-main_10b5e63d.jpeg?region=0%2C0%2C1280%2C720&width=768', 'img_alt':'Y-Wing de la República', 'capacidad':2, 'caracteristicas':["Torpedos", "Hipervelocidad", "Cabina"]},
    {'nombre':'Magna Guard Fighter', 'marca':'CSI', 'archivo':'magna-guard', 'gama':'Media', 'color':'Gris Oscuro', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/magnaguard-fighter-main-image_078e5f8b.jpeg?region=0%2C58%2C1560%2C878&width=768', 'img_alt':'Caza Magna Guard de los separatistas', 'capacidad':2, 'caracteristicas':["Cañones de iones", "Escudos", "Cabina"]},
    {'nombre':'Neimoidian Escort Shuttle', 'marca':'CSI', 'archivo':'neimoidian-escort', 'gama':'Media', 'color':'Gris', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/neimoidian_escort_shuttle_7602d574.jpeg?region=0%2C6%2C1433%2C806&width=768', 'img_alt':'Lanzadera de los separatistas', 'capacidad':4, 'caracteristicas':["Escudos", "Hipervelocidad", "Patas extensibles", "Puente de mando"]},
    {'nombre':'Cañonera de la República', 'marca':'República', 'archivo':'cañonera-republica', 'gama':'Media', 'color':'Blanco', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/databank_republicattackgunship_01_169_4ed5c0a7.jpeg?region=0%2C0%2C1560%2C878&width=768', 'img_alt':'Cañonera de la República', 'capacidad':6, 'caracteristicas':["Cañones de iones", "Misileros", "Cabina", "Camara de carga"]},
    {'nombre':'Twilight', 'marca':'CSI', 'archivo':'twilight', 'gama':'Media', 'color':'Gris', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/databank_twilight_01_169_9b1eb370.jpeg?region=0%2C0%2C1560%2C878&width=768', 'img_alt':'Twilight de los separatistas', 'capacidad':5, 'caracteristicas':["Cañones de iones", "Escudos", "Hipervelocidad", "Patas extensibles", "Camara de carga"]},
    {'nombre':'AA-9', 'marca':'República', 'archivo':'aa-9', 'gama':'Media', 'color':'Marrón', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/aa-9-coruscant-freighter_a856053d.jpeg?region=92%2C0%2C1181%2C665&width=768', 'img_alt':'AA-9 de la República', 'capacidad':30, 'caracteristicas':["Escudos", "Hipervelocidad", "Puente de mando", "Camara de carga"]},
    {'nombre':'GR-75', 'marca':'Rebelión', 'archivo':'gr-75', 'gama':'Alta', 'color':'Blanco', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/gr-75-medium-transport_cd04862d.jpeg?region=15%2C0%2C770%2C433&width=768', 'img_alt':'GR-75 de la Rebelión', 'capacidad':8, 'caracteristicas':["Turbo laser", "Escudos", "Hipervelocidad", "Puente de mando", "Camara de carga", "Puerto"]},
    {'nombre':'Imperial Shuttle', 'marca':'Imperio Galáctico', 'archivo':'imperial-shuttle', 'gama':'Alta', 'color':'Gris', 'img_dir':'https://lumiere-a.akamaihd.net/v1/images/veh_ia_1752_040381b2.jpeg?region=0%2C70%2C1280%2C720&width=768', 'img_alt':'Lanzadera imperial', 'capacidad':6, 'caracteristicas':["Cañones de iones", "Escudos", "Hipervelocidad", "Patas extensibles", "Puente de mando"]}
    ]

for element in nave:
    crearPagina(element['nombre'], element['marca'], element['archivo'], element['gama'], element['color'], element['img_dir'], element['img_alt'], element['capacidad'], element['caracteristicas'])