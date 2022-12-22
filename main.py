from flight import FlightMap


def main(): 

	flight_map = FlightMap()

	flight_map.import_airports('public/aeroports.csv')
	flight_map.import_flights('public/flights.csv')

	# print(flight_map.airport_find("SEA"))


	print(flight_map.flights_where("SEA"))

	print(flight_map.flight_exist("AKL", "CPT"))
	print(flight_map.flight_exist("AKL", "CDG"))

	print(flight_map.airports_from("CDG"))
	print(flight_map.airports_from("CD"))



if __name__ == "__main__":
	main()