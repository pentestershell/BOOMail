import smtplib, ssl

# Configuración
smtp_server = "smtp.office365.com"
port = 587  # Usar 465 para SSL
sender_alias = "El nombre que quieres que se vea en el envio"
sender_email = "tucorreo@outlook.com"
receiver_email = "elcorreo@quevaarecibir.com"
password = "la pass de remitente"
tu_nombre = "nombre personalizado"  # Tu nombre personalizado

# Mensaje
subject = "Asunto del envio"
body = f"Cuerpo del correo."
message = f"From: {sender_alias} <{sender_email}>\nSubject: {subject}\n\n{body}"

# Conexión segura al servidor
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)

    # Envío del correo
    server.sendmail(sender_email, receiver_email, message)
