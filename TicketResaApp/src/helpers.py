GetStartedPage = """
MDFloatLayout:
    MDLabel:
        text: "Your One-Stop Ticket Booking App"
        pos_hint: {"center_y": .48}
        font_style: "H4"
        halign: "center"
        theme_text_color: "Primary"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: "Effortless Reservations at Your Fingertips"
        pos_hint: {"center_y": .35}
        font_style: "H6"
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
        pos_hint: {"center_y": .15}
        font_style: "Subtitle1"
        halign: "center"
        theme_text_color: "Primary"
    MDFlatButton:
        text: "Login here"
        pos_hint: {"center_x": .5,"center_y": .1}
        font_style: "Subtitle1"
        halign: "center"

"""

MainWindow = """
MDFloatLayout:
    MDLable:
        text: "Login"
        pso_hint: {"center_y": .85}
        font_style: "H4"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 1, 1


"""