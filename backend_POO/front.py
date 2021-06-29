import logic
import model
# from datetime import datetime, date, time, timezone
# Librería datetime esta incluida por defecto, permite la correcta elaboración para formatos de fecha
# import datetime
from datetime import datetime, timedelta
# Librería PIL esta incluida por defecto, importa el método Image con el fin de producir una imagen
from PIL import Image
# Librería webbrowser esta incluida por defecto, será usada para abrir una dirección en el navegador
import webbrowser
# Libreria incluida por defecto que permite crear directorio en la maquina
import os
# Libreria incluida por defecto para eliminar directorios recursivamente
import shutil
# # from dateutil.relativedelta import relativedelta


class Persona:
    def __init__(self) -> None:
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
        
    def imprimirMenu(self):
        while True:
            opcion = input('Ingrese el número de la opcion que desea realizar:\n'+
                        '1. Crear nuevo afiliado\n'+
                        '2. Consultar afiliado\n'+
                        '3. Desafiliar usuario\n'+
                        '4. Atras\n')
            if opcion != '':
                opcion = int(opcion)
                if opcion == 1: 
                    self.logicaPersona.crearUsuario(self.infoUsuario())
                elif opcion == 2: 
                    texto = 'Ingrese a continuación el documento de identidad de la persona que desea consultar:\n'
                    resultado = self.logicaPersona.consultarUsuario(self.pedirDocumento(texto))
                    if resultado:
                        self.persona = resultado
                        print("No. Identificación:", self.persona.noId)
                        print("Nombre:", self.persona.nombre)
                        print("Apellido:", self.persona.apellido)
                        print("Dirección:", self.persona.direccion)
                        print("Teléfono:", self.persona.telefono)
                        print("Correo:", self.persona.correo)
                        print("Ciudad:", self.persona.ciudad)
                        print("Fecha de nacimiento:", self.persona.fechaNacimiento)
                        print("Fecha de afiliacion:", self.persona.fechaAfiliacion)
                        print("¿Vacunado?:", self.persona.vacunado)
                        if self.persona.fechaDesafiliacion != None:
                            print("Fecha de desafiliación:", self.persona.fechaDesafiliacion)
                    else:
                        print('El paciente no se encuentra en los registros.\n')
                elif opcion == 3: 
                    texto = 'Ingrese a continuación el documento de identidad de la persona que desea desafiliar:\n'
                    self.logicaPersona.desafiliarUsuario(self.usuarioADesafiliar(texto))
                elif opcion == 4: 
                    break
            else: continue
    
    def infoUsuario(self):
        print('Ingrese a continuación los datos de la persona que desea registrar:')
        while True:
            try:
                self.persona.noId = int(input('Documento de Identidad:\n'))
                break
            except ValueError:
                print('El documento de identidad debe contener solo números')
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        if not resultado:
            self.persona.nombre = input('Nombre:\n').title()
            self.persona.apellido = input('Apellido:\n').title()
            self.persona.direccion = input('Dirección:\n').title()
            self.persona.telefono = int(input('Teléfono:\n'))
            self.persona.correo = input('Correo:\n')
            self.persona.ciudad = input('Ciudad:\n').title()
            while True:
                print('Fecha de nacimiento:')
                self.persona.fechaNacimiento = formatoFechas()
                try:
                    fechaNacimientoDt = datetime.strptime(self.persona.fechaNacimiento, "%Y-%m-%d")
                    fechaActual = datetime.now()
                    assert fechaNacimientoDt < fechaActual
                    break
                except AssertionError:
                    print('La fecha ingresada es invalida')
            while True:
                print('Fecha de afiliación:')
                self.persona.fechaAfiliacion = formatoFechas()
                try:
                    fechaAfiliacionDt = datetime.strptime(self.persona.fechaAfiliacion, "%Y-%m-%d")
                    fechaActual = datetime.now()
                    assert (fechaActual > fechaAfiliacionDt > fechaNacimientoDt)
                    break
                except AssertionError:
                    print('La fecha ingresada es invalida')
            # Se crea variable (vacunado) que identifica si el usuario esta vacunado o no, ("S" vacunado) o ("N" no vacunado)
            # while True:
            #     vacunado = input('¿Ha sido vacunado? (S/N):\n').title() 
            #     if vacunado == 'N': break
            self.persona.vacunado = 'N'
            return self.persona
        else:
            # Se mostrara el mensaje si la variable (resultado) es diferente de 0, en caso de que ya hubieran datos almacenados en la variable noId digitada por el usuario
            print('Este usuario ya existe\n')

    def pedirDocumento(self, texto):
        # se pide el documento de identidad del paciente a buscar
        self.persona.noId = int(input(texto))
        return self.persona.noId

    def usuarioADesafiliar(self,texto):
        self.persona.noId = self.pedirDocumento(texto)
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        if resultado:
            while True:
                print('Fecha de desafiliacion:')
                self.persona.fechaDesafiliacion = formatoFechas()
                try:
                    fechaDesafiliacionDt = datetime.strptime(self.persona.fechaDesafiliacion, "%Y-%m-%d")
                    fechaAfiliacionDt = datetime.strptime(resultado.fechaAfiliacion, "%Y-%m-%d")
                    fechaActual = datetime.now()
                    assert (fechaActual > fechaDesafiliacionDt > fechaAfiliacionDt)
                    break
                except AssertionError:
                    print('La fecha ingresada es invalida')
            return self.persona
        # Se mostrara el mensaje si la variable (resultado) es igual a 0, en caso de que no hallan datos almacenados en la variable noId digitada por el usuario
        else: print('El paciente no se encuentra en los registros.')

