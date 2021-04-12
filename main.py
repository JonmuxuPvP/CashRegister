from shop import Product, CashRegister, Server

def main():
    cr = CashRegister('Test')

    list = [Product('N64 Controller', 49.99, 'Nintendo'), Product('PS4 Controller', 29.99, 'Sony'), 
            Product('GC Controller', 129.99, 'Nintendo'), Product('PS2 Controller', 12.99, 'Sony'),
            Product('PS1 Controller', 34.99, 'Sega'), Product('Wii Remote', 24.99, 'Nintendo'),
            Product('Switch Pro Controller', 99.99, 'Sega'), Product('Nunchuck Controller', 4.99, 'Sega')]

    for product in list:
        Server.add_product(product)

    print(Server.print_products())

    cr.checkout()
    input('Printing all the tickets...')
    Server.print_tickets()

if __name__ == '__main__':
    main()