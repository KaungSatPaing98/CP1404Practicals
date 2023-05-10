from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
        layout = BoxLayout(orientation='vertical')
        for name in names:
            label = Label(text=name)
            layout.add_widget(label)
        return layout


if __name__ == '__main__':
    DynamicLabelsApp().run()
