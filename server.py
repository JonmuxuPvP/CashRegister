# This class holds a Shop's data. 
# It simulates a Server although it's just a class holding local information.
# Server does not need to be instantiated as an object as all of its methods are static.
class Server:
    current_product_id = 0
    current_ticket_id = 0
    tickets = []
    products = {}

    @classmethod
    def generate_product_id(self):
        id = self.current_product_id
        self.current_product_id += 1
        return id

    @classmethod
    def add_product(self, new_product):
        key = new_product.manufacturer
        temp_list = []
        new_product.id = Server.generate_product_id()
        if key in self.products:
            temp_list = self.products.get(key)
            temp_list.append(new_product)
            self.products[key] = temp_list
        else:
            temp_list.append(new_product)
            self.products[key] = temp_list
        
        
    @classmethod
    def remove_product(self, product):
        for key in self.products.keys():
            if product in self.products.get(key):
                self.products.get(key).remove(product)

    @classmethod
    def print_products(self):
        output = '\n'
        for key in self.products.keys():
            output += f'[{key}]\n'
            for product in self.products.get(key):
                output += f'{product} - ID: {product.id} \n'
            output += '\n'
        return output

    @classmethod
    def generate_ticket_id(self):
        id = self.current_ticket_id
        self.current_ticket_id += 1
        return id

    @classmethod
    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    @classmethod
    def print_tickets(self):
        for ticket in self.tickets:
            print(ticket)

    @classmethod
    def read_tickets_from_file(self):
        pass

    @classmethod
    def write_tickets_from_file(self):
        pass