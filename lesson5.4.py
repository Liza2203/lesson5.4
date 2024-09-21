# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#          print(first)
#          print(second)
#          print(third)
# ex = Example('data', second=25, third=3.14)

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return  self.number_of_floors

    def __str__(self):
        result=str(f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")
        return result

    def __eq__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors==other.number_of_floors
    def __lt__(self,other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors<other.number_of_floors
    def __le__(self,other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors<=other.number_of_floors
    def __gt__(self,other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors>other.number_of_floors
    def __ge__(self,other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors>=other.number_of_floors
    def __ne__(self,other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors!=other.number_of_floors
    def __add__(self,value):
        if isinstance(value, int):
            self.number_of_floors=self.number_of_floors+value
        return self
    def __radd__(self,value):
        if isinstance(value, int):
            return self.__add__(value)
    def __iadd__(self,value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    houses_history = []
    def __new__(cls, *args,**kwargs):
        house_name=args[0] if args else 'No name'
        obj=super().__new__(cls)
        cls.houses_history.append(house_name)
        return obj


    def __del__(self):
        result=str(f"{self.name} снесён, но он останется в истории")
        print(result)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

