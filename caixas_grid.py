from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.core.window import Window
Window.size = (300,650)

class Aplicativo(App):
    def build(self):

            #-----BoxLauouts-----
        layout = BoxLayout(orientation='vertical')
        header = BoxLayout(orientation='horizontal')
        footer = BoxLayout()
        footer.size_hint = (1, 0.3)
        main = GridLayout(cols=2)


            #-----widget-----

        self.zerar = Button(text='Zerar')
        self.zerar.size_hint=(1.0,0.2)

        self.display = Label(text='Aplicativo',font_size='32px')
        devs = Label(text='Develop by @Fabrica32')

        self.bot1 = Button(text='1')
        self.bot2 = Button(text='2')
        self.btnMais = Button(text='+')
        self.btnIgual = Button(text='=')



            # -----Binds-----
        self.bot1.bind(on_press=self.armazenar)
        self.bot2.bind(on_press=self.armazenar)
        self.btnMais.bind(on_press=self.armazenar)


        self.btnIgual.bind(on_press=self.calcular)

        self.zerar.bind(on_press=self.limpar)




            # -----add_widgets-----
        header.add_widget(self.display)
        main.add_widget(self.bot1)
        main.add_widget(self.bot2)
        main.add_widget(self.btnMais)
        main.add_widget(self.btnIgual)

        footer.add_widget(devs)

        layout.add_widget(self.zerar)
        layout.add_widget(header)
        layout.add_widget(main)
        layout.add_widget(footer)


        return layout

    
    def armazenar(self,event):
        # print(event.text)
        self.display.text += event.text

    def limpar(self,event):
        # print(self.display.text)
        self.display.text = ''

    def calcular(self, event):
        if('+' in self.display.text):
            numbers = self.display.text.split('+')
            soma = float(numbers[0]) + float(numbers[1])
            self.display.text = str(soma)


if __name__ == '__main__':
    Aplicativo().run()