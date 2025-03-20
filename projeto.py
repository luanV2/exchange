import datetime
import sys

#LOGIN: 47207050810
#SENHA: 230905


now = datetime.datetime.now()
time = now.replace(second=0, microsecond= 0)

Ethereum = 0
Bitcoin = 0
Ripple = 0
Reais = 0

reais_infinito = 1000000000000



global saldo_carteira 
global saque_carteira



extrato = []



login = int(input("Digite o seu login: "))
senha = int(input("Digite a sua senha: "))


if login == 472 and senha == 23:
    print("-" * 50)
    print("Acesso autorizado!")
    print("-" * 50)

elif login != 472 or senha != 23:
    print("Acesso negado!")
    tentativas = 1
    while tentativas <= 3:
        login2 = int(input("Digite novamente o seu login: "))
        senha2 = int(input("Digite novamente a sua senha: "))
        if login2 == 472 and senha2 == 23:
            print("Acesso autorizado!")
            break
        else:
            print("Acesso negado! Tentativas restantes:", 3 - tentativas)
            tentativas += 1
    else:
        print("Muitas tentativas, tente novamente mais tarde.")
        exit()
        
def exibir_saldo():
    print("-" *50)
    print(f"Reais: R$ {Reais}")
    print(f"Bitcoin: BTC {Bitcoin}")
    print(f"Ethereum: ETH {Ethereum}")
    print(f"Ripple: XRP {Ripple}")
    print("-" *50)

def exibir_dados():
    print("Nome: Luan Garcia Candido")
    print("CPF: 472.070.508-10")
    


def cripto():
    print("1. Bitcoin")
    print("2. Ethereum")
    print("3. Ripple")
    
    

    
