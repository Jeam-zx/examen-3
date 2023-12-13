JAVAC = javac --release 11
JAVA = java

# Rutas a los archivos fuente
SRC_DIR = ./pregunta-2/
MAIN_SRC = $(SRC_DIR)/Main.java
CONTADOR_SRC = $(SRC_DIR)/ContadorDirectoriosConcurrente.java
PRODUCTO_SRC = $(SRC_DIR)/ProductoPuntoConcurrente.java

all: Main.class

Main.class: $(MAIN_SRC) ContadorDirectoriosConcurrente.class ProductoPuntoConcurrente.class
	$(JAVAC) -cp $(SRC_DIR) $(MAIN_SRC)

ContadorDirectoriosConcurrente.class: $(CONTADOR_SRC)
	$(JAVAC) -cp $(SRC_DIR) $(CONTADOR_SRC)

ProductoPuntoConcurrente.class: $(PRODUCTO_SRC)
	$(JAVAC) -cp $(SRC_DIR) $(PRODUCTO_SRC)

run: Main.class
	$(JAVA) -cp $(SRC_DIR) Main

clean:
	rm -f $(SRC_DIR)/*.class

.PHONY: all run clean