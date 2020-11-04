import imaplib
import email


host = 'imap.gmail.com'
username = 'lelinbabu784@gmail.com'
password = 'rashed$043134'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")


_, search_data = mail.search(None, 'UNSEEN')

# print(search_data)

for num in search_data[0].split():
    # print(num)
    _, data = mail.fetch(num, '(RFC822)')
    # print(data[0])
    _, b = data[0]
    email_message = email.message_from_bytes(b)
    print(email_message)