class Lote:
    def __init__(self) -> None:
        self.lote = model.Lote()
        self.logicaLote = logic.Lote()
        
    # Función de menú para las opciones crearLote() y consultarLote()
    def imprimirMenu(self):
        # se crea un ciclo que finaliza únicamente cuando el usuario elige la opción (3. Atras)
        while True:
            opcion = input('Ingrese el número de la opcion que desea realizar:\n'+
                        '1. Crear nuevo lote de vacunas\n'+
                        '2. Consultar lote de vacunas\n'+
                        '3. Atras\n')
            if opcion != '':
                opcion = int(opcion)
                # Trae la función (crearLote)
                if opcion == 1: 
                    self.logicaLote.crearLote(self.infoLote())
                # Trae la función (consultarLote)
                elif opcion == 2: 
                    texto = 'Ingrese a continuación número de lote que desea consultar:\n'
                    resultado = self.logicaLote.consultarLote(self.pedirNoLote(texto))
                    if resultado:
                        self.lote = resultado
                        print("No. de Lote:", self.lote.noLote)
                        print("Fabricante:", self.lote.fabricante)
                        print("Tipo de vacuna:", self.lote.tipoVacuna)
                        print("Cantidad de vacunas recibidas:", self.lote.cantidadRecibida)
                        print("Cantidad de vacunas asignadas:", self.lote.cantidadAsignada)
                        print("Cantidad de vacunas usadas:", self.lote.cantidadUsada)
                        print("Dosis necesarias:", self.lote.dosisNecesaria)
                        print("Temperatura de almacenamiento:", self.lote.temperatura)
                        print("Efectividad:", self.lote.efectividad)
                        print("Tiempo de protección:", self.lote.tiempoProteccion)
                        print("Fecha de vencimiento:", self.lote.fechaVencimiento)
                        # se muestra una imagen recogiendo los datos de fabricante, imagenBinaria de la tabla lote_vacunas y la variable (cursorObj)
                        self.mostrarImagen(self.lote.fabricante, self.lote.imagen)
                        print('\n')
                    # Se mostrará un mensaje si el valor de (noLote) es nulo
                    else: print('El lote no se encuentra registrado.\n')
                elif opcion == 3: 
                    break
            # El programa dara otra vuelta en caso de que la variable (opcion) este vacía
            else: continue
            
    def infoLote(self):
        print('Ingrese a continuación los datos del lote que desea registrar:')
        while True:
            try:
                self.lote.noLote = int(input('Número del lote:\n'))
                break
            except ValueError:
                print('El número del lote debe contener solo números')
        resultado = self.logicaLote.consultarLote(self.lote.noLote)
        if not resultado:
            # Se ingresan datos respectivos al nuevo lote
            self.lote.fabricante = input('Fabricante:\n').title()
            self.lote.tipoVacuna = input('Tipo de vacuna:\n').title()
            self.lote.cantidadRecibida = int(input('Cantidad de vacunas recibidas:\n'))
            # self.lote.cantidadAsignada = int(input('Cantidad de vacunas asignadas:\n'))
            # self.lote.cantidadUsada = int(input('Cantidad de vacunas usadas:\n'))
            self.lote.cantidadAsignada = 0
            self.lote.cantidadUsada = 0
            self.lote.dosisNecesaria = int(input('Dosis necesarias:\n'))
            self.lote.temperatura = float(input('Temperatura de almacenamiento:\n'))
            self.lote.efectividad = float(input('Efectividad de la vacuna:\n'))
            self.lote.tiempoProteccion = int(input('Tiempo de protección (meses):\n'))
            while True:
                print('Fecha de vencimiento:')
                self.lote.fechaVencimiento = formatoFechas()
                try:
                    fechaVencimientoDt = datetime.strptime(self.lote.fechaVencimiento, "%Y-%m-%d")
                    fechaActualDt = datetime.now()
                    # if fechaVencimientoDt > fechaActualDt + relativedelta(months=1):
                    assert fechaVencimientoDt > fechaActualDt
                    break
                except AssertionError:
                    print('La fecha ingresada es invalida')
            # se da la opcion para ingresar una imagen del lote según su ruta
            rutaImagen = input('Ruta completa a la imagen:\n')
            # se abre el archivo respectivo y se lee, almacenándose en la variable (imagenBinaria)
            with open(rutaImagen, "rb") as File:
                self.lote.imagen = File.read()
            return self.lote
        else:
            # se mostrara un mensaje si el número identificador digitado ya existe dentro de la tabla lote_vacuna
            print('Este lote de vacunas ya existe\n')
    
    def pedirNoLote(self, texto):
        noLote = int(input(texto))
        return noLote
        
    def mostrarImagen(self, fabricante, imagenBinaria):
        # Se crea un ciclo que solo se cierra cuando el usuario halla terminado de visualizar una imagen o hasta que la variable (opcion) sea 2
        while True:
            opcion = input('¿Desea abrir la imagen?:\n'+
                        '1. Si\n'+
                        '2. No\n')
            if opcion != '':
                opcion = int(opcion)
                if opcion == 1:
                    # Se toma la información de la ruta en donde se encuentra la imagen
                    directorio = "imagenesDescargadas/"
                    try:
                        os.stat(directorio)
                    except FileNotFoundError:
                        os.mkdir(directorio)
                    rutaDeGuardado = '{}{}.jpg'.format(directorio, fabricante)
                    with open(rutaDeGuardado, "wb") as File:
                        File.write(imagenBinaria)
                    # Se abre la imagen abriendo su ruta almacenada en (rutaDeGuardado) con el método .open() y se visualiza con el método .show()
                    imagen = Image.open(rutaDeGuardado)
                    imagen.show()
                    shutil.rmtree(directorio)
                    break
                # Termina el bucle
                elif opcion == 2: break
            else: continue
        
    
