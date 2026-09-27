"""Pantalla base para los módulos que aún no tienen funcionalidad propia."""
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel


class ModuleScreen(MDScreen):
    def __init__(self, title, description, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical", padding=dp(24), spacing=dp(18))

        back = MDRaisedButton(text="‹  Volver al inicio", size_hint_y=None, height=dp(48))
        back.bind(on_release=lambda *_: setattr(self.manager, "current", "inicio"))
        layout.add_widget(back)

        layout.add_widget(
            MDLabel(text=title, font_style="H4", bold=True, size_hint_y=None, height=dp(52))
        )
        layout.add_widget(
            MDLabel(text=description, font_style="Subtitle1", theme_text_color="Secondary")
        )

        self.content = MDLabel(
            text="Esta sección está lista para que agregues tus datos.",
            theme_text_color="Secondary",
        )
        layout.add_widget(self.content)
        self.add_widget(layout)