import socket  # importa o módulo socket 
import ipaddress  # importa o módulo ipaddress 
import sys  # importa o módulo sys 
from datetime import datetime  # importa o módulo datetime 
#-------------------------------------------------------------
def start_port_scan(): #função para iniciar o scan
    print("""    |+++++++++++++++++++++++++++++++++++++++++++|
    |   ░░█▀█░█▀█░█▀▄░▀█▀░░░█▀▀░█▀▀░█▀█░█▀█░░   |
    |   ░░█▀▀░█░█░█▀▄░░█░░░░▀▀█░█░░░█▀█░█░█░░   |
    |   ░░▀░░░▀▀▀░▀░▀░░▀░░░░▀▀▀░▀▀▀░▀░▀░▀░▀░░   |
    |++++++++++| Este é o Port Scan |+++++++++++|
    """)  # imprime uma mensagem de boas vindas
    print ("               Bem vindo ao NET Probe\n")  # Printa uma mensagem de bem vindo
    dns = input("insira o IP/Nome do host/site desejado: ")  # recebe o IP do host
    host_informado = socket.gethostbyname(dns)
    try:                                                                                          
        host = ipaddress.ip_network(host_informado, strict=False)  # converte o IP do host para um objeto ipaddress.ip_network
    except:
        print('\033[1;41m[!] IP Inválida!\033[m')  # imprime uma mensagem de erro
        sys.exit()  # sai do programa

    opcao = input("\nDigite [1] para escolher a porta de scan\nDigite [2] para fazer scan com a lista automatica\nAqui -->: ")  # recebe a opção do usuário

    t1 = datetime.now() #guarda tempo atual

    if opcao == "1":  # se a opção for 1
        porta_input = input("\nDigite as portas que deseja scanear (ex.: 8080, 80, 443) - Aqui -->: ")  # recebe as portas que o usuário deseja scanear
        
        print ("\n")
        print ("-" * 50)  # imprime uma linha de separação
        print (f"[*] Escaneado o Host {host_informado}")  # imprime uma mensagem de escaneamento
        print ("-" * 50, "\n")  # imprime uma linha de separação
        
        porta_op = [int(p) for p in porta_input.split(',')]  # converte as portas para uma lista de inteiros
        for port in porta_op:  # para cada porta na lista de portas
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria um socket
            s.settimeout(1.0)  # define um tempo limite para a conexão
            codigo = s.connect_ex((str(host_informado), port))  # tenta conectar ao host na porta
            s.close()  # fecha o socket
            if codigo == 0: # se a conexao for igual a 0     
                try:
                    servico = socket.getservbyport(port) #pega o nome do serviçop pelo numero da porta
                    print(f"\033[1;32mPorta {port} = {servico} - aberta\033[m") #imprime a porta e o nome do serviço
                except:
                    print(f"\033[1;32mPorta {port} = Serviço desconhecido - aberta\033[m") #imprime a porta e o nome do serviço
            else:
                print(f"\033[1;31mPorta {port} fechada\033[m") #imprime a porta fechada

    elif opcao == "2":  # se a opção for 2
        opcao = int(input("\nEscolha qual opcao deseja:\n1 = todas as 65535 portas (pode lvar horas)\n2 = as mais primeiras 1024 mais usadas\n3 = As portas mais usadas em serviços web\nAqui -->: "))  # recebe a opção do usuário
        
        match opcao:  # verifica a opção do usuário
            case 1:    
                portas = range(1, 65535) # Opcao para escanear todas as portas     
            case 2:
                portas = range(1, 1024) # Opcao para escanear as primeiras 1024 portas
            case 3:
                portas = (21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 989, 990, 993, 995, 3306, 3389, 5432, 8080)  # Opcao para escanear as portas mais usadas em serviços web
            case _ :
               print('\033[1;41m[!] Opção Inválida!\033[m')  # imprime a mensagem de erro
               exit()  # sai do programa
        
        print ("\n")    
        print ("-" * 50)  # imprime uma linha de hífens
        print (f"[*] Escaneado o Host {host_informado}")  # imprime a mensagem de escaneamento
        print ("-" * 50, "\n")  # imprime uma linha de hífens

        for porta in portas:  # para cada porta na lista de portas
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # cria um socket
            s.settimeout(0.5)  # define um tempo limite para a conexão
            codigo = s.connect_ex((str(host_informado), porta))  # tenta conectar ao host e porta
            s.close()  # fecha o socket
            if codigo == 0: # se a conexao for igual a 0     
                try:
                    servico = socket.getservbyport(porta) #pega o nome do serviçop pelo numero da porta
                    print(f"\033[1;32mPorta {porta} = {servico} - aberta\033[m") #imprime a porta e o nome do serviço
                except:
                    print(f"\033[1;32mPorta {porta} = Serviço desconhecido - aberta\033[m") #imprime a porta e o nome do serviço
            else:
                print(f"\033[1;31mPorta {porta} fechada\033[m") #imprime a porta fechada
    else:
        print('\033[1;41m[!] Opção Inválida!\033[m')  # imprime a mensagem de erro
        exit()  # sai do programa

    t2 = datetime.now()#guarda tempo atual
    tempo = t2 - t1 #calcula os dois tempos, para ter o tempo de operacao do script
    print(f"\nScan completo em {tempo}\n") #imprime o tempo de operacao do script











