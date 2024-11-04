import json
from tabulate import tabulate

def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def parse_user_data(data):
    user_data = []

    for user in data:
        name = user["name"]
        phone = user.get("phoneNumber", "Not Available")
        email = user.get("email", "Not Available")
        address = user["address"]
        full_address = f"{address['street']}, {address['city']}, {address['state']} {address['zipcode']}"
        languages = len(user["preferences"]["languages"])
        theme = user["preferences"].get("theme", "Not Available")
        user_agent = user.get("userAgent", "Not Available")
        hex_color = user.get("hexcolor", "Not Available")

        user_data.append([
            name, phone, email, full_address, languages, theme, user_agent, hex_color
        ])

    return user_data

def display_table(user_data):
    headers = ["Name", "Phone", "Email", "Address", "Languages", "Theme", "User Agent", "Hex Color"]
    table = tabulate(user_data, headers=headers, tablefmt="pipe")
    print(table)