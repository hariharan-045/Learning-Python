# not to use "" the print numbers , "" only used the string 
print(42,33.2,True)
# sep= used the between the string used /OUTPUT = c}d}r 
print("c","d","r",sep="}")
# end= is used new line object create the same function 
    #print("hii", end=" 123",)




# ============== formating string ==============
# the f string is used derictly insaid {} the value or data 
a = 10
name = "hari"
print(f"hii{name} what is your age{a}")

# float formating 
score = 3.34345
print(f"Score: {score:.2f}")

# center formate 
print(f"{'centered':^20}")

# right align 
print(f"{'centered':>20}")

# left align
print(f"{'centered':<20}")

# add comma large number 

print(f"{100000:,}")

# hexa decimal convert 

print(f"{233:#x}")

# ===================================================== format()  and %style

print("my {} is {}".format('age',19))

# tuple index based this format run example first format {0} second format {1} the .formate call values index based 

print("{0} + {1} = {2}".format(2, 3 ,2))


''' mock questions 
nums = [0, 1, 2, 0, 3]
print(sum(bool(x) for x in nums))
print(sum(x > 1 for x in nums))
'''