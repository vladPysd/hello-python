class Parser:
    def __init__(self) -> None:
        pass
    
    def __convert_types(self, value_str):
        result = 0
        if isinstance(value_str, str):
            if "." in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result
    
    def parse(self, expression):
        packed_values = tuple(expression.split(' '))
        if(len(packed_values)<3):
            print("Wrong indentation, check your expression")
            return 0, 0, "+"
        a, op, b = packed_values
        a = self.__convert_types(a)
        b = self.__convert_types(b)
        return a, b, op
        
class Core:
    def __init__(self) -> None:
        self._parser = Parser()
        self._functions = {
            "+": lambda a, b: a+b,
            "-": lambda a, b: a-b,
            "/": lambda a, b: a/b,
            "*": lambda a, b: a*b,
        }
    
    def calculate(self, expression):
        a, b, op = self._parser.parse(expression)
        result = self._functions.get(op)(a, b)
        return result
    
class Interface:
    def __init__(self) -> None:
        self._core = Core() 
        
    def run_culcaltor(self):
        while(True):
            print("Enter your expression: eg. '2 + 2' ")
            expression = input()
            result = self._core.calculate(expression)
            print(f'Result: {result}')
            print("="*10)
            
if __name__ == "__main__":
    calculator = Interface()
    calculator.run_culcaltor()