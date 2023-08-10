from captura_fala import capturar_fala
from enviar_email import enviar_email

def main():
    while True:
        opcao = input("Escolha uma opção:\n1. Abrir microfone\n2. Sair\n")

        if opcao == "1":
            texto_falado = capturar_fala()
            if texto_falado:
                print("Texto falado: " + texto_falado)
                keywords = ["socorro", "agressão", "ajuda", "pedido"]
                if any(keyword in texto_falado.lower() for keyword in keywords):
                    destinatario = "destinatario@gmail.com"
                    assunto = "Socorro!"
                    corpo = """
                    <p>Prezados, </p>
                    <p>Socorro! Alguma coisa está errada.</p>
                    """
                    enviar_email(destinatario, assunto, corpo)
            else:
                print("Não foi possível reconhecer a fala.")
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
