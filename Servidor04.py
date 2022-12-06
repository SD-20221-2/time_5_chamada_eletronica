from xmlrpc.server import SimpleXMLRPCServer 
class RPC: # classe que implementa RPC
    _metodos_rpc = ['classificacao'] # array de métodos criados
    def __init__(self, direcao): #construtor
        self._servidor = SimpleXMLRPCServer(direcao, allow_none=True) # instancia o servidor
        for metodo in self._metodos_rpc: # registro do método
            self._servidor.register_function(getattr(self, metodo)) # registro dos métodos em array

    def classificacao(self, altura, sexo):
        peso_ideal = 0
        if sexo == 'masculino':   
            peso_ideal = (72.7*float(altura))-58
            return "O peso ideal para ele é ", peso_ideal
        elif sexo == 'feminino':
            peso_ideal = (62.1*float(altura))-44.7
            return "O peso ideal para ela é ", peso_ideal
        else:
            return "Informação errada, tente novamente"
    def iniciar_servidor(self): # inicia o servidor 
        self._servidor.serve_forever()
if __name__ == '__main__' : 
    rpc = RPC(('', 20064)) # porta que vai ficar aberta para receber as informações
    print("Servidor RPC iniciado ... ")
    rpc.iniciar_servidor()