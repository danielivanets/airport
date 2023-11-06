from controllerAirport import ControllerAirport
controller = ControllerAirport()

def getIata():
    iata = ""
    while True:
        iata = input("Enter the IATA: ")
        if len(iata) == 3:
            break
        print("Error entering the IATA - [AAA]")
    return iata.upper()

while True:
    print("")
    print(controller.countAirports(),"airports!")
    print("1.- Import an airport")
    print("2.- Delete an airport")
    print("3.- Add a flight operator to an airport")
    print("4.- Delete a flight operator from an airport")
    print("5.- List airports by operators")
    print("6.- List number of planes by operator – (by airport / all)")
    print("7.- Exit")
    option = int(input("Select an option: "))
    

    #EXIT
    if option == 7:
        print("Bye!")
        break

    ##########################################
    #           IMPORT airport               #
    ##########################################
    elif option == 1:
        iata = getIata()
        if (controller.addAirport(iata)):
            print("Airport added!")
        else:
            print("Error adding the airport")

    ##########################################
    #              DELETE airport            #
    ##########################################
    elif option == 2:
        iata = getIata()
        if (controller.deleteAirport(iata)):
            print("Airport deleted!")
        else:
            print("Error deleting")


    ##########################################
    #       ADD operator TO AN airport       #
    ##########################################
    elif option == 3:
        iata = getIata()
        name = input("Enter the operator name: ")
        planes = int(input("Enter the planes of the operator: "))
        if controller.addOperator(iata,name,planes):
            print("Operator added!")
        else:
            print("Error adding operator")

    ##########################################
    #  DELETE the operator from the airport  #
    ##########################################
    elif option == 4:
        iata = getIata()
        name = input("Enter the operator name: ")
        if controller.deleteOperator(iata,name):
            print("Operator removed!")
        else:
            print("Error removing operator")
    ##################################################
    # List all the airports where the operator works #
    ##################################################
    elif option == 5:
        name = input("Enter the operator name: ")
        aeropuertos = controller.listAirportsOperatorWorks(name)
        if len(aeropuertos) > 0:
            print("The operator ",name," works in this airports:")
            for a in aeropuertos:
                print("\n",a.getName(),a.getLocation(),a.getIata())
        else:
            print("Error. This operator doesn't works in any airport")
   
    ##############################################################
    #   LIST number of planes BY operators – (by airport / all)  #
    ##############################################################
    elif option == 6:
        print("\n1.Count planes in all airports")
        print("2.Count planes in one airport")
        coption = int(input("Select count option: "))
        ##############################################
        # list the number of planes in this airport  #
        ##############################################
        if coption == 1:
            operator = input("Enter the operator name: ")
            planes = controller.listAllPlanesInTheOperator(operator)
            if planes > 0:
                print("The operator ",operator," has ",planes," planes in all airports")
            else:
                print("Error. This operator doesn't have any plane in any airport")
        #####################################
        # list all planes for this operator #
        #####################################
        elif coption == 2:
            operator = input("Enter the operator name: ")
            iata = getIata()
            planes = controller.listAllPlanesInTheAirport(iata,operator)
            if planes > 0:
                print("The operator ",operator," has ",planes," planes in ",iata," airport")
            else:
                print("Error. This operator doesn't have any plane in ",iata," airport")