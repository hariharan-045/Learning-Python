#valid variables
'''
_hii
_hii_jjj
hii123
HiiJiii
Hii_Jiii
_Hii_32_JII

'''
# invalid variables
'''
$num
num$
12num
num-num

'''


#multiple variable assigin use one value

a = b = c = "pavi"
print(a,end="=>")
print(b,end="=>")
print(c)

#multiple variable declared value using one line 
a ,b ,c = 10 ,20 ,30 
print(a)
print(b)
print(c)

# Globle variable 

x = 10  

def myfun():
    x = 20
    print("my age is",x)  

myfun()  #check global variable insaid value (20)  False check local variable have it print a value (10)

print(x)
print("Global Kye Var:")

# gloable kye 

x = 100 

def myfun():
    global x 
    x = 400
myfun()

print(x)



