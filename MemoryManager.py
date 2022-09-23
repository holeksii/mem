from argparse import ArgumentError
from MemoryAllocator import MemoryAllocator
import util

class MemoryManager:
    def __init__(self, max_cells: int, cells_in_row: int) -> None:
        if (max_cells < cells_in_row):
            raise ArgumentError('cells_in_row cannot be bigger than max_cells')
        self.max_cells = max_cells
        self.cells_in_row = cells_in_row
        self.memory = ['*' for i in range(self.max_cells)]
        self.pointers = []

    def allocate(self, cells: int) -> int:
        pointer = util.find(self.memory, ['*' for i in range(cells)])
        if pointer == -1 or cells < len(str(pointer)):
            raise MemoryError('Out of memory')

        m = MemoryAllocator.allocate(cells, pointer)
        self.memory = util.replace(self.memory, ['*' for i in range(cells)], m)
        self.pointers.append((pointer, cells))
        return pointer

    def free(self, pointer: int) -> bool:
        if pointer < 0 or pointer > self.max_cells:
            return False
        
        for i in self.pointers:
            if i[0] == pointer:
                to_delete = MemoryAllocator.allocate(i[1], i[0])
                self.memory = util.replace(self.memory, to_delete, ['*' for i in range(i[1])])
                self.pointers.remove(i)
                return True
        return False

    def print(self) -> None:
        count = 0
        for i in self.memory:
            if (i == '*'):
                print('_', end='')
            else:
                print(i, end='')
            count += 1
            if count == self.cells_in_row:
                print()
                count = 0
        print()
        