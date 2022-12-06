from xmlrpc.client import ServerProxy # RPC usando HTTP como protocolo de transporte
cliente = ServerProxy('http://localhost:20064', allow_none=True) # instancia o cliente na porta 
while True:
    altura = input("Digite a altura \n")
    sexo = input("(1) Masculino (2) Feminino \n")
    print(cliente.classificacao(altura, sexo)) # chamada da função no servidor e retorno da informação