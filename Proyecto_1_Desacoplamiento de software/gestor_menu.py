
DIAS_SEMANA = {
    0: "lunes",
    1: "martes",
    2: "miercoles",
    3: "jueves",
    4: "viernes",
    5: "sabado",
    6: "domingo",
} # Diccionario que asigna cada número (0–6) a un día de la semana.


class GestorMenus:
    def __init__(self):
        self._menus = {}

    def registrar_menu(self, dia_semana, menu):
        self._menus[dia_semana.lower()] = menu
    def menu_por_dia(self, dia):
        return self._buscar_menu(dia.lower().strip())
    def _buscar_menu(self, dia):
        menu = self._menus.get(dia)
        if menu is None:
            print(f"No hay menú registrado para el {dia}.")
        return menu
