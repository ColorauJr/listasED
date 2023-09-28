import tkinter as tk

# Classe que define um nó em uma lista encadeada
class Node:
    def __init__(self, data):
        self.data = data  # Armazena o dado do nó
        self.next = None  # Inicializa a referência para o próximo nó como None
        self.prev = None  # Inicializa a referência para o nó anterior como None (para listas duplamente encadeadas)

# Classe que define as operações em uma lista encadeada
class Lists:
    def __init__(self):
        self.head = None  # Inicializa a cabeça da lista como None (a lista está vazia inicialmente)
        self.tail = None  # A cauda é usada para otimizar a inserção no final da lista

    # Método para adicionar um elemento ao final da lista
    def append(self, data):
        new_node = Node(data)  # Cria um novo nó com o dado
        if not self.head:
            self.head = new_node  # Se a lista estiver vazia, o novo nó se torna a cabeça
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node  # Encontra o último nó e faz seu próximo apontar para o novo nó
            new_node.prev = current  # Define o nó anterior do novo nó como o último nó

    # Método para remover um elemento por valor ou posição
    def remove(self, data, position):
        current = self.head
        position = int(position)
        i = 0

        if position < 0:  # Se a posição for negativa, remove por valor
            while current:
                if current.data == data:
                    if current.prev:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                    return
                current = current.next
        else:  # Caso contrário, remove por posição
            while current:
                if current.data == data and i == position:
                    if current.prev:
                        current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                    return
                i = i + 1
                current = current.next

    # Método para inserir um elemento em uma posição específica
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position <= 0:  # Se a posição for menor ou igual a zero, insere no início
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            current_position = 0
            while current_position < position - 1 and current:
                current = current.next
                current_position += 1
            new_node.prev = current
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node

    # Método para exibir a lista de diferentes maneiras
    def display(self, index):
        current = self.head
        elements = []
        if index == -1:
            return ""
        while current:
            elements.append(str(current.data))
            current = current.next
        if index == 0:
            return " | ".join(elements)
        if index == 1:
            return " -> ".join(elements)
        if index == 2:
            return " <-> ".join(elements)

    # Método para encontrar todas as posições de um valor na lista
    def find_positions(self, value):
        positions = []
        current = self.head
        current_position = 0
        while current:
            if current.data == value:
                positions.append(current_position + 1)
            current = current.next
            current_position += 1
        return positions

    # Método para encontrar o valor em uma posição específica
    def find_value_at_position(self, position):
        current = self.head
        current_position = 0
        while current:
            if current_position == position - 1:
                return current.data
            current = current.next
            current_position += 1
        return None

