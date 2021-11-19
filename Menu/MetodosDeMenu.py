from Anses.Anses import leerCuilsDelAnses, leerCiudadano, leerDataEspecificaDeCiudadano, escribirCiudadano, \
    leerDataEspecificaDeAdmin, escribirAdministrador, leerTiposDeEvento, escribirEvento
from GestionUsuarios.Ciudadano import Ciudadano
from GestionUsuarios.Administrador import Administrador
from GestionUsuarios.ABM import crearAdministrador, eliminarAdministrador, modificarUsernameAdministrador, modificarContrasenaDeAdmin
from Mapa.Mapa import mapa


def login():
    print("1- Registrarse")
    print("2- Iniciar sesion como administrador")
    print("3- Iniciar sesion como usuario")
    print("4- Salir del programa")
    try:
        x=int(input("seleccione la opción: "))
        if x==1:
            ContieneCuilEnAnses()
        elif x==2:
            EstaElUsernameAdmin()
        elif x==3:
            EstaElUsernameCiudadano()
        elif x==4:
            print("Gracias por usar el programa")
        else:
            print("opción invalida, seleccione otra vez")
            login()
    except ValueError:
        print("valor incorrecto, vuelva a elegir el numero")
        login()

def ContieneCuilEnAnses():
    cuil = str(input("Ingrese su numero de CUIL sin guion(debe ser de 11 digitos, EJ: 23440529259), en caso de querer volver atras ingrese el numero 0: "))
    if cuil == "0":
        login()
    else:
        listaCUILsDelAnses = []
        leerCuilsDelAnses(listaCUILsDelAnses)
        posicionListaCuilsDelAnses = 0
        existeEnAnses = False
        while posicionListaCuilsDelAnses < len(listaCUILsDelAnses):
            if cuil == listaCUILsDelAnses[posicionListaCuilsDelAnses]:
                existeEnAnses = True
                posicionListaCuilsDelAnses = posicionListaCuilsDelAnses + len(listaCUILsDelAnses)
            else:
                posicionListaCuilsDelAnses = posicionListaCuilsDelAnses + 1
        if existeEnAnses == True:
            yaExisteElUsuario(cuil)
        else:
            print("Su numero de Cuil no se encuentra en la lista del Anses, vuelva a escribirlo. En caso de seguir teniendo este problema comuniquese con el Anses.")
            ContieneCuilEnAnses()
def yaExisteElUsuario(cuil):
    listaCUILsDeUsersCreados = []
    leerDataEspecificaDeCiudadano(listaCUILsDeUsersCreados,0)
    estaDuplicado = False
    posicionListaCuilDeUsersCreados = 0
    while posicionListaCuilDeUsersCreados < len(listaCUILsDeUsersCreados):
        if cuil == listaCUILsDeUsersCreados[posicionListaCuilDeUsersCreados]:
            estaDuplicado = True
            posicionListaCuilDeUsersCreados = posicionListaCuilDeUsersCreados + len(listaCUILsDeUsersCreados)
        else:
            posicionListaCuilDeUsersCreados= posicionListaCuilDeUsersCreados + 1
    if estaDuplicado == True:
        print("El CUIL que ingresó es de un usuario ya creado. Si es el suyo vaya a login para iniciar sesión,sino escriba un nuevo cuil.")
        ContieneCuilEnAnses()
    else:
        EstaRepetidoElCelular(cuil)
def EstaRepetidoElCelular(cuil):
    celular = str(input("Ingrese su numero de telefono sin su codigo de país(debe tener 10 digitos en total, EJ: 1154885993), en caso de querer volver atras ingrese el numero 0: "))
    if celular == "0":
        login()
    elif len(celular) == 10:
        listaCelularesDeUsersCreados = []
        leerDataEspecificaDeCiudadano(listaCelularesDeUsersCreados,1)
        estaDuplicado = False
        posicionListaCelularesDeUsersCreados = 0
        while posicionListaCelularesDeUsersCreados < len(listaCelularesDeUsersCreados):
            if celular == listaCelularesDeUsersCreados[posicionListaCelularesDeUsersCreados]:
                estaDuplicado = True
                posicionListaCelularesDeUsersCreados = posicionListaCelularesDeUsersCreados + len(listaCelularesDeUsersCreados)
            else:
                posicionListaCelularesDeUsersCreados = posicionListaCelularesDeUsersCreados + 1
        if estaDuplicado == True:
            print("El numero de telefono que ingresó se encuentra en uso por otro usuario, ingrese uno nuevo.")
            EstaRepetidoElCelular(cuil)
        else:
            creadorDelUsuario(cuil,celular)
    else:
        print("el numero ingresado no tiene 10 digitos,ingreselo otra vez.")
        EstaRepetidoElCelular(cuil)
