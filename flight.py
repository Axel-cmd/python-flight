import csv
from airport import Airport

def formatString(text: str) -> str:
	return text.replace('"', "").replace(" ", "")


class Flight:
	def __init__(self, src_code: str, dst_code: str, duration: float) -> None:
		self.src_code = src_code
		self.dst_code = dst_code
		self.duration = duration


class FlightPathBroken(Exception):
	def __init__(self, *args: object) -> None:
		super().__init__(*args)


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

				try :
					duration = float(duration)
				except ValueError:
					print('Erreur dans le CSV')
					continue



				flight = Flight(origin, destination, duration)

				self.__flights.append(flight)

	def airport_find(self, airport_code: str) -> Airport:
		try :
			airport = self.__airports[airport_code]
			return airport
		except KeyError:
			print(f"L'aéroport {airport_code} n'a pas été trouvé !")
			return None
	
	def flight_exist(self, src_airport_code: str, dst_airport_code: str) -> bool :
		for flight in self.__flights:
			if flight.src_code == src_airport_code \
				and flight.dst_code == dst_airport_code:
				return True
			else : 
				return False	
			
	def flights_where(self, airport_code: str) -> list[Flight]:
		flights = []
		for flight in self.__flights:
			if flight.src_code == airport_code or flight.dst_code == airport_code:

				flights.append(flight)
		return flights

	def airports_from(self, airport_code: str) -> list[Airport]:
		destinations = []

		for flight in self.__flights:

			if flight.src_code == airport_code:
				airport = self.__airports[flight.dst_code]
			elif flight.dst_code == airport_code:
				airport =  self.__airports[flight.src_code]
			else : 
				continue

			if airport not in destinations:
				print(airport.code)
				destinations.append(airport)


		return destinations


