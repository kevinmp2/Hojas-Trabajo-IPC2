# Clase receta 
class Receta: 
    def __init__(self, paciente, fecha_nac, doctor, colegiado, fecha_cita, hora_cita, tipo_consulta, tratamiento):
        self.paciente = paciente
        self.fecha_nac = fecha_nac
        self.doctor = doctor 
        self.colegiado = colegiado
        self.fecha_cita = fecha_cita
        self.hora_cita = hora_cita
        self.tipo_consulta = tipo_consulta
        self.tratamiento = tratamiento

# Definicion clase nodo 
class Nodo:
    def __init__(self, receta = None , siguiente = None):
        self.receta = receta
        self.siguiente = siguiente

class Lista_enlazada:
    def __init__(self):
        self.primero = None
    
    def insertar(self, receta):
        if self.primero is None:
            self.primero = Nodo(receta = receta)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(receta = receta)

    def recorrer(self):
        actual = self.primero

        while actual != None:
            print('Paciente: ', actual.receta.paciente, '- Fecha de nacimiento: ', actual.receta.fecha_nac, '- Doctor: ', actual.receta.doctor, '- Colegiado: ', actual.receta.colegiado, '- Fecha de cita: ', actual.receta.fecha_cita, '- Hora de cita: ', actual.receta.hora_cita, '- Tipo de consulta: ', actual.receta.tipo_consulta, '- Tratamiento: ', actual.receta.tratamiento)
            actual = actual.siguiente

    def eliminar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None

        while actual and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            anterior = actual
            actual = actual.siguiente

        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None 
    # Busca por paciente y modifica los parametros ingresados
    def buscar_modificar(self, paciente, fecha_cita, hora_cita):
        actual = self.primero

        while actual != None:
            if actual.receta.paciente == paciente:
                actual.receta.fecha_cita = fecha_cita
                actual.receta.hora_cita = hora_cita
                return None
            actual = actual.siguiente

#Creacion de objetos Receta
r1 = Receta('Gerson Lopez', '03/10/1990', 'Melvin Ortiz', 20156, '17/01/2023', '11:30', 'Medicina', '2 pildoras de acetaminofen cada 6 horas')
r2 = Receta('Karen Gómez', '08-05-2000', 'Jorge Merida', 8567, '31-01-20233', '09:00', 'Medicina interna', 'Tylenol de 20 ml cada 4 horas')
r3 = Receta('Luis García', '17-09-1987', 'Melvin Ortiz', 20156, '02-02-2023', '12:00', 'Medicina general', '2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca')
#insercion 
lista_enlazada = Lista_enlazada()
lista_enlazada.insertar(r1)
lista_enlazada.insertar(r2)
lista_enlazada.insertar(r3)

#recorrer
lista_enlazada.recorrer()
lista_enlazada.eliminar(20156,'17/01/2023','11:30')
lista_enlazada.recorrer()
# Añade los nuevos parametros ingrasados a la lista
lista_enlazada.buscar_modificar('Gerson Lopez','16/02/2023','22:20')
# Recorre la lista con los datos ya anteriormente modificados
lista_enlazada.recorrer()
    

