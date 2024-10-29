class Product:
    def __init__(self, name: str, wight: float, category: str):
        self.name = name
        self.wight = wight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.wight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r+')
        read_file = file.read()
        file.close()
        return read_file

    def add(self, *products):
        file = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in open(self.__file_name).read():
                file.write(f'{product.name}, {product.wight}, {product.category}\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())








