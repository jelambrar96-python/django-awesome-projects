import unittest
from pytube import YouTube


YOUTUBE_LINK = 'https://www.youtube.com/watch?v=arj7oStGLkU'


class TestPYtube(unittest.TestCase):

    def test_pytube(self):
        link = YOUTUBE_LINK
        video = YouTube(link) 
        stream = video.streams.get_lowest_resolution() 
        stream.download() 


if __name__ == '__main__':
    unittest.main()