from pytube import YouTube


class Yt_downloader:
    def __init__(self,link):
        self.link = link

    def get_info(self):
        yt = YouTube(self.link)
        self.title = yt.title
        self.views = yt.views
        return f'Title of video is {self.title} and it has {self.views} views on it'

    def download(self):
        yt = YouTube(self.link)
        yd = yt.streams.get_lowest_resolution()
        yd.download()


new_video = Yt_downloader("https://www.youtube.com/watch?v=7hjuTARjX4o")

print(new_video.get_info())