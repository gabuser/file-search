#perguntar em qual diretorio ou path ele deseja fazer a busca
#cada diretorio pode alterar dependendo, entretanto, a função de busca deve ser a mesma
#duas classes, uma pra usuário configurar os requisitos da busca como nome do arquivo
#segunda classe irá realizar a busca herdando os parâmetros que o usuário definiu

import os
class usuario: 
    def __init__(self,path, file): # definindo o estado inicial do objeto, nesse caso estamos instanciandos os valores que iremos trabalhar
        self.path=path 
        os.chdir(self.path) #propriedade do objeto os, ele nos permite nos mover entre os diretórios
        self.file= file

class buscar(usuario):# classe que herda todas as configurações(métodos, atributos) da superclasse
    
     def __init__(self, path, file):
        try:
            usuario.__init__(self,path, file) #chamando o método init do usuário classe
        
            for self.nov_cami, self.variavel, self.arquiv in os.walk(os.getcwd()): #fazendo a busca usando o for  iterando para cada valor dentro do diretório
          
                os.chdir(self.nov_cami)
            
                if self.file in self.arquiv:
                   print(f'arquivo encontrado em {self.nov_cami}/{self.file}') #retorna caso o valor seja encontrado
                   break #impede que o valor itere mais que o necessário
                
                else:
                    print('arquivo não encontrado') #caso o valor não seja encontrado, então uma msg de erro é retornada
                    break
        except FileNotFoundError:
            print(f'erro: diretório inexistente')
        
            
            
    

camin=input('copie o caminho do diretório:')

ar=input('insira o nome do arquivo:')

arq=buscar(camin, ar) #definindo os valores que o usuário colocar, isso pode mudar.

#arq.busca()

#user=usuario(camin, ar)

#def busca(self):
    #    
    #    for nov_cami, self.caminho_arq, self.arquiv in os.walk(os.getcwd()):
    #        if self.file == self.arquiv:
    #            return f'arquivo encontrado em {os.getcwd()}'
    #            break
    #    return f'arquivo não econtrado