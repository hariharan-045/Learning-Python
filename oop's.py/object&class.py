class goa:
    name = "" 
    drink = ""
    def party(self):
        return "enjoyy the party...."

    def beach (self):
        return "enjoy the beach...."
    
ramesh = goa()
suresh = goa()

ramesh.name ="ramesh"
suresh.name ="suresh"
ramesh.drink = "yes"
suresh.drink = "Noo"

print(ramesh.name)
print(suresh.name)
print(ramesh.drink)
print(suresh.drink)

print(ramesh.party())
print(suresh.beach())

print()
# another way
print("**another way to print the function**")

print()
class goa:
    name = "" 
    drink = ""
    def party(self):
        print("enjoyy the party....")

    def beach (self):
        print("enjoy the beach....")
    
ramesh = goa()
suresh = goa()

ramesh.party()
suresh.beach()





