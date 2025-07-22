from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
ScreenManager:
    SplashScreen:
    LoginScreen:
    ParkingScreen:

<SplashScreen>:
    name: "splash"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(30)
        spacing: dp(20)
        md_bg_color: 1, 0.84, 0, 1
        MDLabel:
            text: "🚗 SMART PARK"
            halign: "center"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 0, 0, 0.3, 1
        MDLabel:
            text: "Smarter Parking, Easier Living"
            halign: "center"
            font_style: "Subtitle1"
            theme_text_color: "Custom"
            text_color: 0, 0, 0.3, 1
        MDRaisedButton:
            text: "Continue"
            md_bg_color: 0, 0.2, 0.5, 1
            pos_hint: {"center_x": 0.5}
            on_release:
                app.root.current = "login"

<LoginScreen>:
    name: "login"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(40)
        spacing: dp(20)
        md_bg_color: 1, 0.84, 0, 1
        MDTextField:
            id: email
            hint_text: "Email"
        MDTextField:
            id: phone
            hint_text: "Phone Number"
        MDTextField:
            id: password
            hint_text: "Password"
            password: True
        MDRaisedButton:
            text: "Login / Register"
            md_bg_color: 0, 0.2, 0.5, 1
            pos_hint: {"center_x": 0.5}
            on_release:
                app.root.current = "parking"

<ParkingScreen>:
    name: "parking"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(10)
        spacing: dp(10)
        md_bg_color: 1, 0.84, 0, 1

        MDTopAppBar:
            title: "Smart Park"
            left_action_items: [["arrow-left", lambda x: app.back_to_login()]]
            elevation: 4

        MDLabel:
            text: "Parking Spots (Ground Floor)"
            halign: "center"
            font_style: "H6"
            theme_text_color: "Custom"
            text_color: 0, 0, 0.3, 1

        ScrollView:
            MDGridLayout:
                id: grid
                cols: 6
                adaptive_height: True
                spacing: dp(10)
                padding: dp(10)
'''

class SplashScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass

class ParkingScreen(MDScreen):
    def on_enter(self):
        self.load_parking_buttons()

    def load_parking_buttons(self):
        grid = self.ids.grid
        grid.clear_widgets()
        for i in range(1, 67):  # 66 parking spots
            btn = MDRaisedButton(
                text=f"P{i}",
                md_bg_color=(0, 0.6, 0, 1),
                on_release=lambda x, spot=f"P{i}": self.show_booking_dialog(spot)
            )
            grid.add_widget(btn)

    def show_booking_dialog(self, spot):
        dialog = MDDialog(
            title=f"Reserve {spot}",
            text=f"Price: 3000 IQD per hour\\nConfirm your booking?",
            buttons=[
                MDRaisedButton(
                    text="Confirm",
                    on_release=lambda x: self.confirm_booking(dialog)
                ),
                MDRaisedButton(
                    text="Cancel",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def confirm_booking(self, dialog):
        dialog.dismiss()
        MDDialog(title="Success", text="Your parking has been reserved!").open()

class SmartParkApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def back_to_login(self):
        self.root.current = "login"

if __name__ == "__main__":
    SmartParkApp().run()