def creadorDelUsuario(cuil,celular):
    intCUIL = int(cuil)
    intCelular = int(celular)
    CiudadanoACrear = Ciudadano(intCUIL,intCelular,0,False)
    escribirCiudadano(CiudadanoACrear)
    print("Se ha creado el usuario.")
    login()

def EstaElUsernameAdmin():
    username=str(input("Ingrese su nombre de usuario, en caso de querer volver atras ingrese el numero 0: "))
    if username == "0":
        login()
    else:
        ListaNombresDeAdmins=[]
        leerDataEspecificaDeAdmin(ListaNombresDeAdmins,0)
        existeElUsuario=False
        indiceDeLista = 0
        posicionDelNombre = -1
        while indiceDeLista < len(ListaNombresDeAdmins):
            if username == ListaNombresDeAdmins[indiceDeLista]:
                existeElUsuario = True
                posicionDelNombre = indiceDeLista
                indiceDeLista= indiceDeLista + len(ListaNombresDeAdmins)
            else:
                indiceDeLista = indiceDeLista + 1
        if existeElUsuario == True:
            EstaLaContrasenaAdmin(username,posicionDelNombre)
        else:
            print("Este username no existe, escriba otro.")
            EstaElUsernameAdmin()
def EstaLaContrasenaAdmin(username,posicionDelNombre):
    contrasena = str(input("Ingrese su contraseña, en caso de querer volver atras ingrese el numero 0: "))
    if contrasena == "0":
        login()
    else:
        ListaContrasenasAdmins=[]
        leerDataEspecificaDeAdmin(ListaContrasenasAdmins,1)
        if contrasena == ListaContrasenasAdmins[posicionDelNombre]:
            crearObjetoAdminEnRuntime(username,contrasena,posicionDelNombre)
        else:
            print("contraseña incorrecta, escribala de nuevo")
            EstaLaContrasenaAdmin(username,posicionDelNombre)
def crearObjetoAdminEnRuntime(username,contrasena,posicionDelNombre):
    ListaPosicionDelABM= []
    leerDataEspecificaDeAdmin(ListaPosicionDelABM,2)
    booleanABM = int(ListaPosicionDelABM[posicionDelNombre])
    ABM = False
    if booleanABM == 1:
        ABM = True
    else:
        ABM = False
    AdminEnRuntime = Administrador(username,contrasena,ABM)
    menuAdmin(AdminEnRuntime)
def menuAdmin(AdminEnRuntime):
    print("¿Que desea hacer?")
    print("1-Agregar tipo de evento")
    print("2-Bloquear usuario")
    print("3-Desbloquear usuario")
    print("4-Crear administrador")
    print("5-Modificar administrador")
    print("6-Eliminar administrador")
    print("7-Salir del programa")
    try:
        x=int(input("seleccione la opción: "))
        if x == 1:
            AdminEnRuntime.crearTipoDeEvento()
            menuAdmin(AdminEnRuntime)
        elif x == 2:
            citizenAModificarEstado = generadorDeCitizenParaBloqueoODesbloqueo(AdminEnRuntime)
            AdminEnRuntime.bloquearCiudadano(citizenAModificarEstado)
            menuAdmin(AdminEnRuntime)

            menuAdmin(AdminEnRuntime)
        elif x == 3:
            menuAdmin(AdminEnRuntime)
        elif x == 4:
            if AdminEnRuntime.accesoAABM == True:
                usuario = checkerInexistenciaDelUsername(AdminEnRuntime)
                newcontrasena = creadorDeContrasena(AdminEnRuntime)
                ABM = selectorDeABM(AdminEnRuntime)
                AdminACrear = crearAdministrador(usuario,newcontrasena,ABM)
                escribirAdministrador(AdminACrear)
                print("se ha creado el administrador nuevo")
                menuAdmin(AdminEnRuntime)
            else:
                print("No se encuentra autorizado para hacer esa operación")
                menuAdmin(AdminEnRuntime)
        elif x == 5:
            menuDeModificacion(AdminEnRuntime)
        elif x == 6:
            if AdminEnRuntime.accesoAABM == True:
                usuarioAEliminar = checkAdminName(AdminEnRuntime)
                eliminarAdministrador(usuarioAEliminar)
                menuAdmin(AdminEnRuntime)
            else:
                print("No se encuentra autorizado para hacer esa operación")
                menuAdmin(AdminEnRuntime)
        elif x == 7:
            print("Se ha cerrado la sesión correctamente.")
            login()
        else:
            print("opción invalida, seleccione otra vez")
            menuAdmin(AdminEnRuntime)
    except ValueError:
        print("valor incorrecto, vuelva a elegir el numero")
        menuAdmin(AdminEnRuntime)
