import os


class Operation:
        
        def __init__(self):
            print("_________     _____  .____   _________  ____ ___.____       ________________________ __________ ")
            print("\\_   ___ \\   /  _  \\ |    |  \\_   ___ \\|    |   \\    |     /  _  \\__    ___/\\_____  \\\\______   \\")
            print("/    \\  \\/  /  /_\\  \\|    |  /    \\  \\/|    |   /    |    /  /_\\  \\|    |    /   |   \\|       _/")
            print("\\     \\____/    |    \\    |__\\     \\___|    |  /|    |___/    |    \\    |   /    |    \\    |   \\")
            print(" \\______  /\\____|__  /_______ \\______  /______/ |_______ \\____|__  /____|   \\_______  /____|_  /")
            print("        \\/         \\/        \\/      \\/                 \\/       \\/                 \\/       \\/ ")
            print("") 
            print("")
            print("")
            self.x = float(input("Enter the first number: "))
            self.operator = (input("Enter an operator (+, -, *, /): "))
            self.y = float(input("Enter the second number: "))

        def calculate(self):
            if  self.operator == '+':
                return self.x + self.y
            elif self.operator == '-':
                return self.x - self.y
            elif self.operator == '*':
                 return self.x * self.y
            elif self.operator == '/':
                 return self.x / self.y
            else:
                return print("Invalid")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
def main():
    while True:
        obj = Operation()
        result = obj.calculate()
        print("Result : ", result)

        choice = input("Do you want to Solve Another Operation? Yes / No: ")
        if choice != 'Yes'and  choice !='yes':
             break

        clear_screen()
if __name__ == "__main__":
     main()
     