from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from setram import getNextTramway

class MirrOS(App):
    def build(self):
        # Create a label widget
        self.label = Label()

        # Schedule the update function to be called every minute
        Clock.schedule_interval(self.update, 1) # 60 seconds = 1 minute

        return self.label

    def update(self, *args):
        # Update the label text with the current date and time
        self.label.text = f"{getNextTramway()}"

if __name__ == '__main__':
    MirrOS().run()

# Path: main.py
