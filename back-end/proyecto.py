import sqlite3
from sqlite3 import Error
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from datetime import datetime, date, time, timezone
import datetime
from PIL import Image

## TODO comments

def sqlConnection():
    try:
        con = sqlite3.connect('./Vacunacion.db')
        return con
    except Error:
        print(Error)

def crearTablas():
    con = sqlConnection()
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
    con.commit()
    con.close()

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

def crearUsuario():
    con = sqlConnection() 
    cursorObj = con.cursor()
    print('Ingrese a continuacion los datos de la persona que desea registrar:')
    documentoID = int(input('Documento de Identidad:\n'))
    cursorObj.execute('SELECT * FROM pacientes WHERE noId = {}'.format(documentoID))
    resultado = cursorObj.fetchall()
    if len(resultado) == 0:
        nombre = input('Nombre:\n').title()
        apellido = input('Apellido:\n').title()
        direccion = input('Direccion:\n').title()
        telefono = int(input('Telefono:\n'))
        correo = input('Correo:\n')
        ciudad = input('Ciudad:\n').title()
        print('Fecha de nacimiento:')
        diaNacimiento = input("Dia: ")
        diaNacimiento = diaNacimiento.ljust(2)
        mesNacimiento = input("Mes: ")
        mesNacimiento = mesNacimiento.ljust(2)
        añoNacimiento = input("Año: ")
        añoNacimiento = añoNacimiento.ljust(4)
        fechaNacimiento = "{}-{}-{}".format(añoNacimiento,mesNacimiento,diaNacimiento)
        print('Fecha de afiliacion:')
        diaAfiliacion = input("Dia: ")
        diaAfiliacion = diaAfiliacion.ljust(2)
        mesAfiliacion = input("Mes: ")
        mesAfiliacion = mesAfiliacion.ljust(2)
        añoAfiliacion = input("Año: ")
        añoAfiliacion = añoAfiliacion.ljust(4)
        fechaAfiliacion = "{}-{}-{}".format(añoAfiliacion,mesAfiliacion,diaAfiliacion)
        vacunado = input('¿Ha sido vacunado? (S/N):\n').title()
        cursorObj.execute('INSERT INTO pacientes VALUES ({a},"{b}","{c}","{d}",{e},"{f}","{g}",date("{h}"),date("{i}"),"{j}", NULL)'.format(a=documentoID, b=nombre, c=apellido, d=direccion, e=telefono, f=correo, g=ciudad, h =fechaNacimiento, i=fechaAfiliacion, j=vacunado))
        con.commit()
    else:
        print('Este usuario ya existe\n')
    
    con.close()

def consultarUsuario():
    con = sqlConnection()
    cursorObj = con.cursor()
    documentoID = int(input('Ingrese a continuacion el documento de identidad de la persona que desea consultar:\n'))
    cursorObj.execute('SELECT * FROM pacientes WHERE noId = {}'.format(documentoID))
    resultado = cursorObj.fetchone()
    print('\n')
    if resultado != None:
        cont = 0
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
            if datos != None:
                print(infoUsuario,datos)
                cont += 1
        print('\n')
    else: print('El paciente no se encuentra en los registros.\n')

    con.close()

def desafiliarUsuario():
    con = sqlConnection()
    cursorObj = con.cursor()
    documentoID = int(input('Ingrese a continuacion el documento de identidad de la persona que desea desafiliar:\n'))
    cursorObj.execute('SELECT * FROM pacientes WHERE noId = {}'.format(documentoID))
    resultado = cursorObj.fetchall()
    if len(resultado) != 0:
        print('Fecha de desafiliacion:')
        diaDesafiliacion = input("Dia: ")
        diaDesafiliacion = diaDesafiliacion.ljust(2)
        mesDesafiliacion = input("Mes: ")
        mesDesafiliacion = mesDesafiliacion.ljust(2)
        añoDesafiliacion = input("Año: ")
        añoDesafiliacion = añoDesafiliacion.ljust(4)
        fechaDesafiliacion = "{}-{}-{}".format(añoDesafiliacion,mesDesafiliacion,diaDesafiliacion)
        cursorObj.execute('UPDATE pacientes SET fechaDesafiliacion = date("{}") WHERE noID = {}'.format(fechaDesafiliacion, documentoID))
        con.commit()
    else: print('El paciente no se encuentra en los registros.')

    con.close()

