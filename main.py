#perguntar em qual diretorio ou path ele deseja fazer a busca
#cada diretorio pode alterar dependendo, entretanto, a função de busca deve ser a mesma
#duas classes, uma pra usuário configurar os requisitos da busca como nome do arquivo
#segunda classe irá realizar a busca herdando os parâmetros que o usuário definiu

import os
class usuario: 
    def __init__(self,caminho, documento):
        self.caminho=caminho 
        os.chdir(self.caminho) 
        self.documento=documento

class buscar(usuario):
    
     def __init__(self, caminho, documento):
        try:
            usuario.__init__(self,caminho, documento)
        
            for self.nov_cami, self.diret, self.arquiv in os.walk(os.getcwd()): 
          
                os.chdir(self.nov_cami)
            
                if self.documento in self.arquiv:
                   print(f'arquivo encontrado em {self.nov_cami}/{self.documento}') 
                   break 
                
                else:
                    print('arquivo não encontrado')
                    break
        except FileNotFoundError:
            print(f'erro: diretório inexistente')
        
            
dir=input('copie o caminho do diretório:')
arquivo=input('insira o nome do arquivo:')
busca=buscar(dir, arquivo)