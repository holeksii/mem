import sys


class Menu:
    help_text = '''Available commands:
    help - show available commands
    exit - close the program
    allocate <num> - allocates num cells and retuns poiter to block
    free <num> - free block by pointer
    print - print block'''
                
    
    def __init__(self, memory_manager):
        self.manager = memory_manager


    def run(self):
              
        
        exit = False
        option = ''
        while not exit:
            option = input('>> ')
            if option == 'help':
                print(Menu.help_text)
            elif option == 'exit':
                exit = True
            elif option.split(' ')[0] == 'allocate':
                try:
                    self.manager.allocate(int(option.split(' ')[1]))
                except Exception as e:
                    print(e)
            elif option.split(' ')[0] == 'free':
                if self.manager.free(int(option.split(' ')[1])):
                    print('Successfully deallocated!')
                else:
                    print('Invalid input!')
            elif option == 'print':
                self.manager.print()
            else:
                print('help - get list of commands')