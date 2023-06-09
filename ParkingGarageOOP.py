#from sys import displayhook
#from tkinter.ttk import DisplayStyle#
from time import sleep
from tkinter import Tk
from tkinter.ttk import Label
from PIL import ImageTk, Image

root = Tk()

image1 = Image.open("image1.jpg")
image1_tk = ImageTk.PhotoImage(image1)
label1 = Label(root, image=image1_tk)
label1.pack()

image2 = Image.open("image2.jpg")

image2_tk = ImageTk.PhotoImage(image2)
label2 = Label(root, image=image2_tk)
label2.pack()

class EwaSamParkGarage():
    def __init__(self):
        self.tickets = list(range(1, 11))
        self.parkingSpaces = list(range(1, 11))
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            space = self.parkingSpaces.pop(0)
            self.currentTicket[ticket] = {'paid': False, 'space': space}
            print(f'Please take ticket {ticket} for your parking spot')
            print(f'Available parking spaces: {self.parkingSpaces}')
            return ticket
        else:
            print('Sorry, the garage is currently full')
            return None

    def payForParking(self):
        ticket = input('Please enter your parking ticket number: ')
        try:
            ticket = int(ticket)
            if ticket in self.currentTicket and not self.currentTicket[ticket]['paid']:
                payment = input('Please enter the payment amount: ')
                if float(payment) < 10:
                    print('Payment received. You have 15 minutes to leave.')
                    self.currentTicket[ticket]['paid'] = True
                else:
                    print('Payment received. Thank you for your generosity!')
                    self.currentTicket[ticket]['paid'] = True
            else:
                print('Invalid ticket number or ticket already paid')
        except ValueError:
            print('Invalid input')

    def leaveGarage(self):
        ticket = input('Please enter your parking ticket number: ')
        try:
            ticket = int(ticket)
            if ticket in self.currentTicket and self.currentTicket[ticket]['paid']:
                space = self.currentTicket[ticket]['space']
                self.parkingSpaces.insert(0, space)
                self.tickets.append(ticket)
                del self.currentTicket[ticket]
                print('Thank you, have a nice day!')
                print(f'Available tickets: {self.tickets}')
                print(f'Available parking spaces: {self.parkingSpaces}')
            elif ticket in self.currentTicket and not self.currentTicket[ticket]['paid']:
                payment = input('Please pay for your parking ticket: ')
                if float(payment) < 10:
                    print('Payment received. Thank you, have a nice day!')
                else:
                    print('Payment received. Thank you for your generosity!')
                self.currentTicket[ticket]['paid'] = True
                space = self.currentTicket[ticket]['space']
                self.parkingSpaces.insert(0, space)
                self.tickets.append(ticket)
                print(f'Available tickets: {self.tickets}')
                print(f'Available parking spaces: {self.parkingSpaces}')
            else:
                print('Invalid ticket number')
        except ValueError:
            print('Invalid input')

    def run(self):
        if image1:
            label1.pack()
        else:
            print("Welcome to Parking!")

    def bye(self):
        if image2:
            label2.pack()
        else:
            print("\nThanks for hanging with us today! Let's do it again sometime!")


    def my_car(self):
        self.run()
        while True:
                action = input(
                    "\nHow can I help you? \nOptions:Take Ticket\nPay\nLost Ticket\nExit\n").lower()
                if action == 'pay':
                    self.payForParking()
                elif action == 'take ticket':
                    self.takeTicket()
                elif action == 'lost ticket':
                    print("\nFor damages on your car or loss of property, please call 911")
                    print("For any other issues, pleae contact Parking Manager at 347-000-1111.\n")
                    sleep(5)
                elif action == 'exit':
                    response = input("Did you already pay y/n \n")
                    if response.lower() == 'n':
                        print("Please pay!")
                        self.payForParking
                        sleep(4)
                        self.leaveGarage()
                    elif response.lower == 'y':
                        self.leaveGarage()
                        sleep(4)
                    break
                else:
                    print("Invalid option.")




my_car = EwaSamParkGarage()
my_car.my_car()

root.mainloop()


