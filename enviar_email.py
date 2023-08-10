import smtplib
import email.message

def enviar_email(destinatario, assunto, corpo):
    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = "seu_email@gmail.com"
    msg['To'] = destinatario
    password = "sua_senha_de_app_do_google"  # senha do email do remetente gerada pelo Google
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo)

    try:
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        print('Email enviado')
    except smtplib.SMTPAuthenticationError:
        print('Erro de autenticação. Verifique suas credenciais.')
    except smtplib.SMTPException as e:
        print('Erro ao enviar o email: {0}'.format(e))
    finally:
        s.quit()
