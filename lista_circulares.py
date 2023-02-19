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
            self.primero = Nodo(receta = receta)
            self.primero.siguiente = self.primero
        else:
            actual = Nodo(receta = receta, siguiente = self.primero.siguiente)
            self.primero.siguiente = actual

    def recorrer(self):
        if self.primero is None:
            return 
        actual = self.primero
        print('Paciente: ', actual.receta.paciente, '- Fecha de nacimiento: ', actual.receta.fecha_nac, '- Doctor: ', actual.receta.doctor, '- Colegiado: ', actual.receta.colegiado, '- Fecha de cita: ', actual.receta.fecha_cita, '- Hora de cita: ', actual.receta.hora_cita, '- Tipo de consulta: ', actual.receta.tipo_consulta, '- Tratamiento: ', actual.receta.tratamiento)
        
        while actual.siguiente != self.primero:
            actual = actual.siguiente
            print('Paciente: ', actual.receta.paciente, '- Fecha de nacimiento: ', actual.receta.fecha_nac, '- Doctor: ', actual.receta.doctor, '- Colegiado: ', actual.receta.colegiado, '- Fecha de cita: ', actual.receta.fecha_cita, '- Hora de cita: ', actual.receta.hora_cita, '- Tipo de consulta: ', actual.receta.tipo_consulta, '- Tratamiento: ', actual.receta.tratamiento)
    
    def eliminar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None
        no_encontrado = False

        while actual and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            anterior = actual
            actual = actual.siguiente

            if actual == self.primero:
                no_encontrado = True
                print('No econtrado')
                break

        if not no_encontrado:
            if anterior is not None:
                    anterior.siguiente = actual.siguiente
                    actual.siguiente = None
            else:
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente
    # Modifica el tratamiento del paciente por uno nuevo
    def modificar(self, paciente, fecha_cita, hora_cita, nuevo_tratamiento):
        actual = self.primero
        no_encontrado = False

        while actual and (actual.receta.paciente != paciente or actual.receta.fecha_cita != fecha_cita or actual.receta.hora_cita != hora_cita):
            actual = actual.siguiente

            if actual == self.primero:
                no_encontrado = True
                break

        if not no_encontrado:
            actual.receta.tratamiento = nuevo_tratamiento






#Creacion de objetos Receta
r1 = Receta('Gerson Lopez', '03/10/1990', 'Melvin Ortiz', 20156, '17/01/2023', '11:30', 'Medicina', '2 pildoras de acetaminofen cada 6 horas')
r2 = Receta('Karen Gómez', '08-05-2000', 'Jorge Merida', 8567, '31-01-20233', '09:00', 'Medicina interna', 'Tylenol de 20 ml cada 4 horas')
r3 = Receta('Luis García', '17-09-1987', 'Melvin Ortiz', 20157, '02-02-2023', '12:00', 'Medicina general', '2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca')

#insercion 
lista_c = lista_circular()
lista_c.insertar(r1)
lista_c.insertar(r2)
lista_c.insertar(r3)

# Recorrer la lista 
lista_c.recorrer()

# Eliminar
#lista_c.eliminar(8567, '31-01-2023','09:00')
lista_c.modificar('Gerson Lopez', '17/01/2023', '11:30', '1 cucharada de Pepto-Bismol cada 6 horas')
lista_c.recorrer()