
#5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
#se (MCU), desarrollar un algoritmo que contemple lo siguiente:

#a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
#leano que indica si es un héroe o un villano, True y False respectivamente;
#b. listar los villanos ordenados alfabéticamente;
#c. mostrar todos los superhéroes que empiezan con C;
#d. determinar cuántos superhéroes hay el árbol;
#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;
#f. listar los superhéroes ordenados de manera descendente;
#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#los villanos, luego resolver las siguiente tareas:
#I. determinar cuántos nodos tiene cada árbol;
#II. realizar un barrido ordenado alfabéticamente de cada árbol.class BinaryTree: 

    class __Node: 

        def __init__(self, value, is_hero, left=None, right=None): 
            self.value = value 
            self.is_hero = is_hero  # True para héroes, False para villanos
            self.left = left 
            self.right = right 

    def __init__(self): 
        self.root = None 

    def insert_node(self, value, is_hero): 
        def __insert(root, value, is_hero): 
            if root is None: 
                return BinaryTree.__Node(value, is_hero) 
            elif value < root.value: 
                root.left = __insert(root.left, value, is_hero) 
            else: 
                root.right = __insert(root.right, value, is_hero) 
            return root 

        self.root = __insert(self.root, value, is_hero) 

    def listar_villanos(self): 
        def __listar_villanos(root): 
            if root is not None: 
                __listar_villanos(root.left) 
                if not root.is_hero: 
                    print(root.value) 
                __listar_villanos(root.right) 

        __listar_villanos(self.root) 

    def superhéroes_con_c(self): 
        def __superhéroes_con_c(root): 
            if root is not None: 
                __superhéroes_con_c(root.left) 
                if root.is_hero and root.value.startswith('C'): 
                    print(root.value) 
                __superhéroes_con_c(root.right) 

        __superhéroes_con_c(self.root) 

    def contar_superhéroes(self): 
        def __contar_superhéroes(root): 
            if root is None: 
                return 0 
            return (__contar_superhéroes(root.left) + 
                    __contar_superhéroes(root.right) + 
                    (1 if root.is_hero else 0)) 

        return __contar_superhéroes(self.root) 

    def buscar_y_modificar(self, old_name, new_name): 
        def __buscar_y_modificar(root, old_name, new_name): 
            if root is not None: 
                if root.value == old_name: 
                    root.value = new_name 
                    return True 
                return (__buscar_y_modificar(root.left, old_name, new_name) or 
                        __buscar_y_modificar(root.right, old_name, new_name)) 
            return False 

        return __buscar_y_modificar(self.root, old_name, new_name) 

    def listar_superhéroes_descendente(self): 
        def __listar_superhéroes_descendente(root): 
            if root is not None: 
                __listar_superhéroes_descendente(root.right) 
                if root.is_hero: 
                    print(root.value) 
                __listar_superhéroes_descendente(root.left) 

        __listar_superhéroes_descendente(self.root) 

    def generar_bosque(self): 
        heroes_tree = BinaryTree()
        villains_tree = BinaryTree()

        def __generar_bosque(root): 
            if root is not None: 
                if root.is_hero: 
                    heroes_tree.insert_node(root.value, True) 
                else: 
                    villains_tree.insert_node(root.value, False) 
                __generar_bosque(root.left) 
                __generar_bosque(root.right) 

        __generar_bosque(self.root)
        return heroes_tree, villains_tree 


tree = BinaryTree() 
tree.insert_node("Iron Man", True) 
tree.insert_node("Thanos", False) 
tree.insert_node("Captain America", True) 
tree.insert_node("Loki", False) 
tree.insert_node("Doctor Strange", True) 
tree.insert_node("Ultron", False) 
tree.insert_node("Black Widow", True) 
tree.insert_node("Hela", False) 

print("Villanos ordenados alfabéticamente:")
tree.listar_villanos()

print("\nSuperhéroes que empiezan con 'C':")
tree.superhéroes_con_c()

print("\nCantidad de superhéroes en el árbol:")
print(tree.contar_superhéroes())

print("\nModificando 'Doctor Strange' a 'Doctor Strange (Sorcerer Supreme)':")
tree.buscar_y_modificar("Doctor Strange", "Doctor Strange (Sorcerer Supreme)")

print("\nSuperhéroes ordenados de manera descendente:")
tree.listar_superhéroes_descendente()

heroes_tree, villains_tree = tree.generar_bosque()
print("\nCantidad de nodos en el árbol de héroes:", heroes_tree.contar_superhéroes())
print("Cantidad de nodos en el árbol de villanos:", villains_tree.contar_superhéroes())