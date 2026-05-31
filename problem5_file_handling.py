import os

def handle_file():
    filename = "students.txt"
    
    # Create file and write 5 sample names
    with open(filename, 'w') as file:
        file.write("Ali\nAisha\nBilal\nFatima\nZain\n")
    
    print("File 'students.txt' created. Reading contents...\n")
    
    # Read file and print names 
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip().upper())

if __name__ == "__main__":
    handle_file()