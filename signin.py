from kivy.app import App
from kivy.ui.boxlayout import Boxlayout 

class SigninWindow(Boxlayout):
    pass

class Signin(App):
    def build(self):
        return SigninWindow()

if __name__=="__main__":
    sa = SignApp()
    sa.run()



