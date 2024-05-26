
class Paciente:
    def __init__(self, idpaciente, genero, nombre, edad, triaje):
        self.idpaciente = idpaciente
        self.genero = genero
        self.nombre = nombre
        self.edad = edad
        self.triaje= triaje
        self.leftchild = None
        self.rightchild = None

class Heap:
    def __init__(self):
        self.heap = []

 
    def __str__(self):
        info_pacientes = []
        for paciente in self.heap:
            info_pacientes.append(f" id: {paciente.idpaciente}, genero: {paciente.genero}, nombre: {paciente.nombre}, edad: {paciente.edad} , triaje: {paciente.triaje}")
        return '\n'.join(info_pacientes)

    def impresion(self, index=0, prefix="", is_left=True):
        if index < len(self.heap):
            paciente = self.heap[index]
            right_child_index = 2 * index + 2
            left_child_index = 2 * index + 1

            if right_child_index < len(self.heap):
                self.impresion(right_child_index, prefix + ("│    " if is_left else "    "), False)

            print(prefix + ("└── " if is_left else "┌── ") + str(paciente.triaje))

            if left_child_index < len(self.heap):
                self.impresion(left_child_index, prefix + ("     " if is_left else "│   "), True)

    def busqueda(self, nodo, triaje):
        if nodo is None:
            return
        if triaje > nodo.data.triaje:
            if nodo.rightchild:
                return self.busqueda(nodo.rightchild, triaje)
            else:
                return nodo
        else:
            if nodo.leftchild:
                return self.busqueda(nodo.leftchild, triaje)
            else:
                return nodo

    def Registrar(self, nodo):
        self.heap.append(nodo)
        self.reordenar_arriba(len(self.heap) -1)


    def atender_paciente(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.reordenar_arriba(0)
        return root

    def eliminar_paciente(self):
        pass

    def reordenar_arriba(self, nodo_indice): #revisa si el nuevo nodo es menor a su padre para intercambiarlos
        #print("nod", self.heap[nodo_indice].triaje, self.heap[nodo_indice].nombre, nodo_indice)

        padre_indice = (nodo_indice - 1) // 2

        if nodo_indice > 0 and self.heap[nodo_indice].triaje < self.heap[padre_indice].triaje:
            self.heap[nodo_indice], self.heap[padre_indice] = self.heap[padre_indice], self.heap[nodo_indice]
            print("padre", self.heap[padre_indice].triaje, self.heap[padre_indice].nombre, padre_indice)
            self.reordenar_arriba(padre_indice)


    def reordenar_abajo(self, nodo_indice): #reordena el arbol tras eliminar un elemento
        left_child_indice = 2 * nodo_indice + 1
        right_child_indice = 2 * nodo_indice + 2
        menor = nodo_indice

        if left_child_indice < len(self.heap) and self.heap[left_child_indice].triaje < self.heap[menor].triaje:
            menor = left_child_indice

        if right_child_indice < len(self.heap) and self.heap[right_child_indice].triaje < self.heap[menor].triaje:
            menor = right_child_indice

        if menor != nodo_indice:
            self.heap[nodo_indice], self.heap[menor] = self.heap[menor], self.heap[nodo_indice]
            self.reordenar_abajo(menor)


paciente = Paciente(2, "m", "John", 30, 5)
paciente1 = Paciente(3, "f", "Alice", 25, 3)
paciente2 = Paciente(1, "m", "Bob", 40, 2)
paciente3 = Paciente(4, "f", "Eve", 50, 4)
paciente4 = Paciente(5, "f", "Carol", 35, 1)

sala_urgencias = Heap()
sala_urgencias.Registrar(paciente)
sala_urgencias.Registrar(paciente1)
sala_urgencias.Registrar(paciente2)
sala_urgencias.Registrar(paciente3)
sala_urgencias.Registrar(paciente4)

print(sala_urgencias)
sala_urgencias.impresion()


class Node:
  __slots__ = 'value', 'next'

  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class LinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode
      curNode = curNode.next

  def __str__(self):
    result = [str(x.value) for x in self]
    return ' '.join(result)

class queue:

  def __init__(self):
    self.linkedlist = LinkedList()

  def __str__(self):
    result = [str(x.value) for x in self.queue]
    return ' '.join(result)

  def is_empty(self):
    return self.linkedlist.head == None

  def enqueue(self, e):
    new_node = Node(e)
    if self.linkedlist.head == None:
      self.linkedlist.head = new_node
      self.linkedlist.tail = new_node
    else:
      new_node.next = None
      self.linkedlist.tail.next = new_node
      self.linkedlist.tail = new_node

  def dequeue(self):
    if self.is_empty():
      return "No hay elementos en la lista"
    else:
      popped_node = self.linkedlist.head
      if self.linkedlist.head == self.linkedlist.tail:
        self.linkedlist.head = None
        self.linkedlist.tail = None
      else:
        self.linkedlist.head = self.linkedlist.head.next
      popped_node.next = None
      return popped_node

class BSTNode:

  def __init__(self, data):
    self.data = data
    self.leftchild = None
    self.rightchild = None

  def __str__(self, level=0):
    ret = "  " *level + str(self.data) + "\n"

    if self.leftchild:
      ret += self.leftchild.__str__(level+1)

    if self.rightchild:
      ret += self.rightchild.__str__(level+1)

    return ret

def printTree(Node, prefix="", is_left=True):
    if not Node:
        return

    if Node.rightchild:
        printTree(Node.rightchild, prefix + ("│    " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(Node.data))

    if Node.leftchild:
        printTree(Node.leftchild, prefix + ("     " if is_left else "│   "), True)


def preOrderTraversal(rootNode):
  if not rootNode:
    return

  print(rootNode.data)
  preOrderTraversal(rootNode.leftchild)
  preOrderTraversal(rootNode.rightchild)


def inOrderTraversal(rootNode):
  if not rootNode:
    return

  inOrderTraversal(rootNode.leftchild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightchild)

def postOrderTraversal(rootNode):
  if not rootNode:
    return

  postOrderTraversal(rootNode.leftchild)
  postOrderTraversal(rootNode.rightchild)
  print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
      return
    else:
      customqueue = queue()
      customqueue.enqueue(rootNode)

      while not(customqueue.is_empty()):
        current = customqueue.dequeue()
        print(current.value.data)
        if (current.value.leftchild is not None):
          customqueue.enqueue(current.value.leftchild)
        if (current.value.rightchild is not None):
          customqueue.enqueue(current.value.rightchild)


def insertNode(rootNode, value):

  if rootNode.data == None:
    rootNode.data = value
  elif value < rootNode.data:
    if rootNode.leftchild is None:
      rootNode.leftchild = BSTNode(value)
    else:
      insertNode(rootNode.leftchild, value)
  else:
    if rootNode.rightchild is None:
      rootNode.rightchild = BSTNode(value)
    else:
      insertNode(rootNode.rightchild, value)

def searchNode(rootNode, value):
  if rootNode is None:
    return

  if value < rootNode.data:
    print("ingresa izquierda")
    print(rootNode.data)
    if rootNode.leftchild is not None:
      if rootNode.leftchild.data == value:
        return "el nodo con valor {} SI fue encontrado".format(value)
      return searchNode(rootNode.leftchild,value)
    else:
      return "el nodo con valor {} NO fue encontrado".format(value)
  else:
    print("ingresa derecha")
    print(rootNode.data)
    if rootNode.rightchild is not None:
      if rootNode.rightchild.data == value:
        return "el nodo con valor {} SI fue encontrado".format(value)
      return searchNode(rootNode.rightchild,value)
    else:
      return "el nodo con valor {} NO fue encontrado".format(value)



def deleteNode(rootNode, value):
  if rootNode is None:
    return rootNode

  if value < rootNode.data:
    rootNode.leftchild = deleteNode(rootNode.leftchild, value)
  elif value > rootNode.data:
    rootNode.rightchild = deleteNode(rootNode.rightchild, value)
  else:
    #caso 1 no tiene hijos
    if rootNode.leftchild is None and rootNode.rightchild is None:
      return None
    #caso 2 tiene ambos hijos
    elif rootNode.leftchild is not None and rootNode.rightchild is not None:
      tempNode = minsuccesor(rootNode.rightchild)
      tempData = tempNode.data
      deleteNode(rootNode,tempData)
      rootNode.data = tempData
    #caso hijo a la izquierda
    elif rootNode.leftchild is not None:
      return rootNode.leftchild
    #caso hijo a la derecha
    else:
      return rootNode.rightchild

  return rootNode


def minsuccesor(rootNode):
  if rootNode.leftchild is not None:
    return minsuccesor(rootNode.leftchild)

  return rootNode