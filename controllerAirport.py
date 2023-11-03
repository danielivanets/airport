#from airport import Airport
import AirportAPI as api

class ControllerAirport():
    def __init__(self):
        self.__airports = {}
    
    '''
    #1 IMPORT AIRPORT
    def addAirport(self,iata,name,location,city,country,website,phone):
        if iata in self.__airports:
            return False
        newAirport = Airport(iata,name,location,city,country,website,phone)
        self.__airports[iata] = newAirport
        return True
    '''
    # COUNT total of airports in our list
    def countAirports(self):
        return len(self.__airports)

    #1 CREATE airport from the IATA and add to list
    def addAirport(self,iata):
        if iata in self.__airports:
            return False
        newAirport = api.getAirport(iata)
        self.__airports[iata] = newAirport
        return True







    #2 DELETES AN AIRPORT SEARCHING THE IATA, IF THIS PLANES ARE 0
    def deleteAirport(self,iata):
        if iata not in self.__airports:
            return False
        #operators = airport.getOperators()
        #if len(operators) > 0:
        #    return False
        print(self.__airports)
        self.__airports.pop(iata)
        print(self.__airports)
        return True
            
    #3 ADD OPERATOR
    def addOperator(self,iata,name,planes):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        airport.addOperator(name,planes)
        return True

    #4 REMOVE OPERATOR FROM AIRPORT
    def deleteOperator(self,iata,name):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        airport.deleteOperator(name)
        return True

    #5 LIST ALL THE AIRPORTS WHERE THE OPERATOR WORKS
    def list5(self,ope):
        aeropuertos = []
        for key,value in self.__airports.items():
            if ope in value.getOperators():
                aeropuertos.append(value)
        return aeropuertos

    def list6General(self,operator):
        count = 0
        for key,value in self.__airports.items():
            if operator in value.getOperators():
                planes = value.getOperators()[operator]
                count += planes
        return count

    def list6Airport(self,iata,operator):
        count = 0
        if iata in self.__airports:
            aeropuerto = self.__airports[iata]
            if operator in aeropuerto.getOperators():
                operadores = aeropuerto.getOperators()[operator]
                count += operadores
        return count


"""
class AirportController():
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

    #2 DELETE airport from the IATA, if there aren’t planes
    def deleteAirport(self,iata):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        self.__airports.pop(iata)
        return True
    
    #3 ADD operator
    def addOperator(self,iata,nameCompany,planes):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        airport.addOperator(nameCompany, planes)
        return True

    #4 REMOVE operator FROM airport
    def deleteOperator(self,iata,nameCompany):
        if iata not in self.__airports:
            return False
        airport = self.__airports[iata]
        airport.deleteOperator(nameCompany)
        return True

    #5 LIST all the AIRPORTS WHERE the operator works
    def list5(self,operador):
        aeropuertos = []
        for key,value in self.__airports.items():
            if operador in value.getOperators():
                aeropuertos.append(value)
        return aeropuertos




"""
"""
    def list6General(self,operator):
        count = 0
        for key,value in self.__airports.items():
            if operator in value.getOperators():
                planes = value.getOperators()[operator]
                count += planes
        return count

    def list6Airport(self,iata,operator):
        count = 0
        if iata in self.__airports:
            aeropuerto = self.__airports[iata]
            if operator in aeropuerto.getOperators():
                operadores = aeropuerto.getOperators()[operator]
                count += operadores
        return count
"""
