class Libro:
    def __init__(self, libro_id, titulo, autor, editorial, anio_publicacion, genero, isbn):
        self.libro_id = libro_id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.anio_publicacion = anio_publicacion
        self.genero = genero
        self.isbn = isbn
        self.estado = "Disponible"  # Estado inicial del libro

    def marcar_como_prestado(self):
        self.estado = "Prestado"
        print(f"El libro '{self.titulo}' ahora está prestado.")

    def marcar_como_disponible(self):
        self.estado = "Disponible"
        print(f"El libro '{self.titulo}' ahora está disponible.")

    def verificar_disponibilidad(self):
        return self.estado == "Disponible"


# Clase Usuario
class Usuario:
    def __init__(self, IDusuario, nombre, direccion, telefono, email, tipo_usuario):
        self.__IDusuario = IDusuario
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.tipo_usuario = tipo_usuario
        self.historial_prestamos = []  # Lista para almacenar préstamos del usuario
        self.multas = []  # Lista para almacenar las multas del usuario
        self.reservas = []  # Lista para almacenar las reservas del usuario

    def mostrar_ID(self):
        print(f"El ID del usuario es: {self.__IDusuario}")

    def actualizar_datos(self, direccion=None, telefono=None, email=None):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
        if email:
            self.email = email
        print(f"Datos actualizados para el usuario {self.nombre}.")

    def agregar_prestamo(self, prestamo):
        self.historial_prestamos.append(prestamo)
        print(f"El préstamo '{prestamo.libro.titulo}' ha sido agregado al historial de {self.nombre}.")

    def agregar_multa(self, multa):
        self.multas.append(multa)
        print(f"Se ha agregado una multa a {self.nombre} por: {multa.descripcion}.")

    def reservar_libro(self, reserva):
        self.reservas.append(reserva)
        print(f"El libro '{reserva.libro.titulo}' ha sido reservado por {self.nombre}.")


# Clase Bibliotecario
class Bibliotecario:
    def __init__(self, IDbibliotecario, nombre, telefono, email, turno):
        self.IDbibliotecario = IDbibliotecario
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.turno = turno

    def registrar_prestamo(self, usuario, libro):
        if libro.verificar_disponibilidad():
            prestamo = Prestamo(libro, usuario)
            libro.marcar_como_prestado()
            usuario.agregar_prestamo(prestamo)
            print(f"Préstamo registrado: Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible para préstamo.")

    def registrar_devolucion(self, libro):
        libro.marcar_como_disponible()
        print(f"Devolución registrada: El libro '{libro.titulo}' está disponible nuevamente.")

    def gestionar_reserva(self, usuario, libro):
        reserva = Reserva(libro, usuario)
        usuario.reservar_libro(reserva)
        print(f"Reserva registrada: El libro '{libro.titulo}' ha sido reservado por {usuario.nombre}.")


# Clase Préstamo
class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.estado = "Activo"

    def marcar_como_devuelto(self):
        self.estado = "Devuelto"
        print(f"El préstamo del libro '{self.libro.titulo}' ha sido marcado como devuelto.")


# Clase Reserva
class Reserva:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.estado = "Reservado"


# Clase Multa
class Multa:
    def __init__(self, descripcion, monto):
        self.descripcion = descripcion
        self.monto = monto
        self.estado = "Pendiente"

    def pagar_multa(self):
        self.estado = "Pagada"
        print(f"La multa de '{self.descripcion}' ha sido pagada.")