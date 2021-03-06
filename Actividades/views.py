from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import Context,Template
from django.template.loader import get_template
from django.shortcuts import render_to_response,render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from bs4 import BeautifulSoup 
import string
import urllib2
import datetime
from dateutil import parser
from models import Actividad,Usuario
# total = Actividad.objects.count()
formulario = "<html><body><form method=POST>\
       User: <input type=text name=fname><br>\
       Paswd:<input type=text name=fname><br>\
       <input type=submit value=Entrar>\
       </form></body></html>"
form_filtro = "<form action= ""method = post>"
form_filtro += "Search: <input name=searchquery type=textsize=70 maxlength=88>"
form_filtro +="<input name=myBtn type=submit> <br><br> Search In: <select name=filter1>"
form_filtro +="<option value=Whole Site>Whole Site</option>"
form_filtro +="<option value=Pages>Pages</option>" 
form_filtro +="<option value=Blog>Blog</option> </select> </form>"


@csrf_exempt
def ayuda(request):
    template = get_template('index_ayuda.html')
    c = Context({'title': 'ayuda'})	
    rend = template.render(c)
    return HttpResponse(rend)
##############################___LOGIN___############################################# 

@csrf_exempt 
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        auth.login(request,user)
        try:
            usu = Usuario.objects.get(nombre = username)
        except:
            url = "http://127.0.0.1:1234/" + username
            rss = url + "/rss"
            titulo_p = "Pagina de " + username
            mi_usuario = Usuario(nombre = username,url = url,titulo_p = titulo_p,fondo = "css/defult.css",rss = rss)
            mi_usuario.save()
        return HttpResponseRedirect('/todas')
    else:
        return HttpResponseRedirect('/') 

########################################___USUARIO__##################################
@csrf_exempt 
def usuario(request,nombre):
    if request.user.is_authenticated():
        template = get_template('index_usuario.html')
        mi_usuario = Usuario.objects.get(nombre = nombre)
        publicaciones = mi_usuario.pagina.all()
        if request.method == "GET":
            try: 
                usu = Usuario.objects.get(nombre = nombre)  
                c = Context({'usuario': usu,'titulo': publicaciones})
                rend = template.render(c)
            except:
                return HttpResponse("estoy en usuario y no esta creado")
            return HttpResponse(rend)
        elif request.method == "POST":
            rqst = request.body.split("=")[0]
            if rqst == "fname":
                pagina = str(request.body.split("=")[1])
                titulo_p = string.replace(pagina,"+"," ")
                usu = Usuario.objects.get(nombre = nombre)
                usu.titulo_p = titulo_p
                usu.save() 
                c = Context({'usuario': usu,'titulo': publicaciones})
                rend = template.render(c)
                return HttpResponse(rend)
            elif rqst == "filter":
                fondo = request.body.split("=")[1].split("&")[0]
                fondo = "css/" + fondo
                usu = Usuario.objects.get(nombre = nombre)
                usu.fondo = fondo
                usu.save() 
                c = Context({'usuario': usu,'titulo': publicaciones})
                rend = template.render(c)
                return HttpResponse(rend)
    else:
        template = get_template('index_usuario_no.html')    
        mi_usuario = Usuario.objects.get(nombre = nombre)
        publicaciones = mi_usuario.pagina.all()
        c = Context({'usuario': nombre,'titulo': publicaciones})
        rend = template.render(c)
        return HttpResponse(rend)


