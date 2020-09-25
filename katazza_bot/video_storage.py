from singleton import Singleton


@Singleton
class VideoStorage:
    videos_ = {(5, 'aesc'): 'https://www.youtube.com/watch?v=Wgz1rNUn7ZI'}

    rick_rolling_video_ = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

    def get_video(self, length, theme):
        key = (length, theme)
        if key in self.videos_:
            return self.videos_[key]
        else:
            return self.rick_rolling_video_
