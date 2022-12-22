from flight import FlightMap, FlightPath

def main(): 

	flight_map = FlightMap()

	flight_map.import_airports('public/aeroports.csv')
	flight_map.import_flights('public/flights.csv')

	# print(flight_map.airport_find("SEA"))



	# print(flight_map.flight_exist("AKL", "CPT"))
	# print(flight_map.flight_exist("AKL", "CDG"))

	# print(flight_map.airports_from("CDG"))
	# print(flight_map.airports_from("CD"))

	airport = flight_map.airport_find("CDG")
	airport2 = flight_map.airport_find("AMS")

	flights = flight_map.flights_where("CDG")
	# print(flights)

	for flight in flights:
		print(flight)

	flight_path = FlightPath(airport)
	flight_path.add(airport2, flights[2])





	print(flight_path.flights())
	print(flight_path.airports())
	print(flight_path.steps())
	print(flight_path.duration())


if __name__ == "__main__":
	main()