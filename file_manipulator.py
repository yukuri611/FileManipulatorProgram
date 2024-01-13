import sys

def main():
    function = input("Function: ")
    inputpath = input("Inputpath: ")
    if function in ["reverse", "copy", "duplicate_contents"]:
        outputpath = input("Outputpath: ")
    else:
        needle = input("Needle: ")
        newstring = input("Newstring: ")


    if function == "reverse":
        reverse(inputpath, outputpath)
    elif function == "copy":
        copy(inputpath, outputpath)
    elif function == "duplicate_contents":
        duplicate_contents(inputpath, outputpath)
    else:
        replace_string(inputpath, needle, newstring)


def reverse(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        new_contents = ""
        contents_length = len(contents)
        for i in range(contents_length):
            new_contents += contents[contents_length - 1 - i]
        f.write(new_contents)
    print("Run successfully!")

def copy(inputpath, outputpath):
    with open(inputpath) as f:
        contents = f.read()
    with open(outputpath, 'w') as f:
        f.write(contents)
    print("Run successfully!")

def duplicate_contents(inputpath, n):
    if type(n) is int:
        with open(inputpath) as f:
            contents = f.read()
        with open(inputpath, 'w') as f:
            new_contents = ""
            for i in range(n):
                new_contents += contents
            f.write(new_contents)
        print("Run successfully!")
    else: print("Error. The second input type was not int")

def replace_string(inputpath, needle, newstring):
    if(type(needle) is str and type(newstring) is str):
        with open(inputpath) as f:
            contents = f.read()
        with open(inputpath, 'w') as f:
            new_contents = contents.replace(needle, newstring)
            f.write(new_contents)
        print("Run successfully!")
    else: print("Error. Both input type must be str.")


if __name__ == "__main__":
    main()
