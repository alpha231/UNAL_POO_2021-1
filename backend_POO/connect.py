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
        # se usa el método fetchall() del objeto cursor para almacenar los valores en la variable (resultado).
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
        self.persona = persona
        con = sqlConnection()
        cursorObj = con.cursor()
        cursorObj.execute(
            'INSERT INTO pacientes VALUES ({a},"{b}","{c}","{d}",{e},"{f}","{g}",date("{h}"),date("{i}"),"{j}", NULL)'.format(
                a=self.persona.noId, b=self.persona.nombre[0:20], c=self.persona.apellido[0:20], d=self.persona.direccion[0:20], e=self.persona.telefono, f=self.persona.correo[0:20],
                g=self.persona.ciudad[0:20], h=self.persona.fechaNacimiento, i=self.persona.fechaAfiliacion, j=self.persona.vacunado))
        con.commit()
        con.close()
        
    def updatePersona(self, persona):
        self.persona = persona
        con = sqlConnection()
        cursorObj = con.cursor()
        # se actualiza la variable (fechaDesafiliacion) de la tabla paciente cuando noID = documentoID por el método .UPDATE
        cursorObj.execute('UPDATE pacientes SET fechaDesafiliacion = date("{}") WHERE noID = {}'.format(self.persona.fechaDesafiliacion, self.persona.noId))
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
        # se usa el método fetchall() del objeto cursor para almacenar los valores en la variable (resultado).
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
    
    def setLote(self, lote):
        self.lote = lote
        con = sqlConnection()
        cursorObj = con.cursor()
        info = (self.lote.noLote, self.lote.fabricante, self.lote.tipoVacuna, self.lote.cantidadRecibida, self.lote.cantidadAsignada, self.lote.cantidadUsada, self.lote.dosisNecesaria,
                self.lote.temperatura, self.lote.efectividad, self.lote.tiempoProteccion, self.lote.fechaVencimiento, self.lote.imagen)
        # Se insertan los datos de (info) dentro de la tabla lote_vacunas por el método INSERT INTO, teniendo en cuenta que el penúltimo valor entra con un formato de fecha con el método date()
        cursorObj.execute('INSERT INTO lote_vacunas VALUES (?,?,?,?,?,?,?,?,?,?,date(?),?)', info)
        con.commit()
        con.close()