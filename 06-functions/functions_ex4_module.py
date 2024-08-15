def get_greeting():
    """
    This function returns a hardcoded greeting string
    """
    return "G'Day!"

def get_greeting_to(name):
    """_summary_
    This function passes in a name and returns a greeting string
    Args:
        name (str): any string

    Returns:
        str: the input string concatented with a greeting
    """
    return "G'Day " + name

def get_product(num1, num2):
    return num1 * num2

def get_first(a_list):
    return a_list[0]

def get_name(a_dict):
    return a_dict["name"]

def get_circumference(radius):
    return 2 * 3.14 * radius

print("something happening in the module")

if __name__ == "__main__":
    # code here will NOT execute in the importing script
    print("code in module if run as main")