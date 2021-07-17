import model
# Librería sqlite3 esta incluida por defecto, permite elaborar y manipular bases de datos
import sqlite3
from sqlite3 import Error

# Función que da conexión a la base de datos mencionada (Vacunacion.db) creada con sqlite3 utilizando el parámetro creado (con), por el método sqlite3.connect()
def sqlConnection():
    try:
        con = sqlite3.connect('./Vacunacion.db')
        return con
    except Error:
        print(Error)

# Esta función creara las tablas mencionadas si estas no se encuentran dentro de la base de datos con el método .execute que permite la manipulación de la información de la base de datos
def crearTablas():
    con = sqlConnection()
    # Se crea método .cursor() para traer y ejecutar declaraciones
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
                    "fechaAfiliacion"	DATE,
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
                    "fechaVencimiento"	DATE,
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
                    "idCita"      INTEGER,
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
    # Se usa el método .commit() para afirmar los cambios realizados dentro de la base de datos
    con.commit()
    # Se cierra la base de datos por el método .close()
    con.close()

class Persona:
    def __init__(self) -> None:
        self.persona = model.Persona()
        self.id = None
        
    def getPersona(self, id):
        self.id = id
        con = sqlConnection()
        cursorObj = con.cursor()
        # se busca dentro de la tabla pacientes el valor (noId) que corresponda con la variable(documentoID)
        cursorObj.execute('SELECT * FROM pacientes WHERE noId = {}'.format(self.id))
        # se usa el método fetchone() del objeto cursor para almacenar los valores en la variable (resultado).
        resultado = cursorObj.fetchone()
        con.close()
        if resultado != None:
            self.persona.noId = resultado[0]
            self.persona.nombre = resultado[1]
            self.persona.apellido = resultado[2]
            self.persona.direccion = resultado[3]
            self.persona.telefono = resultado[4]
            self.persona.correo = resultado[5]
            self.persona.ciudad = resultado[6]
            self.persona.fechaNacimiento = resultado[7]
            self.persona.fechaAfiliacion = resultado[8]
            self.persona.vacunado = resultado[9]
            self.persona.fechaDesafiliacion = resultado[10]
            return self.persona
        return False
    
    def setPersona(self, persona):
        con = sqlConnection()
        cursorObj = con.cursor()
        cursorObj.execute(
            'INSERT INTO pacientes VALUES ({a},"{b}","{c}","{d}",{e},"{f}","{g}",date("{h}"),date("{i}"),"{j}", NULL)'.format(
                a=persona.noId, b=persona.nombre[0:20], c=persona.apellido[0:20], d=persona.direccion[0:20], e=persona.telefono, f=persona.correo[0:20],
                g=persona.ciudad[0:20], h=persona.fechaNacimiento, i=persona.fechaAfiliacion, j=persona.vacunado))
        con.commit()
        con.close()
        
    def updatePersona(self, persona):
        con = sqlConnection()
        cursorObj = con.cursor()
        # se actualiza la variable (fechaDesafiliacion) de la tabla paciente cuando noID = documentoID por el método .UPDATE
        cursorObj.execute('UPDATE pacientes SET fechaDesafiliacion = date("{}") WHERE noID = {}'.format(persona.fechaDesafiliacion, persona.noId))
        # Se afirman los cambios realizados
        con.commit()
        con.close()
        
    def getEstadoPersonaCitada(self, id):
        self.id = id
        con = sqlConnection()
        cursorObj = con.cursor()
        # Se obtiene el valor de (cita) con la tabla programacion_vacunas donde corresponda con (documentoID) usando el método INNER JOIN en la tabla pacientes
        cursorObj.execute('''SELECT pc.fechaDesafiliacion , pc.vacunado FROM programacion_vacunas pgv 
                        INNER JOIN pacientes pc ON (pc.noid = pgv.noid)
                        WHERE pc.noId = {}'''.format(self.id))
        resultado = cursorObj.fetchone()
        con.close()
        if resultado != None:
            self.persona.fechaDesafiliacion = resultado[0]
            self.persona.vacunado = resultado[1]
            return self.persona
        return False
    
    def setPacienteVacunado(self, persona):
        con = sqlConnection()
        cursorObj = con.cursor()
        # se actualiza el estado de vacunación del paciente y se suma 1 a (cantidadUsada) de la tabla lote_vacunas con el método UPDATE
        cursorObj.execute('UPDATE pacientes SET vacunado = "{}" WHERE noId = {}'.format(persona.vacunado, persona.noId))
        cursorObj.execute('UPDATE lote_vacunas SET cantidadUsada = cantidadUsada + 1 WHERE noLote = (SELECT noLote FROM programacion_vacunas WHERE noId = {})'.format(persona.noId))
        # Se afirman los cambios realizados
        con.commit()
        con.close()

