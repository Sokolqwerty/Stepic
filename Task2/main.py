from tabulate import tabulate
from HTML_parsing import extract_data, load_data
from comment_analysis import *
from save_to_json import save_to_json


def display_table(word_comments):
    for word, comments in word_comments.items():
        print(f"\nСлово: '{word}'")
        table = tabulate(comments, headers="keys", tablefmt="grid")
        print(table)


html_content = load_data("dom.html")
comments_data = extract_data(html_content)
save_to_json(comments_data, "comments.json")


html_content = load_data("dom.html")
comments_data = extract_data(html_content)
popular_words = extract_popular_words(comments_data)
top_comments = get_top_comments_for_words(comments_data, popular_words)
display_table(top_comments)