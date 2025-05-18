  1. INTRODUÇÃO

O Net Probe é uma ferramenta de análise de rede. Este manual fornecerá instruções detalhadas sobre como utilizar o software de forma eficaz.

  2. REQUISITOS DO SISTEMA

Sistema operacional: Windows, Linux ou macOS
Python 3 instalado no sistema

  3. INSTALAÇÃO E CONFIGURAÇÃO

Baixe o código-fonte do Net Probe no repositório GitHub.
Extraia os arquivos do código-fonte para uma pasta de sua escolha.
Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos foram extraídos.
O software está pronto para ser utilizado.

Digitando no prompt:

    python3 netprobe.py <-h, ns, ps>

usage: netprobe.py [-h] {ps,ns}

Net Probe - Ferramenta de análise de rede.

positional arguments:
  {ps,ns}     Operação a ser realizada: "-ps" para scan de porta ou "-ns" para scan de rede.

options:
  -h, --help  show this help message and exit

  4. UTILIZAÇÃO

O Net Probe oferece duas funcionalidades principais: Port Scan e Net Scan. Siga as instruções abaixo para utilizar cada uma delas:

Port Scan:
Insira o endereço IP do dispositivo que deseja escanear.
Escolha uma das seguintes opções:

Digite 1(as portas específicas que deseja escanear separadas por vírgula.)

Ou digite 2 para listas automáticas.

  Escolha a opção 1 para escanear automaticamente as 65535 portas.
  Escolha a opção 2 para escanear automaticamente as 1024 portas mais comuns.
  Escolha a opção 3 para escanear as portas mais comuns em serviços web.
Aguarde enquanto o software realiza o escaneamento das portas.
Os resultados serão exibidos no terminal, indicando quais portas estão abertas ou fechadas.

Net Scan:

Insira o endereço IP da rede que deseja escanear.
Escolha o intervalo de IPs que deseja escanear, fornecendo o endereço de início e fim.
Aguarde enquanto o software realiza o escaneamento da rede.
Os resultados serão exibidos no terminal, indicando os dispositivos ativos na rede, seus endereços IP e status de conectividade.