class Lote:
    def __init__(self) -> None:
        self.lote = model.Lote()
        self.id = None
        
    def getLote(self, id):
        self.id = id
        con = sqlConnection()
        cursorObj = con.cursor()
        # se busca dentro de la tabla pacientes el valor (noId) que corresponda con la variable(documentoID)
        cursorObj.execute('SELECT * FROM lote_vacunas WHERE noLote = {}'.format(self.id))
        # se usa el método fetchone() del objeto cursor para almacenar los valores en la variable (resultado).
        resultado = cursorObj.fetchone()
        con.close()
        if resultado != None:
            self.lote.noLote = resultado[0]
            self.lote.fabricante = resultado[1]
            self.lote.tipoVacuna = resultado[2]
            self.lote.cantidadRecibida = resultado[3]
            self.lote.cantidadAsignada = resultado[4]
            self.lote.cantidadUsada = resultado[5]
            self.lote.dosisNecesaria = resultado[6]
            self.lote.temperatura = resultado[7]
            self.lote.efectividad = resultado[8]
            self.lote.tiempoProteccion = resultado[9]
            self.lote.fechaVencimiento = resultado[10]
            self.lote.imagen = resultado[11]
            return self.lote
        return False
    
    def getLotes(self):
        con = sqlConnection()
        cursorObj = con.cursor()
        cursorObj.execute('SELECT * FROM lote_vacunas'.format())
        # Se trae el valor individual de la tabla lote_vacunas que concuerda con (noLote)
        resultados = cursorObj.fetchall()
        con.close()
        if len(resultados) != 0:
            listaDeLotes=[]
            for resultado in resultados:
                self.lote = model.Lote()
                self.lote.noLote = resultado[0]
                self.lote.fabricante = resultado[1]
                self.lote.tipoVacuna = resultado[2]
                self.lote.cantidadRecibida = resultado[3]
                self.lote.cantidadAsignada = resultado[4]
                self.lote.cantidadUsada = resultado[5]
                self.lote.dosisNecesaria = resultado[6]
                self.lote.temperatura = resultado[7]
                self.lote.efectividad = resultado[8]
                self.lote.tiempoProteccion = resultado[9]
                self.lote.fechaVencimiento = resultado[10]
                listaDeLotes.append(self.lote)
            return listaDeLotes
        else:
            return False
            
    
    def setLote(self, lote):
        con = sqlConnection()
        cursorObj = con.cursor()
        info = (lote.noLote, lote.fabricante, lote.tipoVacuna, lote.cantidadRecibida, lote.cantidadAsignada, lote.cantidadUsada, lote.dosisNecesaria,
                lote.temperatura, lote.efectividad, lote.tiempoProteccion, lote.fechaVencimiento, lote.imagen)
        # Se insertan los datos de (info) dentro de la tabla lote_vacunas por el método INSERT INTO, teniendo en cuenta que el penúltimo valor entra con un formato de fecha con el método date()
        cursorObj.execute('INSERT INTO lote_vacunas VALUES (?,?,?,?,?,?,?,?,?,?,date(?),?)', info)
        con.commit()
        con.close()
        
    def setValoresVacunasDefault(self):
        con = sqlConnection()
        cursorObj = con.cursor()
        # Se cambian los datos de la tabla paciente: vacunados a "N" y fechaDesafiliacion a NULL
        cursorObj.execute('UPDATE pacientes SET vacunado = "N", fechaDesafiliacion= NULL')
        # Se cambian los datos de la tabla lote_vacunas: cantidadUsada a 0 y cantidadAsignada a 0
        cursorObj.execute('UPDATE lote_vacunas SET cantidadUsada = 0, cantidadAsignada = 0')
        con.commit()
        con.close()

