import wmi

def configurar_ip_manual(interface, endereco_ip, mascara_subrede, gateway):                                  # Conectar ao serviço WMI do Windows
    try:
        
        c = wmi.WMI()

        # Obter a interface de rede especificada
        nic = c.Win32_NetworkAdapterConfig(IPEnabled=True, Description=interface)[0]

        # Configurar o endereço IP manualmente
        retorno = nic.EnableStatic(IPAddress=[endereco_ip], SubnetMask=[mascara_subrede])
        
        # Configurar o gateway
        gateway_config = nic.SetGateways(DefaultIPGateway=[gateway])
        
        if retorno[0] == 0 and gateway_config[0] == 0:
            print("Configuração de IP manual bem-sucedida.")
        else:
            print("Erro ao configurar IP manualmente.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Defina as informações da interface de rede e o endereço IP manual aqui
interface = "Sua Interface de Rede"  # Exemplo: "Ethernet"
endereco_ip = "192.168.1.100"
mascara_subrede = "255.255.255.0"
gateway = "192.168.1.1"

# Chame a função para configurar o IP manualmente
configurar_ip_manual(interface, endereco_ip, mascara_subrede, gateway)