def checkerInexistenciaDelUsername(AdminEnRuntime):
    username = str(input("Ingrese el nombre de usuario, escriba 0 si desea volver atras: "))
    if username == "0":
        menuAdmin(AdminEnRuntime)
    else:
        ListaNombresDeAdmins = []
        leerDataEspecificaDeAdmin(ListaNombresDeAdmins, 0)
        existeElUsuario = False
        indiceDeLista = 0
        while indiceDeLista < len(ListaNombresDeAdmins):
            if username == ListaNombresDeAdmins[indiceDeLista]:
                existeElUsuario = True
                indiceDeLista = indiceDeLista + len(ListaNombresDeAdmins)
            else:
                indiceDeLista = indiceDeLista + 1
        if existeElUsuario == True:
            print("Ya existe un admin con ese nombre")
            menuAdmin(AdminEnRuntime)
        else:
            return username
def creadorDeContrasena(AdminEnRuntime):
    contrasena = str(input("ingrese la contraseña del nuevo administrador, escriba 0 si desea volver atras: "))
    if contrasena == "0":
        menuAdmin(AdminEnRuntime)
    else:
        return contrasena
def selectorDeABM(AdminEnRuntime):
    x= str(input("escriba 1 si desea que este admin tenga acceso a los metodos ABM, 0 si desea volver atras, y cualquier otro valor en caso de que no desea que tenga acceso a los metodos ABM:"))
    if x == "0":
        menuAdmin(AdminEnRuntime)
    elif x == "1":
        return True
    else:
        return False
def checkAdminName(AdminEnRuntime):
    username = str(input("escriba el nombre de usuario del Admin: "))
    listaNombre = []
    leerDataEspecificaDeAdmin(listaNombre,0)
    indiceLista = 0
    existeElUser = False
    while indiceLista < len(listaNombre):
        if username == listaNombre[indiceLista]:
            existeElUser = True
            indiceLista = indiceLista + len(listaNombre)
        else:
            indiceLista = indiceLista + 1
    if existeElUser == True:
        return username
    else:
        print("No existe este username de administrador")
        menuAdmin(AdminEnRuntime)
def checkAdminNametoModify(AdminEnRuntime):
    username = str(input("escriba el nombre de usuario del Admin: "))
    if username == AdminEnRuntime.usuario:
        listaNombre = []
        leerDataEspecificaDeAdmin(listaNombre,0)
        indiceLista = 0
        existeElUser = False
        while indiceLista < len(listaNombre):
            if username == listaNombre[indiceLista]:
                existeElUser = True
                indiceLista = indiceLista + len(listaNombre)
            else:
                indiceLista = indiceLista + 1
        if existeElUser == True:
            return username
        else:
            print("No existe este username de administrador")
            menuAdmin(AdminEnRuntime)
    else:
        print("ese no es tu username")
        menuDeModificacion(AdminEnRuntime)
def checkAdminPassword(AdminEnRuntime):
    contrasena=str(input("escriba su contraseña: "))
    if contrasena == AdminEnRuntime.contrasena:
        listaContrasena = []
        leerDataEspecificaDeAdmin(listaContrasena,1)
        indiceLista = 0
        existeLaContra = False
        while indiceLista < len(listaContrasena):
            if contrasena == listaContrasena[indiceLista]:
                existeLaContra = True
                indiceLista = indiceLista + len(listaContrasena)
            else:
                indiceLista = indiceLista + 1
        if existeLaContra == True:
            return contrasena
        else:
            print("no existe esa contrasena")
            menuAdmin(AdminEnRuntime)
    else:
        print("no escribiste tu contraseña")
        menuDeModificacion(AdminEnRuntime)