###########################___________ TODAS______________############################
@csrf_exempt
def todo(request):
    template = get_template('index_todo.html')
    template1 = get_template('index_todo_no.html')
    N = Actividad.objects.count()   
    usuar = {}
    nombre = request.user.username
    url = "http://127.0.0.1:1234/" + nombre
    users = Usuario.objects.all()
    m = 1
    for n in users:
        usuar[n] = m
        m = m+1
    if request.user.is_authenticated():
        if request.method == "GET":
            todo = Actividad.objects.order_by('-fecha')
            c = Context({'t': todo,'filtro':form_filtro,'nombre': nombre,'url':url,'numero': N,'usuarios':usuar})
        elif request.method == "POST":
            reqst = request.body.split("=")[0]
            if reqst == "filter":
                metodo = request.body.split("=")[1]
                metodo = metodo.split("&")[0]
                if metodo == "fecha":
                    todo = Actividad.objects.order_by("-" + metodo)
                else: 
                    todo = Actividad.objects.order_by(metodo)
                c = Context({'t': todo,'filtro':form_filtro,'nombre': nombre,'url':url,'numero': N,'usuarios':usuar})    
            else:
                peticion = request.body.split("=")[1]
                mi_id = request.body.split("=")[0]
                activ = Actividad.objects.get(id = mi_id)
                if peticion == "Add":
                    activ.seleccionado = str(datetime.datetime.now())
                    activ.save()
                    usu = Usuario.objects.get(nombre = nombre)
                    usu.url = "http://127.0.0.1:1234/" + nombre
                    usu.pagina.add(activ)
                    usu.save()
                else:
                    activ.puntos = activ.puntos + 1
                    activ.save()
                return HttpResponseRedirect("/todas")             
        rend = template.render(c)
        return HttpResponse(rend) 
    else:
        if request.method == "GET":
            todo = Actividad.objects.order_by('-fecha')
            c = Context({'t': todo,'filtro':form_filtro})
            rend = template1.render(c)
            return HttpResponse(rend)
        else: 
            mi_id = request.body.split("=")[0]
            activ = Actividad.objects.get(id = mi_id)
            activ.puntos = activ.puntos + 1
            activ.save()
            todo = Actividad.objects.order_by('-fecha')
            c = Context({'t': todo,'filtro':form_filtro})
            rend = template1.render(c)
            return HttpResponse(rend)
            return HttpResponse()


#########################_________ACTUALIZAR____________##############################
def actualizar(request):
    #fichero = open('datos.txt','r')  
    #soup = fichero.read()
    #fichero.close()
    recurso  = "http://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31"
    recurso += "cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0"
    recurso += "aRCRD&format=xml&file=0&filename=206974-0-agenda-eventos-cultura"
    recurso += "les-100&mgmtid=6c0b6d01df986410VgnVCM2000000c205a0aRCRD"
    url = urllib2.urlopen(recurso)
    soup = url.read()
    soup = BeautifulSoup(soup)
    variable = soup.find_all('contenido') 
    for cont in variable:
        id_evento = cont.find(nombre="ID-EVENTO")
        id_evento = int(id_evento.string)
        print id_evento
        titulo = cont.find(nombre = "TITULO") 
        tipo = cont.find(nombre = "GRATUITO")
        if tipo.string == "1":
            tipo = "Gratis"
        elif tipo.string == "0":
            tipo = "No Gratis"
        else:
            tipo = "No INFO"
        fecha= cont.find(nombre="FECHA-EVENTO")
        hora = cont.find(nombre="HORA-EVENTO")		
        larga_duracion = cont.find(nombre="EVENTO-LARGA-DURACION")
        if larga_duracion == None:
            larga_duracion = "NO INFO" 
        elif larga_duracion.string == "1":
            larga_duracion = "SI"
        elif larga_duracion.string == "0":
            larga_duracion = "NO"
        url = cont.find(nombre="CONTENT-URL")
        fecha_fin = cont.find(nombre = "FECHA-FIN-EVENTO")
        fecha_ini = cont.find(nombre = "FECHA-EVENTO")
        hora = hora.string
        fecha_fin = fecha_fin.string
        hora = parser.parse(hora)
        final = parser.parse(fecha_fin)
        duracion = str(final-hora)
        try:
            duracion = duracion.split(' ')[2]
        except:
            duracion = duracion
        duracion = datetime.datetime.strptime(duracion, '%H:%M:%S')
        try:
            if precio.string == None:
                precio = "No hay info"
            else:
                precio = precio.string       
        except:    
            precio = "No hay info"
        hora = str(hora).split(" ")[1]
        fecha = fecha.string
        fecha = fecha.split(" ")[0]
        try:
            activ = Actividad.objects.get(id_evento = id_evento)
        except:
            actividad = Actividad(id_evento = id_evento,titulo = titulo.string, tipo = tipo, precio = precio, 
		                          fecha = fecha, hora = hora, duracion = duracion, 
                                  larga_duracion = larga_duracion,url = url.string, seleccionado = 0,puntos = 0)
            actividad.save()
    return HttpResponseRedirect("http://127.0.0.1:1234/todas")

