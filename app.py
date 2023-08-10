import speech_recognition as sr
import smtplib
import email.message

def abrir_microfone():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Por favor, fale alguma coisa!!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse: " + texto)
        return texto
    except sr.UnknownValueError:
        print("Não foi possível reconhecer a fala.")
    except sr.RequestError as e:
        print("Erro ao conectar-se ao serviço de reconhecimento de fala: {0}".format(e))

    return None

def enviar_email():
    corpo_email = """
    <p>Prezados, </p>
    <p>Socorro! Alguma coisa está errada.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Socorro!"
    msg['From'] = "seu_email@gmail.com"
    msg['To'] = "destinatario@gmail.com"
    password = "sua_senha_de_app_do_google"  # senha do email do remetente gerada pelo Google
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    try:
        s = smtplib.SMTP('smtp.gmail.com:587')
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        print('Email enviado')
    except smtplib.SMTPAuthenticationError:
        print('Erro de autenticação. Verifique suas credenciais.')
    except smtplib.SMTPException as e:
        print('Erro ao enviar o email: {0}'.format(e))
    finally:
        s.quit()

def main():
    while True:
        opcao = input("Escolha uma opção:\n1. Abrir microfone\n2. Sair\n")

        if opcao == "1":
            texto_falado = abrir_microfone()
            if texto_falado:
                print("Texto falado: " + texto_falado)
                if any(keyword in texto_falado.lower() for keyword in ["socorro", "agressão", "ajuda", "pedido"]):
                    enviar_email()
            else:
                print("Não foi possível reconhecer a fala.")
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
