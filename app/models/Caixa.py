from .Despesa import Despesa
from datetime import datetime
from time import strptime
from calendar import monthrange

class Caixa():
    def lancar_despesa(self, autor, data, valor, descricao = None):
        valor_adaptado = self._adaptar_valor(valor)
        despesa = Despesa(valor_adaptado, autor, self._converter_datetime(data))
        despesa.descricao = descricao

        return despesa.save()

    def _adaptar_valor(self, valor):
        try:
            return float(valor.replace(',', '.'))
        except:
            raise ValueError('valor')

    def _converter_datetime(self, data):
        try:
            return datetime.strptime(data, "%Y-%m-%d")
        except:
            raise ValueError('data')