# Función para mostrar un menú de opciones relacionados a los planes de vacunación
def menuModuloTres():
    miPlan = model.PlanDeVacunacion()
    # se crea un bucle que solo se detiene cuando la variable (opcion) sea igual a 3
    while True:
        opcion = input('Ingrese el número de la opcion que desea realizar:\n'+
                       '1. Crear plan de vacunación\n'+
                       '2. Consultar plan de vacunación\n'+
                       '3. Atras\n')
        if opcion != '':
            opcion = int(opcion)
            if opcion == 1: miPlan.crearPlanVacunacion()
            if opcion == 2: miPlan.consultarPlanVacunacion()
            if opcion == 3: break
        else: continue


# Función que genera un menú para las opciones relacionadas a las programaciones de vacunación
def menuModuloCuatro():
    miProgramacion = model.ProgramacionDeVacunas()
    # Se genera un bucle que solo se detiene cunado (opcion) sea igual a 4
    while True:
        opcion = input('Ingrese el número de la opcion que desea realizar:\n'+
                       '1. Crear la programación de vacunas\n'+
                       '2. Consultar la programación de vacunas\n'+
                       '3. Consultar vacunación de un paciente\n'+
                       '4. Atras\n')
        if opcion != '':
            opcion = int(opcion)
            # Si (opcion) es igual a 1, se inicia la función programacionDeVacunacion()
            if opcion == 1: miProgramacion.programacionDeVacunacion()
            elif opcion == 2:
                # se inicia un bucle para obtener un dato de consulta según lo elija el usuario, este bucle solo se detendrá cuando (opcion) sea 11
                while True:
                    opcion = input('Por que campo desea organizar la consulta:\n'+
                                   '1. Número de Identificación\n'+
                                   '2. Nombre\n'+
                                   '3. Apellido\n'+
                                   '4. Dirección\n'+
                                   '5. Teléfono\n'+
                                   '6. Correo\n'+
                                   '7. Fecha Programada\n'+
                                   '8. Hora Programada\n'+
                                   '9. Número de lote\n'+
                                   '10. Fabricante\n'+
                                   '11. Salir de la consulta\n'+
                                   '')
                    if opcion != '':
                        opcion = int(opcion)
                        # Se realiza una selección para organizar la consulta según (opcion) digitada por el usuario
                        if opcion == 1: datoConsulta = 'pc.noId'
                        elif opcion == 2: datoConsulta = 'pc.nombre'
                        elif opcion == 3: datoConsulta = 'pc.apellido'
                        elif opcion == 4: datoConsulta = 'pc.direccion'
                        elif opcion == 5: datoConsulta = 'pc.telefono'
                        elif opcion == 6: datoConsulta = 'pc.correo'
                        elif opcion == 7: datoConsulta = 'pgv.fechaProgramada'
                        elif opcion == 8: datoConsulta = 'pgv.horaProgramada'
                        elif opcion == 9: datoConsulta = 'lv.noLote'
                        elif opcion == 10: datoConsulta = 'lv.fabricante'
                        elif opcion == 11: break
                        else: continue
                    else: continue
                    # Se llama a la función consultarProgramacionCompleta() con la entrada (datoConsulta)
                    miProgramacion.consultarProgramacionCompleta(datoConsulta)
            # Si (opcion) es igual a 3, se inicia la función consultarProgramacionIndividual()
            elif opcion == 3: miProgramacion.consultarProgramacionIndividual()
            # el programa deja el bucle por medio de la función break
            elif opcion == 4: break
        else: continue


