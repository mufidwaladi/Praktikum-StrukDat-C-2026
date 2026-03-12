class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def tampilkan_antrian(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def sispkan_vip(head, newNode, plat_target):
  if plat_target == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(plat_target - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
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

# Insert a new node with value 97 at position 2
newNode = Node("B 88 Q")
node1 = sispkan_vip(node1, newNode, 2)
tampilkan_antrian(node1) 