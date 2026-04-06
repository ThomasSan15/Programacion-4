from datetime import datetime
 
 
class ProcesadorVenta:
    def __init__(self):
        self._ventas = []
 
    def generar_tiquete(self, cliente, plato):
        precio_base = plato.precio
        total       = cliente.precio_final(precio_base)
        descuento   = cliente.calcular_descuento(precio_base)
 
        tiquete = {
            "id_cliente": cliente.id_cliente,
            "nombre":        cliente.nombre,
            "plato":         plato.nombre,
            "precio_base":   precio_base,
            "descuento":     descuento,
            "total":         total,
            "hora":          datetime.now().strftime("%H:%M:%S"),
        }
 
        self._ventas.append(tiquete)
        self._imprimir_tiquete(tiquete)
        return tiquete
 
    def _imprimir_tiquete(self, tiquete):
        print("\n" + "=" * 42)
        print("          CAFETERÍA NutriUTP")
        print("=" * 42)
        print(f"  Hora       : {tiquete['hora']}")
        print(f"  cliente    : {tiquete['nombre']} ({tiquete['id_cliente']})")
        print(f"  Plato      : {tiquete['plato']}")
        print(f"  Precio base: ${tiquete['precio_base']:>10,.0f}")
        print(f"  Descuento  : ${tiquete['descuento']:>10,.0f}")
        print(f"  TOTAL      : ${tiquete['total']:>10,.0f}")
        print("=" * 42)
