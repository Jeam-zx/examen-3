// PARTE 1

// Protocolo Secuencia
protocol Secuencia {
    // Un tipo asociado que representa el tipo de elementos que la secuencia puede contener.
    associatedtype Elemento
    
    // Un método que permite agregar un nuevo elemento a la secuencia.
    // El tipo del elemento debe ser el mismo que el tipo asociado `Elemento`.
    func agregar(_ elemento: Elemento)
    
    // Un método que permite remover un elemento de la secuencia.
    // Este método puede lanzar un error si no hay elementos para remover.
    // El tipo del elemento devuelto debe ser el mismo que el tipo asociado `Elemento`.
    func remover() throws -> Elemento
    
    // Una propiedad computada que indica si la secuencia está vacía.
    // Devuelve `true` si la secuencia está vacía y `false` en caso contrario.
    var vacio: Bool { get }
}

// Enumeración ErrorSecuencia
// Define los errores que pueden ocurrir al trabajar con secuencias.
enum ErrorSecuencia: Error {
    // Error que se lanza cuando se intenta operar en una secuencia vacía.
    case secuenciaVacia(String)
    // Error que se lanza cuando se intenta operar en una secuencia que no es concreta.
    case secuenciaAbstracta(String)
}

// Clase ListBasedSecuencia
// Implementa el protocolo Secuencia utilizando una lista para almacenar los elementos.
class ListBasedSecuencia<T>: Secuencia {
    // El tipo de elementos que la secuencia puede contener.
    typealias Elemento = T
    
    // La lista de elementos en la secuencia.
    var items = [T]()
    
    // Propiedad computada que indica si la secuencia está vacía.
    // Devuelve `true` si la secuencia está vacía y `false` en caso contrario.
    var vacio: Bool {
        return self.items.count == 0
    }
    
    // Método para agregar un nuevo elemento a la secuencia.
    // En esta implementación, el método no hace nada.
    func agregar(_ elemento: T) {}
    
    // Método para remover un elemento de la secuencia.
    // En esta implementación, el método siempre lanza un error porque la secuencia no es concreta.
    func remover() throws -> T {
        throw ErrorSecuencia.secuenciaAbstracta("Error. Esta secuencia no es concreta")
    }
}

// Clase Pila
// Es una implementación concreta de la clase ListBasedSecuencia.
// En una pila, el último elemento agregado es el primero en ser removido (LIFO).
class Pila<T>: ListBasedSecuencia<T> {
    // Sobreescribe el método agregar para agregar un elemento al final de la lista.
    override func agregar(_ elemento: T) {
        self.items.append(elemento)
    }
    
    // Sobreescribe el método remover para remover el último elemento de la lista.
    // Si la lista está vacía, lanza un error.
    override func remover() throws -> T {
        if self.vacio {
            throw ErrorSecuencia.secuenciaVacia("Error. La pila esta vacia")
        }
        return items.removeLast()
    }
}

// Clase Cola
// Es una implementación concreta de la clase ListBasedSecuencia.
// En una cola, el primer elemento agregado es el primero en ser removido (FIFO).
class Cola<T>: ListBasedSecuencia<T> {
    // Sobreescribe el método agregar para agregar un elemento al final de la lista.
    override func agregar(_ elemento: T) {
        items.append(elemento)
    }
    
    // Sobreescribe el método remover para remover el primer elemento de la lista.
    // Si la lista está vacía, lanza un error.
    override func remover() throws -> T {
        if self.vacio {
            throw ErrorSecuencia.secuenciaVacia("Error. La cola esta vacia")
        }
        return items.removeFirst()
    }
}

// PARTE 2

// Clase Grafo
// Representa un grafo utilizando una lista de adyacencia.
final class Grafo {
    // La lista de adyacencia, representada como una lista de tuplas.
    // Cada tupla representa una arista y contiene dos nodos: el nodo base y el nodo objetivo.
    private let listAdy: [(Int, Int)]
    
    // Inicializador de la clase Grafo.
    // Toma una lista de adyacencia como parámetro.
    init(listAdy: [(Int, Int)]) {
        self.listAdy = listAdy
    }
    
    // Método que devuelve todos los nodos adyacentes a un nodo dado.
    func adyacencias(of nodo: Int) -> [Int] {
        return self.listAdy.filter { (base, target) in
            return base == nodo
        }.map { (_, target) in
            return target
        }
    }
}

// Clase Busqueda
// Realiza una búsqueda en un grafo.
class Busqueda {
    // El grafo en el que se realiza la búsqueda.
    final let grafo: Grafo
    // Un conjunto de nodos que ya han sido visitados.
    final var closed: Set<Int> = []
    
