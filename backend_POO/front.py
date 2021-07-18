# se importan logic.py, model.py y connect.py, requeridos para el programa
import logic
import model
import connect
# from datetime import datetime, date, time, timezone
# Librería datetime esta incluida por defecto, permite la correcta elaboración para formatos de fecha
# import datetime
from datetime import datetime, timedelta

# Se crea una clase identificada como persona, relacionada a los valores y funciones propias de los pacientes
class Persona:
    def __init__(self) -> None:
        self.persona = model.Persona()
        self.logicaPersona = logic.Persona()
    
    # Propiedad para mostrar el menu de afiliados
    def imprimirMenu(self):
        # se crea un bucle para seleccionar una acción del programa, se cierra al sigitar "4"
        while True:
            opcion = input('Ingrese el número de la opcion que desea realizar:\n'+
                        '1. Crear nuevo afiliado\n'+
                        '2. Consultar afiliado\n'+
                        '3. Desafiliar usuario\n'+
                        '4. Atras\n')
            # si (opcion) NO esta vacia, se transformara la variable a un numero entero con int()
            if opcion != '':
                opcion = int(opcion)
                # si (opcion) es "1", llamara a la propiedad crearUsuario() del metodo logicaPersona
                if opcion == 1: 
                    self.logicaPersona.crearUsuario(self.infoUsuario())
                # si (opcion) es "2", se pedira el valor para consultar un afiliado
                elif opcion == 2: 
                    texto = 'Ingrese a continuación el documento de identidad de la persona que desea consultar:\n'
                    # se llama al metodo consultarUsuario() de logicaPersona para obtener los datos del usuario y se almacenan en la variable (resultado)
                    resultado = self.logicaPersona.consultarUsuario(self.pedirDocumento(texto))
                    # se muestra la información recogida
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
                        # se muestra la fecha de desafiliación solo si esta existe
                        if self.persona.fechaDesafiliacion != None:
                            print("Fecha de desafiliación:", self.persona.fechaDesafiliacion)
                    # Si (resultado) esta vacío, se imprime un mensaje
                    else:
                        print('El paciente no se encuentra en los registros.\n')
                # si (opcion) es "3", se pedirá el valor identificador del afiliado y se almacenará en (texto)
                elif opcion == 3: 
                    texto = 'Ingrese a continuación el documento de identidad de la persona que desea desafiliar:\n'
                    # se llama al metodo desafiliarUsuario() de logicaPersona con el identificador (texto)
                    self.logicaPersona.desafiliarUsuario(self.usuarioADesafiliar(texto))
                # si (opcion) es "3", se detendra el ciclo
                elif opcion == 4: 
                    break
            else: continue
    
    # Se define la propiedad infoUsuario() para recolectar la información de un nuevo usuario
    def infoUsuario(self):
        print('Ingrese a continuación los datos de la persona que desea registrar:')
        # se genera un ciclo que se detendra al registrar un documento de identidad exitosamente
        while True:
            try:
                # Lo digitado por el usuario se almacena en self.persona.noId
                self.persona.noId = int(input('Documento de Identidad:\n'))
                break
            # en caso de que lo digitado contenga valores diferentes a numeros enteros se mostrará un mensaje
            except ValueError:
                print('El documento de identidad debe contener solo números')
        # se llama al metodo consultarUsuario() de logicaPersona y su valor se almacena en la variable (resultado)
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        # si no hay valores para resultado, se pedirá al usuario digitar la información referente al afiliado
        if not resultado:
            self.persona.nombre = input('Nombre:\n').title()
            self.persona.apellido = input('Apellido:\n').title()
            self.persona.direccion = input('Dirección:\n').title()
            self.persona.telefono = int(input('Teléfono:\n'))
            self.persona.correo = input('Correo:\n')
            self.persona.ciudad = input('Ciudad:\n').title()
            # se genera un ciclo que parará al validar una fecha de nacimiento del afiliado
            while True:
                print('Fecha de nacimiento:')
                self.persona.fechaNacimiento = formatoFechas()
                # se toma el valor de la fecha obtenido y se usa el metodo datetime.strptime()
                try:
                    fechaNacimientoDt = datetime.strptime(self.persona.fechaNacimiento, "%Y-%m-%d")
                    # se compara la fecha obtenida con la fecha actual con la función assert
                    fechaActual = datetime.now()
                    assert fechaNacimientoDt < fechaActual
                    break
                # al invalidarse una fecha dada por el usuario, aparecerá un mensaje
                except AssertionError:
                    print('La fecha ingresada es invalida')
            # se genera un ciclo que se detiene al validar la fecha de afiliación
            while True:
                print('Fecha de afiliación:')
                self.persona.fechaAfiliacion = formatoFechas()
                # se toma el valor de la fecha obtenido y se usa el metodo datetime.strptime()
                try:
                    fechaAfiliacionDt = datetime.strptime(self.persona.fechaAfiliacion, "%Y-%m-%d")
                    # se compara la fecha obtenida con la fecha de nacimiento y la fecha actual con la función assert
                    fechaActual = datetime.now()
                    assert (fechaActual > fechaAfiliacionDt > fechaNacimientoDt)
                    break
                # en caso de invalidarse una fecha dada por el usuario, aparecerá un mensaje
                except AssertionError:
                    print('La fecha ingresada es invalida')
            # Se crea variable (vacunado) que identifica si el usuario esta vacunado o no, ("S" vacunado) o ("N" no vacunado)
            # while True:
            #     vacunado = input('¿Ha sido vacunado? (S/N):\n').title() 
            #     if vacunado == 'N': break
            self.persona.vacunado = 'N'
            return self.persona
        else:
            # En caso de que la variable (resultado) NO este vacia, aparecerá un mensaje
            print('Este usuario ya existe\n')

    # se crea una propiedad que pide y obtiene el documento de identidad del afiliado
    def pedirDocumento(self, texto):
        # se pide el documento de identidad del paciente correspondiente y se almacena en self.persona.noId
        self.persona.noId = int(input(texto))
        return self.persona.noId
    # se crea una propiedad para validar la desafiliación de un usuario
    def usuarioADesafiliar(self,texto):
        self.persona.noId = self.pedirDocumento(texto)
        resultado = self.logicaPersona.consultarUsuario(self.persona.noId)
        # si la variable (resultado) NO esta vacía, se generará un bucle que solo se detendra al validar la fecha
        if resultado:
            while True:
                print('Fecha de desafiliacion:')
                self.persona.fechaDesafiliacion = formatoFechas()
                # Se valida la fecha obtenida y se valida por el método assert
                try:
                    fechaDesafiliacionDt = datetime.strptime(self.persona.fechaDesafiliacion, "%Y-%m-%d")
                    fechaAfiliacionDt = datetime.strptime(resultado.fechaAfiliacion, "%Y-%m-%d")
                    fechaActual = datetime.now()
                    assert (fechaActual > fechaDesafiliacionDt > fechaAfiliacionDt)
                    break
                # En caso de que no se valide la fecha se mostrará un mensaje
                except AssertionError:
                    print('La fecha ingresada es invalida')
            return self.persona
        # En caso de que la variable (resultado) este vacía, se mostrará un mensaje
        else: print('El paciente no se encuentra en los registros.')

