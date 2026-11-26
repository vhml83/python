# @Author: Victor Martin

import re
import random

class TorneoFutbol:

    # listas de equipos
    lista_8_equipos = []
    lista_4_equipos = []
    lista_2_equipos = []

    # constructor
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.total_goles_favor = 0
        self.total_goles_en_contra = 0

    # setters
    def set_resultado(self, puntos, goles_anotado, goles_en_contra):
        self.puntos += puntos
        self.total_goles_favor += goles_anotado
        self.total_goles_en_contra += goles_en_contra

    # getters
    def get_nombre(self):
        return self.nombre

    def get_puntos(self):
        return self.puntos

    def get_total_goles_favor(self):
        return self.total_goles_favor

    def get_total_goles_en_contra(self):
        return self.total_goles_en_contra

    @staticmethod
    def esperar_usuario():
        while True:
            ent = input("Presione 'Enter' para continuar... ")
            if ent == "":
                print("")
                break

    @classmethod
    def jugar_partido_cuartos(cls, x, y):
        equipo_1 = TorneoFutbol.lista_8_equipos[x]
        equipo_2 = TorneoFutbol.lista_8_equipos[y]
        print(f"\nIniciando el partido de cuartos de final entre los equipos: '{equipo_1.get_nombre()}' y '{equipo_2.get_nombre()}'")
        TorneoFutbol.esperar_usuario()
        goles_equipo_1 = random.randint(0, 3)  # rango de goles posibles
        goles_equipo_2 = random.randint(0, 3)  # rango de goles posibles
        print("\nEl árbitro da el silbatazo final...")
        TorneoFutbol.esperar_usuario()
        TorneoFutbol.mostrar_marcador(equipo_1, equipo_2, goles_equipo_1, goles_equipo_2)
        if goles_equipo_1 > goles_equipo_2:
            print(f"\nEl equipo '{equipo_1.get_nombre()}' avanza a la siguiente fase")
            equipo_1.set_resultado(3, goles_equipo_1, goles_equipo_2)
            equipo_2.set_resultado(0, goles_equipo_2, goles_equipo_1)
            TorneoFutbol.lista_4_equipos.append(equipo_1)
        elif goles_equipo_1 < goles_equipo_2:
            print(f"\nEl equipo '{equipo_2.get_nombre()}' avanza a la siguiente fase")
            equipo_1.set_resultado(0, goles_equipo_1, goles_equipo_2)
            equipo_2.set_resultado(3, goles_equipo_2, goles_equipo_1)
            TorneoFutbol.lista_4_equipos.append(equipo_2)
        else:
            print("\n¡El partido terminó en empate!")
            equipo_1.set_resultado(1, goles_equipo_1, goles_equipo_2)
            equipo_2.set_resultado(1, goles_equipo_2, goles_equipo_1)
            print("\nEl desempate se resolverá mediante un 'volado'...")
            TorneoFutbol.esperar_usuario()
            TorneoFutbol.jugar_volado(equipo_1, equipo_2, 'cuartos')
        TorneoFutbol.mostrar_puntaje(equipo_1, equipo_2)

    @classmethod
    def jugar_partido_semifinales(cls, x, y):
        equipo_1 = TorneoFutbol.lista_4_equipos[x]
        equipo_2 = TorneoFutbol.lista_4_equipos[y]
        print(f"\nIniciando el partido semifinales entre los equipos: '{equipo_1.get_nombre()}' y '{equipo_2.get_nombre()}'")
        TorneoFutbol.esperar_usuario()
        goles_equipo_1 = random.randint(0, 2)  # rango de goles posibles
        goles_equipo_2 = random.randint(0, 2)  # rango de goles posibles
        print("\nEl árbitro da el silbatazo final...")
        TorneoFutbol.esperar_usuario()
        TorneoFutbol.mostrar_marcador(equipo_1, equipo_2, goles_equipo_1, goles_equipo_2)
        if goles_equipo_1 > goles_equipo_2:
            print(f"\n¡El equipo '{equipo_1.get_nombre()}' avanza a la gran final!")
            equipo_1.set_resultado(3, goles_equipo_1, goles_equipo_2)
            equipo_2.set_resultado(0, goles_equipo_2, goles_equipo_1)
            TorneoFutbol.lista_2_equipos.append(equipo_1)
        elif goles_equipo_1 < goles_equipo_2:
            print(f"\n¡El equipo '{equipo_2.get_nombre()}' avanza a la gran final!")
            equipo_1.set_resultado(0, goles_equipo_1, goles_equipo_2)
            equipo_2.set_resultado(3, goles_equipo_2, goles_equipo_1)
            TorneoFutbol.lista_2_equipos.append(equipo_2)
        else:
            print("\n¡El partido terminó en empate!")
            equipo_1.set_resultado(1, goles_equipo_1, goles_equipo_2)
            equipo_2.set_resultado(1, goles_equipo_2, goles_equipo_1)
            print("\n-------- Equipos Empatados ------")
            TorneoFutbol.mostrar_puntaje(equipo_1, equipo_2)
            print("\nEl desempate se resolverá mediante el puntaje obtenido...")
            TorneoFutbol.esperar_usuario()
            if equipo_1.get_puntos() > equipo_2.get_puntos():
                print(f"\n¡El equipo '{equipo_1.get_nombre()}' ganó por puntos! +{str(equipo_1.get_puntos())}")
                print(f"\n¡El equipo '{equipo_1.get_nombre()}' avanza a la gran final!")
                TorneoFutbol.lista_2_equipos.append(equipo_1)
            elif equipo_1.get_puntos() < equipo_2.get_puntos():
                print(f"\n¡El equipo '{equipo_2.get_nombre()}' ganó por puntos! +{str(equipo_2.get_puntos())}")
                print(f"\n¡El equipo '{equipo_2.get_nombre()}' avanza a la gran final!")
                TorneoFutbol.lista_2_equipos.append(equipo_2)
            else:
                print("\n¡Hubo un empate en el puntaje!")
                TorneoFutbol.esperar_usuario()
                print("\nEl desempate se resolverá mediante diferencia de goles...")
                TorneoFutbol.esperar_usuario()
                diferencia_1 = equipo_1.get_total_goles_favor() - equipo_1.get_total_goles_en_contra()
                diferencia_2 = equipo_2.get_total_goles_favor() - equipo_2.get_total_goles_en_contra()
                if diferencia_1 > diferencia_2:
                    print(f"\n¡El equipo '{equipo_1.get_nombre()}' ganó por diferencia de goles! +{str(diferencia_1)}")
                    print(f"\n¡El equipo '{equipo_1.get_nombre()}' avanza a la gran final!")
                    TorneoFutbol.lista_2_equipos.append(equipo_1)
                elif diferencia_1 < diferencia_2:
                    print(f"\n¡El equipo '{equipo_2.get_nombre()}' ganó por diferencia de goles! +{str(diferencia_2)}")
                    print(f"\n¡El equipo '{equipo_2.get_nombre()}' avanza a la gran final!")
                    TorneoFutbol.lista_2_equipos.append(equipo_2)
                else:
                    print("\n¡Hubo un empate en la diferencia de goles!")
                    print(f"\nEl equipo '{equipo_1.get_nombre()}' tiene una diferencia de goles: +{str(diferencia_1)}")
                    print(f"\nEl equipo '{equipo_2.get_nombre()}' tiene una diferencia de goles: +{str(diferencia_2)}")
                    print("\nEl desempate se resolverá mediante un 'volado'...")
                    TorneoFutbol.esperar_usuario()
                    TorneoFutbol.jugar_volado(equipo_1, equipo_2, 'semifinal')
        TorneoFutbol.mostrar_puntaje(equipo_1, equipo_2)

    @classmethod
    def jugar_partido_final(cls, x, y):
        equipo_1 = TorneoFutbol.lista_2_equipos[x]
        equipo_2 = TorneoFutbol.lista_2_equipos[y]
        print(f"\nIniciando el partido de la Gran Final entre los equipos: '{str(equipo_1.get_nombre())}' y '{str(equipo_2.get_nombre())}' ")
        TorneoFutbol.esperar_usuario()
        goles_equipo_1 = random.randint(0, 1)  # rango de goles posibles
        goles_equipo_2 = random.randint(0, 1)  # rango de goles posibles
        print("\nEl árbitro da el silbatazo final...")
        TorneoFutbol.esperar_usuario()
        TorneoFutbol.mostrar_marcador(equipo_1, equipo_2, goles_equipo_1, goles_equipo_2)
        if goles_equipo_1 > goles_equipo_2:
            print(f"\n¡El equipo '{equipo_1.get_nombre()}' ganó el torneo!")
            equipo_1.set_resultado(3, goles_equipo_1, goles_equipo_2)
            equipo_2.set_resultado(0, goles_equipo_2, goles_equipo_1)
        elif goles_equipo_1 < goles_equipo_2:
            print(f"\n¡El equipo '{equipo_2.get_nombre()}' ganó el torneo!")
            equipo_1.set_resultado(0, goles_equipo_1, goles_equipo_2)
            equipo_2.set_resultado(3, goles_equipo_2, goles_equipo_1)
        else:
            print("\n¡El partido terminó en empate!")
            TorneoFutbol.jugar_penales(equipo_1, equipo_2)

    @classmethod
    def jugar_penales(cls, equipo_1, equipo_2):
        print("\n¡Inicia la tanda de Penales!")
        TorneoFutbol.esperar_usuario()
        # Variables tanda de penales
        numero_max_penales = 5
        turno = 1
        penales_equipo_1 = 0
        penales_equipo_2 = 0
        # Ciclo de tiros penales
        while numero_max_penales > 0:
            resultado_parcial = random.randint(0, 1)  # '0' el equipo falló; '1' el equipo anotó
            print(f"\nEs el turno del equipo '{equipo_1.get_nombre()}' de cobrar el penal #{str(turno)} ...")
            TorneoFutbol.esperar_usuario()
            if resultado_parcial == 0:
                print(f"\n¡El equipo '{equipo_1.get_nombre()}' falló su disparo en la portería contraria!")
                TorneoFutbol.esperar_usuario()
                print("-------- MARCADOR PARCIAL: TURNO " + str(turno) + "/5 ---------")
                print(equipo_1.get_nombre() + ": " + str(penales_equipo_1))
                print(equipo_2.get_nombre() + ": " + str(penales_equipo_2))
                print("-----------------------------------")
                TorneoFutbol.esperar_usuario
            else:
                print(f"\n¡El equipo '{equipo_1.get_nombre()}' anotó su disparo en la portería contraria!")
                TorneoFutbol.esperar_usuario()
                penales_equipo_1 += 1
                print("-------- MARCADOR PARCIAL: TURNO " + str(turno) + "/5 ---------")
                print(equipo_1.get_nombre() + ": " + str(penales_equipo_1))
                print(equipo_2.get_nombre() + ": " + str(penales_equipo_2))
                print("-----------------------------------")
                TorneoFutbol.esperar_usuario()
            if turno == 4:
                max_score = penales_equipo_2+2
                if (penales_equipo_1 > max_score):
                    break
            if turno == 5:
                max_score = penales_equipo_2+1
                if (penales_equipo_1 > max_score):
                    break
                if (penales_equipo_2 > penales_equipo_1):
                    break
            resultado_parcial = random.randint(0, 1)  # '0' el equipo falló; '1' el equipo anotó
            print(f"\nEs el turno del equipo '{equipo_2.get_nombre()}' de cobrar el penal #{str(turno)} ... ")
            TorneoFutbol.esperar_usuario()
            if resultado_parcial == 0:
                print(f"\n¡El equipo '{equipo_2.get_nombre()}' falló su disparo en la portería contraria!")
                TorneoFutbol.esperar_usuario()
                print("-------- MARCADOR PARCIAL: TURNO " + str(turno) + "/5 ---------")
                print(equipo_1.get_nombre() + ": " + str(penales_equipo_1))
                print(equipo_2.get_nombre() + ": " + str(penales_equipo_2))
                print("-----------------------------------")
                TorneoFutbol.esperar_usuario()
            else:
                print(f"\n¡El equipo '{equipo_2.get_nombre()}' anotó su disparo en la portería contraria!")
                TorneoFutbol.esperar_usuario()
                penales_equipo_2 += 1
                print("-------- MARCADOR PARCIAL: TURNO " + str(turno) + "/5 ---------")
                print(equipo_1.get_nombre() + ": " + str(penales_equipo_1))
                print(equipo_2.get_nombre() + ": " + str(penales_equipo_2))
                print("-----------------------------------")
                TorneoFutbol.esperar_usuario()
            if turno == 3:
                if (penales_equipo_1 - penales_equipo_2 == 3) or (penales_equipo_2 - penales_equipo_1 == 3):
                    break
            if turno == 4:
                max_score = penales_equipo_1+1
                if (penales_equipo_2 > max_score):
                    break         
            turno += 1
            numero_max_penales -= 1
        print("\n¡La ronda de penales ha terminado!")
        TorneoFutbol.esperar_usuario()
        print("-------- MARCADOR FINAL ---------")
        print(equipo_1.get_nombre() + ": " + str(penales_equipo_1))
        print(equipo_2.get_nombre() + ": " + str(penales_equipo_2))
        print("-----------------------------------", end="\n\n")
        TorneoFutbol.esperar_usuario()
        if penales_equipo_1 > penales_equipo_2:
            print(f"\n¡El equipo '{equipo_1.get_nombre()}' ganó el torneo!")
        elif penales_equipo_1 < penales_equipo_2:
            print(f"\n¡El equipo '{equipo_2.get_nombre()}' ganó el torneo!")
        else:
            print("El desempate se resolverá mediante un 'volado'...")
            TorneoFutbol.esperar_usuario()
            ganador_volado = random.randint(1, 2)
            if ganador_volado == 1:
                print(f"\n¡El equipo '{equipo_1.get_nombre()}' ganó el volado!")
                print(f"\n¡El equipo '{equipo_1.get_nombre()}' ganó el torneo!")
            else:
                print(f"\n¡El equipo '{equipo_2.get_nombre()}' ganó el volado!")
                print(f"\n¡El equipo '{equipo_2.get_nombre()}' ganó el torneo!")


    @classmethod
    def solicitar_nombres_equipos(cls):
        # solicitar nombres de 8 equipos y agregarlos a una lista
        max_numero_equipos = 8
        index = 1
        regex = r'(.*?)\w(.*?)'
        while max_numero_equipos > 0:
            nombre_equipo = input(f"Ingrese un nombre para el equipo #{str(index)}: ")
            is_repeated = True
            while True:
                # evitar que el usuario intente crear un equipo sin nombre
                if re.match(regex, nombre_equipo):
                    # evitar nombres de equipos repetidos
                    if len(TorneoFutbol.lista_8_equipos) > 0 and is_repeated:
                        for obj in TorneoFutbol.lista_8_equipos:
                            if obj.get_nombre() == nombre_equipo:
                                is_repeated = True
                                print("\nERROR: ¡El equipo '" + nombre_equipo + "' ya existe en el torneo!")
                                nombre_equipo = input(f"Ingrese otro nombre para el equipo #{str(index)}: ")
                                break
                            else:
                                is_repeated = False
                                continue
                    # crear una instancia "equipo futbol" con el nombre
                    else:
                        equipo = TorneoFutbol(nombre_equipo)
                        break
                else:
                    print("\nERROR: ¡El nombre del equipo no puede ser vacío!")
                    nombre_equipo = input(f"Ingrese nombre del equipo #{str(index)}: ")
            # agregar equipo a la lista de equipos
            TorneoFutbol.lista_8_equipos.append(equipo)
            print("\nEl equipo '" + nombre_equipo + "' ha sido agregado al torneo")
            index += 1
            max_numero_equipos -= 1
            print(f"Total de equipos agregados: {str(len(TorneoFutbol.lista_8_equipos))}/8")
            print("\n--------------------------------")

    @classmethod
    def mostrar_marcador(cls, equipo_1, equipo_2, goles_equipo_1, goles_equipo_2):
        print("\n¡Terminó el partido!")
        print("\nMarcador final:")
        print(equipo_1.get_nombre() + ": " + str(goles_equipo_1))
        print(equipo_2.get_nombre() + ": " + str(goles_equipo_2))
        print("--------------------------------")

    @classmethod
    def jugar_volado(cls, equipo_1, equipo_2, etapa):
        ganador_volado = random.randint(1, 2)  # simular un volado
        if ganador_volado == 1:
            print(f"\n¡El equipo '{equipo_1.get_nombre()}' ganó el volado!")
            print(f"\n¡El equipo '{equipo_1.get_nombre()}' avanza a la siguiente fase!")
            if etapa == 'cuartos':
                TorneoFutbol.lista_4_equipos.append(equipo_1)
            else:
                TorneoFutbol.lista_2_equipos.append(equipo_1)
        else:
            print(f"\n¡El equipo '{equipo_2.get_nombre()}' ganó el volado!")
            print(f"\n¡El equipo '{equipo_2.get_nombre()}' avanza a la siguiente fase!")
            if etapa == 'cuartos':
                TorneoFutbol.lista_4_equipos.append(equipo_2)
            else:
                TorneoFutbol.lista_2_equipos.append(equipo_2)
    
    @classmethod
    def mostrar_puntaje(cls, equipo_1, equipo_2):
        print("--------------------------------")
        print("Equipo: ", equipo_1.get_nombre())
        print("Puntos: ", equipo_1.get_puntos())
        print("Total de goles a favor: ", equipo_1.get_total_goles_favor())
        print("Total de goles en contra: ", equipo_1.get_total_goles_en_contra())
        print("--------------------------------")
        print("Equipo: ", equipo_2.get_nombre())
        print("Puntos: ", equipo_2.get_puntos())
        print("Total de goles a favor: ", equipo_2.get_total_goles_favor())
        print("Total de goles en contra: ", equipo_2.get_total_goles_en_contra())
        print("--------------------------------", end="\n\n")

    @classmethod
    def mostrar_tabla_inicial(cls):
        print("Lista de Equipos en el Torneo:", end="\n\n")
        for count, equipo in enumerate(TorneoFutbol.lista_8_equipos):
            print(count+1, equipo.get_nombre())

    @classmethod
    def mostrar_tabla_semifinales(cls):
        print("Equipos que avanzan a semifinales:", end="\n\n")
        for equipo in TorneoFutbol.lista_4_equipos:
            print("Equipo: ", equipo.get_nombre())
            print("Puntos: ", equipo.get_puntos())
            print("Total de goles a favor: ", equipo.get_total_goles_favor())
            print("Total de goles en contra: ", equipo.get_total_goles_en_contra())
            print("--------------------------------")

    @classmethod
    def mostrar_tabla_final(cls):
        print("Equipos que se enfrentarán en la gran final:", end="\n\n")
        for equipo in TorneoFutbol.lista_2_equipos:
            print("Equipo: ", equipo.get_nombre())
            print("Puntos: ", equipo.get_puntos())
            print("Total de goles a favor: ", equipo.get_total_goles_favor())
            print("Total de goles en contra: ", equipo.get_total_goles_en_contra())
            print("--------------------------------")


