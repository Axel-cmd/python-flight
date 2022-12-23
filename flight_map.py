import csv
from airport import Airport
from flight import Flight
from flight_path import FlightPath

def formatCsvString(text: str) -> str:
    return text.replace('"', "").replace(" ", "")


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
                name, code = formatCsvString(name), formatCsvString(code)
                latitude = float(formatCsvString(latitude))
                longitude = float(formatCsvString(longitude))

                airport = Airport(name, code, latitude, longitude)

                self.__airports[code] = airport

    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                origin, destination, duration = row

                origin, destination = formatCsvString(origin), formatCsvString(destination)

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

    def paths(self, src_airport_code: str, dst_airport_code: str) -> list[FlightPath]:

      paths = []

      # initialise les structures de données
      flight_paths = {}
      airports_not_visited = self.__airports.copy()
      airports_future = {src_airport_code}
      airports_visited = set()

      if len(flight_paths) == 0:
        flight_paths[src_airport_code] = FlightPath(src_airport_code)

      #tant qu'il y a des aéroport à visité 
      while airports_future:

        # aéroports à visiter prochainement
        airports_next = set()

        #on parcours les aéroport à visiter 
        for airport in airports_future:
          # pour chaque prochain aéroport accessible 
          for flight in self.flights_where(airport):
            # s'y la destination n'a pas déjà été visité 
            if flight.dst_code not in airports_visited:
              # on l'ajoute dans les prochaines destinations
              airports_next.add(flight.dst_code)
            
              next_flight_path = flight_paths[flight.src_code].copy() 


        # mettre à jour les données

        airports_visited |= airports_future
        

      return paths
    


