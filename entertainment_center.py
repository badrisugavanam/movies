import media
import fresh_tomatoes
import tmdbsimple as upcomingmovies
import tmdb
import json
import logging


"""entertainment center
If any errors in the movie information fetched from the movie API can be 
traced with the log file 'fresh_tomatoes.log'
"""
__author__ = 'Badri(bnarayanan@gmail.com)'
__version__ = '1.6'


def get_latest_upcoming_movie():
    """ Returns the list of movies and their information fetched from 
        https://www.themoviedb.org/ API

    Replace YOUR_API_KEY with the actual API KEY
    Uses two third party API for the moviedb API 
    They are 
      - tmdbsimple from [1]
        [1] : https://github.com/celiao/tmdbsimple/tree/master/tmdbsimple
        for fetching the trailer information
      - tmdb from https://github.com/doganaydin/themoviedb for fetching all 
        the information about a specific movie 

    """
    my_movies_list = []
    tmdb.configure('YOUR_API_KEY')
    upcomingmovies.API_KEY = 'YOUR_API_KEY'
    m1 = upcomingmovies.Movies()
    # get the latest upcoming movie
    latest_movies = m1.upcoming()
    logger.debug(latest_movies)
    for c in m1.results:
        movieinfo = tmdb.Movie(c['id'])
        trailers = upcomingmovies.Movies(c['id'])
        trailers.videos()
        if(len(trailers.results) != 0):
            d = trailers.results[0]
            logger.debug(
                "trailer url: "+"https://www.youtube.com/watch?v="+d['key'])
            logger.debug("movie title: "+movieinfo.get_title())
            logger.debug("movie overview: "+movieinfo.get_overview())
            logger.debug("movie release date: "+movieinfo.get_release_date())
            posterurl = movieinfo.get_poster('m')
            if posterurl is None:
                posterurl = "https://upload.wikimedia.org/wikipedia/en" \
                    "/archive/d/d6/20080101230921%21Image_coming_soon.png"
            logger.debug("poster image url: "+posterurl)

            # if there is no poster image in the API put up a default coming
            # soon image from http://tinyurl.com/pofdefk
            youtubeurl = "https://www.youtube.com/watch?v=" + d['key']
            movieresults = media.Movie(movieinfo.get_title(
            ), posterurl, youtubeurl, movieinfo.get_overview(
            ), movieinfo.get_release_date())
            my_movies_list.append(movieresults)
    fresh_tomatoes.open_movies_page(my_movies_list)

logger = logging.getLogger(__name__)
logging.basicConfig(filename='fresh_tomatoes.log', level=logging.DEBUG)
get_latest_upcoming_movie()
