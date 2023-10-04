import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

# Intialize an email message
email = EmailMessage()

# Format email with name, subject, recipient, and message
html = Template(Path('index.html').read_text())
email['from'] =  # Insert name here
email['to'] =  # Insert email here (Not included for privacy reasons)
email['subject'] = 'You won $1,000!'
email.set_content(html.substitute({'name': insert name here), 'html')

# Connect to google email, run encryption, login to sender email, and send msg
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
smtp.starttls()
smtp.login(  # Insert 'email' and 'password here (Not included for privacy reasons))
    smtp.send_message(email)
print('Message Sent')
