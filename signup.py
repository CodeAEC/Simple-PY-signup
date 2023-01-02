# Welcome to Sign up program!!
# I am a beginner At python so i made this simple python sign up
# still no fully finished but when i get better i will drop some updates! Thank you
# Discord: ErrorCode#6979 


print("=========== Sign Up ===========")
name = str(input("Your Name: "))
passw = str(input("Your password: "))

print("======= Sign Up Complet =======")
print("Please sign in!")
print("WARNING! if you type wrong password or name the whole program will die.")

name_check = str(input("Name: "))
passw_check = str(input("Password: "))

if name_check == name and passw_check == passw:
	input("Worked!")
elif name_check != name and passw_check != passw:
	print("Wrong Name!")
	input("Please try again (You have to restart the whole program)")
