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

class lista_circular:
    def __init__(self):
        self.primero = None

def insertar(self, receta):
    if self.primero is None:
        self.primer = Nodo(receta = receta)
        self.primero.siguiente = self.primero
    else:
        actual = Nodo(receta = receta, siguiente = self.primero.siguiente)
        self.primero.siguiente = actual

#Creacion de objetos Receta
r1 = Receta('Gerson Lopez', '03/10/1990', 'Melvin Ortiz', 20156, '17/01/2023', '11:30', 'Medicina', '2 pildoras de acetaminofen cada 6 horas')
r2 = Receta('Karen Gómez', '08-05-2000', 'Jorge Merida', 8567, '31-01-20233', '09:00', 'Medicina interna', 'Tylenol de 20 ml cada 4 horas')
r3 = Receta('Luis García', '17-09-1987', 'Melvin Ortiz', 20156, '02-02-2023', '12:00', 'Medicina general', '2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca')

#insercion 
lista_enlazada = lista_circular()
lista_enlazada.insertar(r1)
lista_enlazada.insertar(r2)
lista_enlazada.insertar(r3)