from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.core.window import Window
Window.size = (300,650)

class Aplicativo(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        header = BoxLayout(orientation='horizontal')

        footer = BoxLayout()
        footer.size_hint = (1, 0.2)

        main = GridLayout(cols=2)

        texto = Label(text='Aplicativo',font_size='32px')

        bot1 = Button(text='Bot 1')
        bot2 = Button(text='Bot 2')
        bot3 = Button(text='Bot 3')
        bot4 = Button(text='Bot 4')
        bot5 = Button(text='Bot 5')

        devs = Label(text='Develop by @Fabrica32')

        header.add_widget(texto)

        main.add_widget(bot1)
        main.add_widget(bot2)
        main.add_widget(bot3)
        main.add_widget(bot4)
        main.add_widget(bot5)

        footer.add_widget(devs)

        layout.add_widget(header)
        layout.add_widget(main)
        layout.add_widget(footer)


        return layout
    

if __name__ == '__main__':
    Aplicativo().run()