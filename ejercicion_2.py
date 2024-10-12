# Clase Cliente
class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono, documento_identidad, metodo_pago):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.documento_identidad = documento_identidad
        self.metodo_pago = metodo_pago

# Clase Vuelo

class Vuelo:
    def __init__(self, id_vuelo, origen, destino, fecha_hora_salida, fecha_hora_llegada, duracion, aeronave, estado_vuelo):
        self.id_vuelo = id_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora_salida = fecha_hora_salida
        self.fecha_hora_llegada = fecha_hora_llegada
        self.duracion = duracion
        self.aeronave = aeronave
        self.estado_vuelo = estado_vuelo
        self.asientos = []

    def agregar_asiento(self, asiento):
        self.asientos.append(asiento)

# Clase Asiento
class Asiento:
    def __init__(self, id_asiento, numero_asiento, clase_asiento, disponibilidad=True):
        self.id_asiento = id_asiento
        self.numero_asiento = numero_asiento
        self.clase_asiento = clase_asiento
        self.disponibilidad = disponibilidad

# Clase Aeronave
class Aeronave:
    def __init__(self, id_aeronave, modelo, capacidad):
        self.id_aeronave = id_aeronave
        self.modelo = modelo
        self.capacidad = capacidad
        self.asientos = []

    def agregar_asientos(self, asientos):
        self.asientos.extend(asientos)

# Clase Aerolínea
class Aerolinea:
    def __init__(self, id_aerolinea, nombre):
        self.id_aerolinea = id_aerolinea
        self.nombre = nombre
        self.vuelos = []

    def agregar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)

# Clase Reserva
class Reserva:
    def __init__(self, id_reserva, cliente, vuelo, asiento, fecha_reserva, precio_total, estado_reserva="Confirmada"):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.vuelo = vuelo
        self.asiento = asiento
        self.fecha_reserva = fecha_reserva
        self.precio_total = precio_total
        self.estado_reserva = estado_reserva

    def cancelar_reserva(self):
        self.estado_reserva = "Cancelada"
        self.asiento.disponibilidad = True