#################################----PAGINA PRINCIPAL----######################################
@csrf_exempt
def principal(request):
    info = {}
    usuar = {}
    template = get_template('index.html')
    nombre = request.user.username
    url_u = "http://127.0.0.1:1234/" + nombre
    if request.method == "GET":
        todo = Actividad.objects.order_by('-fecha')
        users = Usuario.objects.all()
        m = 1
        for n in users:
            usuar[n] = m
            m = m+1
        for k in range(0,10):
            info[todo[k]] = k
            c = Context({'titulo': info,'usuarios':usuar,'url_u': url_u})
        rend = template.render(c)
    return HttpResponse(rend)

########################______RSS_____###################################
def rss(request,nombre):
    
    documento = '<?xml version= "1.0" encoding= "ISO-8859-1" ?>\n'
    documento += '<rss version="2.0">\n'
    documento += '\t<channel>\n' 
    usuario = Usuario.objects.get(nombre = nombre)
    publicaciones = usuario.pagina.all()

    items = ""
    for activ in publicaciones:
        items += '\t\t<item>\n'
        items += '\t\t\t<titulo>' + activ.titulo + '</titulo>\n'
        items += '\t\t\t<fecha>' + activ.fecha + '</fecha>\n'
        items += '\t\t\t<duracion>' + activ.duracion +'</duracion>\n'
        items += '\t\t\t<precio>' + activ.precio + '</precio>\n'
        items += '\t\t</item>\n'
    documento += '\t\t<titulo> Canal Rss de: '+ usuario.nombre + '</titulo>\n'
    documento += '\t\t<url>' + usuario.url + '</url>\n'
    documento += items
    documento += '\t</channel>\n</rss>'

    return HttpResponse(documento,content_type = 'rss')


def rss_principal(request):
    todo = Actividad.objects.order_by('-fecha')
    documento = '<?xml version= "1.0" encoding= "ISO-8859-1" ?>\n'
    documento += '<rss version="2.0">\n'
    documento += '\t<channel>\n' 
    documento += '\t\t<titulo> Canal Rss de la Pagina Principal</titulo>\n'
    documento += '\t\t<url>http://127.0.0.1/</url>\n'
    documento += '\t\t<descripcion> Las 10 actividades mas recientes </descripcion>\n'
    items = ""
    m = 0
    for activ in todo:
        items += '\t\t<item>\n'
        items += '\t\t\t<id_evento>' + str(activ.id_evento) + '</id_evento>\n'
        items += '\t\t\t<titulo>' + activ.titulo + '</titulo>\n'
        items += '\t\t\t<precio>' + activ.precio + '</precio>\n'
        items += '\t\t\t<fecha>' + activ.fecha + '</fecha>\n'
        items += '\t\t\t<hora>' + activ.hora + '</hora>\n'
        items += '\t\t\t<duracion>' + activ.duracion +'</duracion>\n'
        items += '\t\t\t<larga_duracion>' + activ.larga_duracion + '</larga_duracion>\n'
        items += '\t\t\t<seleccionado>' + activ.seleccionado + '</seleccionado>\n'
        items += '\t\t\t<puntos>' + str(activ.puntos) + '</puntos>\n'
        items += '\t\t</item>\n'
        m = m+1
        if m == 10:
            break
    documento += items
    documento += '\t</channel>\n</rss>'
    return HttpResponse(documento,content_type = 'rss')

