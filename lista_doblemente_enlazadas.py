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

class Nodo:
    def __init__(self, receta = None, siguiente = None, anterior = None):
        self.receta = receta
        self.siguiente = siguiente
        self.anterior = anterior 

class Lista_Doble:
    def __init__(self):
        self.primero = None

    def insertar(self, receta):
        if self.primero is None:
            self.primero = Nodo(receta = receta)
        else:
            actual = Nodo(receta = receta, siguiente = self.primero)
            self.primero.anterior = actual
            self.primero = actual

    def recorrer(self):
        if self.primero is None:
            return
        actual = self.primero
        print('Paciente: ', actual.receta.paciente, '- Fecha de nacimiento: ', actual.receta.fecha_nac, '- Doctor: ', actual.receta.doctor, '- Colegiado: ', actual.receta.colegiado, '- Fecha de cita: ', actual.receta.fecha_cita, '- Hora de cita: ', actual.receta.hora_cita, '- Tipo de consulta: ', actual.receta.tipo_consulta, '- Tratamiento: ', actual.receta.tratamiento)
        
        while actual.siguiente:
            actual = actual.siguiente
            print('Paciente: ', actual.receta.paciente, '- Fecha de nacimiento: ', actual.receta.fecha_nac, '- Doctor: ', actual.receta.doctor, '- Colegiado: ', actual.receta.colegiado, '- Fecha de cita: ', actual.receta.fecha_cita, '- Hora de cita: ', actual.receta.hora_cita, '- Tipo de consulta: ', actual.receta.tipo_consulta, '- Tratamiento: ', actual.receta.tratamiento)

    def eliminar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        while actual:
            if actual.receta.colegiado == colegiado and actual.receta.fecha_cita == fecha_cita and actual.receta.hora_cita == hora_cita:
                if actual.anterior:
                    if actual.siguiente:
                        actual.anterior.siguiente = actual.siguiente
                        actual.siguiente.anterior = actual.anterior
                    else:
                        actual.anterior.siguiente = None
                        actual.anterior = None
                else:
                    if actual.siguiente:
                        self.primero = actual.siguiente
                        actual.siguiente.anterior = None       
                    else:
                        self.primero = None
                return True
            else:
                actual = actual.siguiente
        return False

    

#Creacion de objetos Receta
r1 = Receta('Gerson Lopez', '03/10/1990', 'Melvin Ortiz', 20156, '17/01/2023', '11:30', 'Medicina', '2 pildoras de acetaminofen cada 6 horas')
r2 = Receta('Karen Gómez', '08-05-2000', 'Jorge Merida', 8567, '31-01-2023', '09:00', 'Medicina interna', 'Tylenol de 20 ml cada 4 horas')
r3 = Receta('Luis García', '17-09-1987', 'Melvin Ortiz', 20157, '02-02-2023', '12:00', 'Medicina general', '2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca')

#insercion 
lista_d = Lista_Doble()
lista_d.insertar(r1)
lista_d.insertar(r2)
lista_d.insertar(r3)

#recorrer
lista_d.recorrer()
#Eliminar un nodo del medio
lista_d.eliminar(8567, '31-01-2023', '09:00')
lista_d.recorrer()
#Eliminar el primer nodo
lista_d.eliminar(20157, '02-02-2023', '12:00')
lista_d.recorrer()
#Eliminar el ultimo nodo
lista_d.eliminar(20156, '17/01/2023', '11:30')
lista_d.recorrer()

print('lista vacia')
lista_d.recorrer()