def Welcome_user():
    print(
        """
*************************************
**      Welcome to Mad Lib         **
**  *****************************  **
** Get ready to have some fun with **
**             words               **
**  Your responses will be used to
**        fill in the blanks       **
**      and complete sentences     **

**  *****************************  **
**       let's get started         **
**           Have fun!             **
*************************************
"""
    )
# Ask user some Question use input

# read_template function
def read_template(file_path):
    with open(file_path, "r") as f:
        read_result = f.read()
    return read_result




def parse_template(x):
    
    extracts = []
    current = ""
    stripped_str = ""
    for char in x:
        if char != "{":
            stripped_str += char
            current = ""

        elif char != "}":
            stripped_str += char
            extracts.append(current)
            current = ""

        elif char != "}":
            current += char
        stripped_str += char
    
    return stripped_str, tuple(extracts)



def merge(stripp, input):
    return stripp.format(*input)


def read_template_raises_exception_with_bad_path():
    try:
        path = "missing.txt"
        read_template(path)
    except FileNotFoundError:
       raise FileNotFoundError(' file was not found')

def excute():
    Welcome_user()    
    content = read_template('../assets/dark_and_stormy_night_template.txt')

if __name__ == "__main__":
   excute()
