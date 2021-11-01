# -*- coding: utf-8 -*-

import requests
import time
import winsound
import sys


# сделать программу
# 1. цикл с таймером каждые 15 секунд данные по тикеру, если цена ласт трейд
# превысил заданное значение (while True)
# 2. выдать звук на происходящее событие beep.wav
# 3. добавить цену порога для оповещений
class CryptoTracker:
    def __init__(self, currencies='BTC-USD', alert_price=0.0):
        self.currencies = currencies
        self.END_POINT = f'https://api.bittrex.com/v3/markets/{self.currencies}/ticker'
        self.sound = 'D://Python/My_projects/PASV/lesson1/button-16.wav'
        self.initial_price = 0
        self.alert = alert_price

    def track_changes(self):
        print(f'The script will inform you if price for {self.currencies} '
              f'will go higher than {self.alert}')

        while True:
            response = requests.get(self.END_POINT)
            if response.ok:
                new_price = float(response.json()['lastTradeRate'])
                if self.initial_price == 0:
                    self.initial_price = new_price
                elif self.initial_price >= new_price:
                    print('Price is unchanged or is lower than target. '
                          'Waiting for update...')
                elif self.initial_price < new_price:
                    winsound.PlaySound('button-16.wav', winsound.SND_ASYNC)
                    winsound.MessageBeep(-1)
                    print(f'The price for {self.currencies} went up and now is {new_price}')
                self.initial_price = new_price
            else:
                print(
                    f'Something went wrong. Response code - {response.status_code}')

            time.sleep(5)


if len(sys.argv) > 1:
    CryptoTracker(sys.argv[1], float(sys.argv[2])).track_changes()
else:
    CryptoTracker().track_changes()
