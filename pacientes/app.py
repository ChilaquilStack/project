from paciente.app import Paciente

class Pacientes(object):
  
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def isEmpty(self):
    return self.length == 0

  def push(self, value):
    paciente = Paciente(value)
    if(self.isEmpty()):
      self.head = paciente
      self.tail = paciente
      self.length += 1
      return paciente
    self.tail.next = paciente
    self.tail = paciente
    self.length += 1

  def pop(self):
    if self.isEmpty():
      return None

    nodeToRemove = self.tail
    
    if self.head == self.tail:
      self.head = None
      self.tail = None
      self.length -= 1
      return nodeToRemove
    
    currentNode = self.head
    while currentNode:
      if currentNode.next == self.tail:
        seconToLastNode = currentNode
        break
      currentNode = currentNode.next
    seconToLastNode.next = None
    self.tail = seconToLastNode
    self.length -= 1

  def get(self, index):
    if index < 0 or index > self.length:
      return None
    
    if self.isEmpty():
      return None
    
    if index == 0:
      return self.head
    
    current = self.head
    iterator = 0

    while iterator < index:
      iterator += 1
      current = current.next
    
    return current

  def delete(self, index):
    if index < 0 or index > self.length - 1:
      return None

    if self.isEmpty():
      return None

    if index == 0:
      nodeToDelete = self.head
      self.head = self.head.next
      self.length += 1
      return nodeToDelete 

    current = self.head
    iterator = 0

    while iterator < index:
      iterator += 1
      previous = current
      current = current.next

    nodeToDelete = current
    previous.next = current.next

  def show(self):
    pacientes = []
    current = self.head
    while current:  
      pacientes.append(current.value)
      current = current.next
    return pacientes