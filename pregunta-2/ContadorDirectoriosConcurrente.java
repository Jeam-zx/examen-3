import java.io.*;
import java.util.*;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Callable;
import java.util.concurrent.TimeUnit;

// Definiendo la clase ContadorDirectoriosConcurrente
public class ContadorDirectoriosConcurrente {

    // Creando un pool de hilos para ejecutar tareas
    static ExecutorService threadPool = Executors.newCachedThreadPool();

    // Variable estática para almacenar el resultado
    static int result = 0;

    // Método sincronizado para incrementar el resultado
    static synchronized void incrementResult() {
        ConcurrentDirCount.result = ConcurrentDirCount.result + 1;
    }

    // Método estático para contar los archivos en un directorio
    static void count(String path) throws Exception {
        // Reiniciando el resultado
        ConcurrentDirCount.result = 0;

        // Creando una nueva instancia de ConcurrentDirCount
        ConcurrentDirCount c = new ConcurrentDirCount(path);

        // Calculando el número de archivos
        c.compute();

        // Cerrando el pool de hilos
        ConcurrentDirCount.threadPool.shutdown();
    }

    // Variable para almacenar la ruta del directorio
    String path;

    // Constructor de la clase ConcurrentDirCount
    ConcurrentDirCount(String path) {
        this.path = path;
    }

    // Método para calcular el número de archivos en un directorio
    void compute() throws Exception {
        // Creando un objeto File para el directorio
        File dir = new File(this.path);

        // Obteniendo la lista de archivos en el directorio
        File listDir[] = dir.listFiles();

        // Creando una lista de tareas
        LinkedList<Callable<Void>> tareas = new LinkedList<Callable<Void>>();

        // Recorriendo la lista de archivos
        for (int i = 0; i < listDir.length; i++) {

            // Si el archivo es un directorio, se crea una nueva tarea
            if (listDir[i].isDirectory()) {
                final int i_ = i;

                // Creando la tarea para contar los archivos en el subdirectorio
                Callable<Void> subDirTask = () -> {
                    ConcurrentDirCount count = new ConcurrentDirCount(listDir[i_].getPath());
                    count.compute();

                    return null;
                };

                // Añadiendo la tarea a la lista de tareas
                tareas.add(subDirTask);
            }
            else {
                // Si el archivo no es un directorio, se incrementa el resultado
                ConcurrentDirCount.incrementResult();
            }
        }

        // Invocando todas las tareas en el pool de hilos
        ConcurrentDirCount.threadPool.invokeAll(tareas);
    }
}

public static void main(String[] args) {
    try {
        // Crear una instancia de ContadorDirectoriosConcurrente con la ruta del directorio a contar
        ContadorDirectoriosConcurrente contador = new ContadorDirectoriosConcurrente("ruta/del/directorio");

        // Llamar al método count para contar los archivos en el directorio
        ContadorDirectoriosConcurrente.count("ruta/del/directorio");

        // Imprimir el resultado
        System.out.println("Número de archivos: " + ContadorDirectoriosConcurrente.result);
    } catch (Exception e) {
        e.printStackTrace();
    }
}