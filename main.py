from dataclasses import dataclass
from datetime import date
import json

'''
Video Content
Movies  /  Series Episodes  /  YouTube Episodes

1 - 5  / episode numb 1-5  / views and likes

Quality numbers:
Movies - stars/10 * 100
Series - stars/10 * 100
YouTube - likes/views * 100
'''


@dataclass
class VideoContent:
    title: str
    price: int
    release_date: date

    def as_dict(self):
        # return {
        #     'title': self.title,
        #     'price': self.price,
        #     'release_date': self.release_date.strftime('%d-%m-%Y')
        # }
        dicts = self.__dict__
        dicts['release_date'] = self.release_date.strftime('%d-%m-%Y')
        return dicts

    def calculate_quality_numbers(self):
        raise NotImplementedError('Must implement calculate_quality_numbers')


@dataclass
class Movie(VideoContent):
    stars: int
    director: str

    def __post_init__(self):
        if not (1 <= self.stars <= 10):
            raise ValueError('Stars must be between 1 and 10')

    def calculate_quality_numbers(self):
        return (self.stars / 10) * 100


@dataclass
class OldMovie(VideoContent):
    stars: int
    director: str

    def __post_init__(self):
        if not (1 <= self.stars <= 10):
            raise ValueError('Stars must be between 1 and 10')

    def calculate_quality_numbers(self):
        return (self.stars / 10) * 100


@dataclass
class SeriesEpisode(Movie):
    series_name: str


@dataclass
class YouTubeVideo(VideoContent):
    __views: int
    __likes: int

    @property
    def views(self):
        return self.__views

    @views.setter
    def views(self, value):
        if value < 1:
            raise ValueError('Views must be positive')

    @property
    def likes(self):
        return self.__likes

    @likes.setter
    def likes(self, value):
        if value < 1:
            raise ValueError('Likes must be positive')

    def calculate_quality_numbers(self):
        return (self.likes / self.views) * 100


if __name__ == '__main__':
    content = VideoContent('Test', 200, date.today())
    content.release_date = date(2008, 2, 1)
    # print(dir(content))
    # print(content.__dict__)
    # content.calculate_quality_numbers()
    # movie = Movie('Bad boy 2026', date.today(), 6, 'Serhii Kyriienko')
    # print(movie.calculate_quality_numbers())
    # video = YouTubeVideo('Test', date.today(), 1700, 300)

    with open('video.json', 'w') as f:
        json.dump(content.as_dict(), f)


