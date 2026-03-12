class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def tambahKendaraan(head,plat):
    currentNode = head
    while currentNode.next:
        currentNode = currentNode.next
    currentNode.next = plat

def hapusKendaraan(head, plat):
  if head == plat:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != plat:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next
  return head


node1 = Node("B 7 M")
node2 = Node("B 11 Y")
node3 = Node("K 3 Y")
node4 = Node("F 2 P")
node5 = Node("N 9 G")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5 = Node("B 21 M")

traverseAndPrint(node1)
tambahKendaraan(node1,node5)
traverseAndPrint(node1)
node1 = hapusKendaraan(node1, node5)
traverseAndPrint(node1)
