import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = [ACCOUNT_SID_TWILIO]

# Your Auth Token from twilio.com/console
auth_token  = [AUTH_TOKER_TWILIO]

client = Client(account_sid, auth_token)

msgTo = [NUMBER_PHONE_RECEIVER]
msgFrom = [NUMBER_PHONE_SENDER]

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'files/{mes}.xlsx')

#    print(f'===== {mes} ===== \n{tabela_vendas.sort_values(by=["Vendas"],ascending=False)}')

    if (tabela_vendas['Vendas'] > 55000).any():

        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Nome do Vendedor: {vendedor}, Valor em Vendas: {vendas}')

        message = client.messages.create(
            to=msgTo,
            from_=msgFrom,
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}'
            )
        
        print(message.sid)



# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
