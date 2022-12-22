from flight import Flight
from airport import Airport
from math import fsum

class FlightPathBroken(Exception):
	pass

class FlightPath: 
	def __init__(self, src_airport: Airport) -> None:
		self.__airports = []
		self.__airports.append(src_airport)
		self.__path: list[Flight] = []
		

	def add(self, dst_airport : Airport, via_flight : Flight) -> None :
		"""Ajouter un vol au chemin"""
		if via_flight.src_code == self.__airports[-1].code :
			self.__path.append(via_flight)
			self.__airports.append(dst_airport)
		else : 
			raise FlightPathBroken("Problème")

	def flights(self) -> list[Flight]:
		return self.__path

	def airports(self) -> list[Airport]:
		return self.__airports

	def steps(self) -> float:
		return len(self.__path)

	def duration(self) -> float:
		return fsum([flight.duration for flight in self.__path])

