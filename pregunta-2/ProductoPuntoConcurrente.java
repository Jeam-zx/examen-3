import java.util.concurrent.*;
import java.util.*;

// Definiendo una clase ProductoPuntoConcurrente
public class ProductoPuntoConcurrente {

    // Declarando arrays de enteros privados vector1, vector2, y resultado
    private int[] vector1;
    private int[] vector2;
    private int[] resultado;

    // Definiendo un constructor para ProductoPuntoConcurrente que toma dos arrays de enteros como parámetros
    public ProductoPuntoConcurrente(int[] vector1, int[] vector2) {

        // Comprobando si las longitudes de los dos arrays de entrada son iguales, si no, lanzando una excepción
        if(vector1.length != vector2.length) {
            throw new IllegalArgumentException("Los vectores deben tener igual longitud");
        }

        // Inicializando las variables de instancia con los parámetros de entrada
        this.vector1 = vector1;
        this.vector2 = vector2;
        // Inicializando el array resultado con la misma longitud que los arrays de entrada
        this.resultado = new int[vector1.length];
    }

    // Definiendo un método calcular que calcula el valor del producto punto de los dos arrays de entrada
    public void calcular() throws Exception {

        // Creando una LinkedList de Callable<Integer> llamada tareas
        LinkedList<Callable<Integer>> tareas = new LinkedList<>();

        // Recorriendo cada elemento de los arrays de entrada
        for(int i = 0; i < vector1.length; i++) {

            // Definiendo un entero final idx igual a la variable de bucle i
            final int idx = i;

            // Definiendo un Callable<Integer> llamado tarea
            Callable<Integer> tarea = () -> {
                // Multiplicando los elementos correspondientes de vector1 y vector2 y almacenando el resultado en resultado
                resultado[idx] = vector1[idx] * vector2[idx];
                // Devolviendo el resultado calculado
                return resultado[idx];
            };

            // Añadiendo la tarea a la LinkedList tareas
            tareas.add(tarea);
        }

        // Creando un ExecutorService con un pool de hilos fijo igual a la longitud de los arrays de entrada
        ExecutorService executor = Executors.newFixedThreadPool(vector1.length);

        // Invocando todas las tareas en la LinkedList tareas
        executor.invokeAll(tareas);

        // Cerrando el executor después de que todas las tareas hayan sido invocadas
        executor.shutdown();
    }
}

public static void main(String[] args) {
    try {
        // Crear dos vectores de prueba
        int[] vector1 = {1, 2, 3, 4, 5};
        int[] vector2 = {6, 7, 8, 9, 10};

        // Crear una instancia de ProductoPuntoConcurrente con los vectores de prueba
        ProductoPuntoConcurrente productoPunto = new ProductoPuntoConcurrente(vector1, vector2);

        // Llamar al método calcular para calcular el producto punto de los vectores
        productoPunto.calcular();

        // Imprimir el resultado
        System.out.println(Arrays.toString(productoPunto.resultado));
    } catch (Exception e) {
        e.printStackTrace();
    }
}

