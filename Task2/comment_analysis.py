import re
from collections import Counter


def extract_popular_words(comments):
    words = []
    for comment in comments:
        for word in re.findall(r'\b\w+\b', comment['text'].lower()):
            if len(word) >= 4:
                words.append(word)

    word_count = Counter(words)
    most_common_words = word_count.most_common(10)
    return most_common_words


def get_likes(comment):
    return comment['likes']


def get_top_comments_for_words(comments, popular_words):
    word_comments = {}

    for word, _ in popular_words:
        filtered_comments = [c for c in comments if word in c['text'].lower()]
        top_comments = sorted(filtered_comments, key=get_likes, reverse=True)[:5]
        word_comments[word] = top_comments
    return word_comments