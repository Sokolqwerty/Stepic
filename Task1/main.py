import json
from tabulate import tabulate
from utils import sort_user_data, get_name
from JSON_parsing import load_data, parse_user_data, display_table

def main():
    data = load_data("data.json")
    user_data = parse_user_data(data)
    sorted_data = sort_user_data(user_data)
    display_table(sorted_data)

main()