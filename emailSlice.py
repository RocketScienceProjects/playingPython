#get user email
email = input("What is your email address?: ").strip()

#slice the username
username = email[:email.index("@")]

#fish out the domain
domain = email[email.index("@") + 1:]

#format msg
output = "Your username is {} and your domain name is {}".format(username, domain)

#spit out
print(output)
