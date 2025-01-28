#Write a program to separate email id and domain name from the email address. Take email address as input from the user and create a tuple.Return email id and domain name as separate elements of the tuple.
email ={}
email['email'] = input("Enter the email address: ")
email_id = email['email'].split('@')[0]
domain_name = email['email'].split('@')[1]
print((email_id,"    ",domain_name))