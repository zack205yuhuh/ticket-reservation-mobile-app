from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import rgba
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (310, 580)

GetStartedPage = """
MDFloatLayout:
    orientation: 'vertical'
    MDLabel:
        text: "Your One-Stop Ticket Booking App"
        font_name: "BPoppins"
        pos_hint: {"center_x": .5, "center_y": .5}
        font_style: "H4"
        halign: "center"
        theme_text_color: "Primary"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: "Effortless Reservations at Your Fingertips"
        pos_hint: {"center_x": .5, "center_y": .35}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Primary"
    MDRaisedButton:
        text: "Get Started"
        pos_hint: {"center_x": .5, "center_y": .25}
        font_style: "H6"
        halign: "center"
        on_release: app.go_to_main_page()
    MDLabel:
        text: "Already have an account?"
        pos_hint: {"center_x": .5, "center_y": .17}
        halign: "center"
    MDFlatButton:
        text: "Login here"
        pos_hint: {"center_x": .5, "center_y": .1}
        halign: "center"
        on_release: app.go_to_log_in_page()
"""

MainWindow = """
MDFloatLayout:
    orientation: 'vertical'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_y": .95}
        user_font_size: "30sp"
        halign: "center"
        theme_text_color: "Custom"
        text_color: rgba(26,24,58,255)
        on_release: app.go_to_get_started_page()
    MDLabel: 
        text: "Welcome!"
        font_size:"26sp"
        pos_hint: {"center_x": .6, "center_y": .85}
    MDLabel: 
        text: "Sign up to continue"
        font_size:"18sp"
        pos_hint: {"center_x": .6, "center_y": .79}
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .63}
        TextInput:
            hint_text: "First name"
            size_hint_y: .75
            pos_hint:{"center_x": .43, "center_y": .5}
            background_color: rgba{0, 0, 59, 255}
            cursor_color: rgba{0, 0, 59, 255}
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
        MDFloatLayout: 
            pos_hint:{"center_x": .45, "center_y": 0}
            size_hint_y: .03
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .53}
        TextInput:
            hint_text: "Last name"
            size_hint_y: .75
            pos_hint:{"center_x": .43, "center_y": .5}
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
        MDFloatLayout: 
            pos_hint:{"center_x": .45, "center_y": 0}
            size_hint_y: .03
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .43}
        TextInput:
            hint_text: "Email"
            size_hint_y: .75
            pos_hint:{"center_x": .43, "center_y": .5}
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
        MDFloatLayout: 
            pos_hint:{"center_x": .45, "center_y": 0}
            size_hint_y: .03
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .33}
        TextInput:
            hint_text: "Password"
            size_hint_y: .75
            pos_hint:{"center_x": .43, "center_y": .5}
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            password: True
        MDFloatLayout: 
            pos_hint:{"center_x": .45, "center_y": 0}
            size_hint_y: .03
    MDRaisedButton:
        text: "Sign Up"
        size_hint:.6, .06
        pos_hint:{"center_x": .5, "center_y": .2}
        background_color: 1, 0, 1, 1
        font_style: "H6"
        halign: "center"
    MDLabel:
        text: "Already have an account?"
        pos_hint: {"center_x": .5, "center_y": .1154}
        halign: "center"
    MDFlatButton:
        text: "Login here"
        pos_hint: {"center_x": .5, "center_y": .07}
        halign: "center" 
        on_release: app.go_to_log_in_page()        
"""
LogInPage = """
MDFloatLayout:
    orientation: 'vertical'
    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_y": .95}
        user_font_size: "30sp"
        halign: "center"
        theme_text_color: "Custom"
        text_color: rgba(26,24,58,255)
        on_release: app.go_to_get_started_page()
    MDLabel: 
        text: "Welcome back!"
        font_size:"26sp"
        pos_hint: {"center_x": .6, "center_y": .85}
    MDLabel: 
        text: "Log in to continue"
        font_size:"18sp"
        pos_hint: {"center_x": .6, "center_y": .79}
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .63}
        TextInput:
            hint_text: "Email"
            size_hint_y: .75
            pos_hint:{"center_x": .43, "center_y": .5}
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
        MDFloatLayout: 
            pos_hint:{"center_x": .45, "center_y": 0}
            size_hint_y: .03
    MDFloatLayout:
        size_hint: .7, .07
        pos_hint: {"center_x": .5, "center_y": .53}
        TextInput:
            hint_text: "Password"
            size_hint_y: .75
            pos_hint:{"center_x": .43, "center_y": .5}
            font_size: "14sp"
            cursor_width: "2sp"
            multiline: False
            passord: True
        MDFloatLayout: 
            pos_hint:{"center_x": .45, "center_y": 0}
            size_hint_y: .03
    MDRaisedButton:
        text: "Log in"
        size_hint:.6, .06
        pos_hint:{"center_x": .5, "center_y": .4}
        background_color: 1, 0, 1, 1
        font_style: "H6"
        halign: "center"
"""

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Builder.load_string(MainWindow))

class GetStartedScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Builder.load_string(GetStartedPage))

class LogInScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.add_widget(Builder.load_string(LogInPage))       


class TicketApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette="Purple"
       
        screen_manager = ScreenManager()
        screen_manager.add_widget(GetStartedScreen(name= "get_started"))
        screen_manager.add_widget(MainScreen(name= "main"))
        screen_manager.add_widget(LogInScreen(name = "log_in"))

        return screen_manager
    
    def go_to_main_page(self):
        self.root.current = "main"

    def go_to_get_started_page(self):
        self.root.current = "get_started"
    
    def go_to_log_in_page(self):
        self.root.current = "log_in"

if __name__ == "__main__":
    TicketApp().run()

