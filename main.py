"""Punto de entrada de SmartCost."""
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from lib.storage import init_db
from screens.home_screen import HomeScreen, MODULES
from screens.module_screen import ModuleScreen
from screens.cost_calculator_screen import CostCalculatorScreen
from screens.recetas_screen import RecetasScreen
from screens.ingenieria_menu_screen import IngenieriaMenuScreen
from screens.menu_visual_screen import MenuVisualScreen
from screens.plantillas_screen import PlantillasScreen

# Pantallas que ya tienen funcionalidad propia (conectadas a SQLite).
# El resto se sigue mostrando como ModuleScreen (placeholder).
PANTALLAS_FUNCIONALES = {
    "calcular_costos", "mis_recetas", "ingenieria_de_menu", "menu_visual", "mis_plantillas"
}

DESCRIPCIONES = {
    "configuracion": "Ajusta moneda, unidades y preferencias de la aplicación.",
    "acerca_de": "SmartCost te ayuda a tomar mejores decisiones para tu negocio.",
}


class SmartCostApp(MDApp):
    def build(self):
        self.title = "SmartCost"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepOrange"

        init_db()

        manager = ScreenManager()
        manager.add_widget(HomeScreen())
        manager.add_widget(CostCalculatorScreen())
        manager.add_widget(RecetasScreen())
        manager.add_widget(IngenieriaMenuScreen())
        manager.add_widget(MenuVisualScreen())
        manager.add_widget(PlantillasScreen())

        for title, _subtitle, _icon, _color, screen_name in MODULES:
            if screen_name in PANTALLAS_FUNCIONALES:
                continue
            manager.add_widget(
                ModuleScreen(
                    title=title,
                    description=DESCRIPCIONES.get(screen_name, ""),
                    name=screen_name,
                )
            )

        return manager


if __name__ == "__main__":
    SmartCostApp().run()