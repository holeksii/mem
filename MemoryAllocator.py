class MemoryAllocator:
    current_pointer = 0

    def __init__(self, num_cells):
        self.num_cells = num_cells
        self.allocate(num_cells)

    def allocate(self, num_cells):
        self.pointer = MemoryAllocator.current_pointer
        self.memory = 'x' * (num_cells - len(str(self.pointer)))
        MemoryAllocator.current_pointer += num_cells
        return self.pointer
