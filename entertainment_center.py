import fresh_tomatoes
import media  # refers to media.py file

imitation_game = media.Movie(
    "The Imitation Game",
    "PG-13",
    "http://cdn1.thr.com/sites/default/files/imagecache/portrait_300x450/2014/09/the_imitation_game_a_p.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM",
    "Netflix, Amazon Video, iTunes",
    "Benedict Cumberbatch, Keira Knightley, Matthew Goode")

the_rock = media.Movie(
    "The Rock",
    "R",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/82/The_Rock_%28movie%29.jpg/220px-The_Rock_%28movie%29.jpg",
    "https://www.youtube.com/watch?v=313n0wga2xo",
    "Amazon Video, iTunes",
    "Sean Connery, Nicolas Cage, Ed Harris")

sense_and_sensibility = media.Movie(
    "Sense and Sensibility",
    "PG",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/69/Sense_and_sensibility.jpg/215px-Sense_and_sensibility.jpg",
    "https://www.youtube.com/watch?v=Q1rb_c_t1-s",
    "Amazon Video",
    "Emma Thompson, Kate Winslet, James Fleet")

ratatouille = media.Movie(
    "Ratatouille",
    "G",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=niD-jahFURU",
    "Amazon Video, iTunes",
    "Brad Garrett, Lou Romano, Patton Oswalt")

playing_by_heart = media.Movie(
    "Playing by Heart",
    "R",
    "http://images.moviepostershop.com/playing-by-heart-movie-poster-1998-1020189858.jpg",
    "https://www.youtube.com/watch?v=DppPtpEbFag",
    "Amazon Video, iTunes",
    "Gillian Anderson, Ellen Burstyn, Sean Connery")

the_holiday = media.Movie(
    "The Holiday",
    "R",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/60/Theholidayposter.jpg/220px-Theholidayposter.jpg",
    "https://www.youtube.com/watch?v=2py-VG-UHhI",
    "Amazon Video, iTunes",
    "Kate Winslet, Cameron Diaz, Jude Law")

movies = [imitation_game, the_rock, sense_and_sensibility,
          ratatouille, playing_by_heart, the_holiday]

# Uses a list of movie instances (movies) as input to generate an HTML file
# and open it in the browser
fresh_tomatoes.open_movies_page(movies)
