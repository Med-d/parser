import requests
from bs4 import BeautifulSoup
from config.py import CONFIG

# Константы. Если надо будет поменять пользователя - изменить cookie
URL = 'https://vk.com/im'
HEADERS = {
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130',
           'accept': '*/*',
           'cookie': CONFIG.COOKIE
          }

# Получает ответ на GET запрос на указанный URL
def get_html(url, param=None):
    return requests.get(url, headers=HEADERS, params=param)

# Получает заданный контент со страницы
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('li', class_='nim-dialog_unread') #Непрочитанные диалоги

    dialogs = []
    for item in items:
        dialogs.append(
            item.find('span', class_='_im_dialog_link').get_text()
        )

    return dialogs


# Сам парсер
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print(*get_content(html.text), sep='\n')
    else:
        print('Error. Status code =', html.status_code)

parse()
