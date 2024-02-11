from product import Product
import os


class ProductList:
    def __init__(self, file_name):
        self.__file_name = file_name_yes

    def add(self, product):
        with open(self.__file_name, 'a', encoding='cp1251') as f:
            f.write(f'{product.get_name()} — {product.get_price()} \n')

    def delete(self, product_name):
        products = self.__get_products()
        os.remove(self.__file_name)

        for product in products:
            if product.get_name() == product_name:
                continue
            self.add(product)

    def edit_price(self, product_name, new_price):
        products = self.__get_products()
        os.remove(self.__file_name)

        for product in products:
            if product.get_name() == product_name:
                product.set_price(new_price)
            self.add(product)

    def edit_name(self, old_product_name, new_product_name):
        products = self.__get_products()
        os.remove(self.__file_name)

        for product in products:
            if product.get_name() == old_product_name:
                product.set_name(new_product_name)
            self.add(product)

    def get_total_amount(self):
        total = 0
        products = self.__get_products()

        for product in products:
            total += product.get_price()

        return total

    def __get_products(self):
        products = []

        with open(self.__file_name, 'r') as f:
            for line in f:
                product_split = line.split(' — ')
                product_name = product_split[0]
                price = int(product_split[1])

                product = Product(product_name, price)
                products.append(product)

        return products
