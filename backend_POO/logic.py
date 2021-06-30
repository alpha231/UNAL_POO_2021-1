import model
import connect
# Librería webbrowser esta incluida por defecto, será usada para abrir una dirección en el navegador
import webbrowser


class Persona:
    def __init__(self) -> None:
        self.persona = model.Persona()
        self.metodosConexion = connect.Persona()

    def crearUsuario(self, info):
        if info != None:
            self.persona = info
            self.metodosConexion.setPersona(self.persona)

    def consultarUsuario(self,id):
        resultado = self.metodosConexion.getPersona(id)
        if resultado:
            self.persona = resultado
            return self.persona
        return resultado
    
    def desafiliarUsuario(self, persona):
        if persona != None:
            self.persona = persona
            self.metodosConexion.updatePersona(self.persona)

    def consultarEstadoPersonaCitada(self, id):
        resultado = self.metodosConexion.getEstadoPersonaCitada(id)
        if resultado:
            self.persona = resultado
            return self.persona
        return resultado

    # Función para cambiar estado de vacunación de un usuario si cumple con los requisitos
    def vacunarPacientes(self, persona):
        if persona != None:
            self.persona = persona
            self.metodosConexion.setPacienteVacunado(self.persona)

    def documentacionDeUsuario(self):
        pass

class Lote:
    def __init__(self) -> None:
        self.lote = model.Lote()
        self.metodosConexion = connect.Lote()

    def crearLote(self, info):
        if info != None:
            self.lote = info
            self.metodosConexion.setLote(self.lote)

    def consultarLote(self,id):
        resultado = self.metodosConexion.getLote(id)
        if resultado:
            self.lote = resultado
            return self.lote
        return resultado
    
    def reiniciarValores(self):
        self.metodosConexion.setValoresVacunasDefault()

class PlanDeVacunacion:
    def __init__(self) -> None:
        self.plan = model.PlanDeVacunacion()
        self.metodosConexion = connect.PlanDeVacunacion()

    def crearPlanVacunacion(self, info):
        if info != None:
            self.plan = info
            self.metodosConexion.setPlan(self.plan)

    def consultarPlanVacunacion(self,id):
        resultado = self.metodosConexion.getPlan(id)
        if resultado:
            self.plan = resultado
            return self.plan
        return resultado
    
    def consultarRangoEdades(self):
        rangoEdades = self.metodosConexion.getRangoEdades()
        return rangoEdades
    
    def verificarEdad(self, edad):
        rangoEdades = self.consultarRangoEdades()
        flag = True
        message = ''
        for rango in rangoEdades:
            if rango[0] <= edad <= rango[1]:
                flag = False
                message = 'La edad seleccionada se encuentra dentro de otro rango'
                break
        return (flag, message)

def crearTablas():
    connect.crearTablas()

# Función para abrir documentación de usuario
def documentacionUsuario():
    # Se almacena un link correspondiente a la ubicación del pdf
    path = 'https://drive.google.com/file/d/1L8BBeJP-mc_QLmNplzYemZgxe4j1F_Bx/view?usp=sharing'
    # Abrimos el archivo en el navegador siguiendo la variable (path) por el método webbrowser.open_new() de la librería webbrowser
    webbrowser.open_new(path)
