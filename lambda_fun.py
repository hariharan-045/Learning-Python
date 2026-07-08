

# lambda build function


def get_odd_numbers(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(get_odd_numbers(numbers))

#basic lambda
x = lambda n: n*2
print(x(3))

#two argument

x = lambda n, b : n * b 

print(x(2,5))



# function used lambda 

def fun(n:int):
    return lambda l: l * n
aa = fun(2)
print(aa(3)) 

#ex 2

def fun(n):
    return lambda l:l+n

vari = fun(5)
print(vari(5))

# fun(n) not nessary to mention but newly create a ex : l its mention in frent of lambda l : 
#   the the n is a this is a argument fun(n) first value pass panna athu neara n ku tha pogum  

