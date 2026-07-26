import smtplib
from email.message import EmailMessage

def sendMail(emailObj, appPassword):
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(emailObj["From"], appPassword)
    smtp.send_message(emailObj)
    smtp.quit()

def prepareNotification(sender, receiver, subject, body, attachment):
    emailObj = EmailMessage()
    
    emailObj["From"] = sender
    emailObj["To"] = receiver
    emailObj["Subject"] = subject
    emailObj.set_content(body)

    lObj = open(attachment, "r")
    emailObj.add_attachment(lObj.read(), subtype = "plain", filename = attachment)
    lObj.close()

    return emailObj