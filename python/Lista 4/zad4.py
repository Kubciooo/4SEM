from inspect import getfullargspec


class Function(object):
    "Obiekt funkcji, żebyśmy mieli tę funkcję w słowniku i mogli na niej pracować"
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        f = Function_dictionary.get_instance().get(self.func, *args)
        if not f: raise Exception("Nie ma takiej funkcji")
        return f(*args, **kwargs)

    def get(self, args=None):
        if args is None: 
            args = getfullargspec(self.func).args
        return tuple([self.func.__module__, self.func.__class__, self.func.__name__, len(args or [])])
    
class Function_dictionary(object):
    "Singleton, który zawiera słownik funkcji, które mają @overload"
    __instance  = None
    def __init__(self):
        if self.__instance  is None: 
            self.functions_gathered = dict() 
            Function_dictionary.__instance = self
            
    @staticmethod
    def get_instance():
        if Function_dictionary.__instance is None: 
            Function_dictionary()
        return Function_dictionary.__instance

    def register(self, func):
        "dodaj funkcję do słownika"
        f = Function(func) # stwórz objekt tej funkcji i dodaj go do słownika
        self.functions_gathered[f.get()] = func
        return f
        
    def get(self, func, *args):
        " zwróc funkcję, która posiada len(*args) argumentów i None jeżeli taka nie istnieje"
        f = Function(func)
        return self.functions_gathered.get(f.get(args=args))


def overload(func):
    return Function_dictionary.get_instance().register(func)

@overload
def norm(x,y,z):
    return abs(x) + abs(y) + abs(z)

@overload
def norm(x,y):
    return x*y

print(norm(1,2,3))
print(norm(1,2))
print(norm(1))
