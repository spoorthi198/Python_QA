import smtplib
from email.message import EmailMessage


msg=EmailMessage()
msg['Subject'] = 'Training inviation'
msg['From'] = 'spurti email'
msg['To'] = 'rajen16@gmail.com'
msg.set_content('Test Email')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('spurti20oct@gmail.com','123@#456')
server.send_message(msg)
server.quit()