# Función para generar un menú de opciones para confirmar la vacunación de un paciente
def menuModuloCinco():
    while True:
        opcion = input('Desea vacunar pacientes?:\n'+
                       '1. Si\n'+
                       '2. No\n')
        if opcion != '':
            opcion = int(opcion)
            if opcion == 1: logic.vacunacionPacientes()
            if opcion == 2: break
        else: continue


# Función para generar un menú principal con las opciones de las funcionalidades del programa
def menuPrincipal():
    persona = Persona()
    lote = Lote()
    # Se crea ciclo que solo termina cuando (opcion) sea igual a 6
    while True:
        opcion = input('Seleccione el modulo al que desea ingresar:\n'+
                       '1. Afiliados\n'+
                       '2. Lotes\n'+
                       '3. Planes de vacunacion\n'+
                       '4. Programación de vacunacion\n'+
                       '5. Vacunar\n'+
                       '6. Documentación de usuario\n'+
                       '7. Salir\n')
        if opcion != '':
            opcion = int(opcion)
            if opcion == 1: persona.imprimirMenu()
            if opcion == 2: lote.imprimirMenu()
            if opcion == 3: menuModuloTres()
            if opcion == 4: menuModuloCuatro()
            if opcion == 5: menuModuloCinco()
            if opcion == 6: logic.documentacionUsuario()
            if opcion == 7: break
            if opcion == 231: reiniciarValores()
        else: continue


# Función principal del programa, inicia las funciones básicas
def main():
    logic.crearTablas()
    menuPrincipal()


# Función para reiniciar valores de los pacientes y usos o asignaciones de vacunas
def reiniciarValores():
    pass


def formatoFechas():
    # se crean variables (diaNacimiento, mesNacimiento y añoNacimiento) que contienen los número de dia, mes y fecha de nacimiento respectivamente con la cantidad de dígitos marcada usando el método .ljust()
    dia = input("Dia: ")
    dia = dia.ljust(2)
    mes = input("Mes: ")
    mes = mes.ljust(2)
    anio = input("Año: ")
    anio = anio.ljust(4)
    # Se juntan y almacenan los valores anteriores pertenecientes a la fecha en la variable (fecha) con el método .format()
    fecha = "{}-{}-{}".format(anio, mes, dia)
    return fecha

# Se llama a la función principal del programa
main()
