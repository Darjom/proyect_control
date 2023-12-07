
#!/usr/bin/python
from email.message import EmailMessage
import smtplib
#!Aqui se envia el correo a el destinatario
#!sin base de datos
#se especifica el remitente y destinatario del email
remitente = "bryancabrera1054@gmail.com"
destinatario = "bryancabrera914@gmail.com"
# se especifica el mensaje que tendra
mensaje = "!Usted no ingreso el Codigo Captcha a tiempo, debe presentar su Justificativo!"
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
#se especifica el titulo de el correo
email["Subject"] = "Aviso!"
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
# el codigo preoporcionado por gmail para el uso de un correo electronico por 3ros programas
smtp.login(remitente, "mvedzkbrsyyoeuhx")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()