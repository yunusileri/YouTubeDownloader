import pafy


class playList:
    def __init__(self, uRl):
        self.uRl = uRl

    def playListuRL(self):
        plaListuRl = pafy.get_playlist(self.uRl)
        playListUzunluk = len(plaListuRl['items'])
        data = []
        print(f'''{plaListuRl['title']} Listesinde Bulanan Videolar''')
        for i in range(playListUzunluk):
            data.append(plaListuRl['items'][i]['pafy'].watch_url)
            print(f'''{i + 1} {plaListuRl['items'][i]['pafy'].title}''')
        return data