# Se crea una clase identificada como Lote, relacionada a los valores y funciones propias de los lotes de vacunas
class Lote:
    def __init__(self) -> None:
        self.lote = model.Persona()
        self.logicaLote = logic.Persona()
        
    # Función de menú para las opciones crearLote() y consultarLote()
    def menuModuloDos(self):
        # se crea un ciclo que finaliza únicamente cuando el usuario elige la opción (3. Atras)
        while True:
            opcion = input('Ingrese el número de la opcion que desea realizar:\n'+
                        '1. Crear nuevo lote de vacunas\n'+
                        '2. Consultar lote de vacunas\n'+
                        '3. Atras\n')
            # Si la variable (opcion) no esta vacía se convertirá a un número entero
            if opcion != '':
                opcion = int(opcion)
                # Trae la función (crearLote) de logicaLote
                if opcion == 1: self.logicaLote.crearLote()
                # Trae la función (consultarLote) de logicaLote
                if opcion == 2: self.logicaLote.consultarLote()
                # Detiene el bucle
                if opcion == 3: break
            # El programa dara otra vuelta en caso de que la variable (opcion) este vacía
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
        # Si la variable (opcion) no esta vacía se convertirá a un número entero
        if opcion != '':
            opcion = int(opcion)
            # Llamará al método crearPlanVacunacion de miPlan
            if opcion == 1: miPlan.crearPlanVacunacion()
            # Llamará al método consultarPlanVacunacion de miPlan
            if opcion == 2: miPlan.consultarPlanVacunacion()
            # Detiene el bucle
            if opcion == 3: break
            # El programa dara otra vuelta en caso de que la variable (opcion) este vacía
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
        # Si la variable (opcion) no esta vacía se convertirá a un número entero
        if opcion != '':
            opcion = int(opcion)
            # Si (opcion) es igual a 1, se inicia la función programacionDeVacunacion() de miProgramacion
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
                    # Si la variable (opcion) no esta vacía se convertirá a un número entero
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
    # Se genera un bucle que se detiene cuando la variable (opcion) sea igual a 2
    while True:
        opcion = input('Desea vacunar pacientes?:\n'+
                       '1. Si\n'+
                       '2. No\n')
        # Si la variable (opcion) no esta vacía se convertirá a un número entero
        if opcion != '':
            opcion = int(opcion)
            # Se llama al método vacunacionPacientes de logic
            if opcion == 1: logic.vacunacionPacientes()
            if opcion == 2: break
        else: continue


