from Lab1.Node import Node
from utils import get_initial_state

class Tree:
    __nodes = None

    def __init__(self):
        node = Node(state = get_initial_state(),
                    cost = 0,
                    depth = 0)
        self.__nodes = {0: [node]}

    def add_node(self, level: int, new_node: "Node"):
        try:
            self.__nodes[level].append(new_node)
        except KeyError:
            self.__nodes[level] = [new_node]

    def get_node(self, node: int) -> list["Node"]:
        return list(self.__nodes[node])

    def print_node(self, node: "Node"):
        ''' Вывод узла на экран '''
        parent_id: int = 0
        if node.parent_node:
            parent_id = node.parent_node.node_id
        node_prev_action: str = None
        if (node.previous_action):
            node_prev_action = node.previous_action.name
        print(f"id = {node.node_id}, parent_id = {parent_id}, " +
              f"action = {node_prev_action}, \ndepth = {node.depth}, " +
              f"cost = {node.path_cost}, state: ")
        self.print_state(node.current_state)
        print("")

    def print_state(self, state: list):
        for i in range(9):
            if (i % 3 == 0 and i != 0):
                print("")
            print(state[i] if state[i] != 0 else " ", end=" ")

    def print_path(self, node: "Node", isReversed=False):
        path = []
        current_node = node

        while current_node.parent_node:
            path.append(current_node)
            current_node = current_node.parent_node
        path.append(current_node)
        if (isReversed):
            path = path[::-1]
        for path_node in path:
            self.print_node(path_node)
            print("\t^\n\t|\n")
