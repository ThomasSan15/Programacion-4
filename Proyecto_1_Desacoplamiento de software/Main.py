from Plato import Plato
from Menu_Dia import MenuDia
from comensal import Comensal
from comensal import Descuento
from procesador_venta import ProcesadorVenta
from gestor_menu import GestorMenu


def configurar_menu():
    gestor = GestorMenu()

    lunes = MenuDia("lunes")
    lunes.agregar_plato(Plato("Pollo a la plancha con papas", 11000))
    lunes.agregar_plato(Plato("Tortilla española",             9000, es_vegetariano=True))
    lunes.agregar_plato(Plato("Fríjoles con chicharrón",      12000))
    lunes.agregar_plato(Plato("Ensalada César",                8500, es_vegetariano=True))

    martes = MenuDia("martes")
    martes.agregar_plato(Plato("Carne en bistec con arroz",   12000))
    martes.agregar_plato(Plato("Hamburguesa vegetariana",     10000, es_vegetariano=True))
    martes.agregar_plato(Plato("Sancocho de pollo",           13000))
    martes.agregar_plato(Plato("Ensalada de quinoa",           9000, es_vegetariano=True))

    miercoles = MenuDia("miercoles")
    miercoles.agregar_plato(Plato("Arroz con cerdo",          11500))
    miercoles.agregar_plato(Plato("Quinoa con verduras",       9500, es_vegetariano=True))
    miercoles.agregar_plato(Plato("Ajiaco santafereño",       12500))
    miercoles.agregar_plato(Plato("Arepas rellenas de queso",  8000, es_vegetariano=True))

    jueves = MenuDia("jueves")
    jueves.agregar_plato(Plato("Sobrebarriga al horno",       13000))
    jueves.agregar_plato(Plato("Crema de champiñones",         8500, es_vegetariano=True))
    jueves.agregar_plato(Plato("Carne a la parrilla",         14000))
    jueves.agregar_plato(Plato("Lasaña vegetariana",          10500, es_vegetariano=True))

    viernes = MenuDia("viernes")
    viernes.agregar_plato(Plato("Filete de pescado frito",    12500))
    viernes.agregar_plato(Plato("Pasta al pesto",              9000, es_vegetariano=True))
    viernes.agregar_plato(Plato("Bandeja paisa mini",         11500))
    viernes.agregar_plato(Plato("Pizza margarita",             9500, es_vegetariano=True))

    gestor.registrar_menu("lunes",     lunes)
    gestor.registrar_menu("martes",    martes)
    gestor.registrar_menu("miercoles", miercoles)
    gestor.registrar_menu("jueves",    jueves)
    gestor.registrar_menu("viernes",   viernes)

    return gestor


def seleccionar_menu(gestor):
    print("\n Seleccion de menú:")
    print("  Elegir día manualmente")

    while True:

            dia  = input("  Ingresa el día al que quiere saber su menú (lunes, martes, ...): ").strip()
            menu = gestor.menu_por_dia(dia)
            if menu:
                return menu
            else:
             print("  Opción inválida, no es un día válido, intente de nuevo.")




def pedir_datos_cliente():
    print("\n--- Datos del cliente ---")
    id_cliente = input("  Ingrese su ID          : ").strip()
    nombre        = input("  Ingrese su nombre      : ").strip()
    
    tipos_clientes = set()
    tipos_subsidio = set()

    for cliente, subsidio in Descuento.keys():
        tipos_clientes.add(cliente)
        tipos_subsidio.add(subsidio)

    print(f"  Tipos de subsidio: {', '.join(tipos_subsidio)}")
    while True:
        tipo_subsidio_ = input("  Tipo subsidio: ").strip().lower()
        if tipo_subsidio_ in tipos_subsidio:
            break
        print(f"  Tipo de subsidio inválido , digitelo de nuevo. Opciones: {', '.join(tipos_subsidio)}")
        
    print(f"  Tipos de cliente: {', '.join(tipos_clientes)}")
        
    while True:
        tipo_cliente_ = input("  Tipo cliente: ").strip().lower()
        if tipo_cliente_ in tipos_clientes:
            break
        print(f"  Tipo de cliente inválido, digite su opcion de nuevo. Opciones: {', '.join(tipos_clientes)}")
        
    return Comensal(id_cliente, nombre, tipo_subsidio_, tipo_cliente_)


def pedir_seleccion_plato(menu):
    while True:
        preferencia = input("\n  Preferencia: estandar/vegetariano ").strip().lower()
        if preferencia in ("estandar", "vegetariano"):
            break
        print("  Preferencia inválida, digite su opcion de nuevo.")

    opciones = menu.seleccionar_opcion(preferencia)

    if not opciones:
        print("  No hay platos disponibles para esa preferencia.")
        return None

    print(f"\n  --- Opciones {preferencia} ---")
    for i, plato in enumerate(opciones, start=1):
        print(f"  {i}. {plato.descripcion_detallada()}")

    while True:
        try:
            numero = int(input("\n  Elige tu plato (número): "))
            plato  = menu.seleccionar_por_numero(opciones, numero)
            if plato:
                return plato
            print("  Número fuera de rango, intenta de nuevo.")
        except ValueError:
            print("  Ingresa un número válido.")


def main():
    gestor = configurar_menu()
    menu   = seleccionar_menu(gestor)

    if menu is None:
        return

    procesador = ProcesadorVenta()

    while True:
        menu.mostrar_menu()

        cliente = pedir_datos_cliente()
        plato      = pedir_seleccion_plato(menu)

        if plato is None:
            continue

        tiquete = procesador.generar_tiquete(cliente, plato)
        procesador.validar_pago(tiquete["total"])

        otro = input("¿Atender otro cliente? (s/n): ").strip().lower()
        if otro != "s":
            break

    procesador.reporte_cierre()


if __name__ == "__main__":
    main()
