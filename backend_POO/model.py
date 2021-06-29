class Persona:
    def __init__(self) -> None:
        self.__noId = None
        self.__nombre = None
        self.__apellido = None
        self.__direccion = None
        self.__telefono = None
        self.__correo = None
        self.__ciudad = None
        self.__fechaNacimiento = None
        self.__fechaAfiliacion = None
        self.__vacunado = None
        self.__fechaDesafiliacion = None
    
    @property
    def noId(self):
        return self.__noId
    @noId.setter
    def noId(self, noId):
        self.__noId = noId
    @noId.deleter
    def noId(self): 
        del self.__noId
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @nombre.deleter
    def nombre(self): 
        del self.__nombre
    
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    @apellido.deleter
    def apellido(self): 
        del self.__apellido
    
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion
    @direccion.deleter
    def direccion(self): 
        del self.__direccion
    
    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono
    @telefono.deleter
    def telefono(self): 
        del self.__telefono
    
    @property
    def correo(self):
        return self.__correo
    @correo.setter
    def correo(self, correo):
        self.__correo = correo
    @correo.deleter
    def correo(self): 
        del self.__correo
    
    @property
    def ciudad(self):
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, ciudad):
        self.__ciudad = ciudad
    @ciudad.deleter
    def ciudad(self): 
        del self.__ciudad
    
    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento):
        self.__fechaNacimiento = fechaNacimiento
    @fechaNacimiento.deleter
    def fechaNacimiento(self): 
        del self.__fechaNacimiento
    
    @property
    def fechaAfiliacion(self):
        return self.__fechaAfiliacion
    @fechaAfiliacion.setter
    def fechaAfiliacion(self, fechaAfiliacion):
        self.__fechaAfiliacion = fechaAfiliacion
    @fechaAfiliacion.deleter
    def fechaAfiliacion(self): 
        del self.__fechaAfiliacion
    
    @property
    def vacunado(self):
        return self.__vacunado
    @vacunado.setter
    def vacunado(self, vacunado):
        self.__vacunado = vacunado
    @vacunado.deleter
    def vacunado(self): 
        del self.__vacunado
    
    @property
    def fechaDesafiliacion(self):
        return self.__fechaDesafiliacion
    @fechaDesafiliacion.setter
    def fechaDesafiliacion(self, fechaDesafiliacion):
        self.__fechaDesafiliacion = fechaDesafiliacion
    @fechaDesafiliacion.deleter
    def fechaDesafiliacion(self): 
        del self.__peso
        
class Lote:
    def __init__(self) -> None:
        self.noLote = None
        self.fabricante = None
        self.tipoVacuna = None
        self.cantidadRecibida = None
        self.cantidadAsignada = None
        self.cantidadUsada = None
        self.dosisNecesaria = None
        self.temperatura = None
        self.efectividad = None
        self.tiempoProteccion = None
        self.fechaVencimiento = None
        self.imagen = None
        
class PlanDeVacunacion:
    def __init__(self) -> None:
        self.idPlan = None
        self.edadMinima = None
        self.edadMaxima = None
        self.fechaInicio = None
        self.fechaFinal = None
        
class ProgramacionDeVacunas:
    def __init__(self) -> None:
        self.idCita = None
        self.noId = None
        self.noLote = None
        self.idPlan = None
        self.ciudadVacunacion = None
        self.fechaProgramada = None
        self.horaProgramada = None  