while True:
    print("-"*50)
    print("1. Consultar saldo")
    print("2. Consultar extrato")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Comprar criptomoedas")
    print("6. Vender criptomoedas")
    print("7. Atualizar cotação")
    print("8. Sair")
    print("-"*50)
    menu = int(input("No que posso te ajudar: "))
    # 1 SALDO DA CARTEIRA
    if menu == 1:
        exibir_dados()
        exibir_saldo()
    # 2 EXTRATO DAS TRANSAÇÕES
    
   
    elif menu == 2:
        exibir_dados()
        print("Extrato de transações:")
        for transacao in extrato:
            print(transacao)
        print("-" * 50)
       
    # 3 DEPÓSITO 
    elif menu == 3:
        saldo_carteira = float(input("Qual o valor será investido? "))
        print(f"Sua carteira em reais é de: {saldo_carteira} ")
        Reais = Reais + saldo_carteira
        extrato.append(f"{time} + {Reais} REAL CT : 0.0    TX : 0.0 REAL: {Reais} BTC: {Bitcoin} ETH: {Ethereum} XRP: {Ripple}")
        exibir_saldo()

    # 4 SACAR 
    elif menu == 4:
        exibir_saldo()
        saque_carteira = float(input("Qual o valor do saque? "))
        saldo_final = Reais - saque_carteira
        Reais = saldo_final
        extrato.append(f"{time} - {saque_carteira} REAL CT : 0.0         TX : 0.0 REAL: {Reais} BTC: {Bitcoin} ETH: {Ethereum} XRP: {Ripple}")

        exibir_saldo()
        

        
    # 5 COMPRAR 
    elif menu == 5:
        exibir_saldo()
        cripto()
        cripto_number = (input("Em qual cripto você irá investir? "))
        deposito = int(input("Qual o valor que será depositado? "))
        if cripto_number == "1":
            taxa_BTC = 0.02 * deposito
            valor_deposito_BTC = (deposito + taxa_BTC)
            novo_valor_BTC = Reais - valor_deposito_BTC
            Reais = novo_valor_BTC
            print(f"Seu novo saldo em Reais é R$ {novo_valor_BTC}")
            valor_BTC = deposito * 0.0000031
            print(f"Seu saldo em bitcoin é BTC {valor_BTC}")
            Bitcoin = valor_BTC
            extrato.append(f"{time} + {deposito} BTC CT : 340.991,92        TX : 0.02 REAL: {Reais} BTC: {Bitcoin} ETH: {Ethereum} XRP: {Ripple}")

            
            
            
        elif cripto_number == "2":
            taxa_ETH = 0.01 * deposito
            valor_deposito_ETH = (taxa_ETH + deposito)
            novo_valor_ETH = Reais - valor_deposito_ETH
            Reais = Reais - novo_valor_ETH
            print(f"Seu novo saldo  em reais é {novo_valor_ETH}")
            valor_ETH = deposito * 0.000064
            print(f"Seu saldo em ethereum é ETH {valor_ETH}")
            Ethereum = valor_ETH
            extrato.append(f"{time} + {deposito} ETH CT : 15.782,71     TX : 0.01 REAL: {Reais} BTC: {Bitcoin} ETH: {Ethereum} XRP: {Ripple}")

            
        elif cripto_number == "3":
            taxa_XRP = 0.01 * deposito
            valor_deposito_XRP = (taxa_XRP + deposito)
            novo_valor_XRP = Reais - valor_deposito_XRP
            Reais = Reais - novo_valor_XRP
            print(f"Seu novo saldo em reais é {novo_valor_XRP}")
            Valor_XRP = deposito * 0.37
            print(f"Seu saldo em etheruem é de XRP {Valor_XRP}")
            Ripple = Valor_XRP
            extrato.append(f"{time} + {deposito} XRP CT : 2,67          TX : 0.01 REAL: {Reais} BTC: {Bitcoin} ETH: {Ethereum} XRP: {Ripple}")

        
    # 6 VENDER 
    elif menu == 6:
        exibir_saldo()
        cripto()
        venda_number = int(input("Qual cripto que será vendida? "))
        if venda_number == 1:
            print(f"BTC {Bitcoin}")
            venda_BTC = float(input("Quanto você quer retirar de REAIS da moeda bitcoin? "))
            calculoVendaBTC = venda_BTC * 0.0000031
            nova_saldo_BTC = Bitcoin - calculoVendaBTC
            calc_taxa_BTC = venda_BTC * 0.03
            prçfinalBTC = venda_BTC - calc_taxa_BTC
            BTC = Reais + prçfinalBTC
            Reais = BTC
            Bitcoin = nova_saldo_BTC
            exibir_saldo()
            extrato.append(f"{time} - {deposito} BTC CT : 340.991,92        TX : 0.03 REAL: {Reais} BTC: {Bitcoin} ETH: {Ethereum} XRP: {Ripple}")
            
        
            
            
            
        elif venda_number == 2:
            print(f"ETH {Ethereum}")
            venda_ETH = float(input("Quanto você quer retirar de REAIS da moeda Ethereum? "))
            calculoVendaETH = venda_ETH * 0.000064
            nova_saldo_ETH = Ethereum - calculoVendaETH
            calc_taxa_ETH = venda_ETH * 0.02
            prçfinalETH = venda_ETH - calc_taxa_ETH
            ETH = Reais + prçfinalETH
            Reais = ETH
            Ethereum = nova_saldo_ETH
            exibir_saldo()
            extrato.append(f"{time} + {venda_ETH} ETH CT : 15.782,71     TX : 0.02 REAL: {ETH} BTC: {Bitcoin} ETH: {Ethereum} XRP: {Ripple}")

            
        elif venda_number == 3:
            print(f"XRP {Ripple}")
            venda_XRP = float(input("Quanto você quer retirar de REAIS da moeda Ripple? "))
            calculoVendaXRP = venda_XRP * 0.0000031
            nova_saldo_XRP = Ripple - calculoVendaXRP
            calc_taxa_XRP = venda_XRP * 0.01
            prçfinalXRP = venda_XRP - calc_taxa_XRP
            XRP = Reais + prçfinalXRP
            Reais = XRP
            Bitcoin = nova_saldo_XRP
            exibir_saldo()
            extrato.append(f"{time} + {deposito} XRP CT : 2,67          TX : 0.01 REAL: {Reais} BTC: {Bitcoin} ETH: {Ethereum} XRP: {Ripple}")

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        

    # 7 ATUALIZAÇÃO
    elif menu == 7:
        print("Aqui será uma aba para atualizar a cotação das criptos.")

    # 8 SAIR 
    elif menu == 8:
        print("Até breve.")
        sys.exit()
        
    elif menu == 2:
        exibir_dados()
        print("Aqui ficará o extrato da transações.")
        print(now, f"{saldo_carteira}")
