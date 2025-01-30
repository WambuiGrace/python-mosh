import os

def main():
    # Get the input from the user
    filename = input('Enter the filename to open or create: ').strip()
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        else:
            with open(filename, 'w') as file:
                print('File created successfully.')
                pass
    except OSError:
        print('Error opening the file. Please try again.')
        return
    
    print('\n Enter the content of the file. Type "SAVE" on a new line to save and exit.')

    content = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        content.append(line)
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(content)) 
            print(f'{filename} saved successfully.')
    except OSError:
        print(f'Error saving the {filename} file.')
        return

if __name__ == "__main__":
    main()