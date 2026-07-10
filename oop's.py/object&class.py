class goa:
    name = "" 
    drink = ""
    def party(self):
        print("enjoyy the party....")

    def beach (self):
        print("enjoy the beach....")
    
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

ramesh.party()
suresh.beach()