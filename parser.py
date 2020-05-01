import requests
from bs4 import BeautifulSoup

# Константы. Если надо будет поменять пользователя - изменить cookie
URL = 'https://vk.com/im'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.130',
           'accept': '*/*',
           'cookie': 'remixlang=0; remixflash=0.0.0; remixscreen_depth=24; remixscreen_orient=1; remixdt=7200; remixusid=NGNkYzQ5MWJlODFiNGNmYzJkMTYzZmU1; tmr_lvid=e7f5787bab559ed28692cb2700a1863e; tmr_lvidTS=1575379054844; remixstid=698539330_h7eP2dfRkhzhURkEEWGNeL4y1S68rhg7QmM2zHcmZjL; remixscreen_width=1366; remixscreen_height=768; remixscreen_dpr=1; remixua=37%7C-1%7C80%7C1806402404; remixmdevice=1366/768/1/!!-!!!!; remixrefkey=580ac283d06b41c0f5; tmr_reqNum=1144; remixgp=08ad6118af772e5a9b584d4e8105289b; remixseenads=1; remixsid=dce9de39eb9b8bc45b4c6744f7967e08de317988296d161146ece7ecbfafa; remixcurr_audio=151849804_456245969; remixscreen_winzoom=1.77'}

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
