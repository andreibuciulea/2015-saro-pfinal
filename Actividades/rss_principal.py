
todo = Actividad.objects.order_by('-fecha')
documento = '<?xml version= "1.0" encoding= "ISO-8859-1" ?>\n'
    documento += '<rss version="2.0">\n'
    documento += '\t<channel>\n' 
    documento += '\t\t<titulo> Canal Rss de la Pagina Principal</titulo>\n'
    documento += '\t\t<url>'http://127.0.0.1/'</url>\n'
    documento += '\t\t<descripcion>' Las 10 actividades más recientes '</descripcion>\n'
    items = ""
    m = 0
    for activ in todo:
        items += '\t\t<item>\n'
        items += '\t\t\t<id_evento>' + activ.id_evento + '</id_evento>\n'
        items += '\t\t\t<titulo>' + activ.titulo + '</titulo>\n'
        items += '\t\t\t<precio>' + activ.precio + '</precio>\n'
        items += '\t\t\t<fecha>' + activ.fecha + '</fecha>\n'
        items += '\t\t\t<hora>' + activ.hora + '</hora>\n'
        items += '\t\t\t<duracion>' + activ.duracion +'</duracion>\n'
        items += '\t\t\t<larga_duracion>' + activ.larga_duracion + '</larga_duracion>\n'
        items += '\t\t\t<seleccionado>' + activ.seleccionado + '</seleccionado>\n'
        items += '\t\t\t<puntos>' + activ.hora + '</puntos>\n'
        items += '\t\t</item>\n'
        m = m+1
        if m == 10:
            break
    documento += items
    documento += '\t</channel>\n</rss>'




tipo = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    hora = models.CharField(max_length=32)
    duracion = models.CharField(max_length=100)
    larga_duracion = models.CharField(max_length=100)
    url  = models.CharField(max_length=200)
    seleccionado = models.CharField(max_length=100)
    puntos = models.IntegerField()
