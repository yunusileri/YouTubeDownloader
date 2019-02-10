import requests
from bs4 import BeautifulSoup


def LinkBul():
    baslik = str(input('Video Başlığını Gir : '))
    if baslik == '':
        print('baslik Boş Olamaz.\n')
        return LinkBul()
    baslik = baslik.replace(' ', '+')

    # Link Search
    uRl: str = f'https://www.youtube.com/results?search_query={baslik}'
    response = requests.get(uRl).text
    cont = BeautifulSoup(response, 'html.parser').body

    link = cont.find_all('a', class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link')
    for i in range(len(link)):
        print(f'{i + 1} {link[i]["title"]}')
    try:
        index = int(input('indirmek istediğiniz Dosyayı seçiniz.\n')) - 1
        watch = str(link[index]['href'])
        title = str(link[index]['title'])
    except IndexError:
        print('Hata! Sınır dizin sınırları dışına çıktınız.\n')
        return

    flink: str = f"http://youtube.com{watch}"
    print(f"\n\nBulunan Video : {title}\n\n\n")
    key = int(input('''Dosyayı İndirmek için '1'e\nYeniden Aramak için 2'ye Basin\n '''))

    if key == 1:
        return flink
    elif key == 2:
        return LinkBul()
    else:
        print('Hatalı Giriş Yaptınız.')
        return