class PlanDeVacunacion:
    def __init__(self) -> None:
        self.plan = model.PlanDeVacunacion()
        self.id = None
        
    def getPlan(self, id):
        self.id = id
        con = sqlConnection()
        cursorObj = con.cursor()
        # se busca dentro de la tabla pacientes el valor (noId) que corresponda con la variable(documentoID)
        cursorObj.execute('SELECT * FROM plan_vacunacion WHERE idPlan = {}'.format(self.id))
        # se usa el método fetchone() del objeto cursor para almacenar los valores en la variable (resultado).
        resultado = cursorObj.fetchone()
        con.close()
        if resultado != None:
            self.plan.idPlan = resultado[0]
            self.plan.edadMinima = resultado[1]
            self.plan.edadMaxima = resultado[2]
            self.plan.fechaInicio = resultado[3]
            self.plan.fechaFinal = resultado[4]
            return self.plan
        return False
    
    def getPlanes(self):
        con = sqlConnection()
        cursorObj = con.cursor()
        # se busca dentro de la tabla pacientes el valor (noId) que corresponda con la variable(documentoID)
        cursorObj.execute('SELECT * FROM plan_vacunacion')
        # se usa el método fetchone() del objeto cursor para almacenar los valores en la variable (resultado).
        resultados = cursorObj.fetchall()
        con.close()
        if len(resultados) != 0:
            listaDePlanes=[]
            for resultado in resultados:
                self.plan = model.PlanDeVacunacion()
                self.plan.idPlan = resultado[0]
                self.plan.edadMinima = resultado[1]
                self.plan.edadMaxima = resultado[2]
                self.plan.fechaInicio = resultado[3]
                self.plan.fechaFinal = resultado[4]
                listaDePlanes.append(self.plan)
            return listaDePlanes
        else:
            return False
    
    def setPlan(self, plan):
        con = sqlConnection()
        cursorObj = con.cursor()
        info = (plan.idPlan, plan.edadMinima, plan.edadMaxima, plan.fechaInicio, plan.fechaFinal)
        # Se insertan los datos de (info) dentro de la tabla plan_vacunas por el método INSERT INTO, teniendo en cuenta que el penúltimo valor entra con un formato de fecha con el método date()
        cursorObj.execute('INSERT INTO plan_vacunacion VALUES (?,?,?,date(?),date(?))', info)
        con.commit()
        con.close()
        
    def getRangoEdades(self):
        con = sqlConnection()
        cursorObj = con.cursor()
        cursorObj.execute('SELECT edadMinima, edadMaxima FROM plan_vacunacion')
        rangoEdades = cursorObj.fetchall()
        con.close()
        return rangoEdades

