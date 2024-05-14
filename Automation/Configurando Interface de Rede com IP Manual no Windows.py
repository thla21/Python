import wmi

def configurar_ip_manual(interface, endereco_ip, mascara_subrede, gateway):                   # Conectar ao serviço WMI do Windows
    try:
        c = wmi.WMI()
        nic = c.Win32_NetworkAdapterConfig(IPEnabled=True, Description=interface)[0]          # Obter a interface de rede especificada
        retorno = nic.EnableStatic(IPAddress=[endereco_ip], SubnetMask=[mascara_subrede])     # Configurar o endereço IP manualmente
        gateway_config = nic.SetGateways(DefaultIPGateway=[gateway])                          # Configurar o gateway
        if retorno[0] == 0 and gateway_config[0] == 0:
            print("Configuração de IP manual bem-sucedida.")
        else:
            print("Erro ao configurar IP manualmente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Defina as informações da interface de rede e o endereço IP manual aqui
interface = "Sua Interface de Rede"                                                          # Exemplo: "Ethernet"
endereco_ip = "192.168.1.100"                                                                # Endereço IP do host.
mascara_subrede = "255.255.255.0"                                                            # Máscara de rede.
gateway = "192.168.1.1"                                                                      # Gateway para conexão com a Internet


configurar_ip_manual(interface, endereco_ip, mascara_subrede, gateway)                       # Chame a função para configurar o IP manualmente       
