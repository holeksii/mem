from MemoryAllocator import MemoryAllocator


class MemoryManager:
    def __init__(self, max_cells, cells_in_row):
        if (max_cells % cells_in_row) != 0:
            raise Exception('max_cells must be a multiple of cells_in_row')

        self.memory_list = []
        self.max_cells = max_cells
        self.cells_in_row = cells_in_row
        self.total_memory_allocated = 0

    def allocate(self, num_cells):
        if num_cells > self.max_cells - self.total_memory_allocated:
            raise Exception('Not enough memory')
        pointer = MemoryAllocator.current_pointer
        self.memory_list.append(MemoryAllocator(num_cells))
        self.total_memory_allocated += num_cells
        return pointer
    
    def free(self, pointer):
        for memory in self.memory_list:
            if memory.pointer == pointer:
                self.memory_list.remove(memory)
                self.total_memory_allocated -= memory.num_cells
                return True
        return False
        
    def print(self):
        cells_in_row = self.cells_in_row
        for memory in self.memory_list:
            pointer_len = len(str(memory.pointer))
            if pointer_len > cells_in_row:
                print(' ' * pointer_len - cells_in_row, '|\n', end='')

            print (memory.pointer, end='')
            cells_in_row -= pointer_len

            for c in memory.memory:
                print(c, end='')
                cells_in_row -= 1
                if cells_in_row == 0:
                    print()
                    cells_in_row = self.cells_in_row
        print()
