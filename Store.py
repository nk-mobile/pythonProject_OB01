class Store:
    """Добавляет новый магазин."""
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Возвращает цену товара, если он есть в ассортименте."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price

    def __repr__(self):
        return f"Store(name='{self.name}', address='{self.address}', items={self.items})"

# Создание объектов класса Store
store1 = Store("Перекрёсток", "123 Адрес Адрес Адрес")
store2 = Store("Магнит", "123 Адрес Адрес Адрес")
store3 = Store("Лента", "123 Адрес Адрес Адрес")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("oranges", 0.6)
store2.add_item("grapes", 1.2)

store3.add_item("milk", 1.5)
store3.add_item("bread", 2.0)

# Тестирование методов на одном из магазинов
# Распечатка товаров магазина №1
print("О магазине №1:\n", store1)
# Добавить товар и печать товаров вместе с новыми
store1.add_item("oranges", 0.65)
print("После добавления товара 'oranges':\n", store1)
# Обновить цену товара
store1.update_price("apples", 0.55)
print("После обновления цены of 'apples':\n", store1)
# Удалить товар
store1.remove_item("bananas")
print("После удаления товара 'bananas':\n", store1)
# Распечатка цены выбранного (oranges) товара
price = store1.get_price("oranges")
print("\nЦена товара 'oranges':", price)
# Распечатка цены выбранного (bananas) товара
price = store1.get_price("bananas")
print("Цена товара после удаления 'bananas' (should be None):", price)