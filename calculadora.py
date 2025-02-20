from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.core.window import Window
Window.clearcolor = '#18181b'
Window.size = (350,650)



class Aplicativo(App):
    def build(self):
            #-----BoxLauouts-----
        layout = BoxLayout(orientation='vertical')
        header = BoxLayout(orientation='horizontal')

        footer = BoxLayout()
        footer.size_hint = (1, 0.3)

        # btnConta = BoxLayout(orientation="vertical")

        btnNumbers = GridLayout(cols=4)

        main = BoxLayout()


            #-----widget-----

        self.zerar = Button(text='Zerar')
        self.zerar.size_hint=(1.0,0.2)

        self.display = Label(text='Aplicativo',font_size='32px')
        devs = Label(text='Develop by @Fabrica32')

        self.bot0 = Button(text='0')
        self.bot1 = Button(text='1')
        self.bot2 = Button(text='2')
        self.bot3 = Button(text='3')
        self.bot4 = Button(text='4')
        self.bot5 = Button(text='5')
        self.bot6 = Button(text='6')
        self.bot7 = Button(text='7')
        self.bot8 = Button(text='8')
        self.bot9 = Button(text='9')
        self.btnVirgula = Button(text=',')


        self.btnAdicao = Button(text='+', background_color='yellow', )
        self.btnSubtracao = Button(text='-', background_color='yellow')
        self.btnMultiplicacao = Button(text='*', background_color='yellow')
        self.btnDivisao = Button(text='/', background_color='yellow')
        self.btnPotenciacao = Button(text='^', background_color='yellow')
        self.btnRaiz = Button(text='√', background_color='yellow')
        self.btnIgual = Button(text='=', background_color='green')
        self.btnApagar = Button(text='<<', background_color='red')




            # -----Binds-----
        self.bot0.bind(on_press=self.armazenar)
        self.bot1.bind(on_press=self.armazenar)
        self.bot2.bind(on_press=self.armazenar)
        self.bot3.bind(on_press=self.armazenar)
        self.bot4.bind(on_press=self.armazenar)
        self.bot5.bind(on_press=self.armazenar)
        self.bot6.bind(on_press=self.armazenar)
        self.bot7.bind(on_press=self.armazenar)
        self.bot8.bind(on_press=self.armazenar)
        self.bot9.bind(on_press=self.armazenar)
        self.btnVirgula.bind(on_press=self.armazenar)

        self.btnAdicao.bind(on_press=self.armazenar)
        self.btnDivisao.bind(on_press=self.armazenar)
        self.btnMultiplicacao.bind(on_press=self.armazenar)
        self.btnSubtracao.bind(on_press=self.armazenar)
        self.btnPotenciacao.bind(on_press=self.armazenar)
        self.btnRaiz.bind(on_press=self.armazenar)

        self.btnIgual.bind(on_press=self.calcular)

        self.zerar.bind(on_press=self.limpar)
        
        self.btnApagar.bind(on_press=self.apagar)




            # -----add_widgets-----
        header.add_widget(self.display)
        btnNumbers.add_widget(self.btnApagar)
        btnNumbers.add_widget(self.btnMultiplicacao)
        btnNumbers.add_widget(self.btnPotenciacao)
        btnNumbers.add_widget(self.btnRaiz)


        btnNumbers.add_widget(self.bot1)
        btnNumbers.add_widget(self.bot2)
        btnNumbers.add_widget(self.bot3)

        btnNumbers.add_widget(self.btnAdicao)

        btnNumbers.add_widget(self.bot4)
        btnNumbers.add_widget(self.bot5)
        btnNumbers.add_widget(self.bot6)
        
        btnNumbers.add_widget(self.btnSubtracao)
        
        btnNumbers.add_widget(self.bot7)
        btnNumbers.add_widget(self.bot8)
        btnNumbers.add_widget(self.bot9)
        btnNumbers.add_widget(self.btnDivisao)


        btnNumbers.add_widget(self.btnVirgula)
        btnNumbers.add_widget(self.bot0)

        main.add_widget(btnNumbers)

        layout.add_widget(self.zerar)
        btnNumbers.add_widget(self.btnIgual)
        # main.add_widget(btnConta)

        footer.add_widget(devs)

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


    def apagar(self, event):
        self.display.text = self.display.text[:-1]


    def calcular(self, event):
        if('+' in self.display.text):
            numbers = self.display.text.split('+')
            soma = float(numbers[0]) + float(numbers[1])
            self.display.text = str(soma)
        elif('-' in self.display.text):
            numbers = self.display.text.split('-')
            soma = float(numbers[0]) - float(numbers[1])
            self.display.text = str(soma)
        elif('*' in self.display.text):
            numbers = self.display.text.split('*')
            soma = float(numbers[0]) * float(numbers[1])
            self.display.text = str(soma)
        elif('/' in self.display.text):
            numbers = self.display.text.split('/')
            soma = float(numbers[0]) / float(numbers[1])
            self.display.text = str(soma)
        elif('^' in self.display.text):
            numbers = self.display.text.split('^')
            soma = float(numbers[0]) ** float(numbers[1])
            self.display.text = str(soma)
        elif('√' in self.display.text):
            numbers = self.display.text.split('√')
            soma = float(numbers[1]) ** 0.5
            self.display.text = str(soma)


if __name__ == '__main__':
    Aplicativo().run()