import movie_data

def main():
    acting_with_judd = []
    flattened_acting_with_judd_list = []
    ally_sheedy_dict = []
    count = 0
    best = ''
    movie_library = movie_data.movies
    movie_library = matthew_sucks(movie_library)
    acting_with_judd = we_played_with_judd(movie_library, acting_with_judd)
    flattened_acting_with_judd_list = flatten_acting_with_judd(acting_with_judd, flattened_acting_with_judd_list)
    movie_library = playing_with_judd_pays(movie_library, flattened_acting_with_judd_list)
    ally_sheedy_dict = get_ally_sheedy_movies(movie_library, ally_sheedy_dict)
    get_best_ally_sheedy_movie(ally_sheedy_dict, count, best)

def matthew_sucks(movie_library):
    for movie in movie_library:
        for name in movie.get('actors'):
            if name == 'Matthew Broderick':
                movie['rating'] -= 1
    return movie_library

def we_played_with_judd(movie_library, acting_with_judd):
    for movie in movie_library:
        if 'Judd Nelson' in movie.get('actors'):
            acting_with_judd.append(movie.get('actors'))
    return acting_with_judd

def flatten_acting_with_judd(acting_with_judd, flattened_acting_with_judd_list):
    for lijst in acting_with_judd:
        if isinstance(lijst, list):
            for nested_lijst in lijst:
                flattened_acting_with_judd_list.append(nested_lijst)
    return flattened_acting_with_judd_list

def playing_with_judd_pays(movie_library, flattened_acting_with_judd_list):
    for movie in movie_library:
        for name in movie.get('actors'):
            if name in flattened_acting_with_judd_list:
                movie['rating'] += 1
                break
    return movie_library

def get_ally_sheedy_movies(movie_library, ally_sheedy_dict):
    for movie in movie_library:
        for name in movie.get('actors'):
                if name == 'Ally Sheedy':
                    ally_sheedy_dict.append(movie)
    return ally_sheedy_dict

def get_best_ally_sheedy_movie(ally_sheedy_dict, count, best):
    for movie in ally_sheedy_dict:
        rating = movie.get('rating')
        if rating > count:
            count = rating
            best = movie.get('title')
    print(f'\nThe best Ally Sheedy movie is {best}, with a rating of {count}\n')
    

if __name__ == '__main__':
    main()
