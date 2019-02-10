import pafy


class Audio:
    def __init__(self, uRl):
        self.uRl = uRl

    def audioDownload(self):
        data = pafy.new(self.uRl)
        data = data.getbestaudio('m4a')
        size = round(data.get_filesize() / (1024*1024),1)
        title = data.title
        print(f'''{title}   {size}mb indiriliyor..''')
        data.download()
        print(f'''{title} indirildi.''')
