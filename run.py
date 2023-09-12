from time import process_time
from Tree import Tree
from utils import bfs, dfs
import sys


if __name__ == '__main__':
    START_TIME = process_time()
    Tree = Tree()
    sys.argv.append('--bfs')
    if len(sys.argv) == 2:
        if sys.argv[1] == '--bfs':
            bfs(Tree)
        elif sys.argv[1] == '--dfs':
            dfs(Tree)
    else:
        print(
            f"Ошибка! Неверное кол-во параметров. \nВведите {sys.argv[0]} -h \n")