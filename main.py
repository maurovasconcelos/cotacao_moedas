from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("screen.kv")


class MyApp(App):
    def build(self):
        return GUI

    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar: R${self.get_price('USD')}" 
        self.root.ids["moeda2"].text = f"Euro: R${self.get_price('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin: R${self.get_price('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum: R${self.get_price('ETH')}"

    def get_price(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_request = requisicao.json()
        price = dic_request[f"{moeda}BRL"]["bid"]
        return price


MyApp().run()