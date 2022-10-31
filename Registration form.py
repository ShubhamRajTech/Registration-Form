rf = open(input("Enter file name with .txt:"), "w")

name = input("Enter your full name:")
gender = input("Enter your gender:")
age = input("Enter your age:")
phone = input("Enter your phone number:")
email = input("Enter your email:")
city = input("Enter your city:")
state = input("Enter your state:")

rf.write("NAME = "+ name+ "\n")
rf.write("GENDER = "+ gender+ "\n")
rf.write("AGE = "+ age+ "\n")
rf.write("PHONE NO. = "+ phone+ "\n")
rf.write("EMAIL = "+ email+ "\n")
rf.write("CITY = "+ city+ "\n")
rf.write("STATE = "+ state+ "\n")

print("DONE!!")

rf.close()