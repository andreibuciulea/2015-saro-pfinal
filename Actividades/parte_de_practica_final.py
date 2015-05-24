    

### esto es para guardar las actividades en la base de datos.
    fichero = open('datos.txt','r')  
    soup = fichero.read()
    fichero.close()
    soup = BeautifulSoup(soup)
    variable = soup.find_all('contenido')
    a = 12
    for cont in variable:
        titulo = cont.find(nombre = "TITULO") 
        tipo = cont.find(nombre = "GRATUITO")
        fecha= cont.find(nombre="FECHA-EVENTO")
        hora =  cont.find(nombre="HORA-EVENTO")
        larga_duracion = cont.find(nombre="EVENTO-LARGA-DURACION") 
        url = cont.find(nombre="CONTENT-URL")
      	actividad = Actividad(titulo = titulo, tipo = 1, precio = a, 
			                  fecha = fecha, hora = hora, duracion = 0, 
                              larga_duracion = 1,
			                  url = url, seleccionado = 0) 
        actividad.save()
    return HttpResponse(titulo)
