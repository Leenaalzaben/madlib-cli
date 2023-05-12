import re


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
def prompts(lst):
    input_arr = []
    for element in lst:
        user_input = input(f"Enter a {element} :")
        input_arr.append(user_input)
    return input_arr


# read_template function
def read_template(path):
    with open(path, "r") as f:
        read_result = f.read()
    return read_result


def parse_template(template):
    variables = re.findall(r"{([^}]+)}", template)
    stripped = re.sub("{[^}]+}", "{}", template)
    return stripped, tuple(variables)


def merge(template, values):
    return template.format(*values)


def new_file(merged_template):
    with open("assets/new_file.txt", mode="w") as f:
        f.write(merged_template)


def read_template_raises_exception_with_bad_path():
    try:
        path = "missing.txt"
        read_template(path)
    except FileNotFoundError:
        raise FileNotFoundError(" file was not found")


if __name__ == "__main__":
    Welcome_user()
    content = read_template("assets/dark_and_stormy_night_template.txt")
    stripped, parts = parse_template(content)
    user_prompts = prompts(parts)
    merged_txt = merge(stripped, user_prompts)
    print(merged_txt)
    new_file(merged_txt)
