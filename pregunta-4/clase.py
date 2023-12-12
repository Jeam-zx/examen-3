class ClassType:
    """
    Una clase para representar un tipo de clase en una simulación.
    """

    def __init__(self, name, superclass=None):
        """
        Construye todos los atributos necesarios para el objeto de la clase.
        """
        self.name = name
        self.superclass = superclass
        self.methods = {}

    def add_method(self, method):
        """
        Agrega un método a la clase.
        """
        self.methods[method] = f'{self.name} :: {method}'

    def get_method(self, method):
        """
        Devuelve el método si existe en la clase o en su superclase.

        """
        if method in self.methods:
            return self.methods[method]
        elif self.superclass:
            return self.superclass.get_method(method)
        else:
            return None


class Simulator:
    def __init__(self):
        self.classes = {}

    def add_class(self, name, methods, superclass_name=None):
        """
        Agrega una nueva clase al simulador.
        """
        # Verifica si el nombre de la clase ya existe en el simulador
        if name in self.classes:
            print(f'Error: La clase {name} ya existe.\n')
            return
        # Verifica si el nombre de la superclase existe en el simulador
        if superclass_name and superclass_name not in self.classes:
            print(f'Error: La super clase {superclass_name} no existe.\n')
            return
        # Verifica si hay nombres de métodos duplicados
        if len(set(methods)) < len(methods):
            print('Error: Nombres de métodos duplicados.\n')
            return
        # Obtiene la superclase del diccionario de clases
        superclass = self.classes.get(superclass_name)
        # Verifica si la clase está intentando heredar de sí misma
        while superclass:
            if superclass.name == name:
                print(f'Error: La clase {name} no puede heredar de ella misma.\n')
                return
            superclass = superclass.superclass
        # Obtiene la superclase del diccionario de clases
        superclass = self.classes.get(superclass_name)
        # Crea una nueva instancia de ClassType
        new_class = ClassType(name, superclass)
        # Agrega los métodos a la nueva clase
        for method in methods:
            new_class.add_method(method)
        # Agrega la nueva clase al diccionario de clases
        self.classes[name] = new_class

    def describe_class(self, name):
        """
        Describe una clase existente en el simulador.
        """

        # Verifica si el nombre de la clase existe en el simulador
        if name not in self.classes:
            print(f'Error: La clase {name} no existe.\n')
            return
        # Obtiene la clase del diccionario de clases
        class_type = self.classes[name]
        # Crea un conjunto para almacenar los métodos impresos
        printed_methods = set()

        string_methods = ""
        # Recorre la clase y sus superclases
        while class_type:
            # Recorre los métodos de la clase
            for method in class_type.methods:
                # Verifica si el método ya ha sido impreso
                if method not in printed_methods:
                    # Incluye el método al string y lo agrega al conjunto de métodos impresos
                    if not string_methods:
                        string_methods = f'{method} -> {class_type.get_method(method)}'
                    else:
                        string_methods += f'\n{method} -> {class_type.get_method(method)}'
                    printed_methods.add(method)
            # Avanza a la superclase
            class_type = class_type.superclass
        # Verifica si se imprimieron métodos
        if not printed_methods:
            string_methods = f'La clase {name} no tiene métodos.'
        return string_methods













































