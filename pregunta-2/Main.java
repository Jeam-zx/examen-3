import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Programa a ejecutar
        System.out.println("Ingrese el numero del programa a ejecutar:");
        System.out.println("1. Producto Punto Concurrente");
        System.out.println("2. Contador de directorios concurrente");
        int programa = scanner.nextInt();
         if(programa == 1){
            // Ingrese el tamaño de los vectores
            System.out.println("Ingrese el tamaño de los vectores: ");
            int n = scanner.nextInt();

            // Ingrese los elementos del primer vector
            System.out.println("Ingrese los elementos del primer vector:");
            int[] vector1 = new int[n];
            for (int i = 0; i < n; i++) {
                 vector1[i] = scanner.nextInt();
            }

            // Ingrese los elementos del segundo vector
            System.out.println("Ingrese los elementos del segundo vector:");
            int[] vector2 = new int[n];
            for (int i = 0; i < n; i++) {
                 vector2[i] = scanner.nextInt();
            }

            // Crear una instancia de ProductoPuntoConcurrente con los vectores de prueba
            ProductoPuntoConcurrente productoPunto = new ProductoPuntoConcurrente(vector1, vector2);

            // Llamar al método calcular para calcular el producto punto de los vectores
            try {
                productoPunto.calcular();
            } catch (Exception e) {
                e.printStackTrace();
            }

            // Imprimir el resultado
            System.out.println("El resultado del producto punto es: ");
            System.out.println(productoPunto.getResultado());

        } else if(programa == 2) {
            // Ingrese la ruta del directorio
            System.out.println("Ingrese la ruta del directorio: ");
            String path = scanner.next();

            // Crear una instancia de ContadorDirectoriosConcurrente con la ruta del directorio a contar
            ContadorDirectoriosConcurrente contador = new ContadorDirectoriosConcurrente(path);

            // Llamar al método count para contar los archivos en el directorio

            try {
                contador.count(path);
            } catch (Exception e) {
                e.printStackTrace();
            }

            // Imprimir el resultado
            System.out.println("Número de archivos: " + ContadorDirectoriosConcurrente.result);
        } else {
            System.out.println("Opción inválida");
        }
    }
}