import sys,os

from pacientes.app import Pacientes
patientName = Pacientes()

"""
    *** Menu principal ***
    Crear:
    Mostrar:
    Buscar:
    Eliminar:
"""
class menuPatient():
    def __init__(self):
        self.choices = {
            "1": self.addPatient,
            "2": self.showPatient,
            "3": self.delPatient,
            "4": self.quit
        }
    
    def displayMenu(self):
        print("""
        \tWillies Consultancy\n\n
        1) Agregar un paciente.
        2) Mostrar pacientes.
        3) Eliminar paciente.
        4) Salir.
        """)
    
    def runMenu(self):
        while True:
            self.displayMenu()
            choice = input("Ingresa una opcion: ")
            selected = self.choices.get(choice)
            if (selected):
                selected()
            else:
                if(choice=="exit"):
                    os.system("clear")
                    print("Hasta Pronto")
                    sys.exit(0)
                print("Opcion {0} invalida".format(choice))

    def addPatient(self):
        self.patientName = input("Ingresa el nombre del paciente: ")
        patientName.push(self.patientName)

    def showPatient(self):
        patients = patientName.show()
        if(len(patients) != 0):
            for index in range(len(patients)):
                print('{} - {}'.format(index + 1, patients[index]))
        else:
            print("No hay pacientes en la base de datos")

    def delPatient(self):
        if(len(patientName.show()) != 0):
            self.delpatient = input("Ingresa el nombre del paciente a eliminar: ")
            if(len(self.delpatient) ==  None):
                menuPatient().delPatient()
            if(self.delpatient in patientName.show()):
                self.index = patientName.show().index(self.delpatient)
                patientName.delete(self.index)
            else:
                print("El paciente no existe")
                menuPatient().delPatient()
        elif(len(patientName.show()) == 0):
            print("No hay pacientes en la base de datos")

    def quit(self):
        os.system("clear")
        print("Hasta Pronto")
        sys.exit(0)

if __name__ == "__main__":
    menuPatient().runMenu()