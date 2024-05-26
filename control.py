
class priorityqueue:
    def __init__(self):
        self.heap = []

    def __str__(self):
        patient_info = []
        for patient in self.heap:
            patient_info.append(f"Nombre: {patient.nombre}, Triaje: {patient.triaje}")
        return '\n'.join(patient_info)

    def is_empty(self):
        return len(self.heap) == 0

    def insertar(self, nuevo_paciente):
        self.heap.append(nuevo_paciente)

    def eliminar(self):
        if self.is_empty():
            return None
        else:
            maxprioridad = self.heap[0]
            for paciente in self.heap[1:]:
                if paciente.triaje < maxprioridad.triaje:
                    maxprioridad = paciente

            self.heap.remove(maxprioridad)
            return self.heap

    def atender_paciente(self):
        if self.is_empty():
            return None
        else:
            maxprioridad = self.heap[0]
            for paciente in self.heap[1:]:
                if paciente.triaje < maxprioridad.triaje:
                    maxprioridad = paciente

            return maxprioridad

    def len(self):
        return len(self.heap)






