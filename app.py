from pacientes.app import Pacientes
pacientes = Pacientes()

pacientes.push('Jose')
pacientes.push('Pedro')
pacientes.push('Luis')
print(pacientes.show())
pacientes.pop()
print(pacientes.show())
pacientes.push('Adrian')
print(pacientes.show())
pacientes.delete(1)
print(pacientes.show())
print(pacientes.get(1).value)