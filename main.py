from stations import Stations
from printer import Printer
from money import Money



stations = Stations()
printer = Printer()
money = Money()

is_on = True 
while is_on:
    print(stations.get_stations())
    choice = input("Where you wanna go:")
    
    if choice == 'off':
        is_on = False
    
    if choice == 'report':
        money.report()
        printer.report()


    else:
        station = stations.find_station(choice)
        if station is None:
            print("Wrong Input")
        else: 
            if printer.has_enough_resources() and money.make_payment(station.cost):
                printer.print_ticket(station)

