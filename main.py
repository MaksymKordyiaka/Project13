'''
1.З використанням наслідування- створити два класи, в них же задати два конструктори, які
прийматимуть різну кількість аргументів.

2.Створити метод за допомогою якого можливо змінювати атрибути об’єкту в батьківському класі.

3.Створити в кожному з класів методи, при зверненні до якого- об’єкт передасть рандомну
кількість пар елементів та в результаті отримає дві множини (ключі / значення) які
будуть одразу ж присвоєні для двох змінних. Зверніть увагу- значення словника можуть
бути змінним типом даних, тоді як елементи сету- ні. Відповідно потрібно виконати
перевірку та перетворення типів.
'''

class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def keys(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
        if isinstance(self.key1, set):
            self.key1 = tuple(self.key1)
        if isinstance(self.key2, set):
            self.key2 = tuple(self.key2)
        return self.key1, self.key2

class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def method(self, new_a, new_b):
        self.a = new_a
        self.b = new_b

    def values(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1, self.value2

obj_b = B(1, 3, 5)
n1, n2 = obj_b.keys({'a', 'b'}, {'c', 'd'})
n3, n4 = obj_b.values({1, 2}, {3, 4})
print(n1, n2)
print(n3, n4)

dct = {}
dct[n1] = n3
dct[n2] = n4
print(dct)























