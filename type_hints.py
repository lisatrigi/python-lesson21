#type hints

def format_name(first_name: str,last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(format_name("Lisa","Shahini"))

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool):
    return item_a, item_b, item_c, item_d

print(get_items("Lisa", 333, 5.46, False))