import re


class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
            self.formatarNumero(self.numero)
        else:
            raise ValueError('Numero incorreto')
    def valida_telefone(self, telefone):
        padrao = '([0-9]{2,3})?[0-9]{2}[0-9]{4,5}[0-9]{4}'
        resposta = (re.findall(padrao, telefone))
        if resposta:
            return True
        else:
            return False

    def formatarNumero(self, numero):
        if len(numero) == 11:
            print(f'+55 {self.numero[0:2]} {self.numero[2]}-{self.numero[3:7]}-{self.numero[7:]}')
        elif len(numero) == 13:
            print(f'+{self.numero[:2]} {self.numero[2:4]} {self.numero[4]}-{self.numero[5:9]}-{self.numero[9:]}')
        elif len(numero) == 14:
            print(f'+{self.numero[:3]} {self.numero[3:5]} {self.numero[5]}-{self.numero[6:10]}-{self.numero[10:]}')





meu = TelefonesBr('85982062167')
