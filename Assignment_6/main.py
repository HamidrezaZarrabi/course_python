from pyfiglet import Figlet
import sys
import qrcode

def show_menu():
    print('welcome to the biggest computer store. Specify your operation: ')
    print('1- Add Product')
    print('2- Edit Product')
    print('3- Delete Product')
    print('4- Search')
    print('5- Show Product')
    print('6- Buy')
    print('7- Generate QR code')
    print('8- Exit')

def add_product(products):
    id = input('Enter ID of product: ')
    for product in products:
        if product['id'] == id:
            print('This product is repetitious and is available in database')
            break
    else:
        product = dict()
        product['id'] = id
        product['name'] = input('Enter name of product: ')
        product['price'] = input('Enter price of product: ')
        product['count'] = input('Enter count of product: ')
        products.append(product)
        print('Product added into database')
    return products

def edit_product(products):
    id = input('Enter id of product that you want to edit: ')
    item = input('Enter item that you want to edit: ')
    item_value = input('Enter new value: ')
    for product in products:
        if product['id'] == id:
            product[item] = item_value
            print('Product edited ........ ')
            break
    return products

def delete_product(products):
    id = input('Enter id of product that you want to delete: ')
    for product in products:
        if product['id'] == id:
            products.remove(product)
            print('Product removed ....... ')
            break
    return products

def serach_product(products):
    name = input('Enter name of product that you want to search: ')
    for product in products:
        if product['name'] == name:
            print(product)
            break
    else:
        print('product not found')

def show_product(products):
    for product in products:
        print(product)

def buy_product(products):
    number_products = int(input('Enter number of product types: '))
    total_price = 0
    receipt = list()
    for number in range(number_products):
        print('Product {}'.format(number+1))
        id = input('Enter id of product that you want to buy: ')
        for product in products:
            if product['id'] == id:
                count = int(input('Enter number of product that you want to buy: '))
                if (int(product['count']) - count) >= 0:
                    product['count'] = str(int(product['count']) - count)
                    receipt.append({'id': id, 'name': product['name'], 'price': product['price'], 'count': count})
                    total_price += (int(count) * int(product['price']))
                else:
                    print('Unfortunately we dont have this number of product')
                break
        else:
            print('Unfortunately we dont have this product')

    print('Thank you for your sale .......... ')
    print('receipt: ', receipt)
    print("total_price: ", total_price)
    return products

def qr_code(products):
    id = input('Enter id of product that you want its qr code: ')
    for product in products:
        if product['id'] == id:
            img = qrcode.make(product)
            img.save('qr_code.png')
            print('Generated QR code ...... ')

def exit_program(products):
    file_database = open('database.txt', 'w')
    for product in products:
        file_database.write(product['id'] + ',' + product['name'] + ',' + product['price'] + ',' + product['count'] + '\n')
    print('Exiting ........')
    sys.exit()

def read_database():
    print('Loading database ....... ')
    file_database = open('database.txt', 'r')
    products = list()
    for line in file_database:
        product = {}
        line = line.strip()
        product_list = line.split(',')
        product['id'] = product_list[0]
        product['name'] = product_list[1]
        product['price'] = product_list[2]
        product['count'] = product_list[3]
        products.append(product)
    return products

if __name__ == '__main__':
    f = Figlet(font='standard')
    print(f.renderText('Computer Store'))
    products = read_database()
    show_menu()
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            products = add_product(products)
        elif choice == '2':
            products = edit_product(products)
        elif choice == '3':
            products = delete_product(products)
        elif choice == '4':
            serach_product(products)
        elif choice == '5':
            show_product(products)
        elif choice == '6':
            products = buy_product(products)
        elif choice == '7':
            qr_code(products)
        elif choice == '8':
            exit_program(products)
        else:
            print("Invalid input")

