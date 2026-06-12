from socket import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('O servidor esta pronto esperando mensagens')

#Listas
Valorant = []
LOL = []
CS = []
FIFA = []
Minecraft = []

#preenchimento
while True:
	connectionSocket, addr = serverSocket.accept()
	Nome = connectionSocket.recv(1024).decode()
	print("Nome do Jogador: ", Nome)
	Nivel = connectionSocket.recv(1024).decode()
	print("Nivel do Jogador: ", Nivel)
	Jogo = connectionSocket.recv(1024).decode()
	print("Jogo do Jogador: ", Jogo)

	#separação
	if Jogo == 'Valorant':
		Valorant.append(Nome)
		MSG = 'Na lista de espera'
		connectionSocket.send(MSG.encode())
	elif Jogo == 'LOL':
		LOL.append(Nome)
		MSG = 'Na lista de espera'
		connectionSocket.send(MSG.encode())
	elif Jogo == 'CS':
		CS.append(Nome)
		MSG = 'Na lista de espera'
		connectionSocket.send(MSG.encode())
	elif Jogo == 'FIFA':
		FIFA.append(Nome)
		MSG = 'Na lista de espera'
		connectionSocket.send(MSG.encode())
	elif Jogo == 'Minecraft':
		Minecraft.append(Nome)
		MSG = 'Na lista de espera'
		connectionSocket.send(MSG.encode())
	else:
		erro = 'Ocorreu um erro no servidor'
		connectionSocket.send(erro.encode())


	connectionSocket.close()