def menuDeModificacion(AdminEnRuntime):
    print("1-Modificar el username.")
    print("2-Modificar la contraseña.")
    y = str(input("seleccione la opción,seleccione 0 para volver atrás: "))
    if y == "0":
        menuAdmin(AdminEnRuntime)
    elif y == "1":
        UsernameViejo = checkAdminNametoModify(AdminEnRuntime)
        modificarUsernameAdministrador(UsernameViejo)
        menuAdmin(AdminEnRuntime)
    elif y == "2":
        contrasena = checkAdminPassword(AdminEnRuntime)
        modificarContrasenaDeAdmin(contrasena)
        menuAdmin(AdminEnRuntime)
    else:
        print("opción invalida, vuelva a escribirlo.")
        menuDeModificacion(AdminEnRuntime)
def generadorDeCitizenParaBloqueoODesbloqueo(AdminEnRuntime):
    cuilUser=str(input("Escriba el cuil del usuario: "))
    listaUsernames=[]
    leerDataEspecificaDeCiudadano(listaUsernames, 0)
    indiceLista=0
    valorABuscar =-1
    existeElUsername = False
    while indiceLista < len(listaUsernames):
        if cuilUser == listaUsernames[indiceLista]:
            valorABuscar = indiceLista
            existeElUsername = True
            indiceLista = indiceLista + len(listaUsernames)
        else:
            indiceLista = indiceLista + 1
    if existeElUsername == True:
        cuilUserINT = int(cuilUser)
        listaTelefonos = []
        leerDataEspecificaDeCiudadano(listaTelefonos,1)
        telefono = int(listaTelefonos[valorABuscar])
        listaSoliRechazada = []
        leerDataEspecificaDeCiudadano(listaSoliRechazada,2)
        soliRechazada = int(listaSoliRechazada[valorABuscar])
        listaBoolNumerico = []
        leerDataEspecificaDeCiudadano(listaBoolNumerico,3)
        boolNumerico = int(listaBoolNumerico[valorABuscar])
        if boolNumerico == 1:
            boolean = True
        else:
            boolean = False
        return Ciudadano(cuilUserINT,telefono,soliRechazada,boolean)
    else:
        print("el usuario a modificar no existe.")
        menuAdmin(AdminEnRuntime)
def modificacionDeUsuario(adminEnRuntime,ciudadano):
    pass

def EstaElUsernameCiudadano():
    cuilCiudadano=str(input("Ingrese su CUIL correspondiente(EJ:42382331653), en caso de querer volver atras ingrese el numero 0: "))
    if cuilCiudadano == "0":
        login()
    else:
        ListaNombresDeCiudadano=[]
        leerDataEspecificaDeCiudadano(ListaNombresDeCiudadano,0)
        existeElUsuario=False
        indiceDeLista = 0
        posicionDelCuil = -1
        while indiceDeLista < len(ListaNombresDeCiudadano):
            if cuilCiudadano == ListaNombresDeCiudadano[indiceDeLista]:
                existeElUsuario = True
                posicionDelCuil = indiceDeLista
                indiceDeLista= indiceDeLista + len(ListaNombresDeCiudadano)
            else:
                indiceDeLista = indiceDeLista + 1
        if existeElUsuario == True:
            checkearCelular(cuilCiudadano,posicionDelCuil)
        else:
            print("Este CUIL no pertenece a ningún usuario, escriba otro.")
            EstaElUsernameCiudadano()
def checkearCelular(cuil,posicionDelCuil):
    celular = str(input("ingrese su numero de telefono, sin su cogigo de país(EJ:1154885993), en caso de querer volver atras introduzca el numero 0: "))
    if celular == "0":
        login()
    else:
        listaTelefonosCiudadanos = []
        leerDataEspecificaDeCiudadano(listaTelefonosCiudadanos, 1)
        if celular == listaTelefonosCiudadanos[posicionDelCuil]:
            crearCiudadanoEnRuntime(cuil,celular,posicionDelCuil)
        else:
            print("el numero de telefono es incorrecto, escribalo otra vez")
            checkearCelular(cuil, posicionDelCuil)
