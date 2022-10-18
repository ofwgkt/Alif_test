class ProductList:
    def init(self, file_name):
        self.__file_name = file_name

    def add(self, product):
        with open(self.__file_name, 'a', encoding='cp1251') as f:
            f.write(f'{product.get_name()} — {product.get_price()} \n')
