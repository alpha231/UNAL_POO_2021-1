import model
import connect

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

    # Función para cambiar estado de vacunación de un usuario si cumple con los requisitos
    def vacunacionPacientes(self):
        pass

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
    
def crearTablas():
    connect.crearTablas()