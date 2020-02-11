import smtplib
from email.message import EmailMessage

email = 'test@email.com'
password = 'password'
msg = EmailMessage()
msg['Subject'] = 'This is the subject'
msg['From'] = email
msg['To'] = 'email@google.com'
msg.set_content('Write your email content here.')

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.ehlo()
connection.starttls()
connection.login(email, password)
connection.send_message(msg)
connection.quit()