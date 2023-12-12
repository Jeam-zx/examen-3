import unittest
from clase import Simulator, ClassType


class TestSimulator(unittest.TestCase):
    """
    Esta es una clase de prueba para la clase Simulator.
    """

    def setUp(self):
        """
        Este método se llama antes de cada prueba.
        Prepara el entorno de prueba.
        Aquí, crea una nueva instancia de la clase Simulator.
        """
        self.simulador = Simulator()

    def test_class_creation_with_valid_data(self):
        """
        Esta prueba verifica si se puede crear una clase con datos válidos.
        Agrega una clase con nombre "C" y métodos "i" y "j".
        Luego verifica si la clase fue creada y si los métodos son correctos.
        """
        self.simulador.add_class("C", ["i", "j"])
        self.assertIsInstance(self.simulador.classes["C"], ClassType)
        self.assertEqual(self.simulador.classes["C"].get_method("i"), "C :: i")
        self.assertEqual(self.simulador.classes["C"].get_method("j"), "C :: j")

    def test_class_creation_with_existing_name(self):
        """
        Esta prueba verifica si se puede crear una clase con un nombre existente.
        Primero agrega una clase con nombre "J" y métodos "k" y "l".
        Luego intenta agregar otra clase con el mismo nombre "J" y un método diferente "b".
        Verifica si el número de clases sigue siendo 1, lo que significa que la segunda clase no se agregó.
        """
        self.simulador.add_class("J", ["k", "l"])
        self.simulador.add_class("J", ["b"])
        self.assertEqual(len(self.simulador.classes), 1)

    def test_class_creation_with_non_existing_superclass(self):
        """
        Esta prueba verifica si se puede crear una clase con una superclase inexistente.
        Intenta agregar una clase con nombre "D", métodos "m" y "n", y superclase "Z".
        Verifica si el número de clases sigue siendo 0, lo que significa que la clase no se agregó.
        """
        self.simulador.add_class("D", ["m", "n"], "Z")
        self.assertEqual(len(self.simulador.classes), 0)

    def test_class_creation_with_duplicate_methods(self):
        """
        Esta prueba verifica si se puede crear una clase con métodos duplicados.
        Intenta agregar una clase con nombre "E" y métodos duplicados "o".
        Verifica si el número de clases sigue siendo 0, lo que significa que la clase no se agregó.
        """
        self.simulador.add_class("E", ["o", "o"])
        self.assertEqual(len(self.simulador.classes), 0)

    def test_class_creation_with_self_inheritance(self):
        """
        Esta prueba verifica si se puede crear una clase con auto herencia.
        Intenta agregar una clase con nombre "F", métodos "p" y "q", y superclase "F" (la misma clase).
        Verifica si el número de clases sigue siendo 0, lo que significa que la clase no se agregó.
        """
        self.simulador.add_class("F", ["p", "q"], "F")
        self.assertEqual(len(self.simulador.classes), 0)

    def test_describe_non_existing_class(self):
        """
        Esta prueba verifica si se puede describir una clase inexistente.
        Intenta describir una clase con nombre "Z" que no existe.
        Verifica si el resultado es None, lo que significa que la clase no existe.
        """
        self.assertIsNone(self.simulador.describe_class("Z"))

    def test_describe_class_without_methods(self):
        """
        Esta prueba verifica si se puede describir una clase sin métodos.
        Agrega una clase con nombre "G" sin métodos.
        Luego intenta describir la clase.
        Verifica si el resultado es "La clase G no tiene métodos.", lo que significa que la clase no tiene métodos.
        """
        self.simulador.add_class("G", [])
        self.assertEqual(self.simulador.describe_class("G"), "La clase G no tiene métodos.")

    def test_describe_class_example_exam(self):
        """
        Esta prueba verifica el comportamiento de la descripción de una clase con una superclase.
        Primero, se crea una clase "A" con los métodos "f" y "g".
        Luego, se crea una clase "B" con los métodos "f" y "h", y con "A" como superclase.
        Se verifica que los métodos de "B" sean los correctos y que herede correctamente los métodos de "A".
        Finalmente, se verifica la descripción de las clases "A" y "B".
        """
        self.simulador.add_class("A", ["f", "g"])
        self.assertIsInstance(self.simulador.classes["A"], ClassType)
        self.assertEqual(self.simulador.classes["A"].get_method("f"), "A :: f")
        self.assertEqual(self.simulador.classes["A"].get_method("g"), "A :: g")
        self.simulador.add_class("B", ["f", "h"], "A")
        self.assertIsInstance(self.simulador.classes["B"], ClassType)
        self.assertEqual(self.simulador.classes["B"].get_method("g"), "A :: g")
        self.assertEqual(self.simulador.classes["B"].get_method("h"), "B :: h")
        self.assertEqual(self.simulador.classes["B"].get_method("f"), "B :: f")
        self.assertEqual(self.simulador.describe_class("A"), "f -> A :: f\ng -> A :: g")
        self.assertEqual(self.simulador.describe_class("B"), "f -> B :: f\nh -> B :: h\ng -> A :: g")

    def test_class_creation_without_methods(self):
        """
        Esta prueba verifica si se puede crear una clase sin métodos.
        Se crea una clase "H" sin métodos y se verifica que se haya creado correctamente.
        """
        self.simulador.add_class("H", [])
        self.assertIsInstance(self.simulador.classes["H"], ClassType)

    def test_class_creation_with_superclass_having_methods(self):
        """
        Esta prueba verifica si se puede crear una clase con una superclase que tiene métodos.
        Primero, se crea una clase "C" con los métodos "i" y "j".
        Luego, se crea una clase "I" con los métodos "r" y "s", y con "C" como superclase.
        Se verifica que los métodos de "I" sean los correctos y que herede correctamente los métodos de "C".
        """
        self.simulador.add_class("C", ["i", "j"])
        self.simulador.add_class("I", ["r", "s"], "C")
        self.assertIsInstance(self.simulador.classes["I"], ClassType)
        self.assertEqual(self.simulador.classes["I"].get_method("r"), "I :: r")
        self.assertEqual(self.simulador.classes["I"].get_method("s"), "I :: s")

    def test_class_creation_with_superclass_without_methods(self):
        """
        Esta prueba verifica si se puede crear una clase con una superclase que no tiene métodos.
        Primero, se crea una clase "H" sin métodos.
        Luego, se crea una clase "J" con los métodos "t" y "u", y con "H" como superclase.
        Se verifica que los métodos de "J" sean los correctos.
        """
        self.simulador.add_class("H", [])
        self.simulador.add_class("J", ["t", "u"], "H")
        self.assertIsInstance(self.simulador.classes["J"], ClassType)
        self.assertEqual(self.simulador.classes["J"].get_method("t"), "J :: t")
        self.assertEqual(self.simulador.classes["J"].get_method("u"), "J :: u")

    def test_describe_class_with_superclass_having_methods(self):
        """
        Esta prueba verifica la descripción de una clase con una superclase que tiene métodos.
        Primero, se crea una clase "C" con los métodos "i" y "j".
        Luego, se crea una clase "M" con los métodos "y" y "z", y con "C" como superclase.
        Finalmente, se verifica la descripción de la clase "M".
        """
        self.simulador.add_class("C", ["i", "j"])
        self.simulador.add_class("M", ["y", "z"], "C")
        self.assertEqual(self.simulador.describe_class("M"), "y -> M :: y\nz -> M :: z\ni -> C :: i\nj -> C :: j")

    def test_describe_class_with_superclass_without_methods(self):
        """
        Esta prueba verifica la descripción de una clase con una superclase que no tiene métodos.
        Primero, se crea una clase "H" sin métodos.
        Luego, se crea una clase "N" con los métodos "a" y "b", y con "H" como superclase.
        Finalmente, se verifica la descripción de la clase "N".
        """
        self.simulador.add_class("H", [])
        self.simulador.add_class("N", ["a", "b"], "H")
        self.assertEqual(self.simulador.describe_class("N"), "a -> N :: a\nb -> N :: b")


if __name__ == '__main__':
    """
    Este bloque de código verifica si este archivo se está ejecutando directamente.
    Si es así, ejecuta la función main() de unittest, que ejecuta todas las pruebas unitarias en este archivo.
    """
    unittest.main()
