class Person:
  def __init__(self, name, age): #method
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()