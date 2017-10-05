import webbrowser


class Movie():
    """ This class provides a way to store movie related information
        and is called by movie_name=movie.Movie. It takes the arguments
        of self, movie_title, movie_storyline, poster_image, and
        youtube_url. The result is a movie poster that shows a
        movie trailer when clicked after fresh_tomatoes makes the
        HTML file."""
    def __init__(self, movie_title, movie_storyline,
                 poster_image, youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
