
# sem comando para interacao 

'''import argparse
import netprobelib

def main():
    print("""    |++++++++++++++++++++++++++++++++++++++++|            
    |   ░█▀█░█▀▀░▀█▀░░░█▀█░█▀▄░█▀█░█▀▄░█▀▀   |
    |   ░█░█░█▀▀░░█░░░░█▀▀░█▀▄░█░█░█▀▄░█▀▀   |
    |   ░▀░▀░▀▀▀░░▀░░░░▀░░░▀░▀░▀▀▀░▀▀░░▀▀▀   |
    |+++++++| Bem-vindo ao Net Probe |+++++++|

    Escolha qual operação você deseja fazer:

    1- Scan de PORTA  |  2- Scan de REDE
""")
    opcao = int(input('Digite a opção: '))
    
    if opcao ==  1:
        # Executar o Port Scan
        print("Iniciando Port Scan:")
        netprobelib.np_port_scan.start_port_scan()
    elif opcao == 2:
        # Executar o Scan de Rede
        print("\nIniciando Scan de Rede:")
        netprobelib.np_net_scan.start_net_scan()
    else:
        print('\033[1;41mOpção Inválida!\033[m')

if __name__ == "__main__":
    main()'''
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#  teste de primeiros comando 
import argparse
import netprobelib

def main():
    parser = argparse.ArgumentParser(description='Net Probe - Ferramenta de análise de rede.')
    parser.add_argument('operation', choices=['ps', 'ns'], help='Operação a ser realizada: "-ps" para scan de porta ou "-ns" para scan de rede.')
    args = parser.parse_args()

    if args.operation == 'ps':
        print("\nIniciando Port Scan:\n\n")
        netprobelib.np_port_scan.start_port_scan()
    elif args.operation == 'ns':
        print("\nIniciando Scan de Rede:\n\n")
        netprobelib.np_net_scan.start_net_scan()

if __name__ == "__main__":
    main()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# teste



'''import argparse
import netprobelib

def main():
    parser = argparse.ArgumentParser(description='Net Probe - Ferramenta de análise de rede.')
    parser.add_argument('-ps', action='store_true', help='Realizar scan de porta.')
    parser.add_argument('host_informado', help='IP do host alvo.')
    parser.add_argument('-pP', nargs='+', type=int, help='Especificar portas para o scan.')
    parser.add_argument('-pA', action='store_true', help='Escaneia todas as portas (pode levar horas).')
    parser.add_argument('-pM', action='store_true', help='Escaneia as primeiras 1024 portas mais comuns.')
    parser.add_argument('-pC', action='store_true', help='Escaneia as portas mais conhecidas em serviços web.')

    args = parser.parse_args()

    if args.ps:
        if args.pP:
            netprobelib.np_port_scan.start_port_scan(args.host_informado, ports=args.pP)
        elif args.pA:
            netprobelib.np_port_scan.start_port_scan(args.host_informado, all_ports=True)
        elif args.pM:
            netprobelib.np_port_scan.start_port_scan(args.host_informado, common_ports=True)
        elif args.pC:
            netprobelib.np_port_scan.start_port_scan(args.host_informado, common_web_ports=True)
        else:
            print("É necessário especificar opções de portas para o scan de porta.")
            parser.print_help()
    else:
        print("É necessário especificar a operação desejada.")
        parser.print_help()

if __name__ == "__main__":
    main()
'''
