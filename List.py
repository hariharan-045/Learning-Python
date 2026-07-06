list = ['hii','jii','welcome']
num = "haiihari"
print(len(list))
print(len(num))

#append
list = ["santa",'hari']
list.append("pavi")
print(list)

# value add only one element using index
list = ['apple','bannana','watermelon']
list[1]='berrie'
print(list)

#slicing a list . the slicing a use multiple element onsert use and then the index also disaide  
list = ['haii','hari','iamvs','daily']

list[1:3]
list[3:-3]=['noo','see']
print(list)

# insert a element 
list = ['haii','welcome','dii']

list.insert(2,'haiijii')
print(list)

#Extend 
list = ['python','javascript']
list.extend(['Html','CSS'])
print(list)

#Extend list2
list1 = ['python','javascript']
list2 = ['Html','CSS','React']
list1.extend(list2)
print(list)

#add iterable

#iterable used morethen function add them ex(tuple,set,dictionari,list)
list = ['Tamil','English0','Kannada']
tuple = ('malayalam','marathi')

list.extend(tuple)
print(list)

#remove 

list = ["enjoy",'in','bangalore']
list.remove('in')
print(list)

#Pop() =======  this is a stack and queue ===============

list = ['Tamil','English0','Kannada']
list.pop(1)

print(list)

#clear()

list = ['Tamil','English0','Kannada']
list.clear()
print(list)

#del()
list = ['Tamil','English0','Kannada']
del list
print(list)
x=list.index(2)
print(x)

'''
 different between del and clear . del clear total variable and datatype but clear() just clear 
 a list elements only
'''


