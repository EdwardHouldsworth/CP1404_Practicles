from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label

NAMES = ["John", "Danno", "Mary", "Macca", "Mark", "David", "Ted"]


class SimpleApp(App):
    def build(self):
        Window.size = (500, 200)
        self.root = Builder.load_file('simple_app.kv')
        self.create_name_labels()
        return self.root

    def create_name_labels(self):
        for name in NAMES:
            name_label = Label(text=name)
            self.root.ids.name_list.add_widget(name_label)


SimpleApp().run()
