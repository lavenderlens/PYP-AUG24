'''a class is a blueprint/template for creating objects
you may choose classes over dictionaries to represnt your data
classes enforce standards applied by all objects of that class'''

class Client:
    def __init__(self):
        self.name= "Client"
        self.email= "no email supplied"
        self.dependents = []
    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, dependents: {self.dependents}"

client1 = Client()

# print(client1) # <__main__.Client object at 0x102bd6950> WITHOUT __str__ override
print(client1) # <__main__.Client object at 0x102bd6950> WITH __str__ override

# note the dot notation is now used to drill down into object props
# NOT square brackets as in dictionaries

print(client1.name)

class ClientWithParams:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.dependents = []

    def add_dependant(self, name):
        # name = input("Enter a dependant name to add:")
        # name = input("Enter a dependant name to add:")
        self.dependents.append(name)
        print(f"{name} added as dependent. No. of dependants is now {len(self.dependents)}")

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, dependents: {self.dependents}"
    
# clientWithParams = ClientWithParams() #TypeError: ClientWithParams.__init__() missing 2 required positional arguments: 'name' and 'email'
# clientWithParams = ClientWithParams("Alan", "alan@me.com", "Sophie", "Susie")
clientWithParams = ClientWithParams("Alan", "alan@me.com")

print(clientWithParams) # when the object reference is passed to print() the object dunder method __str__ is called implicitly

clientWithParams.add_dependant("Margaret")
clientWithParams.add_dependant("Sophie")
clientWithParams.add_dependant("Susie")

print(clientWithParams)

