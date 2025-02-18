from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window
Window.size = (500,600)

class MyApp(App):
    def build(self):
        
        main = BoxLayout(orientation='horizontal')
        

        layout = BoxLayout(orientation='vertical')

        header = BoxLayout(orientation='horizontal')
        element1 = Label(text='Nome')
        element2 = TextInput()

        salvar = Button(text='Salvar', font_size='35px')
        # salvar.size_hint('0.5,1.0')

        header.add_widget(element1)
        header.add_widget(element2)
        header.add_widget(salvar)



        box1 = BoxLayout(orientation='vertical')
        box2 = BoxLayout(orientation='vertical')

        button1 = Button(text='Botão1')
        button2 = Button(text='Botão2')
        button3 = Button(text='Botão3')

        button4 = Button(text='Botão4')
        button5 = Button(text='Botão5')
        button6 = Button(text='Botão6')

        box1.add_widget(button1)
        box1.add_widget(button2)
        box1.add_widget(button3)

        box2.add_widget(button4)
        box2.add_widget(button5)
        box2.add_widget(button6)

        main.add_widget(box1)
        main.add_widget(box2)

        layout.add_widget(header)
        layout.add_widget(main)

        return layout

if __name__ == '__main__':
    MyApp().run()