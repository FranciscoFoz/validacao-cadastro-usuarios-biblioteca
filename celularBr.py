from multiprocessing.sharedctypes import Value
import re

class CelularBr:
    def __init__(self,celular):
        if self.valida_celular(celular):
            self.numero = celular
        else:
            raise ValueError('Inválido')

    def valida_celular(self,celular):
        padrao = '[1-9]{2}9[1-9]{2}[0-9]{6}'
        resposta = re.findall(padrao,celular)
        if resposta:
            return True
        else:
            return False
    
        #def formata_numero(self):
            #numero_formatado = "({}) {}-{}".format(
            #resposta.group(1),
            #resposta.group(2),
            #resposta.group(3)
            #)
            #return numero_formatado
