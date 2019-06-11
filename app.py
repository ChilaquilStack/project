from pacientes.app import Pacientes
pacientes = Pacientes()

pacientes.push('Jose')
pacientes.push('Pedro')
print(pacientes.show())
pacientes.pop()
pacientes.pop()
print(pacientes.show())
pacientes.push('David Morales')
print(pacientes.show())