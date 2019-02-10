import requests
from bs4 import BeautifulSoup


class Url:
    def __init__(self):
        self.baslik = str(input('Video Başlığını Gir : '))

    def UrlBul(self):

        if self.baslik == '':
            print('baslik Boş Olamaz.\n')
            self.__init__()
        self.baslik = self.baslik.replace(' ', '+')

        # Link Search
        uRl: str = f'https://www.youtube.com/results?search_query={self.baslik}'
        response = requests.get(uRl).text
        cont = BeautifulSoup(response, 'html.parser').body

        link = cont.find_all('a', class_='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link')
        for i in range(len(link)):
            print(f'{i + 1} {link[i]["title"]}')
        try:
            index = int(input('indirmek istediğiniz Dosyayı seçiniz.\n')) - 1
            watch = str(link[index]['href'])
            title = str(link[index]['title'])
            flink: str = f"http://youtube.com{watch}"
            print(f"\n\nBulunan Video : {title}\n")
            key = int(input('''Dosyayı İndirmek için '1'e\nYeniden Aramak için 2'ye Basin\n '''))

            if key == 1:
                return flink
            elif key == 2:
                self.baslik = ''
                return self.UrlBul()
            else:
                print('Hatalı Giriş Yaptınız.')
                exit(0)

        except IndexError:
            print('Hata! Sınır dizin sınırları dışına çıktınız.\n')
            exit(0)
