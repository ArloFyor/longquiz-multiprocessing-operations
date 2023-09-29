'''

Write a function that first asks for 2 numbers and performs the 4 mathematical operations such as addition, subtraction, multiplicaiton, and division.
The output will be display using 4 different processes. Display the PID of each process and the number of cores in your computer.

'''

#Importing Libraries

from multiprocessing import Process, Pool
import os

def perform_operations(numA, numB, operation):
    if operation == 'add':
        return numA + numB
    
    elif operation == 'subtract':
        return numA - numB
    
    elif operation == 'multiply':
        return numA * numB
    
    elif operation == 'divide':
        return numA / numB

def main(numA, numB, operation):
    temp = perform_operations(numA, numB, operation)

    print(f"------------------------------------")
    print(f"Process Parent ID: {os.getppid()}")
    print(f"Process ID: {os.getpid()}")
    print(f"Operation: {operation}, Result: {temp} ")
    print(f"------------------------------------")
    print("")

if __name__ == '__main__':
    numA = float(input("Input your first number: "))
    numB = float(input("Input your second number: "))

    print(f"Number of cores in my computer: {os.cpu_count()}")

    operations = ['add', 'subtract', 'multiply', 'divide']

    for i in operations:

        processes = [Process(target=main, args=[numA, numB, i])]

        for process in processes:
            process.start()

        for process in processes:
            process.join()

    print(f"Done")