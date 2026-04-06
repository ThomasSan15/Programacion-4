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
        ancho = 44

        print("\n+" + "─" * ancho + "+")
        print(f"|{'CAFETERÍA NutriUTP':^{ancho}}".ljust(ancho) + "|")
        print("+" + "─" * ancho + "+")

        print(f"| {'Hora':<12}: {tiquete['hora']:<28} |".ljust(ancho))
        print(f"| {'Cliente':<12}: {tiquete['nombre']} ({tiquete['id_cliente']})".ljust(ancho) + " |")
        print(f"| {'Plato':<12}: {tiquete['plato']}".ljust(ancho) + " |")
        print(f"| {'Precio base':<12}: $ {tiquete['precio_base']:>10,.0f}".ljust(ancho) + " |")
        print(f"| {'Descuento':<12}: $ {tiquete['descuento']:>10,.0f}".ljust(ancho) + " |")
        print(f"| {'TOTAL':<12}: $ {tiquete['total']:>10,.0f}".ljust(ancho) + " |")

        print("+" + "─" * ancho + "+")
 
    def validar_pago(self, total):
        # Punto de integración con el sistema de tesorería de la UTP
        print(f"  [Tesorería] Pago de ${total:,.0f} aprobado.\n")
        return True
 
    def reporte_cierre(self):
        if not self._ventas:
            print("No hay ventas registradas.")
            return
 
        total_recaudado = sum(v["total"] for v in self._ventas)
 
        print("\n" + "=" * 42)
        print("          REPORTE DE CIERRE")
        print("=" * 42)
        for v in self._ventas:
            print(f"  {v['nombre']:<22} ${v['total']:>8,.0f}")
        print("-" * 42)
        print(f"  {'TOTAL RECAUDADO':<22} ${total_recaudado:>8,.0f}")
        print("=" * 42)
 
