import os  # Importa o modulo OS (para comando de sistema operaconal)   
import sys # Importa o modulo sys (para comando de sistema operaconal)
import platform  # Importa o modulo platform (para verificar o sistema operacional)
import threading  # Importa o modulo threading (para criar threads)
from datetime import datetime  # Importa o modulo datetime (para pegar a data e hora)
from scapy import * # Importa o modulo scapy (para realizar o scan)
import socket # Importa o modulo socket (para realizar o scan)
from scapy.layers.l2 import ARP, Ether, srp  # Importa o modulo ARP (para realizar o scan)

def start_net_scan():  # Funcao para realizar o scan de rede
    print("""     |+++++++++++++++++++++++++++++++++++++++|
     |   ░░█▀█░█▀▀░▀█▀░░░█▀▀░█▀▀░█▀█░█▀█░░   |
     |   ░░█░█░█▀▀░░█░░░░▀▀█░█░░░█▀█░█░█░░   | 
     |   ░░▀░▀░▀▀▀░░▀░░░░▀▀▀░▀▀▀░▀░▀░▀░▀░░   |
     |+++++| Este é o Network Scanner |++++++|
        """)  # Printa o banner, para interface em modo ascii
    print ("               Bem vindo ao NET Probe\n")  # Printa uma mensagem de bem vindo
    print ("             |escolha forma de scanner|\n")  # Printa uma mensagem para o usuario
    print ("1 - Executar em modo Multi-Thread (mais rapito, menos preciso) ") # Printa uma mensagem para o usuario
    print ("2 - Executar como Scan Normal (mais lento, mais preciso)") # Printa uma mensagem para o usuario
    
    opcao = int(input("Digite a opção desejada: "))  # Recebe a opcao desejada do usuario

    if opcao == 1:  # Modo multi-thread mais rapido mas menos preciso

        max_threads = 30  # Numero maximo de threads que o script pode criar

        ip = input("\nDigite o IPv4 da Rede:")  # Recebe um IPv4 como entrada do usuario
        ip_dividido = ip.split('.')  # Divide o IP em quatro partes (0-3)

        try:
            rede = ip_dividido[0] + '.' + ip_dividido[1] + '.' +  ip_dividido[2] + '.'    # Cria a variavel rede com as primeiras duas casas decimais do IP
            start = int(input('\nInicio do intervalo (ex.: 1):'))  # Recebe o inicio do intervalo de IPs
            end = int(input('Fim do intervalo (ex.: 254):'))  # Recebe o fim do intervalo de IPs
        except:
            print('\033[1;41m[ERRO]: Digite um IP ou intervalo de IP valido!\033[m')  # Printa uma mensagem de erro
            sys.exit(1)  # Encerra o script

        if platform.system() == "Windows":  # se o sistema for windows usara o parametro (-n) para enviar uma quantidade especifica de pacote para o host especifico
            ping = "ping -n 4"  # comando para verificar se o host está online (windows)
        else:  # se o sistema for Unix/linux usara o parametro (-c) para enviar uma quantidade especifica de pacote para o host especifico
            ping = "ping -c 4"      # comando para verificar se o host está online (linux/mac)


        class Thread(threading.Thread):     # define uma classe thread para realizar a verificacao de disponibilidade dos IPs
            def __init__(self, start, end):     # metodo especial para iniciar os objetos (start) e (end)
                threading.Thread.__init__(self)     # Inicia o Thread da classe Thread 
                self.start_ip = start       # Armazena o Ip inicial da sub-rede, que sera verificado
                self.end_ip = end     # Armazena o Ip final da sub-rede, que sera verificado
                
            def run(self):      # Metodo que executa as tarefas dos topicos
                for subrede in range(self.start_ip, self.end_ip + 1):   #  Loop que percorre todos os ips da sub-rede
                    address = rede + str(subrede)    # Monta o Endereço completo do IP, para ser verificado
                    resposta = os.popen(ping + " " + address)   # Executa o Comando Ping, para o endereco IP

                    for linha in resposta.readlines():  # Le a saida do comando Ping
                        if "ttl" in linha.lower() or "tempo" in linha.lower():  # Se encontrar alguma das palavras chave
                            try:
                                hostname = socket.gethostbyaddr(address)  # Tenta obter o nome do Host correspondente ao IP
                            except:
                                hostname = ["\033[1;31mNone\033[m"]  # Se  nao encontrar o Hostname, ele vai ficar None | foi colocado dento de um vetor para que aparecesse no print {hostname[0]}

                            try:
                                mac_address = get_mac_address(address)  # Tenta pegar o MAC Address do equipamento
                                if mac_address is None:    # Se nao encontrar o MAC Address, ele vai ficar None
                                    mac_address = "\033[1;31mNone\033[m"  # cor do texto sera vermelha
                                else:
                                    mac_address = "\033[1;32m" + mac_address + "\033[m"  # cor do texto sera verde
                            except:
                                mac_address = "\033[1;31mNone\033[m"    # Caso não encontre o MAC Address, ele vai ficar None
                            
                            if "ttl=64" in  linha.lower() or "ID" in linha:  # Por meio deste parametro do TTL  ou ID, entende que o host e "Linux/Unix" (nao preciso)   
                                sistema_operacional = "Linux/Unix" 
                            elif "ttl=128" in  linha.lower() or "DF" in linha:  # Por meio deste parametro do TTL  ou DF, entende que o host e "Windows" (nao preciso)
                                sistema_operacional = "Windows"
                            else:
                                sistema_operacional = "\033[1;31mNone\033[m"  # se nao conseguir identificar, ele fica "None"

                            print(f"\033[1;32m{hostname[0]}\033[m | \033[1;32m{address}\033[m | \033[1;32m{mac_address}\033[m | \033[1;32m{sistema_operacional}\033[m \033[1;34mesta Ativo\033[m")    # exibe o IP que esta On na rede 
                            break       # interrompe o loop para evitar repeticao  desnecessaria
                        

            # Função para obter o endereço MAC de um dispositivo
        def get_mac_address(ip):    # Funcao para obter o MAC Address de um dispositivo
            arp = ARP(pdst=ip)    # Cria um pacote ARP
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")    # Cria um pacote Ethernet
            packet = ether / arp    # Cria um pacote com o Ether e o ARP
            result = srp(packet, timeout=3, verbose=False)[0]    # Envia o pacote para o dispositivo e recebe a resposta

            # Retorna o endereço MAC se houver resposta
            if result:
                return result[0][1].hwsrc    # Retorna o MAC Address
            
            # registra o horario do inicio das requisicoes de verificacoes feitas pelos threads
        start_time = datetime.now()     # Guarda a Hora Inicial do Script

            # Exibe uma mensagem  informativa do inicio da verificacao
        print(f"\n[*] A verificacao esta sendo exedutada de {rede + str(start)} para  {rede + str(end)}\n")
            # Mostra a informacao de que a verificacao esta sendo realizada entre essas faixas de IPs


        # calcula o numero de IPs a serem  verificados, para saber quantos processos devem ser criados
        numero_ips = end - start + 1        #calcula o numero total de IPs a serem verificados
        numero_threads = min(numero_ips, max_threads)      #Calcula o numero de threads com base no numero de IPs e no limite maximo de threads

        # Calcula o intervalo de IPs para cada thread
        intervalo_ip = numero_ips // numero_threads # Calcula o intervalo de IPs a serem  verificados por cada thread
        ip_inicial = start # define o IP inicial para a primeira thread
        threads = [] # inicializa uma lisra para armazenar as threads

        try:
            # Cria e inicia as threads para realizar a verificacao dos IPs
            for i in range(numero_threads): #  Laço que vai criar as threads
                ip_final = min(ip_inicial + intervalo_ip -1, end) #  Define o IP Final para cada thread
                thread = Thread(ip_inicial, ip_final) # Cria uma nova thread para cad intervalo de IPs Determinado
                thread.start()  # inicia a thread
                threads.append(thread)  # Adiciona a thread na lista de threads
                ip_inicial = ip_final + 1  # atualiza o IP inicial para o proximo thread 
        except Exception as e:            
            print('\033[1;41m[!] Erro ao criar threads:\033[m', e)  # em caso  de erro na criação das threads, mostra a mensagem de erro
            sys.exit(2) # Encerre o programa com o codigo de erro 2

        # Aguarda o termino de todas as threads
        for thread in threads:
            thread.join()  # Espera ate que a thread seja concluida 

        # Registra o horario de termino da verificacao
        end_time = datetime.now()  # Obtem o horario atual

        # clacula e exibe a duracao total da verificacao 
        tempo_duracao = end_time - start_time
        print("\n\n[*] a verificacao durou %s" % tempo_duracao )


