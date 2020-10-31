import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

def find_article_with_keywords(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for article in soup.find_all('article', class_='post'):
        post = article.find('div', 'post__text')
        post_text = post.text

        for kw in KEYWORDS:
            if kw in post_text:
                time_element = article.find('span', class_='post__time')
                time = time_element.text
                title_element = article.find('a', 'post__title_link')
                title = title_element.text
                link = title_element.attrs.get('href')
                print(f'{time} - {title} - {link}')
                break

if __name__ == '__main__':
    url = 'https://habr.com/ru/all/'
    find_article_with_keywords(url)