# Función para generar un menú principal con las opciones de las funcionalidades del programa
def menuPrincipal():
    # Se introduce valores de la clase Persona() en la variable (persona)
    persona = Persona()
    # Se crea ciclo que solo termina cuando (opcion) sea igual a 7
    while True:
        opcion = input('Seleccione el modulo al que desea ingresar:\n'+
                       '1. Afiliados\n'+
                       '2. Lotes\n'+
                       '3. Planes de vacunacion\n'+
                       '4. Programación de vacunacion\n'+
                       '5. Vacunar\n'+
                       '6. Documentación de usuario\n'+
                       '7. Salir\n')
        # Si la variable (opcion) no esta vacía se convertirá a un número entero
        if opcion != '':
            opcion = int(opcion)
            # Se llama al método imprimirMenu de persona
            if opcion == 1: persona.imprimirMenu()
            # Se llama al método menuModuloDos de persona
            if opcion == 2: persona.menuModuloDos()
            # Se llama a la función menuModuloTres
            if opcion == 3: menuModuloTres()
            # Se llama a la función menuModuloCuatro
            if opcion == 4: menuModuloCuatro()
            # Se llama a la función menuModuloCinco
            if opcion == 5: menuModuloCinco()
            # Se llama al método documentacionUsuario de logic
            if opcion == 6: logic.documentacionUsuario()
            # Se detiene el bucle
            if opcion == 7: break
            # Se llama a la función reiniciarValores() para reiniciar valores de la base de datos
            if opcion == 231: reiniciarValores()
        else: continue


# Función principal del programa, inicia las funciones básicas
def main():
    connect.crearTablas()
    menuPrincipal()


# Función para reiniciar valores de los pacientes y usos o asignaciones de vacunas
def reiniciarValores():
    pass

# Función para designar el formato con el que se manejan las fechas
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
