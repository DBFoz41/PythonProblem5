"""
Interpreter problem

Read a list of commands in RAM and use a set of registers to execute them
"""
import file_reader as fr

class Problem5:

    def __init__(self):
        self.register = [0 for i in range(10)]
        self.ram = [0 for i in range(1000)]
        self.instruction = 0
        self.instruction_digit1 = 0
        self.instruction_digit2 = 0
        self.instruction_digit3 = 0
        self.ram_counter = 0

    def read_ram(self):
        file_reader = fr.FileReader("inputFile.txt")
        self.ram = file_reader.file_as_int_list()
        return self.ram

    def instruction_router(self, instruction):
        self.instruction = instruction
        self.instruction_digit1 = int(self.instruction/100)
        self.instruction_digit2 = int((self.instruction % 100)/10)
        self.instruction_digit3 = int(((self.instruction % 100)% 10))

        match self.instruction_digit1:
            case 0:
                if self.register[self.instruction_digit3] == 0:
                    return 100
                else:
                    self.instruction = self.ram[self.register[self.instruction_digit2]]
                    self.ram_counter = self.register[self.instruction_digit2]
            
            case 1:
                print("halt")

            case 2:
                self.register[self.instruction_digit2] = self.instruction_digit3
                self.register[self.instruction_digit2] = (self.register[self.instruction_digit2] % 1000)
            case 3:
                self.register[self.instruction_digit2] += self.instruction_digit3
                self.register[self.instruction_digit2] = (self.register[self.instruction_digit2] % 1000)

            case 4:
                self.register[self.instruction_digit2] *= self.instruction_digit3
                self.register[self.instruction_digit2] = (self.register[self.instruction_digit2] % 1000)

            case 5:
                self.register[self.instruction_digit2] = self.register[self.instruction_digit3]
                self.register[self.instruction_digit2] = (self.register[self.instruction_digit2] % 1000)

            case 6:
                self.register[self.instruction_digit2] += self.register[self.instruction_digit3]
                self.register[self.instruction_digit2] = (self.register[self.instruction_digit2] % 1000)

            case 7:
                self.register[self.instruction_digit2] *= self.register[self.instruction_digit3]
                self.register[self.instruction_digit2] = (self.register[self.instruction_digit2] % 1000)
            
            case 8:
                self.register[self.instruction_digit2] = self.ram[self.register[self.instruction_digit3]]
                self.register[self.instruction_digit2] = (self.register[self.instruction_digit2] % 1000)

            case 9:
                self.ram[self.instruction_digit3] = self.register[self.instruction_digit2]
                self.ram[self.instruction_digit3] = (self.ram[self.instruction_digit3] % 1000)
        return 0

    def get_ram_contents(self):
        return self.ram

    def update_ram_counter(self):
        return self.ram_counter

def execute_main():
    ram = []
    ram_current_location = 0
    ram_instruction = 0
    instruction_count = 0
    return_instruction = 0
    problem5 = Problem5()
    ram = problem5.read_ram()
    ram_instruction = ram[0]

    while ram_instruction != 100 and ram_current_location < 1000:
        return_instruction = problem5.instruction_router(ram[ram_current_location])
        if return_instruction == 0:
            ram = problem5.get_ram_contents()
            if int(ram_instruction/100) == 0:
                ram_current_location = problem5.update_ram_counter()
            else:
                ram_current_location += 1
            ram_instruction = ram[ram_current_location]
            instruction_count += 1
        else:
            ram_current_location += 1
            ram_instruction = ram[ram_current_location]
            instruction_count += 1
    #increment instruction_count once more for the 100 halt command
    instruction_count += 1
    print(instruction_count)


if __name__ == "__main__":
    execute_main()