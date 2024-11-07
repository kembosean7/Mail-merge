import sys
import os

#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def get_files(filename):

    try :
        with open(filename, 'r', errors= 'ignore') as f :
            contents = f.read()
            return contents
    except FileNotFoundError:
        print("File not found.")
        sys.exit()

    
def get_names(filename):

    try:
        with open(filename, 'r', errors= 'ignore') as f :
            data = f.read().splitlines()
            return data
    except FileNotFoundError:
        print("File not found.")
        sys.exit()
    


def save_letters(letter,names):

    os.makedirs("ReadyToSend", exist_ok=True )

    for name in names :
        personal_letter = letter.replace("[name]", name)
        filename = f"{name}.txt"
        file_path =  os.path.join(r'C:\Users\LENOVO\Mail-merge\mail merge\ReadyToSend', filename)
        try:
            with open(file_path, 'w') as f:
                f.write(personal_letter)
        except IOError:
            print(f"Error occurred while writing to the file")
            sys.exit()


def main():
    if len(sys.argv) < 3:
        print("Invalid usage, too little arguments.")
        sys.exit()

    letter = get_files(sys.argv[1])
    names = get_names(sys.argv[2])
    save_letters(letter,names)

main()