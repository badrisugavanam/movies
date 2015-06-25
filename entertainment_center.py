import media
import fresh_tomatoes

#For Getting trailer a movie uses API for https://www.themoviedb.org/ using the lib@https://github.com/badrisugavanam/tmdbsimple
import tmdbsimple as upcomingmovies

#For all the movie info of a particular movie from https://www.themoviedb.org/ using the lib@https://github.com/badrisugavanam/themoviedb
import tmdb
import json
import logging

""" Builds my_movies_list fetching the latest information from https://www.themoviedb.org/  API 
""" returns none
def get_latest_upcoming_movie():
    my_movies_list=[]
    tmdb.configure('YOUR_API_KEY')
    upcomingmovies.API_KEY = 'YOUR_API_KEY'
    m1=upcomingmovies.Movies()
    # get the latest upcoming movie
    latest_movies=m1.upcoming()
    logger.debug(latest_movies)
    for c in m1.results:
        movieinfo=tmdb.Movie(c['id'])
        trailers=upcomingmovies.Movies(c['id'])
        trailers.videos()
        if(len(trailers.results) <> 0):
            d=trailers.results[0]
            logger.debug("trailer url"+"https://www.youtube.com/watch?v="+d['key'])
            logger.debug("movie title"+movieinfo.get_title())
            logger.debug("movie overview"+movieinfo.get_overview()) 
            logger.debug("movie release date"+movieinfo.get_release_date())
            movieresults=media.Movie(movieinfo.get_title(),movieinfo.get_poster('m'),"https://www.youtube.com/watch?v="+d['key'],movieinfo.get_overview(),movieinfo.get_release_date())
            my_movies_list.append(movieresults)
    fresh_tomatoes.open_movies_page(my_movies_list)


logger = logging.getLogger(__name__)
logging.basicConfig(filename='fresh_tomatoes.log',level=logging.DEBUG)
get_latest_upcoming_movie()