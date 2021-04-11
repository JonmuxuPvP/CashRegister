from server import Server
from datetime import date
import time

class CashRegister:

    # TODO Add a payment method, either credit card or cash
    # Find ways to format strings better
    def checkout(self):
        ticket_id = Server.generate_ticket_id()
        time_tuple = time.localtime()
        date_time = time.strftime('%m/%d/%Y, %H:%M:%S', time_tuple) 
        product_info = ''
        total = 0
        payment_method = None

        products = input('Product IDs: ')
        ids = products.split(',')

        for key in Server.products.keys():
            for product in Server.products.get(key):
                for id in ids:
                    if product.id == int(id):
                        total += product.price
                        product_info += product.get_info()

        given = int(input('Money: '))
        exchange = given - total

        ticket = Ticket(ticket_id, date_time, product_info, payment_method, 
                        round(given, 2), round(exchange, 2), round(total, 2))
        # print(ticket)
        Server.add_ticket(ticket)


class Product:

    def __init__(self, name, price, manufacturer):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer

    def get_info(self):
        return f'{self.name}\t\t{self.price}\n'

    def __str__(self):
        return f'Name: {self.name} - Price: {self.price}'


class Ticket:

    def __init__(self, ticket_id, date_time, product_info, payment_method, given, exchange, total):
        self.ticket_id = ticket_id
        self.date_time = date_time
        self.product_info = product_info
        self.payment_method = payment_method
        self.given = given
        self.exchange = exchange
        self.total = total

    def __str__(self):
        output = f'--------------------------------\n'
        output += f'Date: {self.date_time}\n'
        output += f'Ticket: #{self.ticket_id}\n'
        output += f'Payment Method: {self.payment_method}\n\n'
        output += f'{self.product_info}\n'
        output += f'Given:\t\t\t{self.given}\nExchange:\t\t{self.exchange}\nTotal:\t\t\t{self.total}\n'
        output += f'--------------------------------'
        return output