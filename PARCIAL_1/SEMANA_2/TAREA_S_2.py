"""
TAREA_SEMANA_2.py

Ejemplo simple de Programación Orientada a Objetos (POO): Clase Estudiante.

La clase Student modela un estudiante real con atributos básicos y métodos
para actualizar y mostrar información. Incluye una pequeña demostración
cuando se ejecuta como script.
"""

from typing import Dict, Any


class Student:
	"""Representa a un estudiante.

	Atributos:
		nombre (str): Nombre completo del estudiante.
		edad (int): Edad en años.
		matricula (str): Número de matrícula o identificación.
		carrera (str): Carrera o especialidad.
		promedio (float): Promedio académico (puede ser en escala 0-100 o 0-20,
						  según convención). El comportamiento de aprobación
						  puede ajustarse mediante el parámetro passing_mark.
	"""

	def __init__(self, nombre: str, edad: int, matricula: str, carrera: str, promedio: float):
		# Validaciones simples
		if edad < 0:
			raise ValueError("La edad no puede ser negativa")
		if promedio < 0:
			raise ValueError("El promedio no puede ser negativo")

		self.nombre = nombre
		self.edad = edad
		self.matricula = matricula
		self.carrera = carrera
		self.promedio = float(promedio)

	def mostrar_informacion(self) -> None:
		"""Imprime la información del estudiante de forma legible."""
		print(f"Nombre    : {self.nombre}")
		print(f"Edad      : {self.edad}")
		print(f"Matrícula : {self.matricula}")
		print(f"Carrera   : {self.carrera}")
		print(f"Promedio  : {self.promedio}")

	def actualizar_promedio(self, nuevo_promedio: float) -> None:
		"""Actualiza el promedio del estudiante con validación simple."""
		if nuevo_promedio < 0:
			raise ValueError("El promedio no puede ser negativo")
		self.promedio = float(nuevo_promedio)

	def es_aprobado(self, passing_mark: float = 60.0) -> bool:
		"""Retorna True si el estudiante alcanza la nota de aprobación.

		passing_mark: Marca mínima para aprobar. Por defecto 60 (escala 0-100).
		Si tu institución usa escala 0-20, ajusta passing_mark a 11.0.
		"""
		return self.promedio >= passing_mark

	def to_dict(self) -> Dict[str, Any]:
		"""Serializa el objeto a un diccionario (útil para guardar o mostrar)."""
		return {
			"nombre": self.nombre,
			"edad": self.edad,
			"matricula": self.matricula,
			"carrera": self.carrera,
			"promedio": self.promedio,
		}

	@classmethod
	def from_dict(cls, data: Dict[str, Any]) -> "Student":
		"""Crea una instancia de Student a partir de un diccionario."""
		return cls(
			nombre=data.get("nombre", ""),
			edad=int(data.get("edad", 0)),
			matricula=data.get("matricula", ""),
			carrera=data.get("carrera", ""),
			promedio=float(data.get("promedio", 0.0)),
		)

	def __str__(self) -> str:
		return f"{self.nombre} ({self.matricula}) - {self.carrera} - Prom: {self.promedio}"


def _demo():
	"""Demostración de uso de la clase Student."""
	# Crear estudiantes de ejemplo
	s1 = Student("Ana Pérez", 20, "2026-001", "Ingeniería", 78.5)
	s2 = Student("Luis Gómez", 22, "2026-002", "Derecho", 58.0)

	print("-- Información inicial --")
	s1.mostrar_informacion()
	print()
	s2.mostrar_informacion()
	print()

	# Actualizar promedio y verificar aprobación
	print(f"¿{s1.nombre} aprobó? {s1.es_aprobado(60)}")
	print(f"¿{s2.nombre} aprobó? {s2.es_aprobado(60)}")
	print()

	print("-- Actualizando promedio de Luis a 65.0 --")
	s2.actualizar_promedio(65.0)
	print(f"{s2.nombre} ahora tiene promedio {s2.promedio} y aprobó? {s2.es_aprobado(60)}")


if __name__ == "__main__":
	_demo()


