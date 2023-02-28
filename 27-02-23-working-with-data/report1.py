from movie_data import movie, movies

def main():
    total_movies()
    average_rating()
    best_movie()
    worst_movie()


def total_movies():
    count = 0
    for films in movies:
        count += 1
    print(f'\nThere are currently {count} movies in this folder')
    

def average_rating():
    count = 0
    total_rating_values = 0
    for films in movies:
        count += 1
        rating_values = list(films.values())
        total_rating_values += rating_values[4]
    average = total_rating_values / count
    print(f'Of all {count} movies the average rating is {average}')


def best_movie():
    highest = 0
    best_movie = []
    for films in movies:
        films = (list(films.values()))
        if films[4] > highest:
            highest = films[4]
            best_movie = films[0]
    print(f'The best movie with a rating of {highest} is {best_movie}')

def worst_movie():
    lowest = 11
    worst_movie = []
    for films in movies:
        films = (list(films.values()))
        if films[4] < lowest:
            lowest = films[4]
            worst_movie = films[0]
    print(f'The worst movie with a rating of {lowest} is {worst_movie}\n')




if __name__ == '__main__':
    main()












