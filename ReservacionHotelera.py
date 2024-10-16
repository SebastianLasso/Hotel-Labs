# Un sistema que permita reservar habitaciones en un hotel. 
# Cada habitación tiene un número, tipo (individual, doble)
# Puede ser reservada por un huésped.

class Habitacion:
    def __init__(self, numero_habitacion, tipo_habitacion):
        self.numero_habitacion = numero_habitacion  # Número de la habitación
        self.tipo_habitacion = tipo_habitacion  # Tipo de la habitación: "individual" o "doble"
        self.disponible = True  # La habitación está disponible inicialmente
        self.huesped = None  # No hay huésped asignado al inicio

    def reservar(self, huesped):
        """Reservar la habitación para un huésped"""
        if self.disponible:
            self.disponible = False  # Cambiar estado a no disponible
            self.huesped = huesped
            print(f"Habitación {self.numero_habitacion} ha sido reservada por {huesped}.")
        else:
            print(f"Habitación {self.numero_habitacion} no está disponible.")

    def liberar(self):
        """Liberar la Habitación"""
        if not self.disponible:
            self.disponible = True  # Cambiar estado a disponible
            print(f"Habitación {self.numero_habitacion} ha sido liberada por {self.huesped}.")
            self.huesped = None  # Quitar al huésped
        else:
            print(f"Habitación {self.numero_habitacion} ya está disponible.")

    def mostrar_estado(self):
        """Estado de la Habitación"""
        estado = "disponible" if self.disponible else f"ocupada por {self.huesped}"
        print(f"Habitación {self.numero_habitacion} ({self.tipo_habitacion}) está {estado}.")


class Hotel:
    def __init__(self, huesped, habitaciones_info):
        self.huesped = huesped
        self.habitaciones = []  # Lista de habitaciones en el hotel

        # Inicializar las habitaciones directamente al crear el hotel
        for numero, tipo in habitaciones_info:
            self.habitaciones.append(Habitacion(numero, tipo))

    def mostrar_habitaciones(self):
        """Estado de todas las Habitaciones"""
        print(f"\nEstado actual de las habitaciones en {self.huesped}:")
        for habitacion in self.habitaciones:
            habitacion.mostrar_estado()

    def reservar_habitacion(self, numero_habitacion, huesped):
        """Reservar una habitación específica por su número"""
        habitacion = self._encontrar_habitacion(numero_habitacion)
        if habitacion:
            habitacion.reservar(huesped)

    def liberar_habitacion(self, numero_habitacion):
        """Liberar una habitación específica por su número"""
        habitacion = self._encontrar_habitacion(numero_habitacion)
        if habitacion:
            habitacion.liberar()

    def _encontrar_habitacion(self, numero_habitacion):
        """Método privado para encontrar una habitación por su número"""
        for habitacion in self.habitaciones:
            if habitacion.numero_habitacion == numero_habitacion:
                return habitacion
        print(f"Habitación {numero_habitacion} no encontrada.")
        return None


# Crear el hotel con las habitaciones definidas al inicio
habitaciones_info = [(101, "individual"), (102, "doble"), (103, "doble"),
(105, "individual"), (106, "individual"),(107, "doble"), (108, "doble"), (109, "doble")]

hotel = Hotel("El Hotel Central Villa del Rosario", habitaciones_info)

# Mostrar estado inicial de las habitaciones
hotel.mostrar_habitaciones()

# Reservar habitaciones
hotel.reservar_habitacion(101, "Juan Cardona")
hotel.reservar_habitacion(102, "Luisa Hernandez")

# Intentar reservar una habitación ya ocupada
hotel.reservar_habitacion(101, "Hernesto Buendia")

# Mostrar estado de las habitaciones después de las reservas
hotel.mostrar_habitaciones()

# Liberar una habitación
hotel.liberar_habitacion(101)

# Mostrar estado de las habitaciones después de liberar
hotel.mostrar_habitaciones()