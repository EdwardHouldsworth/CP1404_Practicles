from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty


class SimpleApp(App):
    grade = StringProperty()

    def build(self):
        Window.size = (400, 200)
        self.root = Builder.load_file('grade_checker.kv')
        return self.root

    def check_grade(self, grade=""):
        if grade.isdigit():
            grade = int(grade)
            if grade > 100:
                self.grade = "-"
            elif grade >= 90:
                self.grade = "HD"
            elif grade >= 76:
                self.grade = "D"
            elif grade >= 65:
                self.grade = "C"
            elif grade >= 50:
                self.grade = "P"
            else:
                self.grade = "F"
        else:
            self.grade = "-"


SimpleApp().run()
