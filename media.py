"""media

media module contains Movie class 
"""
__author__ =  'Badri(bnarayanan@gmail.com)'
__version__=  '1.1'

import webbrowser
class Movie :
	"""Movie class represents a movie for the website"""
	def __init__(self ,title ,poster_image_url ,trailer_youtube_url ,storyline):
		""" Constructor for the movie
        Keyword arguments:
        title -- title of a movie
        poster_image_url -- poster url of a movie
        trailer_youtube_url -- represents youtube url of a movie
        storyline -- represents the storyline of a movie
        """
		self.title=title
		self.poster_image_url=poster_image_url
		self.trailer_youtube_url=trailer_youtube_url
		self.storyline=storyline

	def show_trailer(self):
		"""Open a webbrowser with the youtube URL      
        """
		webbrowser.open(self.trailer_youtube_url)	

