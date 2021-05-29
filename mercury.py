import smtplib, ssl
from email.message import EmailMessage

def ReportError(error):
  adminmail = "quirinustech@gmail.com"
  send_mail(adminmail, "Error Report - MHI Tool", error)

def send_mail(receiver,subject,message):
  
  """
    sends an email using python smtp/ssl protocols
  """

  msg = EmailMessage()
  msg.set_content(message)
  msg['Subject'] = subject
  msg['From'] = "quirinus.mercury.service@gmail.com"
  msg['To'] = receiver


  sender = 'quirinus.mercury.service@gmail.com'
  password = "clsjplavcjcxdiwa"

  # Send the message via our own SMTP server.
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login(sender, password)
  server.send_message(msg)
  server.quit()


