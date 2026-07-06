schore = (int(input("Enter a number")))
cash = int(7000)
if schore < cash:
  print("eligible")
  if schore==cash:
    print("also eligible for a scholership")
    if schore <= cash:
       print("!=")
    else:
       print("!= wrong")
  else:
    print("not eligible")
else:
    print("nothing")