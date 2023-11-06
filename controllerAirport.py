from airport import Airport
import AirportAPI as api

class ControllerAirport():
    def __init__(self):
        self.__airports = {}
    
    # COUNT total of airports in our list
    def countAirports(self):
        return len(self.__airports)

    #1 CREATE airport from the IATA and add to list
    def addAirport(self,iata):
        if iata in self.__airports:
            return False
        newAirport = api.getAirport(iata)
        self.__airports[iata] = newAirport
        print(self.__airports[iata])
        return True

    def addAirport2(self, iata):
        if iata in self.__airports:
            return False
        newAirport = Airport(iata)  # Create an instance of the Airport class
        self.__airports[iata] = newAirport
        return True
    
    #2 DELETE airport from the IATA, if there aren’t planes
    def deleteAirport(self,iata):
        if iata not in self.__airports:
            return False
        #airport = self.__airports[iata]
        #operators = airport.getOperators()
        #if len(operators) > 0:
        #    return False
        print(self.__airports)
        self.__airports.pop(iata)
        print(self.__airports)
        return True
    
    #3 ADD operator
    def addOperator(self,iata,name,planes):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        airport.addOperator(name,planes)
        return True

    #4 DELETE operator FROM airport
    def deleteOperator(self,iata,name):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        airport.deleteOperator(name)
        return True

    #5 LIST all the airports WHERE the operator works
    def listAirportsOperatorWorks(self,ope):
        airports = []
        for key,value in self.__airports.items():
            if ope in value.getOperators():
                airports.append(value)
        return airports

###################################################################
    #COUNT all planes in operator
    def listAllPlanesInTheOperator(self,operator):
        count = 0
        for key,value in self.__airports.items():
            if operator in value.getOperators():
                planes = value.getOperators()[operator]
                count += planes
        return count
    #COUNT the number of planes in one airport
    def listAllPlanesInTheAirport(self,iata,operator):
        count = 0
        if iata in self.__airports:
            aeropuerto = self.__airports[iata]
            if operator in aeropuerto.getOperators():
                operadores = aeropuerto.getOperators()[operator]
                count += operadores
        return count