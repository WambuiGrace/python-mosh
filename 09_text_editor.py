import os

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
       
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def get_user_iput():
    print('\n Enter the content of the file. Type "SAVE" on a new line to save and exit.')

    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)
    return '\n'.join(lines)

def main():
    # Get the input from the user
    filename = input('Enter the filename to open or create: ').strip()
    try:
        if os.path.exists(filename):
            print(read_file(filename))
        else:
           write_file(filename, '')
           print('File created successfully.')
            
        content = get_user_iput()
        write_file(filename, content) 
        print(f'{filename} saved successfully.')
    except OSError:
        print(f'Error opening the {filename} file.')
        return

if __name__ == "__main__":
    main()