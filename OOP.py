from __future__ import annotations
import re
from abc import ABC, abstractmethod

"""адаптер__!, декоратор__!, синглтон__!, фабрика__!, фасад__!"""

#Monostate
#разные объекты но у них всех одни праметры
class Monostate:
    __data = {
        'adress': '127.0.0.0',
        'port': 8000
    }

    def __init__(self) -> None:
        self.__dict__ = self.__data


#Sigletone
#каждый новый оъект это сслыка на уже имеющиийся
class Singleton:
    _instances = None
    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
        return cls._instances
    
    def __del__(self):
        Singleton._instances = None
    
    def __init__(self, ip='127.0.0.0', port=8000) -> None:
        if self._instances is None:
            self.ip = ip
            self.port = port
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

#Adapter
#структурный шаблон проектирования, предназначенный для организации использования функций объекта,
# недоступного для модификации, через специально созданный интерфейс
class System: # Класс, представляющий систему
    def __init__(self, text):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor): # Метод, требующий на вход класс-обработчик
        result = processor.process_text(self.text) # Вызов метода обработчика
        print(*result, sep='\n')
        
class WordCounter: # Обработчик, несовместимый с основной системой
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()
    

class WordCounterAdapter(): # Адаптер к обработчику
    def __init__(self, adaptee): # В конструкторе указывается, к какому объекту следует подключить адаптер
        self.adaptee = adaptee

    def process_text(self, text): # Реализация интерфейса обработчика, требуемого системой.
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words, key=lambda x: self.adaptee.get_count(x), reverse=True)


#Factory
class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()
        # Далее, работаем с этим продуктом.
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass




class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")



#Facade
#структурный шаблон проектирования, позволяющий скрыть сложность системы
# путём сведения всех возможных внешних вызовов к одному объекту
class Tree:
    
    def grow(self):
        print("grow tree")
    
class Child:
    
    def born(self):
        print("born child")
    
class House:
    
    def build(self):
        print("build house")
    
    
class TheMenFacade:
    
    def __init__(self):
        self._tree = Tree()
        self._child = Child()
        self._house = House()
    
    def growTree(self):
        self._tree.grow()
        
    def bornChild(self):
        self._child.born()
        
    def buildHouse(self):
        self._house.build()
    

#Decorator
#структурный шаблон проектирования, предназначенный для динамического подключения дополнительного поведения к объекту.
class WrittenText:

	"""Represents a Written text """

	def __init__(self, text):
		self._text = text

	def render(self):
		return self._text

class UnderlineWrapper(WrittenText):

	"""Wraps a tag in <u>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<u>{}</u>".format(self._wrapped.render())

class ItalicWrapper(WrittenText):

	"""Wraps a tag in <i>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<i>{}</i>".format(self._wrapped.render())

class BoldWrapper(WrittenText):

	"""Wraps a tag in <b>"""

	def __init__(self, wrapped):
		self._wrapped = wrapped

	def render(self):
		return "<b>{}</b>".format(self._wrapped.render())

#Factoru_method_test
# print("App: Launched with the ConcreteCreator1.")
# client_code(ConcreteCreator1())
# print("\n")
# print("App: Launched with the ConcreteCreator2.")
# client_code(ConcreteCreator2())

#Decorator_test
# before_gfg = WrittenText("GeeksforGeeks")
# after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))
# print("before :", before_gfg.render())
# print("after :", after_gfg.render())

#Facade_test
# facade = TheMenFacade()
# facade.bornChild()
# facade.buildHouse()
# facade.growTree()

#Singleton_test
# a = Singleton(123, 2)
# b = Singleton(431, 3)
# print(b._instances)
# print(a.__dict__)

#Monostate_test
# a = Monostate()
# b = Monostate()
# print(b)
# print(a)
# print(id(a) is id(b))

#Adaptor
# text = 'la bla la la text test'
# system_one = System(text)
# system_two = WordCounter()
# adapter_one_two = WordCounterAdapter(system_two)
# system_one.get_processed_text(adapter_one_two)