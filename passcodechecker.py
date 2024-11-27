x=input("Enter your passcode:")
y=len(x)
if x=="access@001":
	print("Correct! Now you can access your Files")
elif y<=8:
	print("insufficient characters") 
else:
	print("Invalid passcode")
    