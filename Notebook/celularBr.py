import re

class CelularBr:
    """
       Esta classe irá validar o número de celular, retornando-o
       no formato padrão do Brasil: (xx) xxxxx-xxxx.

       Caso o número não seja válido, retornará a mensagem:
       "Número inválido"
    """
    def __init__(self, celular):
        self.celular = str(celular)

    def verifica_validacao(self):
        """
        Esta função irá verificar a validação do número retornado,
        pela função valida_celular.
        Se for válido, ela formatará nopadrão da formata_celular,
        se não for imprimirá "Número inválido"
        """
        if self.valida_celular(self.celular):
            return self.formata_numero()
        else:
            return "Número inválido"

    def valida_celular(self, celular):
        """
        Esta função irá validar (com Regex) o número de celular
        com o DDD.
        Retornando True ou False.
        """
        padrao = '[1-9]{2}9[5-9]{1}[0-9]{7}'
        primeira_validacao = re.findall(padrao, celular)
        if primeira_validacao:
            segundo_padrao = '0{6}|1{6}|2{6}|3{6}|4{6}|5{6}|6{6}|7{6}|8{6}|9{6}'
            segunda_validacao = re.findall(segundo_padrao,
                                           primeira_validacao[0])
            if segunda_validacao:
                return False
            else:
                return True
        else:
            return False

    def formata_numero(self):
        """
        Esta função retornará o o número formatado no padrão:
        (xx) xxxxx-xxxx.
        """
        padrao = '([1-9]{2})(9[0-9]{4})([0-9]{4})'
        resposta = re.search(padrao, self.celular)

        ddd = resposta.group(1)
        primeiros_digitos = resposta.group(2)
        ultimos_digitos = resposta.group(3)
        numero_formatado = (f"({ddd}) {primeiros_digitos}-{ultimos_digitos}")

        return numero_formatado