import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, movie_title, movie_rating, poster_image,
                 trailer_youtube, streaming_availability, movie_stars):
        """ input arguments store data for each Movie instance """
        self.title = movie_title
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.streaming = streaming_availability
        self.stars = movie_stars
        