'''
def evenorodd():

    a = (int(input("enter a intege :")))
    if a%2 == 0:
        print("even")
    else:
        print("odd")

evenorodd()

def inputpassorfail(a,b):
    if a <= b:
        print("pass")
    else:
        print("fail")

x = int(input("Enter a pass mark :"))
y = int(input("Enter obitiant mark :"))

inputpassorfail(x,y)


def printrange(a,b):

    for i in range(a,b+1):
        print(i)

x = int(input("Enter range :"))
y = int(input("Enter end range"))

printrange(x,y)


j=0
def workreturn(j):
    for i in range(1,5+1):
            j+=i
    return j
    
print(workreturn())        
print(j)


Ri_USERNAME = 'hari'
Ri_PASSWORD = '12345'

Ussername = input("Enter user name :")
Password = input("Enter password :")

def curractpassword(): 
    if (Ri_USERNAME==Ussername and Ri_PASSWORD==Password):
        return True
    else:
        return False
a=curractpassword()
print(a)

# LIST FUNCTION
# if you create global variable (out side of function) you will can't modified . but youcan check it 


def listfun(listsorg):
    copy1 = ""
    for lists in range (len(listsorg)):
        copy1 += (listsorg[lists])
    return copy1
    
a = ['hari','logu','pavi','sumathu']
print(listfun(a))

def dicfun(value):
        dic = {"name":'hari','age' : 23}
        return dic[value]
print(dicfun('name'))

def returnall(myfun,myvalue):
    return myfun[myvalue]
result = returnall(['jii','bii','nii'],2) 
print(result)

def multipleargument(tup):
     print("typeof",type(tup))
     print("index 1",tup[1])
     print("index 2",tup[2])
     print(tup)
tup=("1","2","3","4") 
multipleargument(tup)

#*args, **kwargs == kye word argument

def argkwargs(*args, **kwargs):

    sum =[]
    for value in kwargs.values():
        sum.append(value)
    print(sum)

    sum2 = 0
    for value in args:
        sum2 +=value
    print(sum2)

argkwargs(1,2,3,3, name = 2 , age = 12)
'''

#decorater 

def login(fun):

    def decorater():
        print("start loading....")
        fun()
        print("end loading....")
    return decorater
@login
def add(num1 ,num2):
   num1 = input("enter1") 
   num2 = input("enter2")
   print(num1+num2)
add()