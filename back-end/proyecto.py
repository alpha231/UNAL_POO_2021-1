#Libreria sqlite3 esta incluida por defecto, permite elaborar y manipular bases de datos
import sqlite3 
from sqlite3 import Error
#Libreria smtplib esta incluida por defecto, permite la creación y envio de correos electronicos
import smtplib
#Libreria incluida por defecto, MIMEMultipart con el fin de organizar los datos relacionados a la aplicación de correos electronicos (remitente y destinatario)
from email.mime.multipart import MIMEMultipart 
#Libreria incluida por defecto, se importa MIMEText para permitir la redacción del mensaje a enviar por correo electronico
from email.mime.text import MIMEText 
# from datetime import datetime, date, time, timezone
#Libreria datetime esta incluida por defecto, permite la correcta elaboración para foematos de fecha
import datetime 
#Libreria PIL esta incluida por defecto, importa el metodo Image con el fin de producir una imagen
from PIL import Image 

## TODO comments

#Función que da conexión a la base de datos mencionada (Vacunacion.db) creada con sqlite3 utilizando el parametro creado (con), por el metodo sqlite3.connect()
def sqlConnection(): 
    try:
        con = sqlite3.connect('./Vacunacion.db')
        return con
    except Error:
        print(Error)

#Esta función creara las tablas mencionadas si estas no se encuentran dentro de la base de datos con el metodo .execute que permite la manipulación de la imformación de la base de datos
def crearTablas(): 
    con = sqlConnection()
    #Se crea metodo .cursor() para traer y ejecutar declaraciónes
    cursorObj = con.cursor()  
    # cursorObj.execute('''DROP TABLE pacientes''')
    cursorObj.execute('''
                CREATE TABLE if not exists "pacientes" (
                    "noId"	NUMERIC(12),
                    "nombre"	CHAR(20),
                    "apellido"	CHAR(20),
                    "direccion"	CHAR(20),
                    "telefono"	NUMERIC(12),
                    "correo"	CHAR(20),
                    "ciudad"	CHAR(20),
                    "fechaNacimiento"	DATE,
                    "fechaAfiliacion"	CHAR(10),
                    "vacunado"	CHAR(20),
                    "fechaDesafiliacion"	CHAR(10),
                    PRIMARY KEY("noId")
                );
                ''')
    # cursorObj.execute('''DROP TABLE lote_vacunas''')
    cursorObj.execute('''
                CREATE TABLE if not exists "lote_vacunas" (
                    "noLote"	NUMERIC(12),
                    "fabricante"	CHAR(12),
                    "tipoVacuna"	CHAR(21),
                    "cantidadRecibida"	NUMERIC(6),
                    "cantidadAsignada"	NUMERIC(6),
                    "cantidadUsada"	NUMERIC(6),
                    "dosisNecesaria"	NUMERIC(1),
                    "temperatura"	NUMERIC(2,1),
                    "efectividad"	NUMERIC(2,1),
                    "tiempoProteccion"	NUMERIC(3),
                    "fechaVencimiento"	CHAR(10),
                    "imagen"	LARGEBLOB,
                    PRIMARY KEY("noLote")
                );
                ''')
    # cursorObj.execute('''DROP TABLE plan_vacunacion''')
    cursorObj.execute('''
                CREATE TABLE if not exists "plan_vacunacion" (
                    "idPlan"	NUMERIC(2),
                    "edadMinima"	NUMERIC(3),
                    "edadMaxima"	NUMERIC(3),
                    "fechaInicio"	DATE,
                    "fechaFinal"	DATE,
                    PRIMARY KEY("idPlan")
                );
                ''')
    # cursorObj.execute('''DROP TABLE programacion_vacunas''')
    cursorObj.execute('''
                CREATE TABLE if not exists "programacion_vacunas" (
                    idCita      INTEGER,
                    "noId"      NUMERIC(12),
                    "noLote"	NUMERIC(12),
                    "idPlan"    NUMERIC(12),
                    "ciudadVacunacion"	CHAR(20),
                    "fechaProgramada"	DATE,
                    "horaProgramada"	TIME,
                    FOREIGN KEY("noId") REFERENCES "pacientes"("noId"),
                    FOREIGN KEY("noLote") REFERENCES "lote_vacuna"("noLote"),
                    FOREIGN KEY("idPlan") REFERENCES "plan_vacunacion"("idPlan"),
                    PRIMARY KEY("idCita" AUTOINCREMENT)
                );
                ''')
    cursorObj.execute('''
                CREATE INDEX if not exists "ix_programacion_vacunas_noId" ON "programacion_vacunas" (
                    "noId"	ASC
                );
                ''')
    #Se usa el metodo .commit() para afirmar los cambios realizados dento de la base de datos
    con.commit() 
    #Se cierra la base de datos por el metodo .close()
    con.close()  

