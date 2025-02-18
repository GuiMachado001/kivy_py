from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# importando a classe window para definir o tamanho da tela
from kivy.core.window import Window

Window.size = (300,700)

class Programa(App):
    # metodo contrutor da classe programa que herda de App
    def build(self):

        layout = BoxLayout(orientation='vertical')

        text = Label(text='MyApp', font_size='50px')
        botao = Button(text='Cadastrar',font_size='50px')
        botao2 = Button(text='Cancelar',font_size='50px')


        layout.add_widget(text)
        layout.add_widget(botao)
        layout.add_widget(botao2)
        
        return layout 
    

if __name__ == "__main__":
    Programa().run()