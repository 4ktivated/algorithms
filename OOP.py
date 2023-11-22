"""адаптер, декоратор, синглтон__!, фабрика, фасад"""


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
class Adapter:
   pass


#Factory
class Factory:
   pass


a = Singleton(123, 2)
b = Singleton(431, 3)
print(b._instances)
print(a.__dict__)


# a = Monostate()
# b = Monostate()
# print(b)
# print(a)
# print(id(a) is id(b))
