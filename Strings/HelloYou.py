# Ask user for email address
email = input(" Enter your email address: ")


# Ask user for reference number
ref = input("Enter reference number: ")


# Ask user for password

password = input("Enter Password: ")
print(email)
print(password)
print(ref)

string = "You have succesfully signed in with the email: {} and the reference number: {} "
output = string.format(email,ref)
# Print output to screen
print(output)