    // Inicializador de la clase Busqueda.
    // Toma un grafo como parámetro.
    init(in grafo: Grafo) {
        self.grafo = grafo
    }
    
    // Método para realizar la búsqueda en el grafo.
    // Toma dos nodos como parámetros: el nodo de inicio (D) y el nodo objetivo (H).
    final func buscar(D: Int, H: Int) -> Int {
        // Marca el nodo de inicio como abierto.
        self.open(nodo: D)
        // Inicializa un contador para llevar la cuenta de los pasos necesarios para llegar al nodo objetivo.
        var count = 0
        
        // Mientras la búsqueda no haya terminado...
        while !self.done() {
            // Selecciona el próximo nodo a visitar.
            // Si no hay más nodos para visitar, devuelve -1.
            guard let next = self.select() else { return -1 }
            // Marca el nodo seleccionado como visitado.
            self.closed.insert(next)
            
            // Si el nodo seleccionado es el nodo objetivo, devuelve el contador.
            if next == H {
                return count
            }
            
            // Incrementa el contador.
            count += 1
            
            // Para cada nodo adyacente al nodo seleccionado...
            for ady in self.grafo.adyacencias(of: next) {
                // Si el nodo adyacente no debe ser descartado, lo marca como abierto.
                if !self.descartar(nodo: ady) {
                    self.open(nodo: ady)
                }
            }
        }
        
        // Si la búsqueda termina sin encontrar el nodo objetivo, devuelve -1.
        return -1
    }
    
    // Método para marcar un nodo como abierto.
    // En esta implementación, el método no hace nada.
    func open(nodo: Int) {}
    
    // Método para seleccionar el próximo nodo a visitar.
    // En esta implementación, el método siempre devuelve `nil`.
    func select() -> Int? { return nil }
    
    // Método para determinar si la búsqueda ha terminado.
    // En esta implementación, el método siempre devuelve `true`.
    func done() -> Bool { return true }
    
    // Método para determinar si un nodo debe ser descartado.
    // En esta implementación, el método siempre devuelve `true`.
    func descartar(nodo: Int) -> Bool { return true }
}

// No colocamos la secuencia en Busqueda porque en swift los generics son invariantes entre si.

// Clase DFS (Depth-First Search)
// Es una implementación concreta de la clase Busqueda que realiza una búsqueda en profundidad.
class DFS: Busqueda {
    // Utiliza una pila para almacenar los nodos que aún no se han visitado.
    var pila = Pila<Int>()
    
    // Sobreescribe el método open para agregar un nodo a la pila.
    override func open(nodo: Int) {
        self.pila.agregar(nodo)
    }
    
    // Sobreescribe el método select para remover y devolver el próximo nodo de la pila.
    override func select() -> Int? {
        return try? self.pila.remover()
    }
    
    // Sobreescribe el método done para indicar si la pila está vacía.
    override func done() -> Bool {
        return self.pila.vacio
    }
    
    // Sobreescribe el método descartar para indicar si un nodo ya ha sido visitado.
    override func descartar(nodo: Int) -> Bool {
        return self.closed.contains(nodo)
    }
}

// Clase BFS (Breadth-First Search)
// Es una implementación concreta de la clase Busqueda que realiza una búsqueda en anchura.
class BFS: Busqueda {
    // Utiliza una cola para almacenar los nodos que aún no se han visitado.
    var cola = Cola<Int>()
    // Utiliza un conjunto para almacenar los nodos que ya se han abierto pero aún no se han visitado.
    var opened: Set<Int> = []
    
    // Sobreescribe el método open para agregar un nodo a la cola y al conjunto de nodos abiertos.
    override func open(nodo: Int) {
        self.cola.agregar(nodo)
        self.opened.insert(nodo)
    }
    
    // Sobreescribe el método select para remover y devolver el próximo nodo de la cola.
    override func select() -> Int? {
        return try? self.cola.remover()
    }
    
    // Sobreescribe el método done para indicar si la cola está vacía.
    override func done() -> Bool {
        return self.cola.vacio
    }
    
    // Sobreescribe el método descartar para indicar si un nodo ya ha sido visitado o abierto.
    override func descartar(nodo: Int) -> Bool {
        return self.closed.contains(nodo) || self.opened.contains(nodo)
    }
}


let g = Grafo(listAdy: [(1,2), (2,8), (8,6), (2,3), (3,4), (4,5), (5,6), (7, 9)])

print(BFS(in: g).buscar(D: 1, H: 8)) // 2
print(DFS(in: g).buscar(D: 1, H: 8)) // 6
print(DFS(in: g).buscar(D: 1, H: 9)) // -1
print(BFS(in: g).buscar(D: 1, H: 9)) // -1