def menuModuloDos():
    while True:
        opcion = input('Ingrese el numero de la opcion que desea realizar:\n1. Crear nuevo lote de vacunas\n2. Consultar lote de vacunas\n3. Atras\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): crearLote()
            if (opcion == 2): consultarLote()
            if (opcion == 3): break
        else: continue

def crearLote():
    con = sqlConnection() 
    cursorObj = con.cursor()
    print('Ingrese a continuacion los datos del lote que desea registrar:')
    numeroLote = int(input('Numero del lote:\n'))
    cursorObj.execute('SELECT * FROM lote_vacunas WHERE noLote = {}'.format(numeroLote))
    resultado = cursorObj.fetchall()
    if len(resultado) == 0:
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
        rutaImagen = input('Ruta completa a la imagen:\n')
        with open(rutaImagen, "rb") as File:
            imagenBinaria = File.read()
        info = (numeroLote, fabricante, tipoVacuna, cantidadRecibida, cantidadAsignada, cantidadUsada, dosisNecesaria, temperatura, efectividad, tiempoProteccion, fechaVencimiento, imagenBinaria)
        cursorObj.execute('INSERT INTO lote_vacunas VALUES (?,?,?,?,?,?,?,?,?,?,date(?),?)', info)
        con.commit()
    else:
        print('Este lote de vacunas ya existe\n')
    
    con.close()

def consultarLote():
    con = sqlConnection()
    cursorObj = con.cursor()
    noLote = int(input('Ingrese a continuacion numero de lote que desea consultar:\n'))
    cursorObj.execute('SELECT * FROM lote_vacunas WHERE noLote = {}'.format(noLote))
    resultado = cursorObj.fetchone()
    print('\n')
    if resultado != None:
        cont = 0
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
                print(infoLote,datos)
                cont += 1
        mostrarImagen(cursorObj, resultado[1], resultado[11])
        print('\n')
    else: print('El lote no se encuentra registrado.\n')

    con.close()

def mostrarImagen(cursorObj, fabricante, imagenBinaria):
    while True:
        opcion = input('¿Desea abrir la imagen?:\n1. Si\n2. No\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): 
                rutaDeGuardado = '/home/alpha23/Downloads/{}.jpg'.format(fabricante)
                with open(rutaDeGuardado, "wb") as File:
                    File.write(imagenBinaria)
                imagen = Image.open(rutaDeGuardado)
                imagen.show()
            break
        else: continue

def menuModuloTres():
    while True:
        opcion = input('Ingrese el numero de la opcion que desea realizar:\n1. Crear plan de vacunación\n2. Consultar plan de vacunación\n3. Atras\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): crearPlanVacunacion()
            if (opcion == 2): consultarPlanVacunacion()
            if (opcion == 3): break
        else: continue

def crearPlanVacunacion():
    con = sqlConnection() 
    cursorObj = con.cursor()
    print('Ingrese a continuacion los datos del plan de vacunación que desea crear:')
    idPlan = int(input('Codigo del plan:\n'))
    cursorObj.execute('SELECT * FROM plan_vacunacion WHERE idPlan = {}'.format(idPlan))
    resultado = cursorObj.fetchall()
    if len(resultado) == 0:
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
        cursorObj.execute('INSERT INTO plan_vacunacion VALUES ({a},{b},{c},date("{d}"),date("{e}"))'.format(a=idPlan, b=edadMinima, c=edadMaxima, d=fechaInicio, e=fechaFinal))
        con.commit()
    else:
        print('Este plan de vacunacion ya existe\n')
    
    con.close()

def consultarPlanVacunacion():
    con = sqlConnection()
    cursorObj = con.cursor()
    idPlan = int(input('Ingrese a continuacion el codigo del plan de vacunacion que desea consultar:\n'))
    cursorObj.execute('SELECT * FROM plan_vacunacion WHERE idPlan = {}'.format(idPlan))
    resultado = cursorObj.fetchone()
    print('\n')
    if resultado != None:
        cont = 0
        for datos in resultado:
            infoLote = ""
            if cont == 0: infoLote = "Id. de Plan: "
            elif cont == 1: infoLote = "Edad minima: "
            elif cont == 2: infoLote = "Edad maxima: "
            elif cont == 3: infoLote = "Fecha de inicio: "
            elif cont == 4: infoLote = "Fecha de finalizacion: "
            if datos != None:
                print(infoLote,datos)
                cont += 1
        print('\n')
    else: print('El plan de vacunación no se encuentra registrado.\n')

    con.close()

def menuModuloCuatro():
    while True:
        opcion = input('Ingrese el numero de la opcion que desea realizar:\n1. Crear la programacion de vacunas\n2. Consultar la programacion de vacunas\n3. Consultar vacunacion de un paciente\n4. Atras\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): programacionDeVacunacion()
            if (opcion == 2): 
                while True:
                    opcion = input('''Por que campo desea organizar la consulta:\n1. Numero de Identificacion\n2. Nombre\n3. Apellido\n4. Direccion\n5. Telefono\n6. Correo\n7. Fecha Programada\n8. Hora Programada\n9. Numero de lote\n10. Fabricante\n11. Salir de la consulta''')
                    if opcion != '': 
                        opcion = int(opcion)
                        if (opcion ==1): datoConsulta = 'pc.noId'
                        if (opcion ==2): datoConsulta = 'pc.nombre'
                        if (opcion ==3): datoConsulta = 'pc.apellido'
                        if (opcion ==4): datoConsulta = 'pc.direccion'
                        if (opcion ==5): datoConsulta = 'pc.telefono'
                        if (opcion ==6): datoConsulta = 'pc.correo'
                        if (opcion ==7): datoConsulta = 'pgv.fechaProgramada'
                        if (opcion ==8): datoConsulta = 'pgv.horaProgramada'
                        if (opcion ==9): datoConsulta = 'lv.noLote'
                        if (opcion ==10): datoConsulta = 'lv.fabricante'
                        if (opcion ==11): break
                    else: continue
                    consultarProgramacionCompleta(datoConsulta)
            if (opcion == 3): consultarProgramacionIndividual()
            if (opcion == 4): break
        else: continue

def programacionDeVacunacion():
    con = sqlConnection() 
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE lote_vacunas SET cantidadAsignada = cantidadUsada')
    cursorObj.execute('DROP TABLE programacion_vacunas')
    con.commit()
    programacionPacienteLote(con)
    programacionFechaHora(con)

    con.close()

def programacionPacienteLote(con):
    cursorObj = con.cursor()
    crearTablas()
    cursorObj.execute('SELECT * FROM plan_vacunacion')
    planVacunacion = cursorObj.fetchall()
    for plan in planVacunacion:
        # print(plan)
        cursorObj.execute('SELECT noId, ciudad, CAST((julianday("now") - julianday(fechaNacimiento))/365.25 as INTEGER) as Edad FROM pacientes WHERE (Edad >= {}) AND (Edad <= {}) AND vacunado = "N" AND fechaDesafiliacion is Null'.format(plan[1], plan[2])) 
        pacientesAVacunar = cursorObj.fetchall()
        for paciente in pacientesAVacunar:
            # print(paciente)
            cursorObj.execute('SELECT noLote FROM lote_vacunas WHERE cantidadAsignada<cantidadRecibida')
            vacunaAAaplicar = cursorObj.fetchone()
            if vacunaAAaplicar == None:
                print('Limite de vacunas alcanzado')
                return
            datos = (paciente[1], paciente[0], vacunaAAaplicar[0], plan[0])
            cursorObj.execute('INSERT INTO programacion_vacunas (ciudadVacunacion, noId, noLote, idPlan) VALUES (?,?,?,?)', datos)
            cursorObj.execute('UPDATE lote_vacunas SET cantidadAsignada = cantidadAsignada+1 WHERE noLote = {}'.format(vacunaAAaplicar[0]))
            con.commit()

def programacionFechaHora(con):
    cursorObj = con.cursor()
    horaInicio = "08:00:00"
    horaFin = "17:00:00"
    cursorObj.execute('''SELECT pgv.*, plv.fechaInicio, pc.correo, lv.fabricante FROM programacion_vacunas pgv 
                        INNER JOIN plan_vacunacion plv ON (plv.idPlan = pgv.idPlan) 
                        INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                        INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote) 
                        WHERE fechaProgramada IS NULL''')
    citaAProgramar = cursorObj.fetchall()
    for cita in citaAProgramar:
        cursorObj.execute('SELECT fechaProgramada, max(horaProgramada) FROM programacion_vacunas WHERE fechaProgramada = (SELECT max(fechaProgramada) FROM programacion_vacunas)')
        ultimaCitaProgramada =  cursorObj.fetchone()
        # print(ultimaCitaProgramada)
        if ultimaCitaProgramada[0] == None:
            fechaCita = cita[7]
            horaCita = horaInicio
        else:
            fechaMaxima = ultimaCitaProgramada[0]
            horaMaxima = ultimaCitaProgramada[1]
            hora = int(horaMaxima[0:2])
            hora += 1
            if hora >= int(horaFin[0:2]): 
                horaCita = horaInicio
                dt = datetime.datetime.strptime(fechaCita, "%Y-%m-%d")
                fechaCitaDt = dt + datetime.timedelta(days=1)
                fechaCita = fechaCitaDt.strftime("%Y-%m-%d")
            else:
                horaCita = '{}:00:00'.format(hora)
                if hora < 10:
                    horaCita = '0{}:00:00'.format(hora)
                fechaCita = fechaMaxima

            fechaCitaDt = datetime.datetime.strptime(fechaCita, "%Y-%m-%d")
            fechaInicioDt = datetime.datetime.strptime(cita[7], "%Y-%m-%d")
            if fechaCitaDt < fechaInicioDt:
                fechaCita = fechaInicioDt.strftime("%Y-%m-%d")
                horaCita = horaInicio
        cursorObj.execute('update programacion_vacunas set fechaProgramada = ?, horaProgramada = ? where idCita = ?', (fechaCita, horaCita, cita[0]))
        con.commit()
        # enviarCorreo(cita[8], fechaCita, horaCita, cita[9])
    print('Programacion de citas de vacunacion exitosa')

def enviarCorreo(destinatario, dia, hora, vacuna):
    mensajeObj = MIMEMultipart()
    mensaje = '''Cordial saludo.
    Le notificamos que su cita de vacunacion esta programada para el dia {} a las {}. Le sera aplicada la vacuna {}.'''

    mensajeObj['From'] = 'pruebas.vacunacion@gmail.com'
    mensajeObj['To'] = destinatario
    mensajeObj['Subject'] = 'Email de prueba'
    password = 'TEST_123*'
    mensajeObj.attach(MIMEText(mensaje.format(dia, hora, vacuna), 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(mensajeObj['From'], password)
        server.sendmail(mensajeObj['From'], mensajeObj['To'], mensajeObj.as_string())
        print('correo enviado')
        server.quit()
    except:
        print('error')

def consultarProgramacionCompleta(datoConsulta):
    con = sqlConnection()
    cursorObj = con.cursor()
    cursorObj.execute('''SELECT pgv.idCita, pc.noId, pc.nombre, pc.apellido, pc.direccion, pc.telefono, pc.correo, pgv.fechaProgramada, pgv.horaProgramada, lv.noLote, lv.fabricante  FROM programacion_vacunas pgv 
                        INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                        INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote)
                        ORDER BY {} ASC'''.format(datoConsulta))
    citasProgramadas = cursorObj.fetchall()
    for cita in citasProgramadas:
        cont = 0
        for dato in cita:
            infoCita = ""
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
                print(infoCita,dato)
                cont += 1
        print('\n')

def consultarProgramacionIndividual():
    con = sqlConnection()
    cursorObj = con.cursor()
    documentoID = int(input('Ingrese a continuacion el documento de identidad de la persona cuya cita desea consultar:\n'))
    cursorObj.execute('''SELECT pc.noId, pc.nombre, pc.apellido, pc.direccion, pc.telefono, pc.correo, pgv.fechaProgramada, pgv.horaProgramada, lv.noLote, lv.fabricante  FROM programacion_vacunas pgv 
                        INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                        INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote)
                        WHERE pgv.noId = {}'''.format(documentoID))
    resultado = cursorObj.fetchone()
    print('\n')
    if resultado != None:
        cont = 0
        for datos in resultado:
            infoCita = ""
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
                print(infoCita,datos)
                cont += 1
        print('\n')
    else: print('El paciente no tiene cita.\n')

    con.close()
    

    con.close()

def menuModuloCinco():
    while True:
        opcion = input('Desea vacunar pacientes?:\n1. Si\n2. No\n')
        if opcion != '': 
            opcion = int(opcion)
            if (opcion == 1): vacunacionPacientes()
            if (opcion == 2): break
        else: continue

def vacunacionPacientes():
    con = sqlConnection()
    cursorObj = con.cursor()
    documentoID = int(input('Ingrese a continuacion el documento de identidad de la persona que desea vacunar:\n'))
    cursorObj.execute('SELECT fechaDesafiliacion, vacunado FROM pacientes WHERE noId = {}'.format(documentoID))
    afiliado = cursorObj.fetchone()
    print('\n')
    if afiliado != None:
        if afiliado[0] != None:
            print('Este paciente se encuentra desafiliado')
        elif afiliado[1] == 'S':
            print('Este paciente ya se encuentra vacunado')
        else:
            cursorObj.execute('''SELECT pc.fechaDesafiliacion , pc.vacunado FROM programacion_vacunas pgv 
                            INNER JOIN pacientes pc ON (pc.noid = pgv.noid)
                            WHERE pc.noId = {}'''.format(documentoID))
            cita = cursorObj.fetchone()
            if cita != None: 
                vacunado = input('¿Desea vacunar a esta persona? (S/N):\n').title()
                if vacunado == 'S':
                    cursorObj.execute('UPDATE pacientes SET vacunado = "{}" WHERE noId = {}'.format(vacunado, documentoID))
                    cursorObj.execute('UPDATE lote_vacunas SET cantidadUsada = cantidadUsada + 1 WHERE noLote = (SELECT noLote FROM programacion_vacunas WHERE noId = {})'.format(documentoID))
                    con.commit()
            else: print('El paciente no tiene cita programada.\n')
    else: print('El paciente no se encuentra en los registros.\n')

    con.close()

def menuPrincipal():
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

def main():
    crearTablas()
    menuPrincipal()

def reinciarValores():
    con = sqlConnection()
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE pacientes SET vacunado = "N", fechaDesafiliacion= NULL')
    cursorObj.execute('UPDATE lote_vacunas SET cantidadUsada = 0, cantidadAsignada = 0')

    con.close()

main()