class ProgramacionDeVacunas(Persona, Lote, PlanDeVacunacion):
    def __init__(self) -> None:
        self.programacion = model.ProgramacionDeVacunas()
        self.fechaInicioIngresada = None
    
    def reiniciarProgramacion(self):
        con = sqlConnection()
        cursorObj = con.cursor()
        # se actualiza la tabla lote_vacunas de manera que cantidadAsignada tenga el valor de cantidadUsada con el método UPDATE
        cursorObj.execute('UPDATE lote_vacunas SET cantidadAsignada = cantidadUsada')
        # se remueve la tabla programacion_vacunas de la base de datos
        cursorObj.execute('DROP TABLE IF EXISTS programacion_vacunas')
        con.commit()
        con.close()
        crearTablas()
        
    def getPacientesAVacunar(self, edadMinima, edadMaxima):
        con = sqlConnection()
        cursorObj = con.cursor()
        # Se toman datos de la tabla paciente según un rango de edad tomado de los valores de (planVacunacion)
        cursorObj.execute('''SELECT noId, ciudad, CAST((julianday("now") - julianday(fechaNacimiento))/365.25 as INTEGER) as Edad FROM pacientes 
                            WHERE (Edad >= {}) AND (Edad <= {}) AND vacunado = "N" AND fechaDesafiliacion is Null'''.format(edadMinima, edadMaxima))
        resultados = cursorObj.fetchall()
        con.close()
        if len(resultados) != 0:
            listaDePacientes=[]
            for resultado in resultados:
                self.persona = model.Persona()
                self.persona.noId = resultado[0]
                self.persona.ciudad = resultado[1]
                self.persona.edad = resultado[2]
                listaDePacientes.append(self.persona)
            return listaDePacientes
        else:
            return False
    
    def getVacunaDisponible(self):
        con = sqlConnection()
        cursorObj = con.cursor()
        cursorObj.execute('SELECT noLote FROM lote_vacunas WHERE cantidadAsignada<cantidadRecibida')
        resultado = cursorObj.fetchone()
        con.close()
        if resultado != None:
            self.lote = model.Lote()
            self.lote.noLote = resultado[0]
            return self.lote
        return False
    
    def setProgramacion(self, persona, lote, plan):
        con = sqlConnection()
        cursorObj = con.cursor()
        datos = (persona.ciudad, persona.noId, lote.noLote, plan.idPlan)
        cursorObj.execute('INSERT INTO programacion_vacunas (ciudadVacunacion, noId, noLote, idPlan) VALUES (?,?,?,?)', datos)
        cursorObj.execute('UPDATE lote_vacunas SET cantidadAsignada = cantidadAsignada+1 WHERE noLote = {}'.format(lote.noLote))
        con.commit()
        con.close()

    def getCitasAProgramar(self):
        con = sqlConnection()
        cursorObj = con.cursor()
        cursorObj.execute('''SELECT pgv.*, plv.fechaInicio, plv.fechaFinal, pc.correo, lv.fabricante FROM programacion_vacunas pgv 
                        INNER JOIN plan_vacunacion plv ON (plv.idPlan = pgv.idPlan) 
                        INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                        INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote) 
                        WHERE fechaProgramada IS NULL''')
        citaAProgramar = cursorObj.fetchall()
        con.close()
        if len(citaAProgramar) != 0:
            listaDeCitas=[]
            for resultado in citaAProgramar:
                self.programacion = model.ProgramacionDeVacunas()
                self.programacion.idCita = resultado[0]
                self.programacion.noId = resultado[1]
                self.programacion.noLote = resultado[2]
                self.programacion.idPlan = resultado[3]
                self.programacion.ciudadVacunacion = resultado[4]
                self.programacion.fechaProgramada = resultado[5]
                self.programacion.horaProgramada = resultado[6]
                self.plan = model.PlanDeVacunacion()
                self.plan.fechaInicio = resultado[7]
                self.plan.fechaFinal = resultado[8]
                self.persona = model.Persona()
                self.persona.correo = resultado[9]
                self.lote = model.Lote()
                self.lote.fabricante = resultado[10]
                listaDeCitas.append([self.programacion, self.plan, self.persona, self.lote])
            return listaDeCitas
        else:
            return False
        return citaAProgramar
    
    def getUltimacita(self):
        con = sqlConnection()
        cursorObj = con.cursor()
        cursorObj.execute('''SELECT fechaProgramada, max(horaProgramada) FROM programacion_vacunas 
                          WHERE fechaProgramada = (SELECT max(fechaProgramada) FROM programacion_vacunas)''')
        ultimaCita = cursorObj.fetchone()
        con.close()
        if ultimaCita[0] != None:
            self.programacion.fechaProgramada = ultimaCita[0]
            self.programacion.horaProgramada = ultimaCita[1]
            return self.programacion
        return False
    
    def setFechaHora(self, programacion):
        con = sqlConnection()
        cursorObj = con.cursor()
        info = (programacion.fechaProgramada, programacion.horaProgramada, programacion.idCita)
        cursorObj.execute('update programacion_vacunas set fechaProgramada = ?, horaProgramada = ? where idCita = ?', info)
        con.commit()
        
    def getProgramacionCompleta(self, datoConsulta):
        con = sqlConnection()
        cursorObj = con.cursor()
        # se seleccionan variables de la tabla programacion_vacunas y se unen los valores que coincidan con el método INNER JOIN
        cursorObj.execute('''SELECT pc.noId, pc.nombre, pc.apellido, pc.direccion, pc.telefono, pc.correo, pgv.fechaProgramada, pgv.horaProgramada, lv.noLote, lv.fabricante  FROM programacion_vacunas pgv 
                            INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                            INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote)
                            ORDER BY {}'''.format(datoConsulta))
        citasProgramadas = cursorObj.fetchall()
        con.close()
        if len(citasProgramadas) != 0:
            listaDeCitas=[]
            for resultado in citasProgramadas:
                self.persona = model.Persona()
                self.persona.noId = resultado[0]
                self.persona.nombre = resultado[1]
                self.persona.apellido = resultado[2]
                self.persona.direccion = resultado[3]
                self.persona.telefono = resultado[4]
                self.persona.correo = resultado[5]
                self.programacion = model.ProgramacionDeVacunas()
                self.programacion.fechaProgramada = resultado[6]
                self.programacion.horaProgramada = resultado[7]
                self.lote = model.Lote()
                self.lote.noLote = resultado[8]
                self.lote.fabricante = resultado[9]
                listaDeCitas.append([self.persona, self.programacion, self.lote])
            return listaDeCitas
        else:
            return False
        
    def getProgramacionIndividual(self, id):
        con = sqlConnection()
        cursorObj = con.cursor()
        # se seleccionan variables de la tabla programacion_vacunas y se unen los valores que coincidan con el método INNER JOIN
        cursorObj.execute('''SELECT pc.noId, pc.nombre, pc.apellido, pc.direccion, pc.telefono, pc.correo, pgv.fechaProgramada, pgv.horaProgramada, lv.noLote, lv.fabricante  FROM programacion_vacunas pgv 
                            INNER JOIN pacientes pc ON (pc.noid = pgv.noid) 
                            INNER JOIN lote_vacunas lv ON (lv.noLote = pgv.noLote)
                            WHERE pgv.noId = {}'''.format(id))
        resultado = cursorObj.fetchone()
        con.close()
        if resultado != None:
            self.persona = model.Persona()
            self.persona.noId = resultado[0]
            self.persona.nombre = resultado[1]
            self.persona.apellido = resultado[2]
            self.persona.direccion = resultado[3]
            self.persona.telefono = resultado[4]
            self.persona.correo = resultado[5]
            self.programacion = model.ProgramacionDeVacunas()
            self.programacion.fechaProgramada = resultado[6]
            self.programacion.horaProgramada = resultado[7]
            self.lote = model.Lote()
            self.lote.noLote = resultado[8]
            self.lote.fabricante = resultado[9]
            return self.persona, self.programacion, self.lote
        return False