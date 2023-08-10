# Projeto de Envio Automático de Email por Palavra-chave

Este projeto consiste em um programa Python que utiliza a biblioteca SpeechRecognition para capturar fala do microfone e, caso a fala contenha palavras-chave específicas, envia um email automaticamente. Esse projeto é relacionado a temática de violência contra mulher, uma possivel solução dentro de um aplicativo. 

## Requisitos

- Python 3.x
- Biblioteca SpeechRecognition (`pip install SpeechRecognition`)
- Biblioteca smtplib (incluída na instalação padrão do Python)

## Como Usar

1. Clone ou baixe este repositório para o seu computador.

2. Abra um terminal ou prompt de comando e navegue até o diretório onde o projeto está localizado.

3. Execute o programa principal `main.py`:

4. Escolha uma opção digitando `1` para abrir o microfone ou `2` para sair.

5. Se você escolher a opção `1`, fale algo no microfone. Se o que você falar contiver as palavras-chave ("socorro", "agressão", "ajuda", "pedido"), um email será enviado automaticamente.

6. Certifique-se de fornecer seu endereço de email, senha do aplicativo do Google e endereço de email do destinatário no código do arquivo `main.py` antes de executar.

## Estrutura do Projeto

- `captura_fala.py`: Contém a função para capturar a fala do microfone utilizando a biblioteca SpeechRecognition.

- `enviar_email.py`: Contém a função para enviar emails utilizando a biblioteca smtplib.

- `main.py`: O programa principal que interage com o usuário, captura a fala e envia emails conforme as palavras-chave.

## Considerações

Este projeto é um exemplo simples de como automatizar o envio de emails com base em palavras-chave identificadas na fala capturada pelo microfone. Note que o código pode ser melhorado e expandido para incluir mais funcionalidades, melhor tratamento de erros e segurança.

Lembre-se de que o código inclui informações sensíveis, como a senha do aplicativo do Google. Evite compartilhar ou publicar o código com essas informações sem as devidas precauções de segurança.