#Función para mostrar opciones relacionadas a la tabla (usuarios)
def menuModuloUno():
    while True:
        opcion = input('Ingrese el numero de la opcion que desea realizar:\n1. Crear nuevo afiliado\n2. Consultar afiliado\n3. Desafiliar usuario\n4. Atras\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): crearUsuario()
            if (opcion == 2): consultarUsuario()
            if (opcion == 3): desafiliarUsuario()
            if (opcion == 4): break
        else: continue

#Función para crear y almacenar una serie de datos dentro de la tabla usuarios
def crearUsuario():
    con = sqlConnection() 
    cursorObj = con.cursor()
    #se crea variable (documentoID) contenedora del numero de documento de identidad del usuario
    print('Ingrese a continuacion los datos de la persona que desea registrar:')
    documentoID = int(input('Documento de Identidad:\n')) 
    #se toma la variable (documentoID) como el indicador noId de la tabla pacientes por el metodo SELECT
    cursorObj.execute('SELECT * FROM pacientes WHERE noId = {}'.format(documentoID)) 
    # se usa el método fetchall() del objeto cursor para almacenar los valores en la variable (resultado).
    resultado = cursorObj.fetchall() 
    if len(resultado) == 0:
        #Se crean variables con los datos recividos del usuario
        nombre = input('Nombre:\n').title()  
        apellido = input('Apellido:\n').title() 
        direccion = input('Direccion:\n').title() 
        telefono = int(input('Telefono:\n')) 
        correo = input('Correo:\n') 
        ciudad = input('Ciudad:\n').title() 
        print('Fecha de nacimiento:')
        #se crean variables (diaNacimiento, mesNacimiento y añoNacimiento) que contienen los numero de dia, mes y fecha de nacimiento respectivamente con la cantidad de digitos marcada usando el metodo .ljust() 
        diaNacimiento = input("Dia: ") 
        diaNacimiento = diaNacimiento.ljust(2)
        mesNacimiento = input("Mes: ")
        mesNacimiento = mesNacimiento.ljust(2)
        añoNacimiento = input("Año: ")
        añoNacimiento = añoNacimiento.ljust(4)
        #Se juntan y almacenan los valores anteriores pertenecientes a la fecha de nacimiento del usuario en la variable (fechaNacimiento) con el metodo .format()
        fechaNacimiento = "{}-{}-{}".format(añoNacimiento,mesNacimiento,diaNacimiento) 
        print('Fecha de afiliacion:')
        #se crean variables (diaAfiliacion, mesAfiliacion y añoAfiliacion) pertenecientes a la fecha de afiliación del usuario
        diaAfiliacion = input("Dia: ") 
        diaAfiliacion = diaAfiliacion.ljust(2)
        mesAfiliacion = input("Mes: ")
        mesAfiliacion = mesAfiliacion.ljust(2)
        añoAfiliacion = input("Año: ")
        añoAfiliacion = añoAfiliacion.ljust(4)
        #Se juntan y almacenan los valores pertenecientes a la fecha de afiliación del usuario en la variable (fechaAfiliacion)
        fechaAfiliacion = "{}-{}-{}".format(añoAfiliacion,mesAfiliacion,diaAfiliacion) 
        #Se crea variable (vacunado) que identifica si el usuario esta vacunado o no, ("S" vacunado) o ("N" no vacunado)
        vacunado = input('¿Ha sido vacunado? (S/N):\n').title() 
        # Se almacenan los datos de usuario recogidos dentro de la tabla pacientes por el metodo INSERT INTO
        cursorObj.execute('INSERT INTO pacientes VALUES ({a},"{b}","{c}","{d}",{e},"{f}","{g}",date("{h}"),date("{i}"),"{j}", NULL)'.format(a=documentoID, b=nombre, c=apellido, d=direccion, e=telefono, f=correo, g=ciudad, h =fechaNacimiento, i=fechaAfiliacion, j=vacunado))
        con.commit()
    else:
        #Se mostrara el mensaje si la variable (resultado) es diferente de 0, en caso de que ya hubieran datos almacenados en la variable noId digitada por el usuario
        print('Este usuario ya existe\n') 
    
    con.close()

#Función para traer y mostrar datos de un paciente registrado 
def consultarUsuario(): 
    con = sqlConnection()
    cursorObj = con.cursor()
    #se pide el documento de identidad del paciente a buscar
    documentoID = int(input('Ingrese a continuacion el documento de identidad de la persona que desea consultar:\n')) 
    #se busca dentro de la tabla pacientes el valor (noId) que corresponda con la variable(documentoID)
    cursorObj.execute('SELECT * FROM pacientes WHERE noId = {}'.format(documentoID)) 
    #se asigna el resultado de la busqueda individual a la variable (resultado) con el metodo .fethcone
    resultado = cursorObj.fetchone() 
    print('\n')
    if resultado != None:
        cont = 0
        #Ciclo que recorre los valores almacenados en (resultado) nombrados como (datos) 
        for datos in resultado: 
            infoUsuario = ""
            if cont == 0: infoUsuario = "No. Identificación: "
            elif cont == 1: infoUsuario = "Nombre: "
            elif cont == 2: infoUsuario = "Apellido: "
            elif cont == 3: infoUsuario = "Dirección: "
            elif cont == 4: infoUsuario = "Telefono: "
            elif cont == 5: infoUsuario = "Correo: "
            elif cont == 6: infoUsuario = "Ciudad: "
            elif cont == 7: infoUsuario = "Fecha de nacimiento: "
            elif cont == 8: infoUsuario = "Fecha de afiliacion: "
            elif cont == 9: infoUsuario = "¿Vacunado?: "
            else: infoUsuario = "Fecha de desafiliación: "
            #Se da una cadena para (infoUsuario) y se imprime junto al dato correspondiente
            print(infoUsuario,datos)
            cont += 1
        print('\n')
    #Se mostrara el mensaje si la variable (resultado) esta vacia, en caso de que no hallan datos almacenados en la variable noId digitada por el usuario
    else: print('El paciente no se encuentra en los registros.\n') 
    #se cierra la table
    con.close()

# Función para desafiliar a un paciente registrado con anterioridad
def desafiliarUsuario(): 
    con = sqlConnection()
    cursorObj = con.cursor()
    # se pide el documento de idetidad del usuario a desafiliar
    documentoID = int(input('Ingrese a continuacion el documento de identidad de la persona que desea desafiliar:\n')) 
    #se busca dentro de la tabla pacientes el valor (noId) que corresponda con la variable(documentoID)
    cursorObj.execute('SELECT * FROM pacientes WHERE noId = {}'.format(documentoID)) 
    resultado = cursorObj.fetchall()
    #Si el usuario se encuentra registrado en la tabla pacientes se procede a crear una fecha de desafiliación
    if len(resultado) != 0: 
        print('Fecha de desafiliacion:')
        diaDesafiliacion = input("Dia: ")
        diaDesafiliacion = diaDesafiliacion.ljust(2)
        mesDesafiliacion = input("Mes: ")
        mesDesafiliacion = mesDesafiliacion.ljust(2)
        añoDesafiliacion = input("Año: ")
        añoDesafiliacion = añoDesafiliacion.ljust(4)
        fechaDesafiliacion = "{}-{}-{}".format(añoDesafiliacion,mesDesafiliacion,diaDesafiliacion)
        #se actualia la variable (fechaDesafiliacion) de la tabla paciente cuando noID = documentoID por el metodo .UPDATE
        cursorObj.execute('UPDATE pacientes SET fechaDesafiliacion = date("{}") WHERE noID = {}'.format(fechaDesafiliacion, documentoID))  
        #Se afirman los cambios realizados
        con.commit() 
    #Se mostrara el mensaje si la variable (resultado) es igual a 0, en caso de que no hallan datos almacenados en la variable noId digitada por el usuario
    else: print('El paciente no se encuentra en los registros.') 
    #Se cierra la tabla
    con.close()

#Función de menú para las opciones crearLote() y consultarLote()
def menuModuloDos(): 
    #se crea un ciclo que finaliza unicamente cuando el usuario elige la opcion (3. Atras)
    while True: 
        opcion = input('Ingrese el numero de la opcion que desea realizar:\n1. Crear nuevo lote de vacunas\n2. Consultar lote de vacunas\n3. Atras\n')
        if opcion != '': 
            opcion = int(opcion)
            #Trae la función (crearLote)
            if (opcion == 1): crearLote() 
            #Trae la función (consultarLote)
            if (opcion == 2): consultarLote() 
            if (opcion == 3): break
        #El programa dara otra vuelta en caso de que la variable (opcion) este vacia
        else: continue 

#Función para crear un nuevo lote dentro de la tabla lote_vacunas
def crearLote(): 
    con = sqlConnection() 
    cursorObj = con.cursor()
    print('Ingrese a continuacion los datos del lote que desea registrar:')
    #se asigna un numero identificador para el nuevo lote que se desea ingresar
    numeroLote = int(input('Numero del lote:\n')) 
    #el numero identificador se compara con los existentes en la tabla lote_vacuna
    cursorObj.execute('SELECT * FROM lote_vacunas WHERE noLote = {}'.format(numeroLote)) 
    #se obtienen los valores correspondientes con el numero identificador y se almacenan en la variable (resultado)
    resultado = cursorObj.fetchall() 
    if len(resultado) == 0:
        #Se ingresan datos respectivos al nuevo lote
        fabricante = input('Fabricante:\n').title()
        tipoVacuna = input('Tipo de vacuna:\n').title()
        cantidadRecibida = int(input('Cantidad de vacunas recibidas:\n'))
        cantidadAsignada = int(input('Cantidad de vacunas asignadas:\n'))
        cantidadUsada = int(input('Cantidad de vacunas usadas:\n'))
        dosisNecesaria = int(input('Dosis necesarias:\n'))
        temperatura = float(input('Temperatura de almacenamiento:\n'))
        efectividad = float(input('Efectividad de la vacuna:\n'))
        tiempoProteccion = int(input('Tiempo de proteccion (meses):\n'))
        print('Fecha de vencimiento:')
        diaVencimiento = input("Dia: ")
        diaVencimiento = diaVencimiento.ljust(2)
        mesVencimiento = input("Mes: ")
        mesVencimiento = mesVencimiento.ljust(2)
        añoVencimiento = input("Año: ")
        añoVencimiento = añoVencimiento.ljust(4)
        fechaVencimiento = "{}-{}-{}".format(añoVencimiento,mesVencimiento,diaVencimiento)
        # se da la opcion para ingresar una imagen del lote segun su ruta
        rutaImagen = input('Ruta completa a la imagen:\n')
        # se abre el archivo respectivo y se lee, almacenandose en la variable (imagenBinaria)
        with open(rutaImagen, "rb") as File:
            imagenBinaria = File.read()
        info = (numeroLote, fabricante, tipoVacuna, cantidadRecibida, cantidadAsignada, cantidadUsada, dosisNecesaria, temperatura, efectividad, tiempoProteccion, fechaVencimiento, imagenBinaria)
        #Se incertan los datos de (info) dentro de la tabla lote_vacunas por el metodo INSERT INTO, tenuendo en cuenta que el penultimo valor entra con un formato de fecha con el metodo date()
        cursorObj.execute('INSERT INTO lote_vacunas VALUES (?,?,?,?,?,?,?,?,?,?,date(?),?)', info) 
        con.commit()
    else:
        #se mostrara un mensaje si el numero identificador digitado ya existe dentro de la tabla lote_vacuna
        print('Este lote de vacunas ya existe\n')
    
    con.close()

# Función con la finalidad de consultar un lote de vacunas ingresado con anterioridad
def consultarLote(): 
    con = sqlConnection()
    cursorObj = con.cursor()
    # se toma (noLote) como variable de busqueda 
    noLote = int(input('Ingrese a continuacion numero de lote que desea consultar:\n'))
    cursorObj.execute('SELECT * FROM lote_vacunas WHERE noLote = {}'.format(noLote)) 
    # Se trae el valor individual de la tabla lote_vacunas que concuerda con (noLote)
    resultado = cursorObj.fetchone() 
    print('\n')
    if resultado != None:
        cont = 0
        #Se realiza un bucle que recorre los datos de la variable (resultado) si esta tiene un valor no nulo
        for datos in resultado[0:-1]:
            infoLote = ""
            if cont == 0: infoLote = "No. de Lote: "
            elif cont == 1: infoLote = "Fabricante: "
            elif cont == 2: infoLote = "Tipo de vacuna: "
            elif cont == 3: infoLote = "Cantidad de vacunas recibidas: "
            elif cont == 4: infoLote = "Cantidad de asignadas recibidas: "
            elif cont == 5: infoLote = "Cantidad de usadas recibidas: "
            elif cont == 6: infoLote = "Dosis necesarias: "
            elif cont == 7: infoLote = "Temperatura de almacenamiento: "
            elif cont == 8: infoLote = "Efectividad: "
            elif cont == 9: infoLote = "Tiempo de proteccion: "
            elif cont == 10: infoLote = "Fecha de vencimiento: "
            if datos != None:
                # Se imprime (infoLote) correspondiente a la descripción de la información junto con el valor correspondiente (datos)
                print(infoLote,datos) 
                cont += 1
        #se muestra una imagen recogiendo los datos de fabricante, imagemBinaria de la tabla lote_vacunas y la variable (cursorObj)
        mostrarImagen(cursorObj, resultado[1], resultado[11]) 
        print('\n')
    #Se mostrará un mensaje si el valor de (noLote) es nulo 
    else: print('El lote no se encuentra registrado.\n') 
    con.close()

# Función para visualizar una imagen, recoge (cursorObj) de la función .cursor(), (fabricante) y (imagenBinaria) información almacenada en la tabla lote_vacunas
def mostrarImagen(cursorObj, fabricante, imagenBinaria): 
    #Se crea un ciclo que solo se cierra cuando el usuario halla terminado de visualizar una imagen o hasta que la variable (opcion) sea 2
    while True:
        opcion = input('¿Desea abrir la imagen?:\n1. Si\n2. No\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): 
                #Se toma la información de la ruta en donde se encuentra la imagen
                rutaDeGuardado = 'imagenesDescargadas/{}.jpg'.format(fabricante) 
                with open(rutaDeGuardado, "wb") as File:
                    File.write(imagenBinaria)
                #Se abre la imagen abriendo su ruta almacenada en (rutaDeGuardado) con el metodo .open() y se visualiza con el metodo .show()
                imagen = Image.open(rutaDeGuardado)
                imagen.show() 
            break
            if (opcion == 2): 
                #Termina el bucle
                break 
            else: continue
        else: continue

#Función para mostrar un menú de opciones relacionados a los planes de vacunación
def menuModuloTres(): 
    #se crea un bucle que solo se detiene cuando la variable (opcion) sea igual a 3
    while True:
        opcion = input('Ingrese el numero de la opcion que desea realizar:\n1. Crear plan de vacunación\n2. Consultar plan de vacunación\n3. Atras\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): crearPlanVacunacion()
            if (opcion == 2): consultarPlanVacunacion()
            if (opcion == 3): break
        else: continue

#Función para crear un nuevo plan de vacunación
def crearPlanVacunacion(): 
    con = sqlConnection() 
    cursorObj = con.cursor()
    print('Ingrese a continuacion los datos del plan de vacunación que desea crear:')
    idPlan = int(input('Codigo del plan:\n'))
    #se selecciona un valor para (idPlan) y se busca dentro de la tabla plan_vacunacion
    cursorObj.execute('SELECT * FROM plan_vacunacion WHERE idPlan = {}'.format(idPlan)) 
    #se toman los valores de la tabla con un (idPlan) igual al ingresado
    resultado = cursorObj.fetchall() 
    if len(resultado) == 0:
        #Se toman del usuario los valores correspondientes
        edadMinima = int(input('Edad minima requerida:\n'))
        edadMaxima = int(input('Edad maxima requerida:\n'))
        print('Fecha de inicio:')
        diaInicio = input("Dia: ")
        diaInicio = diaInicio.ljust(2)
        mesInicio = input("Mes: ")
        mesInicio = mesInicio.ljust(2)
        añoInicio = input("Año: ")
        añoInicio = añoInicio.ljust(4)
        fechaInicio = "{}-{}-{}".format(añoInicio,mesInicio,diaInicio)
        print('Fecha de finalizacion:')
        diaFinal = input("Dia: ")
        diaFinal = diaFinal.ljust(2)
        mesFinal = input("Mes: ")
        mesFinal = mesFinal.ljust(2)
        añoFinal = input("Año: ")
        añoFinal = añoFinal.ljust(4)
        fechaFinal = "{}-{}-{}".format(añoFinal,mesFinal,diaFinal)
        #los valores tomados se insertan en la tabla plan_vacunacion por el metodo INSERT INTO
        cursorObj.execute('INSERT INTO plan_vacunacion VALUES ({a},{b},{c},date("{d}"),date("{e}"))'.format(a=idPlan, b=edadMinima, c=edadMaxima, d=fechaInicio, e=fechaFinal))
        con.commit()
    else:
        #Se mostrará un mensaje si el (idPlan) ingresado ya ha sido ingresado con anterioridad
        print('Este plan de vacunacion ya existe\n') 
    
    con.close()
    
#Función para ver los datos de un plan de vacunación ya existente en la tabla plan_vacunacion
def consultarPlanVacunacion(): 
    con = sqlConnection()
    cursorObj = con.cursor()
    idPlan = int(input('Ingrese a continuacion el codigo del plan de vacunacion que desea consultar:\n'))
    cursorObj.execute('SELECT * FROM plan_vacunacion WHERE idPlan = {}'.format(idPlan))
    resultado = cursorObj.fetchone() #se toma un valor correspondiente con el (idPlan) ingresado
    print('\n')
    #si el valor obtenido de (resultado) no es nulo, proseguira
    if resultado != None: 
        cont = 0
        #se genera un bucle que recorre los datos en (resultado) mientras se le asigna un nombre a la variable (infoLote) segun un contador (cont) que crece con cada vuelta
        for datos in resultado:
            infoLote = ""
            if cont == 0: infoLote = "Id. de Plan: "
            elif cont == 1: infoLote = "Edad minima: "
            elif cont == 2: infoLote = "Edad maxima: "
            elif cont == 3: infoLote = "Fecha de inicio: "
            elif cont == 4: infoLote = "Fecha de finalizacion: "
            if datos != None:
                # se imprimen los actuales valores de (infoLote): descripción de la información y (datos): el valor correspondiente 
                print(infoLote,datos)
                cont += 1
        print('\n')
    #se mostrara un mensaje si (resultado) es nulo
    else: print('El plan de vacunación no se encuentra registrado.\n') 
    #se cierra tabla
    con.close()

#Función que genera un menú para las opciones relacionadas a las programaciones de vacunación
def menuModuloCuatro(): 
    # Se genera un bucle que solo se detiene cunado (opcion) sea igual a 4
    while True:
        opcion = input('Ingrese el numero de la opcion que desea realizar:\n1. Crear la programacion de vacunas\n2. Consultar la programacion de vacunas\n3. Consultar vacunacion de un paciente\n4. Atras\n')
        if opcion != '': 
            opcion = int(opcion)
            # Si (opcion) es igual a 1, se inicia la función programacionDeVacunacion()
            if (opcion == 1): programacionDeVacunacion() 
            elif (opcion == 2): 
                # se inicia un bucle para obtener un dato de consulta según lo elija el usuario, este bucle solo se detendrá cuando (opcion) sea 11
                while True:
                    opcion = input('''Por que campo desea organizar la consulta:\n1. Numero de Identificacion\n2. Nombre\n3. Apellido\n4. Direccion\n5. Telefono\n6. Correo\n7. Fecha Programada\n8. Hora Programada\n9. Numero de lote\n10. Fabricante\n11. Salir de la consulta''')
                    if opcion != '': 
                        opcion = int(opcion)
                        #Se realiza una selección para organizar la consulta segun (opcion) digitada por el usuario
                        if (opcion ==1): datoConsulta = 'pc.noId'
                        elif (opcion ==2): datoConsulta = 'pc.nombre'
                        elif (opcion ==3): datoConsulta = 'pc.apellido'
                        elif (opcion ==4): datoConsulta = 'pc.direccion'
                        elif (opcion ==5): datoConsulta = 'pc.telefono'
                        elif (opcion ==6): datoConsulta = 'pc.correo'
                        elif (opcion ==7): datoConsulta = 'pgv.fechaProgramada'
                        elif (opcion ==8): datoConsulta = 'pgv.horaProgramada'
                        elif (opcion ==9): datoConsulta = 'lv.noLote'
                        elif (opcion ==10): datoConsulta = 'lv.fabricante'
                        else: break
                    else: continue
                    #Se llama a la función consultarProgramacionCompleta() con la entrada (datoConsulta)
                    consultarProgramacionCompleta(datoConsulta)
            # Si (opcion) es igual a 3, se inicia la función consultarProgramacionIndividual()
            elif (opcion == 3): consultarProgramacionIndividual() 
            # el programa deja el bucle por medio de la función break
            elif (opcion == 4): break 
        else: continue 

#Función para programar vacunación
def programacionDeVacunacion(): 
    con = sqlConnection() 
    cursorObj = con.cursor()
    # se actualiza la tabla lote_vacunas de manera que cantidadAsignada tenga el valor de cantidadUsada con el metodo UPDATE
    cursorObj.execute('UPDATE lote_vacunas SET cantidadAsignada = cantidadUsada') 
    #se remueve la tabla programacion_vacunas de la base de datos
    cursorObj.execute('DROP TABLE programacion_vacunas')
    con.commit() 
    #Se llama a la función programacionPacienteLote(con)
    programacionPacienteLote(con) 
    #Se llama a la función programacionFechaHora(con)
    programacionFechaHora(con) 

    con.close()

#función para programar vacunación de paciente según el lote, recive la la funcion con
def programacionPacienteLote(con): 
    cursorObj = con.cursor()
    crearTablas()
    # se toman los datos almacenados de la tabla plan_vacunacion 
    cursorObj.execute('SELECT * FROM plan_vacunacion') 
    planVacunacion = cursorObj.fetchall()
    # se crea un bucle que recorre los datos en (planVacunacion)
    for plan in planVacunacion:
        # Se toman datos de la tabla paciente según un rango de edad tomado de los valores de (planVacunacion)
        cursorObj.execute('SELECT noId, ciudad, CAST((julianday("now") - julianday(fechaNacimiento))/365.25 as INTEGER) as Edad FROM pacientes WHERE (Edad >= {}) AND (Edad <= {}) AND vacunado = "N" AND fechaDesafiliacion is Null'.format(plan[1], plan[2])) 
        pacientesAVacunar = cursorObj.fetchall()
        #Se hace un bucle que recorre los valores de (pacientesAVacunar)
        for paciente in pacientesAVacunar:
            #Se toman los valores de cantidadAsignada y cantidadRecibida de la tabla lote_vacunas y se busca un valor en donde cantidadAsignada < cantidadRecibida
            cursorObj.execute('SELECT noLote FROM lote_vacunas WHERE cantidadAsignada<cantidadRecibida')
            vacunaAAaplicar = cursorObj.fetchone()
            #En caso de que no se encuentre un valor tal que cantidadAsignada < cantidadRecibida, vacunaAAaplicar estara vacio
            if vacunaAAaplicar == None:
                print('Limite de vacunas alcanzado')
                return
            datos = (paciente[1], paciente[0], vacunaAAaplicar[0], plan[0])
            cursorObj.execute('INSERT INTO programacion_vacunas (ciudadVacunacion, noId, noLote, idPlan) VALUES (?,?,?,?)', datos)
            cursorObj.execute('UPDATE lote_vacunas SET cantidadAsignada = cantidadAsignada+1 WHERE noLote = {}'.format(vacunaAAaplicar[0]))
            con.commit()

#Función para programar una fecha y hora de vacunación
def programacionFechaHora(con): 
    cursorObj = con.cursor()
    #se crean variables str para acomodar la hora (horaInicio) y (horaFin)
    horaInicio = "08:00:00"
    horaFin = "17:00:00"
    #se seleccionan variables de la tabla programacion_vacunas y se unen los valores que coincidan con (fechaProgramada) estando vacia, con el metodo INNER JOIN
    cursorObj.execute('''SELECT pgv.*, plv.fechaInicio, pc.correo, lv.fabricante FROM programacion_vacunas pgv 
                        INNER JOIN plan_vacunacion plv ON (plv.idPlan = pgv.idPlan) 
                        INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                        INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote) 
                        WHERE fechaProgramada IS NULL''')
    citaAProgramar = cursorObj.fetchall()
    #Se genera bucle que recorre los valores en (citaAProgramar)
    for cita in citaAProgramar:
        #Se toman los valores de (horaProgramada) y (fechaProgramada) que sean mayores usando max()
        cursorObj.execute('SELECT fechaProgramada, max(horaProgramada) FROM programacion_vacunas WHERE fechaProgramada = (SELECT max(fechaProgramada) FROM programacion_vacunas)')
        ultimaCitaProgramada =  cursorObj.fetchone()
        # print(ultimaCitaProgramada)
        #En caso de iniciarse la programación de vacunación, se empezará con la hora inicial (horaInicio)
        if ultimaCitaProgramada[0] == None:
            fechaCita = cita[7]
            horaCita = horaInicio
        #se toma la ultima hora registrada y se le suma 1
        else:
            fechaMaxima = ultimaCitaProgramada[0]
            horaMaxima = ultimaCitaProgramada[1]
            hora = int(horaMaxima[0:2])
            hora += 1
            #se da la fecha y hora almacenandola en dt con el metodo datetime.datetime.strptime()
            if hora >= int(horaFin[0:2]): 
                horaCita = horaInicio
                dt = datetime.datetime.strptime(fechaCita, "%Y-%m-%d")
                fechaCitaDt = dt + datetime.timedelta(days=1)
                fechaCita = fechaCitaDt.strftime("%Y-%m-%d")
            #Se agrega la hora conseguida a (horaCita)
            else:
                horaCita = '{}:00:00'.format(hora)
                if hora < 10:
                    horaCita = '0{}:00:00'.format(hora)
                #Se iguala la fecha de la cita obtenida (fechaCita) como la fecha maxima que se tiene (fechaMaxima)
                fechaCita = fechaMaxima

            fechaCitaDt = datetime.datetime.strptime(fechaCita, "%Y-%m-%d")
            fechaInicioDt = datetime.datetime.strptime(cita[7], "%Y-%m-%d")
            # en caso de que el valor de (fechaCitaDt) sea menor a (fechaInicioDt), se le asigna el valor de (horaInicio) a (horaCita)
            if fechaCitaDt < fechaInicioDt:
                fechaCita = fechaInicioDt.strftime("%Y-%m-%d")
                horaCita = horaInicio
        cursorObj.execute('update programacion_vacunas set fechaProgramada = ?, horaProgramada = ? where idCita = ?', (fechaCita, horaCita, cita[0]))
        con.commit()
        # enviarCorreo(cita[8], fechaCita, horaCita, cita[9])
    print('Programacion de citas de vacunacion exitosa')

#Función para enviar un correo electronico prediseñado, toma las variables (destinatario), (dia), (hora), (vacuna)
def enviarCorreo(destinatario, dia, hora, vacuna): 
    #se crea el mensaje electronico con todos sus componentes como (mensajeObj) con la función MIMEMultipart() del respositorio email.mime.multipart
    mensajeObj = MIMEMultipart()
    #se crea la variable que contendrá el mensaje (mensaje)
    mensaje = '''Cordial saludo.
    Le notificamos que su cita de vacunacion esta programada para el dia {} a las {}. Le sera aplicada la vacuna {}.'''

    #se crean variables de remitente, destinatario, asunto y contraseña se correo emisor
    mensajeObj['From'] = 'pruebas.vacunacion@gmail.com'
    mensajeObj['To'] = destinatario
    mensajeObj['Subject'] = 'Email de prueba'
    password = 'TEST_123*'
    #se adjuntan valores al mensaje con el metodo .attach()
    mensajeObj.attach(MIMEText(mensaje.format(dia, hora, vacuna), 'plain'))

    #Por medio del metodo smtplib.SMTP() se inicia una sesión para enviar el mensaje electronico 
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        #se activa el metodo almacenado en (server) con el metodo .starttls()
        server.starttls()
        #Se da inicio de sesión con el metodo server.login()
        server.login(mensajeObj['From'], password)
        #Se adjunta y envia el correo con el metodo server.sendmail()
        server.sendmail(mensajeObj['From'], mensajeObj['To'], mensajeObj.as_string())
        print('correo enviado')
        #Se realiza el cierre de la conexión con el metodo .quit()
        server.quit()
    #se imprimira "error" si ha ocurrido una excepción
    except:
        print('error')

#Función para hacer una programación de vacunación a todos los usuarios de un plan de vacunación 
def consultarProgramacionCompleta(datoConsulta): 
    con = sqlConnection()
    cursorObj = con.cursor()
    #se seleccionan variables de la tabla programacion_vacunas y se unen los valores que coincidan con el metodo INNER JOIN
    cursorObj.execute('''SELECT pgv.idCita, pc.noId, pc.nombre, pc.apellido, pc.direccion, pc.telefono, pc.correo, pgv.fechaProgramada, pgv.horaProgramada, lv.noLote, lv.fabricante  FROM programacion_vacunas pgv 
                        INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                        INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote)
                        ORDER BY {} ASC'''.format(datoConsulta))
    citasProgramadas = cursorObj.fetchall()
    for cita in citasProgramadas:
        cont = 0
        #Se crea un bucle que recorre los datos en (resultado)
        for dato in cita:
            infoCita = ""
            #la variable (infoCita) toma un contenido str que corresponde a la descripción de la información 
            if cont == 1: infoCita = "No. Identificación: "
            elif cont == 2: infoCita = "Nombre: "
            elif cont == 3: infoCita = "Apellido: "
            elif cont == 4: infoCita = "Dirección: "
            elif cont == 5: infoCita = "Telefono: "
            elif cont == 6: infoCita = "Correo: "
            elif cont == 7: infoCita = "Fecha programada: "
            elif cont == 8: infoCita = "Hora programada: "
            elif cont == 9: infoCita = "Numero de lote de vacuna: "
            else: infoCita = "Fabricante de la vacuna: "
            if dato != None and dato != 0:
                # se imprime (infoCita) juanto al valor al que corresponde (datos)
                print(infoCita,dato)
                cont += 1
        print('\n')

#Función para programar la vacunación de un usuario individual
def consultarProgramacionIndividual(): 
    con = sqlConnection()
    cursorObj = con.cursor()
    documentoID = int(input('Ingrese a continuacion el documento de identidad de la persona cuya cita desea consultar:\n'))
    #se seleccionan variables de la tabla programacion_vacunas y se unen los valores que coincidan con el metodo INNER JOIN
    cursorObj.execute('''SELECT pc.noId, pc.nombre, pc.apellido, pc.direccion, pc.telefono, pc.correo, pgv.fechaProgramada, pgv.horaProgramada, lv.noLote, lv.fabricante  FROM programacion_vacunas pgv 
                        INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                        INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote)
                        WHERE pgv.noId = {}'''.format(documentoID))
    resultado = cursorObj.fetchone()
    print('\n')
    if resultado != None:
        cont = 0
        #Se crea un bucle que recorre los datos en (resultado)
        for datos in resultado:
            infoCita = ""
            #la variable (infoCita) toma un contenido str que corresponde a la descripción de la información 
            if cont == 0: infoCita = "No. Identificación: "
            elif cont == 1: infoCita = "Nombre: "
            elif cont == 2: infoCita = "Apellido: "
            elif cont == 3: infoCita = "Dirección: "
            elif cont == 4: infoCita = "Telefono: "
            elif cont == 5: infoCita = "Correo: "
            elif cont == 6: infoCita = "Fecha programada: "
            elif cont == 7: infoCita = "Hora programada: "
            elif cont == 8: infoCita = "Numero de lote de vacuna: "
            else: infoCita = "Fabricante de la vacuna: "
            if datos != None:
                # se imprime (infoCita) juanto al valor al que corresponde (datos)
                print(infoCita,datos)
                cont += 1
        print('\n')
    #se muestra mensaje si (resultado) esta vacio
    else: print('El paciente no tiene cita.\n')

    con.close()
    

    con.close()

#Función para generar un menú de opciones para confirmar la vacunación de un paciente
def menuModuloCinco(): 
    while True:
        opcion = input('Desea vacunar pacientes?:\n1. Si\n2. No\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): vacunacionPacientes()
            if (opcion == 2): break
        else: continue

#Función para cambiar estado de vacunación de un usuario si cumple con los requisitos
def vacunacionPacientes(): 
    con = sqlConnection()
    cursorObj = con.cursor()
    # se pide y compara un numero de busqueda (documentoID) para saber sus datos
    documentoID = int(input('Ingrese a continuacion el documento de identidad de la persona que desea vacunar:\n'))
    cursorObj.execute('SELECT fechaDesafiliacion, vacunado FROM pacientes WHERE noId = {}'.format(documentoID))
    #Se toma (afiliado) de la tabla pacientes
    afiliado = cursorObj.fetchone()
    print('\n')
    if afiliado != None:
        #si (afiliado) no esta vacio, se compara su casilla de desafiliado
        if afiliado[0] != None:
            print('Este paciente se encuentra desafiliado')
        #se compara la casilla vacunado de (afiliado) con "S" de otra manera almacenaria a "N"
        elif afiliado[1] == 'S':
            print('Este paciente ya se encuentra vacunado')
        else:
            #Se obtiene el valor de (cita) con la tabla programacion_vacunas donde corresponda con (documentoID) usando el metodo INNER JOIN en la tabla pacientes
            cursorObj.execute('''SELECT pc.fechaDesafiliacion , pc.vacunado FROM programacion_vacunas pgv 
                            INNER JOIN pacientes pc ON (pc.noid = pgv.noid)
                            WHERE pc.noId = {}'''.format(documentoID))
            cita = cursorObj.fetchone()
            if cita != None: 
                #se pide confirmación de vacunación al usuario si (cita) no esta vacio
                vacunado = input('¿Desea vacunar a esta persona? (S/N):\n').title()
                if vacunado == 'S':
                    #se actualiza el estado de vacunación del paciente y se suma 1 a (cantidadUsada) de la tabla lote_vacunas con el metodo UPDATE
                    cursorObj.execute('UPDATE pacientes SET vacunado = "{}" WHERE noId = {}'.format(vacunado, documentoID))
                    cursorObj.execute('UPDATE lote_vacunas SET cantidadUsada = cantidadUsada + 1 WHERE noLote = (SELECT noLote FROM programacion_vacunas WHERE noId = {})'.format(documentoID))
                    con.commit()
            #se mostrará un mensaje si el valor (cita) esta vacio
            else: print('El paciente no tiene cita programada.\n')
    #se mostrará un mensaje si (afiliado) esta vacio
    else: print('El paciente no se encuentra en los registros.\n')

    con.close()

# Función para generar un menú principal con las opciones de las funcionalidades del programa
def menuPrincipal(): 
    #Se crea ciclo que solo termina cuando (opcion) sea igual a 6
    while True:
        opcion = input('Seleccione el modulo al que desea ingresar:\n1. Afiliados\n2. Lotes\n3. Planes de vacunacion\n4. Programacion de vacunacion\n5. Vacunar\n6. Salir\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): menuModuloUno()
            if (opcion == 2): menuModuloDos()
            if (opcion == 3): menuModuloTres()
            if (opcion == 4): menuModuloCuatro()
            if (opcion == 5): menuModuloCinco()
            if (opcion == 6): break
            if (opcion == 231): reinciarValores()
        else: continue
        
# Función principal del programa, inicia las funciones basicas
def main(): 
    crearTablas()
    menuPrincipal()
    
# Función para reiniciar valores de los pacientes y usos o asignaciones de vacunas
def reinciarValores(): 
    con = sqlConnection()
    cursorObj = con.cursor()
    # Se cambian los datos de la tabla paciente: vacunados a "N" y fechaDesafiliacion a NULL
    cursorObj.execute('UPDATE pacientes SET vacunado = "N", fechaDesafiliacion= NULL')
    # Se cambian los datos de la tabla lote_vacunas: cantidadUsada a 0 y cantidadAsignada a 0
    cursorObj.execute('UPDATE lote_vacunas SET cantidadUsada = 0, cantidadAsignada = 0')
    con.commit()

    con.close()

#Se llama a la función principal del programa    
main()
