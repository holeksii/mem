from MemoryManager import MemoryManager
from Menu import Menu


def main():
    memory_cells = cells_per_row = 0
    while True:
        memory_cells = int(input('Enter number of memory cells:\n>> '))
        cells_per_row = int(input('Enter number of memory cells per row:\n>> '))
        if (memory_cells < cells_per_row):
            print('Invalid input!')
        else:
            break

    ma = MemoryManager(memory_cells, cells_per_row)
    menu = Menu(ma)
    menu.run()


if __name__ == '__main__':
    main()