# Classe principal que cria a interface gráfica
class LinkedListApp:
    def __init__(self, root):
        # Strings explicativas para as operações
        self.string_operations = [
            "Adicionar:\nProcesso de inserir um novo elemento na estrutura de dados."
            "\nO novo elemento é adicionado ao final da estrutura de dados."
            "\nSe inserir um valor no campo de posição, o elemento é adicionado na posição informada.",
            
            "Remover:\nProcesso de eliminar um elemento existente da estrutura de dados."
            "\nPode eliminar por posição, ou valor (a primeira ocorrência será removida).",
            
            "Consultar:\nProcesso de buscar informações em uma estrutura de dados."
            "\nA consulta pode ser feita por valor (exibe todas as posições de ocorrência)"
            " ou posição (exibe seu elemento).\n"

        ]

        self.index = -1  # Índice para escolher o tipo de lista (inicializado como -1)
        self.root = root
        self.root.title("Implementador de listas")
        self.doubly_linked_list = Lists()  # Cria uma instância da classe Lists para gerenciar a lista encadeada

        # Rótulos explicativos para as operações
        self.add_label = tk.Label(root, text=self.string_operations[0])
        self.add_label.pack(side=tk.TOP)

        self.add_by_position_label = tk.Label(root, text=self.string_operations[1])
        self.add_by_position_label.pack(side=tk.TOP)

        self.remove_label = tk.Label(root, text=self.string_operations[2])
        self.remove_label.pack(side=tk.TOP)

        # Rótulo divisor
        self.divider = tk.Label(root, text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
        self.divider.pack()

        # Botões para escolher o tipo de lista
        self.ls_button = tk.Button(root, text="LS", command=self.ls_def)
        self.ls_button.pack(side=tk.TOP)

        self.lse_button = tk.Button(root, text="LSE", command=self.lse_def)
        self.lse_button.pack(side=tk.TOP)

        self.lde_button = tk.Button(root, text="LDE", command=self.lde_def)
        self.lde_button.pack(side=tk.TOP)

        self.line_feed = tk.Label(root, text="\n")
        self.line_feed.pack(side=tk.TOP)

        #Entrada de posição, entrada de valor e botões para adicionar, remover e consultar elementos
        self.label = tk.Label(root, text="")
        self.remove_button = tk.Button(root, text="Remover", command=self.remove_element)
        self.remove_button.pack(side=tk.BOTTOM)
        self.query_button = tk.Button(root, text="Consultar", command=self.query_element)
        self.query_button.pack(side=tk.BOTTOM)
        self.add_button = tk.Button(root, text="Adicionar", command=self.add_element)
        self.add_button.pack(side=tk.BOTTOM)
        self.position_entry = tk.Entry(root)
        self.position_entry.pack(side=tk.BOTTOM)
        self.position_label = tk.Label(root, text="Posição:")
        self.position_label.pack(side=tk.BOTTOM)
        self.element_entry = tk.Entry(root)
        self.element_entry.pack(side=tk.BOTTOM)
        self.value_label = tk.Label(root, text="Valor:")
        self.value_label.pack(side=tk.BOTTOM)

        # Rótulo para exibir a lista
        self.display_text = tk.StringVar()
        self.display_label = tk.Label(root, textvariable=self.display_text)
        self.display_label.pack()

    # Função para selecionar o tipo de lista como Lista Sequencial (LS)
    def ls_def(self):
        self.index = 0  # Define o índice como 0 (Lista Sequencial)
        self.label.pack_forget()  # Remove o rótulo anterior (se houver)
        self.display_text.set("")  # Limpa o rótulo de exibição
        self.label = tk.Label(root, text="\nLista Sequencial\n")  # Define o rótulo para Lista Sequencial
        self.label.pack(side=tk.TOP)  # Exibe o novo rótulo
        self.doubly_linked_list = Lists()  # Cria uma nova instância da classe Lists

    # Função para selecionar o tipo de lista como Lista Simplesmente Encadeada (LSE)
    def lse_def(self):
        self.index = 1  # Define o índice como 1 (Lista Simplesmente Encadeada)
        self.label.pack_forget()  # Remove o rótulo anterior (se houver)
        self.display_text.set("")  # Limpa o rótulo de exibição
        self.label = tk.Label(root, text="\nLista Simplesmente Encadeada\n")  # Define o rótulo para LSE
        self.label.pack(side=tk.TOP)  # Exibe o novo rótulo
        self.doubly_linked_list = Lists()  # Cria uma nova instância da classe Lists

    # Função para selecionar o tipo de lista como Lista Duplamente Encadeada (LDE)
    def lde_def(self):
        self.index = 2  # Define o índice como 2 (Lista Duplamente Encadeada)
        self.label.pack_forget()  # Remove o rótulo anterior (se houver)
        self.display_text.set("")  # Limpa o rótulo de exibição
        self.label = tk.Label(root, text="\nLista Duplamente Encadeada\n")  # Define o rótulo para LDE
        self.label.pack(side=tk.TOP)  # Exibe o novo rótulo
        self.doubly_linked_list = Lists()  # Cria uma nova instância da classe Lists

    # Função para adicionar um elemento à lista
    def add_element(self):
        data = self.element_entry.get()  # Obtém o valor do campo de entrada de valor
        position = self.position_entry.get()  # Obtém o valor do campo de entrada de posição

        if data:
            if position:
                position = int(position) - 1  # Converte a posição para um número inteiro (base 0)
                self.doubly_linked_list.insert_at_position(data, position)  # Insere na posição especificada
            else:
                self.doubly_linked_list.append(data)  # Adiciona ao final da lista se a posição não for especificada

            self.display_text.set(self.doubly_linked_list.display(self.index))  # Atualiza a exibição da lista
            self.element_entry.delete(0, tk.END)  # Limpa o campo de entrada de valor
            self.position_entry.delete(0, tk.END)  # Limpa o campo de entrada de posição

    # Função para remover um elemento da lista
    def remove_element(self):
        position = self.position_entry.get()  # Obtém o valor do campo de entrada de posição
        value = self.element_entry.get()  # Obtém o valor do campo de entrada de valor

        if position:
            self.delete_by_position(position)  # Remove por posição, se especificada
        elif value:
            self.doubly_linked_list.remove(value, -1)  # Remove por valor se a posição não for especificada

        self.display_text.set(self.doubly_linked_list.display(self.index))  # Atualiza a exibição da lista

        self.element_entry.delete(0, tk.END)  # Limpa o campo de entrada de valor
        self.position_entry.delete(0, tk.END)  # Limpa o campo de entrada de posição

    # Função para remover um elemento por posição
    def delete_by_position(self, position):
        position = int(position) - 1  # Converte a posição para um número inteiro (base 0)
        current = self.doubly_linked_list.head
        current_position = 0
        while current_position < position and current:
            current = current.next
            current_position += 1

        if current:
            self.doubly_linked_list.remove(current.data, position)  # Remove o elemento na posição especificada
            self.display_text.set(self.doubly_linked_list.display(self.index))  # Atualiza a exibição da lista

    # Função para consultar elementos na lista
    def query_element(self):
        self.display_text.set(self.doubly_linked_list.display(self.index))  # Atualiza a exibição da lista
        query_by_position = self.position_entry.get()  # Obtém o valor do campo de entrada de posição
        query_by_value = self.element_entry.get()  # Obtém o valor do campo de entrada de valor
        exibition_linked_list = self.doubly_linked_list.display(self.index) + "\n\n"

        if query_by_value:
            query = query_by_value
            positions = self.doubly_linked_list.find_positions(query)  # Encontra as posições do valor na lista
            if positions:
                self.display_text.set(exibition_linked_list + f"Posições dos elementos de valor {query}: {positions}")
            else:
                self.display_text.set(exibition_linked_list + f"Elemento {query} não encontrado na lista")
            exibition_linked_list = self.display_text.get() + "\n"

        if query_by_position:
            query = int(query_by_position)
            value = self.doubly_linked_list.find_value_at_position(query)  # Encontra o valor na posição especificada
            if value is not None:
                self.display_text.set(exibition_linked_list + f"Elemento na posição {query}: [{value}]")
            else:
                self.display_text.set(exibition_linked_list + f"Elemento não encontrado na posição {query}")

        self.element_entry.delete(0, tk.END)  # Limpa o campo de entrada de valor
        self.position_entry.delete(0, tk.END)  # Limpa o campo de entrada de posição

# Função principal que cria a janela da interface gráfica e inicia o loop
if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListApp(root)
    root.mainloop()
