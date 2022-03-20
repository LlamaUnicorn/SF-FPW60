import json
import requests
from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f'https://api.exchangerate.host/convert?from={base_key}&to={sym_key}&amount={amount}')
        total_base = json.loads(r.content)['result']
        print('result: ', json.loads(r.content))
        total_base = round(total_base, 3)
        message = f"Цена {amount} {base} в {sym} : {total_base}"
        return message


c = Convertor()
print(c.get_price('доллар', 'рубль', 1))
