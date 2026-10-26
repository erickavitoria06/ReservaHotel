class Cliente:
    def __init__(self, nome, documento, contato):
        self.nome = nome
        self.documento = documento
        self.contato = contato

    def __str__(self):
        return f"Cliente: {self.nome} | Documento: {self.documento} | Contato: {self.contato}"


# Classe Base 
class Quarto:
    def __init__(self, numero, valor_diaria):
        self.numero = numero
        self.valor_diaria = valor_diaria
        self.status = "Disponível"

    def obter_tipo(self):
        return "Quarto Padrão"

    def __str__(self):
        return f"Quarto {self.numero} ({self.obter_tipo()}) - R$ {self.valor_diaria:.2f} [{self.status}]"


# Classes Filhas
class QuartoSolteiro(Quarto):
    def __init__(self, numero):
        super().__init__(numero, valor_diaria=120.0)

    def obter_tipo(self):
        return "Solteiro"


class QuartoCasal(Quarto):
    def __init__(self, numero):
        super().__init__(numero, valor_diaria=200.0)

    def obter_tipo(self):
        return "Casal"


class Suite(Quarto):
    def __init__(self, numero):
        super().__init__(numero, valor_diaria=350.0)

    def obter_tipo(self):
        return "Suíte Master"


class Reserva:
    def __init__(self, cliente, quarto, data_inicio, data_fim):
        self.cliente = cliente
        self.quarto = quarto
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def __str__(self):
        return f"Reserva: {self.cliente.nome} | Quarto: {self.quarto.numero} ({self.quarto.obter_tipo()}) | Período: {self.data_inicio.strftime('%d/%m/%Y')} até {self.data_fim.strftime('%d/%m/%Y')}"