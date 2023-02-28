import movie_data

def main():
    movie_library = movie_data.movies
    total_movies(movie_library)
    average_rating(movie_library)
    best_movie(movie_library)
    worst_movie(movie_library)

def total_movies(movie_library):
    print(f'\nThere are {len(movie_library)} movies in this folder')

def average_rating(movie_library):
    count = 0
    for movie in movie_library:
        count += movie.get('rating')
    print(f'\nThe average rating is {count/len(movie_library)}')

def best_movie(movie_library):
    highest = 0
    for movie in movie_library:
        if movie.get('rating') > highest:
            highest = movie.get('rating')
            best = movie.get('title')
    print(f'\nThe best movie is {best} with a rating of {highest}')

def worst_movie(movie_library):
    lowest = 11
    for movie in movie_library:
        if movie.get('rating') < lowest:
            lowest = movie.get('rating')
            worst = movie.get('title')
    print(f'\nThe worst movie is {worst} with a rating of {lowest}\n')

if __name__ == '__main__':
    main()
