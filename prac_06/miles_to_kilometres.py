from kivy.app import App
from kivy.lang import Builder

CONVERSION_RATE = 1.61


class MilesToKilometres(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_conversion(self):
        try:
            input = float(self.root.ids.input_number.text)
        except ValueError:
            input = 0.0
        output = input * CONVERSION_RATE
        self.root.ids.output_label.text = str(output)

    def handle_increment(self,value):
        try:
            input = float(self.root.ids.input_number.text)
        except ValueError:
            input = 0.0
        output = input + int(value)
        self.root.ids.input_number.text = str(output)

MilesToKilometres().run()