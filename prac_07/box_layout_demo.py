from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        Window.size = (512,128)
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        print("hello")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_button(self):
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''

BoxLayoutDemo().run()
