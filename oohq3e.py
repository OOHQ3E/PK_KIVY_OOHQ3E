from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
Builder.load_file("oohq3e.kv")

global playername
global points

playername = ""
points = 0

class MenuScreen(Screen):
    inputid = ObjectProperty()

    def fileCheck(self):
        self.text = self.inputid.text
        hasInFile = False
        self.inputid.text = ""
        print(self.text)
        file = open("data.txt", "r+")
        global playername

        global score
        for aline in file:
            values = aline.split(';')
            if values[0] == self.text:
                hasInFile = True
                playername = self.text
                score = values[1]

        file.close()

        if hasInFile == False:
            file = open("data.txt", "a")
            file.write(self.text + ";0\n")
            file.close()
            playername = self.text
            score = 0

class GameScreen(Screen):
    pass

class Manager(ScreenManager):
    pass

class Game(App):
    def build(self):
        return Manager()

Game().run()

