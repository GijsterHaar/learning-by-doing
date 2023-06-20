'''
    This program will print the following information to the screen:
    Total number of movies: 231
    Average rating of movies: 2.7
    Best movie: "2 Fast 2 Furious"
    Worst movie: "Citizen Kane"

    class: Movie, MovieCollection

    class Movie:
    properties: title, actors, year, genre, rating

    class MovieCollection:
    properties: collection
    methods: calculate avg rating, find best movie, find worst movie
'''

class Movie:
    def __init__(self, title, actors, year, genre, rating):
        self.title = title
        self.actors = actors
        self.year = year
        self.genre = genre
        self.rating = rating

    def __str__(self):
        return f'{self.title}, {self.rating}'

    def __lt__(self, other):
        if not isinstance(other, Movie):
            raise TypeError('object "other" is not an instance of movie')
        return self.rating < other.rating

    def __gt__(self, other):
        return self.rating > other.rating

class MovieCollection:
    def __init__(self, movies):
        self._collection = []
        if movies:
            for movie in movies:
                self._collection.append(movie)

    def number_of_movies_in_collection(self):
        return f'There are {len(self._collection)} movies'

    def calculate_avg_rating(self):
        avg_rating = 0
        for movie in self._collection:
            avg_rating += movie.rating
        avg_rating = avg_rating / len(self._collection)
        return f'The average rating is {avg_rating}'

    def get_best_movie(self):
        the_best_movie = None
        for movie in self._collection:
            if the_best_movie is None or the_best_movie < movie:
                the_best_movie = movie
        return f'The best movie is {the_best_movie.title} with a rating of {the_best_movie.rating}'

    def get_worst_movie(self):
        the_worst_movie = None
        for movie in self._collection:
            if the_worst_movie is None or the_worst_movie > movie:
                the_worst_movie = movie
        return f'The worst movie is {the_worst_movie.title} with a rating of {the_worst_movie.rating}'

    def __str__(self):
        return f'{self.calculate_avg_rating()}, {self.get_best_movie()}'

movies = [
    Movie("Star Wars Episode IV: A New Hope", ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guiness"], 1977, "science fiction", 7),
    Movie("Star Wars Episode I: The Phantom Menace", ["Liam Neeson", "Ewan McGregor", "Natalie Portman", "Jake Lloyd", "Brian Blessed"], 1999, "science fiction", 3),
    Movie("Star Trek IV: The Voyage Home", ["William Shatner", "Leonard Nimoy", "Michelle Nichols"], 1986, "science fiction", 8),
    Movie("Airplane!", ["Leslie Nielsen", "Robert Stack", "Lloyd Bridges"], 1980, "comedy", 9),
    Movie("The Naked Gun: From The Files Of Police Squad!", ["Leslie Nielsen", "O. J. Simpson", "Priscilla Presley"], 1988, "comedy", 8),
    Movie("Leprechaun", ["Warwick Davis", "Jennifer Aniston"], 1993, "horror", 6),
    Movie("Leprechaun 4: In Space", ["Warwick Davis"], 1996, "horror", 10),
    Movie("Flash Gordon", ["Brian Blessed", "Timothy Dalton", "Max von Sydow"], 1980, "science fiction", 6),
    Movie("The Rock", ["Nicolas Cage", "Sean Connery", "Ed Harris", "Michael Biehn"], 1996, "action", 8),
    Movie("Con Air", ["Nicolas Cage", "John Malkovich", "John Cusack", "Steve Buscemi", "Ving Rhames"], 1997, "action", 9),
    Movie("Airheads", ["Brendan Fraser", "Adam Sandler", "Steve Buscemi", "Judd Nelson", "Lemmy Kilmister"], 1994, "comedy", 5),
    Movie("The Breakfast Club", ["Judd Nelson", "Emilio Estevez", "Ally Sheedy", "Molly Ringwald"], 1985, "drama", 6),
    Movie("Wargames", ["Matthew Broderick", "Ally Sheedy"], 1983, "drama", 8),
    Movie("Godzilla", ["Matthew Broderick", "Jean Reno"], 1998, "action", 6),
    Movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 10),
]

my_collection = MovieCollection(movies)
# print(my_collection)
# movies.clear()
# print(len(movies))
# print(my_collection.number_of_movies_in_collection())
# print(my_collection.calculate_avg_rating())
print(my_collection.get_best_movie())
print(my_collection.get_worst_movie())
