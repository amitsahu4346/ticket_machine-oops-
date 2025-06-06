from importlib import resources
from datetime import datetime 


class Printer:
    def __init__(self):
        self.resources = {
            'paper':10,
            'ink': 5
        }

    def report(self):
        '''Prints a report of all printer resources''' 
        for key in self.resources:
            print(f"{key}: {self.resources[key]}, tickets left")
        input()

    def has_enough_resources(self):
        '''Returns True if ticket can be printed or return false if Paper and Ink is not sufficient.''' 
        for key in self.resources:
            if self.resources[key] < 1:
                print(f'Sorry there is not enough {key} to print ticket')
                return False 
        return True



    def print_ticket(self, station):
        '''Print Ticket with From, To and Cost Detail'''
        print('------------ Ticket --------------')
        print("From: Vidisha")
        print(f"To: {station.name}")
        print(f"Cost: {station.cost}")
        print(f"Printed: {str(datetime.now())}")
        print('----------------------------------')
        input()

        for key in self.resources:
            self.resources[key] = self.resources[key] - 1