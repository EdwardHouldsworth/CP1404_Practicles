"""miles to kilometers (kivy)"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometersApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file("miles_to_kilometers.kv")
        Window.size = (512, 256)
        return self.root

    def convert_miles_kilometers(self, miles='0'):
        if miles.isdigit():
            kilometers = int(miles) * 1.60934
            self.root.ids.output_label.text = str(kilometers)
        else:
            self.root.ids.output_label.text = "0.0"

    def adjust_miles(self, amount):
        miles = self.root.ids.input_number.text
        if miles.isdigit():
            miles = 1 if miles == '' else int(miles)
        else:
            miles = 1
        adjusted_number = miles + amount
        adjusted_number = 1 if adjusted_number < 1 else adjusted_number
        self.root.ids.input_number.text = str(adjusted_number)


MilesToKilometersApp().run()
