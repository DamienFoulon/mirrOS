from kivy.app import App
from kivy.uix.label import Label
from weather import getWeather

class MirrOS(App):
    def build(self):
        return Label(text=f"{str(getWeather()['current_temperature'])}°C")


if __name__ == '__main__':
    MirrOS().run()

# Path: main.kv
