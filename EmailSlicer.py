
# get user email address
UserEmail = input("Please enter your email address: ").strip()


#slice out user name
UserName  = UserEmail[0:UserEmail.index("@")]
#print(UserName)

#slice domain name
DomainName = UserEmail[(UserEmail.index("@")+1):]
#print(DomainName)

#format message
string = "Your username is {} and your domain is {}"
output = string.format(UserName, DomainName)
#display output message
print(output)
