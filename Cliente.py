from socket import *
import Servidor

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Digite uma frase minuscula:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('Resposta do servidor:', modifiedSentence.decode())
clientSocket.close()

# Informações básicas Cliente.
NomeJogador = input('Digite o nome do jogador: ')
NivelJogador = int(input('Digite o nivel do jogador: '))
print('jogos: ')
print('--- Valorant, LOL, CS, FIFA, Minecraft ---')
JogoDesejado = input('Deseja jogar qual jogo?: ')

return NomeJogador, NivelJogador, JogoDesejado

# Resposta ao cliente.