from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetTest(App):
    def build(self):
        self.title = "Dynamic Widget Test"
        self.root = Builder.load_file('dynamic_widgets_test.kv')
        self.names = ['John', 'Sarah', 'Dave']
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicWidgetTest().run()
