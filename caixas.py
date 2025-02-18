from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch

from kivy.core.window import Window
Window.size = (500,600)


class MyApp(App):
    def build(self):
        main = BoxLayout(orientation='vertical')
        header = BoxLayout(orientation='horizontal')

        btnOne = Button(text='One', color=[1,1,0,1])
        btnTwo = Button(text='Two')

        switch = Switch()

        header.add_widget(switch)
        header.add_widget(btnOne)
        header.add_widget(btnTwo)

        btnTree = Button(text='Three')
        btnFour = Button(text='Four')
        # btnTree.size_hint = (0.1,0.3) ajustar tamanho

        main.add_widget(btnTree)
        main.add_widget(btnFour)



        layout = BoxLayout(orientation='vertical')

        layout.add_widget(header)
        layout.add_widget(main)

        return layout


if __name__=='__main__':
    MyApp().run()