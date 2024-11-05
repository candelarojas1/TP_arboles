# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:

class Nodo:
    def __init__(self, criatura, capturada=None, descripcion=""):
        self.criatura = criatura
        self.capturada = capturada
        self.descripcion = descripcion
        self.left = None
        self.right = None

class ArbolBinario:
    def __init__(self):
        self.root = None

    def insert_node(self, criatura, capturada=None, descripcion=""):
        def __insert(root, criatura, capturada, descripcion):
            if root is None:
                return Nodo(criatura, capturada, descripcion)
            if criatura < root.criatura:
                root.left = __insert(root.left, criatura, capturada, descripcion)
            else:
                root.right = __insert(root.right, criatura, capturada, descripcion)
            return root

        self.root = __insert(self.root, criatura, capturada, descripcion)

    # a. Listado inorden de las criaturas y quienes las derrotaron
    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f"Criatura: {root.criatura}, Capturada por: {root.capturada}")
                __inorden(root.right)

        __inorden(self.root)

    # b. Buscar y mostrar la información de una criatura específica
    def buscar_criatura(self, criatura):
        def __buscar(root, criatura):
            if root is None:
                return None
            if root.criatura == criatura:
                return root
            elif criatura < root.criatura:
                return __buscar(root.left, criatura)
            else:
                return __buscar(root.right, criatura)

        nodo = __buscar(self.root, criatura)
        if nodo:
            print(f"Criatura: {nodo.criatura}, Capturada por: {nodo.capturada}, Descripción: {nodo.descripcion}")
        else:
            print(f"La criatura {criatura} no se encontró en el árbol.")

    # d. Determinar los héroes que capturaron más criaturas (sin defaultdict)
    def top_heroes(self, top_n=3):
        capturas = {}

        def __contar_capturas(root):
            if root is not None:
                if root.capturada:
                    if root.capturada in capturas:
                        capturas[root.capturada] += 1
                    else:
                        capturas[root.capturada] = 1
                __contar_capturas(root.left)
                __contar_capturas(root.right)

        __contar_capturas(self.root)
        top_capturas = sorted(capturas.items(), key=lambda x: x[1], reverse=True)[:top_n]

        print(f"Top {top_n} héroes o dioses que capturaron más criaturas:")
        for heroe, cantidad in top_capturas:
            print(f"{heroe}: {cantidad} criaturas")

    # e. Listar las criaturas derrotadas por un héroe o dios específico
    def criaturas_derrotadas_por(self, heroe):
        def __buscar_criaturas(root, heroe, lista):
            if root is not None:
                if root.capturada == heroe:
                    lista.append(root.criatura)
                __buscar_criaturas(root.left, heroe, lista)
                __buscar_criaturas(root.right, heroe, lista)

        lista_criaturas = []
        __buscar_criaturas(self.root, heroe, lista_criaturas)

        if lista_criaturas:
            print(f"Criaturas derrotadas por {heroe}: {', '.join(lista_criaturas)}")
        else:
            print(f"{heroe} no ha derrotado ninguna criatura en el árbol.")

    # f. Listar las criaturas que no han sido derrotadas
    def criaturas_no_derrotadas(self):
        def __buscar_no_derrotadas(root, lista):
            if root is not None:
                if root.capturada is None:
                    lista.append(root.criatura)
                __buscar_no_derrotadas(root.left, lista)
                __buscar_no_derrotadas(root.right, lista)

        lista_no_derrotadas = []
        __buscar_no_derrotadas(self.root, lista_no_derrotadas)

        if lista_no_derrotadas:
            print(f"Criaturas no derrotadas: {', '.join(lista_no_derrotadas)}")
        else:
            print("Todas las criaturas han sido derrotadas.")


tree = ArbolBinario()

# Insertar criaturas del árbol
tree.insert_node("Cerbero")
tree.insert_node("León de Nemea", "Heracles", "León invulnerable")
tree.insert_node("Hidra de Lerna", "Heracles", "Serpiente gigante con muchas cabezas")
tree.insert_node("Quimera", "Belerofonte", "Criatura con partes de león, cabra y dragón")
tree.insert_node("Talos", "Medea", "Gigante de bronce de Creta")

# a. Listado inorden de las criaturas y quienes las derrotaron
print("Listado Inorden:")
tree.inorden()

# b. Cargar una breve descripción sobre cada criatura (ya lo estamos haciendo en insert_node)

# c. Mostrar toda la información de la criatura Talos
print("\nInformación de Talos:")
tree.buscar_criatura("Talos")

# d. Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
print("\nTop 3 héroes o dioses que capturaron más criaturas:")
tree.top_heroes()

# e. Listar las criaturas derrotadas por Heracles
print("\nCriaturas derrotadas por Heracles:")
tree.criaturas_derrotadas_por("Heracles")

# f. Listar las criaturas que no han sido derrotadas
print("\nCriaturas no derrotadas:")
tree.criaturas_no_derrotadas()