def crearCiudadanoEnRuntime(cuil,celular,posicionDelCuil):
    listaSolicitudesRechazadas = []
    leerDataEspecificaDeCiudadano(listaSolicitudesRechazadas,2)
    solicitudesR = int(listaSolicitudesRechazadas[posicionDelCuil])
    listaBloqueo = []
    leerDataEspecificaDeCiudadano(listaBloqueo,3)
    bloqueoINT= int(listaBloqueo[posicionDelCuil])
    if bloqueoINT == 1:
        bloqueoBOOLEAN = True
    else:
        bloqueoBOOLEAN = False
    ciudadanoEnRuntime = Ciudadano(cuil,posicionDelCuil,solicitudesR,bloqueoBOOLEAN)
    menuCitizen(ciudadanoEnRuntime)
def menuCitizen(ciudadanoEnRuntime):
    print("1-Crear Evento")
    print("2-Ver invitaciones")
    print("3-Enviar invitación")
    print("4-Ver mapa")
    print("5-Salir del programa")
    try:
        x = int(input("Seleccione la opción:"))
        if x == 1:
            if ciudadanoEnRuntime.estaBloqueado == True:
                print("Actualmente se encuentra bloqueado, comuniquese con un administrador.")
                menuCitizen(ciudadanoEnRuntime)
            else:
                try:
                    nombre = str(input("Escriba el nombre del evento: "))
                    ano = int(input("Escriba el año del evento de forma numerica(EJ 2021): "))
                    mes = int(input("Escriba el mes de forma numerica(EJ 12): "))
                    dia = int(input("Escriba el dia de forma numerica(EJ 26): "))
                    hora = int(input("Escriba la hora de forma numerica(23): "))
                    minuto = int(input("Escriba el minuto de foma numerica(37): "))
                    tipoDeEvento = chequertipoEvento()
                    cantidadMaximaDePersonas = chequerCantidadMaximaDePersonas()
                    coordenadaEnx = float(input("Escriba la coordenada en el eje X: "))
                    coordenadaEny = float(input("Escriba la coordenada en el eje Y: "))
                    newEvento = ciudadanoEnRuntime.crearEvento(nombre,ano,mes,dia,hora,minuto,tipoDeEvento,cantidadMaximaDePersonas,coordenadaEnx,coordenadaEny)
                    escribirEvento(newEvento)
                    print("se añadio el evento " + nombre + " a la lista de eventos.")
                    menuCitizen(ciudadanoEnRuntime)
                except ValueError:
                    print("Ingresaste un valor invalido,cargue la información de nuevo")
                    menuCitizen(ciudadanoEnRuntime)
        elif x == 2:
            menuCitizen(ciudadanoEnRuntime)
        elif x == 3:
            if ciudadanoEnRuntime.estaBloqueado == True:
                print("Actualmente se encuentra bloqueado, comuniquese con un administrador.")
                menuCitizen(ciudadanoEnRuntime)
            else:
                print("Se encuentra bloqueado en estos momentos.")
                menuCitizen(ciudadanoEnRuntime)
        elif x == 4:
            mapa()
            menuCitizen(ciudadanoEnRuntime)

        elif x == 5:
            print("Se ha cerrado la sesión correctamente.")
            login()
        else:
            print("opción invalida, seleccione otra vez.")
            menuCitizen(ciudadanoEnRuntime)
    except ValueError:
        print("valor incorrecto, vuelva a elegir el numero")
        menuCitizen(ciudadanoEnRuntime)
def chequertipoEvento():
    listaTiposDeEvento =  []
    leerTiposDeEvento(listaTiposDeEvento)
    for x in listaTiposDeEvento:
        print(x)
    tipoDeEventoABuscar = str(input("Ingrese el tipo de evento: "))
    indiceLista = 0
    estaEnLosTipos=False
    while indiceLista < len(listaTiposDeEvento):
        if tipoDeEventoABuscar == listaTiposDeEvento[indiceLista]:
            estaEnLosTipos=True
            indiceLista = indiceLista + len(listaTiposDeEvento)
        else:
            indiceLista = indiceLista + 1
    if estaEnLosTipos == True:
        return tipoDeEventoABuscar
    else:
        print("Este tipo de evento no existe,escriba otro")
        chequertipoEvento()
def chequerCantidadMaximaDePersonas():
    x=int(input("Escriba la cantidad maxima de personas para asistir al evento: "))
    if x >= 1:
        return x
    else:
        print("Cargaste un valor invalido, vuelva a cargarlo.")
        chequerCantidadMaximaDePersonas()


