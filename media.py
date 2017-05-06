import webbrowser
from video import Video

class Movie(Video):
    
    """This class provides a way to store movie related information."""
    VALID_RATINGS = ["G","PG","PG-13","R"] #Rating as given by the movie rating system.

    def __init__(self,movie_title, duration,movie_storyline, poster_image_url,trailer_youtube_url):
        Video.__init__(self,movie_title,duration)
        #self.title=movie_title
        #self.duration = duration
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

        