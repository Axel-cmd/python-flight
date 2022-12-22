import csv
from airport import Airport

def formatString(text: str) -> str:
	return text.replace('"', "").replace(" ", "")


class Flight:
	def __init__(self, src_code: str, dst_code: str, duration: float) -> None:
		self.src_code = src_code
		self.dst_code = dst_code
		self.duration = duration


class FlightMap:
	def __init__(self) -> None:
		# dictionnaire des aéroports
		self.__airports = {}
		#Liste des vols 
		self.__flights = []

	def airports(self) -> list[Airport]:
		return self.__airports.values()

	def flights(self) -> list[Flight]:
		return self.__flights

	def import_airports(self, csv_file: str) -> None:

		with open(csv_file, 'r') as file:
			reader = csv.reader(file)

			for row in reader:

				name, code, latitude, longitude = row

				#formater les données récupéré
				name, code = formatString(name), formatString(code)
				latitude = float(formatString(latitude))
				longitude = float(formatString(longitude))

				airport = Airport(name, code, latitude, longitude)

				self.__airports[code] = airport

	def import_flights(self, csv_file: str) -> None:
		with open(csv_file, 'r') as file:
			reader = csv.reader(file)

			for row in reader:
				origin, destination, duration = row

				origin, destination = formatString(origin), formatString(destination)

				duration = float(duration)

				try :
					origin_airport = self.__airports[origin]
					destination_airport = self.__airports[destination]
				except KeyError:
					print(f"Aéroport introuvable pour le vol de {origin} vers {destination}")
					continue


				flight = Flight(origin_airport, destination_airport, duration)

				self.__flights.append(flight)

	def airport_find(self, airport_code: str) -> Airport:
		try :
			airport = self.__airports[airport_code]
			return airport
		except KeyError:
			print(f"L'aéroport {airport_code} n'a pas été trouvé !")
			return None
			


