import os

email_txt = os.path.join("templates", "email.txt")


content = ""


with open(email_txt, 'r') as f:
    content = f.read()


print(content.format(name='rashed'))    