print("---------- Bienvenido al Torneo -------------", end="\n\n")
TorneoFutbol.solicitar_nombres_equipos()

TorneoFutbol.esperar_usuario()

TorneoFutbol.mostrar_tabla_inicial()

print("---------- Inicio del Torneo -------------", end="\n\n")
TorneoFutbol.esperar_usuario()

print("--- Primer Partido de Cuartos de Final ---")
TorneoFutbol.jugar_partido_cuartos(0, 1)

TorneoFutbol.esperar_usuario()

print("--- Segundo Partido de Cuartos de Final ---")
TorneoFutbol.jugar_partido_cuartos(2, 3)

TorneoFutbol.esperar_usuario()

print("--- Tercer Partido de Cuartos de Final ---")
TorneoFutbol.jugar_partido_cuartos(4, 5)

TorneoFutbol.esperar_usuario()

print("--- Último Partido de Cuartos de Final ---")
TorneoFutbol.jugar_partido_cuartos(6, 7)

TorneoFutbol.esperar_usuario()

print("\n--- Los Partidos de Cuartos de Final han terminado ---")

TorneoFutbol.esperar_usuario()

TorneoFutbol.mostrar_tabla_semifinales()

TorneoFutbol.esperar_usuario()

print("--- Primer Partido de Semifinales ---")
TorneoFutbol.jugar_partido_semifinales(0, 1)

TorneoFutbol.esperar_usuario()

print("--- Último Partido de Semifinales ---")
TorneoFutbol.jugar_partido_semifinales(2, 3)

TorneoFutbol.esperar_usuario()

print("--- Los Partidos de Semifinales han terminado ---", end="\n\n")

TorneoFutbol.esperar_usuario()

TorneoFutbol.mostrar_tabla_final()

TorneoFutbol.esperar_usuario()

print("--- Inicia el Partido de la Gran Final ---")
TorneoFutbol.jugar_partido_final(0, 1)

TorneoFutbol.esperar_usuario()

print("--- FIN ---")
