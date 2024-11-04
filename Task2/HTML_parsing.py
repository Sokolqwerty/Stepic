import re
from datetime import datetime


def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


month_translate = {
    "января": "January",
    "февраля": "February",
    "марта": "March",
    "апреля": "April",
    "мая": "May",
    "июня": "June",
    "июля": "July",
    "августа": "August",
    "сентября": "September",
    "октября": "October",
    "ноября": "November",
    "декабря": "December"
}


def translate_month(date_str):
    for ru_month, en_month in month_translate.items():
        date_str = date_str.replace(ru_month, en_month)
    return date_str


def date_formatting(dates):
    formatted_dates = []
    for date in dates:
        try:
            date = translate_month(date)
            parsed_date = datetime.strptime(date, "%d %B %Y %H:%M")
            formatted_date = parsed_date.strftime("%d.%m.%y %H:%M:%S")
            formatted_dates.append(formatted_date)
        except ValueError as e:
            print(f"Ошибка при парсинге даты '{date}': {e}")
            formatted_dates.append(None)
    return formatted_dates


def extract_data(html_content):
    authors = re.findall(r'class="comment-item__author ws-nowrap js-comm-author">(.+?)</div>', html_content)
    texts = re.findall(r'class="comment-item__main full-text clearfix"><div id=\'comm-id-\d+\'>(.+?)</div>', html_content)
    dates = re.findall(r'class="comment-item__date ws-nowrap">(.+?)</div>', html_content)
    likes = [int(num) for num in re.findall(r'id="comments-likes-id-\d+">(\d+)</span>', html_content)]
    dislikes = [int(num) for num in re.findall(r'id="comments-dislikes-id-\d+">(\d+)</span>', html_content)]

    formatted_dates = date_formatting(dates)

    comments_data = []
    for i in range(len(authors)):
        comments_dict = {
            "author": authors[i],
            "text": texts[i],
            "date": formatted_dates[i],
            "likes": likes[i],
            "dislikes": dislikes[i]
        }
        comments_data.append(comments_dict)
    return comments_data