import sys,os

from pacientes.app import Pacientes
patients = Pacientes()

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
        name = input("Ingresa el nombre del paciente: ")
        patients.push(name.lower())

    def showPatient(self):
        pacientes = patients.show()
        if(len(pacientes) != 0):
            for index in range(len(pacientes)):
                print('{} - {}'.format(index + 1, pacientes[index]).title())
        else:
            print("No hay pacientes en la base de datos")

    def delPatient(self):
        if(patients.isEmpty()):
            print("No hay pacientes en la base de datos")
        else:
            index = int(input("Ingresa el numero de paciente a eliminar: "))
            patient = patients.delete(index - 1)
            if(patient):
                print('Se elimini {}'.format(patient))
            else:
                print('El paciente no existe')

    def quit(self):
        os.system("clear")
        print("Hasta Pronto")
        sys.exit(0)

if __name__ == "__main__":
    menuPatient().runMenu()