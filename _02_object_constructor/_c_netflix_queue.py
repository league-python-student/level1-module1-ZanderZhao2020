class Movie:
    def __init__(self, title, stars):
        self.title = title
        self.stars = stars

    def to_string(self):
        return "\"" + self.title + "\" - " + str(self.stars) + " stars"

    def get_ticket_price(self):
        if self.stars > 2:
            return "That will be $12 please."
        elif 'twilight' in self.title.lower():
            return "This movie is so bad, we'll pay YOU to watch it!"
        else:
            return "Don't waste your money on this horrible rubbish."


class NetflixQueue:
    def __init__(self):
        self.movies = list()

    def get_best_movie(self):
        self.sort_movies_by_rating()
        return self.movies[0]

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movie(self, movie_number):
        return self.movies[movie_number]

    def sort_movies_by_rating(self):
        self.movies.sort(key=lambda movie: movie.stars, reverse=True)

    def print_movies(self):
        print("Your Netflix queue contains: ")

        for movie in self.movies:
            print(movie.to_string())


if __name__ == '__main__':
    pass
    # Use Movie and NetflixQueue classes above to complete the following changes:

    # TODO 1) Instantiate (create) at least 5 Movie objects.
    movies = []
    for c in range(5):
        movies.append(Movie("movie " + str(c), c))
    # TODO 2) Use the Movie class to get the ticket price of one of your movies.
    print(movies[0].get_ticket_price())
    # TODO 3) Instantiate a NetflixQueue object.
    queue = NetflixQueue()
    # TODO 4) Add your movies to the Netflix queue.
    for movie in movies:
        queue.add_movie(movie)
    # TODO 5) Print all the movies in your queue.
    queue.print_movies()
    # TODO 6) Use your NetflixQueue object to finish the sentence "the best movie is...."
    queue.sort_movies_by_rating()
    print("the best movie is " + queue.movies[0].title)
    # TODO 7) Use your NetflixQueue to finish the sentence "the second best movie is...."
    print("the second best movie is " + queue.movies[1].title)