#==========================================================================================================================================================



#   Versão sem threads, para que cada ping seja testado um por um, para garantir que cada dispositivos foi testado 

    elif opcao == 2:  #modo normal, proccesso mais lento, mas mais preciso

            ip = input("Digite o IPv4 da Rede:")  # Recebe um IPv4 como entrada do usuario
            ip_dividido = ip.split('.')  # Divide o IP em quatro partes (0-3)

            try:
                rede = ip_dividido[0] + '.' + ip_dividido[1] + '.' + ip_dividido[2] + '.'  # Cria a variavel rede com as primeiras duas casas decimais do IP
                start = int(input('Inicio do intervalo (ex.: 1):'))  # Recebe o inicio do intervalo
                end = int(input('Fim do intervalo (ex.: 254):'))  # Recebe o fim do intervalo
            except:
                print('\033[1;41m[ERRO]: Digite um IP e um intervalo valido!\033[m')  # Mensagem de erro caso o usuario digite um IP ou intervalo invalido
                sys.exit(1)  # Encerra o programa

            if platform.system() == "Windows":  # se o sistema for windows usara o parametro (-n) para enviar uma quantidade especifica de pacote para o host especifico
                ping = "ping -n 2"  # comando para verificar se o host está online (windows)
            else:  # se o sistema for Unix/linux usara o parametro (-c) para enviar uma quantidade especifica de pacote para o host especifico
                ping = "ping -c 2"  # comando para verificar se o host está online (linux/mac)


            def get_mac_address(ip):  # Função para pegar o endereço MAC de um host
                arp = ARP(pdst=ip)  # Cria um pacote ARP
                ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Cria um pacote Ethernet
                packet = ether / arp  # Cria um pacote com o Ethernet e o ARP
                result = srp(packet, timeout=3, verbose=False)[0]  # Envia o pacote e recebe a resposta

                # Retorna o endereço MAC se houver resposta
                if result:  # Se houver resposta 
                    return result[0][1].hwsrc  # Retorna o endereço MAC

            start_time = datetime.now()  # Guarda a Hora Inicial do Script

            print(f"[*] A verificacao esta sendo exedutada de {rede + str(start)} para  {rede + str(end)}\n")  # Mensagem de inicio do script

            # Loop para verificar os hosts

            for subrede in range(start, end + 1): 
                address = rede + str(subrede)  # Cria uma variavel com o endereço IP
                resposta = os.popen(ping + " " + address)  # Envia o ping para o host

                # Verifica se o host esta online

                for linha in resposta.readlines():  # Loop para ler as linhas da resposta
                    if "ttl" in linha.lower() or "tempo" in linha.lower():  # Verifica se a linha contem ttl ou tempo
                        try:
                            hostname = socket.gethostbyaddr(address)  # Obtem o nome do host
                        except:
                            hostname = ["\033[1;31mNone\033[m"]  # Caso nao consiga obter o nome do host, retorna None com cor vermelha
                        try:
                            mac_address = get_mac_address(address)  # Obtem o endereço MAC
                            if mac_address is None:  # Verifica se o endereço MAC é None
                                mac_address = "\033[1;31mNone\033[m"  # Caso seja None, retorna None com cor vermelha   
                            else:
                                mac_address = "\033[1;32m" + mac_address + "\033[m"  # Caso contrario, retorna o endereço MAC com cor verde
                        except:
                            mac_address = "\033[1;31mNone\033[m"  # Caso nao consiga obter o endereço MAC, retorna None com cor vermelha

                        # Verifica o sistema operacional do host
                        if "ttl=64" in linha.lower() or "ID" in linha:  # Se o TTL for igual 64 ou ID, entende que o sistema é Linux/Unix like          
                            sistema_operacional = "Linux/Unix"                  
                        elif "ttl=128" in linha.lower() or "DF" in linha:  # Se o TTL for igual 128 ou DF, entende que o sistema é Windows                                 
                            sistema_operacional = "Windows"
                        else:
                            sistema_operacional = "\033[1;31mNone\033[m"  # Caso nao consiga obter o sistema operacional, retorna None com cor vermelha

                        # Imprime o resultado

                        print(f"\033[1;32m{hostname[0]}\033[m | \033[1;32m{address}\033[m | {mac_address} | \033[1;32m{sistema_operacional}\033[m \033[1;34mesta Ativo\033[m")
                        break

            end_time = datetime.now()  # Obtem o horario atual

            tempo_duracao = end_time - start_time  # Calcula o tempo de duracao

            # Imprime o tempo de duracao
            print("\n\n[*] a verificacao durou %s" % tempo_duracao)


    else:
        print('\033[1;41m[!] Opção Inválida!\033[m')  # Caso a opção seja invalida, imprime uma mensagem de erro


