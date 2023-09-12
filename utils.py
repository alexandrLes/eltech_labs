import os

import psutil

from Action import Action
from Node import Node
from time import process_time

START_TIME = 0  # время запуска программы
TIME_STOP = 0  # время окончания программы
TREE = None  # дерево решения
DEBUG = 0

def get_initial_state() -> list:
    """(Вариант 1)"""
    return [5, 8, 3,
            4, 0, 2,
            7, 6, 1]

def get_finish_state() -> list:
    """(Вариант 1)"""
    return [1, 2, 3,
            4, 5, 6,
            7, 8, 0]

def state_swap(new_states: dict, current_state: list, i: int, j: int, action: Action):
    state = list(current_state)
    state[i], state[j] = state[j], state[i]
    new_states[action] = state

def get_new_states(current_state: list) -> dict[Action, list[Node]]:
    ''' Получение новых состояний поля '''
    # В словаре ключ - действие для получения состояния, значение - само состояние
    new_states = {}
    pos = current_state.index(0)
    # up
    if pos not in (0, 1, 2):
        state_swap(new_states, current_state, pos, pos - 3, Action.UP)
    # down
    if pos not in (6, 7, 8):
        state_swap(new_states, current_state, pos, pos + 3, Action.DOWN)
    # right
    if pos not in (2, 5, 8):
        state_swap(new_states, current_state, pos, pos + 1, Action.RIGHT)
    # left
    if pos not in (0, 3, 6):
        state_swap(new_states, current_state, pos, pos - 1, Action.LEFT)
    return new_states

def print_info(iterations: int, time: float):
    print(f"Итого узлов: {Node.get_nodes_count()}")
    print(f"Итого итераций: {iterations}")
    print(f"Потраченное время процессора: {time * 1000} миллисекунд")
    print(f"Памяти использовано: {psutil.Process(os.getpid()).memory_info().rss} байтов")

def bfs(Tree):
    '''Поиск в ширину'''
    cur_lvl: int = 0
    hashes = set()
    step_i: int = 1
    iteration_count: int = 0
    while (True):
        nodes_previous_lvl = Tree.get_node(cur_lvl)
        cur_lvl += 1
        if (DEBUG): print(f"Глубина = {cur_lvl}")
        for node_i in nodes_previous_lvl:
            if (DEBUG):
                print("\nТекущий узел:")
                Tree.print_node(node_i)
            new_states_dict = get_new_states(node_i.current_state)
            new_nodes: list[Node] = []
            if (DEBUG): print("\nЕго дети:")
            for new_action in new_states_dict:
                new_state = new_states_dict[new_action]
                new_state_hash: int = hash(tuple(new_state))
                if (new_state_hash in hashes):
                    if (DEBUG):
                        print("Вывод состояния: ")
                        Tree.print_state(new_state)
                    continue
                new_node = Node(new_state, cur_lvl, cur_lvl, node_i, new_action)
                # Поиск в ширину - это частный случай поиска по критерию стоимости, когда стоимость равна глубине.
                new_nodes.append(new_node)
                hashes.add(new_state_hash)
                Tree.add_node(cur_lvl, new_node)
                if (DEBUG): Tree.print_node(new_node)
            for new_node_i in new_nodes:
                iteration_count += 1
                if new_node_i.current_state == get_finish_state():
                    print("Ответ найден!")
                    TIME_STOP = process_time()
                    Tree.print_path(new_node_i)
                    print_info(iteration_count, TIME_STOP - START_TIME)
                    exit(0)
        if (DEBUG):
            print(f"Текущий шаг: {step_i}. Нажмите Enter... ")
            input()
        step_i += 1

def dfs(Tree):
    '''Поиск в глубину'''
    cur_lvl: int = 0
    hashes = set()
    step_i: int = 1
    iteration_count: int = 0
    while (True):
        nodes_previous_lvl = Tree.get_node(cur_lvl)
        cur_lvl += 1
        if (DEBUG): print(f"Глубина = {cur_lvl}")
        for node_i in nodes_previous_lvl:
            if (DEBUG):
                print("\nТекущий узел:")
                Tree.print_node(node_i)
            new_states_dict = get_new_states(node_i.current_state)
            new_nodes: list[Node] = []
            if (DEBUG): print("\nЕго дети:")
            for new_action in new_states_dict:
                new_state = new_states_dict[new_action]
                new_state_hash: int = hash(tuple(new_state))
                if (new_state_hash in hashes):
                    if (DEBUG):
                        print("Вывод состояния: ")
                        Tree.print_state(new_state)
                    continue
                new_node = Node(new_state, cur_lvl, cur_lvl, node_i, new_action)
                # Поиск в ширину - это частный случай поиска по критерию стоимости, когда стоимость равна глубине.
                new_nodes.append(new_node)
                hashes.add(new_state_hash)
                Tree.add_node(cur_lvl, new_node)
                if (DEBUG): Tree.print_node(new_node)
            for new_node_i in new_nodes:
                iteration_count += 1
                if new_node_i.current_state == get_finish_state():
                    print("Ответ найден!")
                    TIME_STOP = process_time()
                    Tree.print_path(new_node_i)
                    print_info(iteration_count, TIME_STOP - START_TIME)
                    exit(0)
        if (DEBUG):
            print(f"Текущий шаг: {step_i}. Нажмите Enter... ")
            input()
        step_i += 1

