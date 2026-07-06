
'''
nested if insaid used a other type of if statement and this (ex: elif , if , if else )
'''
age = int(input("ENTER YOUR AGE :"))

if age >= 21:
    print("You are eligible for loan")
    aadhar = input("Do you have Aadhar? (yes/no): ")

    if aadhar.lower() == 'yes':
        print("You're eligible for loan")
        property1 = str(input("gold/land :"))
        if property1 == 'land': 
            print("you are eligible for land loan")
        elif True:
            print("ok gold") if property1 == 'gold' else print("are you not eligible for loan besouse you no have property")
            loanprice = int(input("enter how much you want : "))  
            gold = int(input("how many pownes gold :"))
        
            print("you are eligible for a gold loan") if loanprice <= (gold * 104000) else print("you are not eligible this loan")
    else:
        print("Sorry, I cannot give you a loan because Aadhar is required.")
else:
    print("You are not eligible because age is below 21")