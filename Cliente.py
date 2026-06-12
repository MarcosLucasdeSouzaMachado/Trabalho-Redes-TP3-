from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

# Informações básicas Cliente.
NomeJogador = input('Digite o nome do jogador: ')
clientSocket.send(NomeJogador.encode())
NivelJogador = input('Digite o nivel do jogador: ')
clientSocket.send(NivelJogador.encode())
print('jogos: ')
print('--- Valorant, LOL, CS, FIFA, Minecraft ---')
JogoDesejado = input('Deseja jogar qual jogo?: ')
clientSocket.send(JogoDesejado.encode())

MSG = clientSocket.recv(1024)
print("Resposta do jogo: ", MSG.decode())

modifiedSentence = clientSocket.recv(1024)
print ('Resposta do servidor:', modifiedSentence.decode())
clientSocket.close()