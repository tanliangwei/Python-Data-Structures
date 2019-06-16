# A Python program to demonstrate inheritance 

class Button(object):
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   html = "<img></img>"

class Input(Button):
   html = "<input></input>"

class Flash(Button):
   html = "<obj></obj>"

class ButtonFactory():
   def create_button(self, typ):
      targetclass = typ.capitalize()
      # print(targetclass)
      print(globals()[targetclass])
      return globals()[targetclass]()

button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
   print (button_obj.create_button(b).get_html())

# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)" 
# example python clas
# class Base(object): 
	
# 	# Constructor 
# 	def __init__(self, name): 
# 		self.name = name 

# 	# To get name 
# 	def getName(self): 
# 		return self.name 


# # Inherited or Sub class (Note Person in bracket) 
# class Child(Base): 
	
# 	# Constructor 
# 	def __init__(self, name, age): 
# 		Base.__init__(self, name) 
# 		self.age = age 

# 	# To get name 
# 	def getAge(self): 
# 		return self.age 

# # Inherited or Sub class (Note Person in bracket) 
# class GrandChild(Child): 
	
# 	# Constructor 
# 	def __init__(self, name, age, address): 
# 		Child.__init__(self, name, age) 
# 		self.address = address 

# 	def getAge(self):
# 		print(super)
# 		return super().getAge()
# 	# To get address 
# 	def getAddress(self): 
# 		return self.address


# # Driver code 
# g = GrandChild("Geek1", 23, "Noida") 
# print(g.getName(), g.getAge(), g.getAddress()) 
