from uRlSearch import Url
from PlayList import playList
from audioDownload import Audio

menu = '''
1 -) Arama Yap
2 -) PlayList İndir
3 -) Çıkış
'''


def main():
    print(menu)
    key = int(input('\n'))
    if key == 1:
        data = Url().UrlBul()
        Audio(data).audioDownload()
    elif key == 2:
        data = playList().playListuRL()
        for i in range(len(data)):
            Audio(data[i]).audioDownload()
    elif key == 3:
        print('Güle Güle')
        exit(0)
    else:
        print('Bilmediğin Tuşlarla Oynama Amacamın Oğlu !!!')
        return main()


main()
