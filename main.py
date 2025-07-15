7#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
from datetime import datetime

HOST = '0.0.0.0'
PORT = 3333

def gerar_resposta_html(ip_cliente):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f"""\
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<html>
  <head><title>Servidor de aplicação em Python</title></head>
  <body>
    <h1>Bem-vindo ao servidor de aplicação em Python na porta {PORT}!</h1>
    <p><strong>Hora atual:</strong> {agora}</p>
    <p><strong>Seu IP:</strong> {ip_cliente}</p>
  </body>
</html>
"""
    return html

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Servidor rodando em http://localhost:{PORT}")

        while True:
            client, address = server.accept()
            with client:
                ip_cliente = address[0]
                print(f"Conexão recebida de {ip_cliente}")
                request = client.recv(1024).decode()
                print("Requisição:\n", request)
                resposta = gerar_resposta_html(ip_cliente)
                client.sendall(resposta.encode('utf-8'))

if __name__ == "__main__":
    main()
