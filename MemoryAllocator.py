class MemoryAllocator:

    def __init__(self, memory_cells: int, pointer: int) -> None:
        self.memory = MemoryAllocator.allocate(memory_cells, pointer)
    
    @staticmethod
    def allocate(memory_cells: int, pointer: int) -> list:
        memory = []
        for i in str(pointer):
            memory.append(int(i))

        for i in range(memory_cells - len(memory)):
            memory.append('x')
        return memory