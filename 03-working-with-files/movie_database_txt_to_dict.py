
SHOW_MENU_AGAIN = True
DO_NOT_SHOW_MENU = False


def main():
    with open("movie_data.txt", 'r') as file:
        chunked_file = get_the_file(file)
    movie_dict = make_movie_dict(chunked_file)
    main_menu = True
    while main_menu:
        start_message()
        main_menu = navigate_main_menu(movie_dict)


def get_the_file(file):
    file = file.readlines()
    clean_file = [i.strip() for i in file]
    chunk_size = 5
    chunked_file = [clean_file[i:i + chunk_size] for i in range(0, len(clean_file), chunk_size)]
    print(chunked_file)
    return chunked_file


def make_movie_dict(chunked_file):
    movie_dict, key_list = [], ['title', 'actors', 'year', 'genre', 'rating']
    for movies in chunked_file:
        zip_dict = dict(zip(key_list, movies))
        zip_dict['actors'] = zip_dict['actors'].split(', ')
        movie_dict.append(zip_dict)
    print(movie_dict)
    return movie_dict
    

def start_message():
    print("""\n   Movie Database. You can enter your choice of action.
===========================================================
1. List: name and year of all movies.
2. Actor search by name: name and year of all their movies.
3. Genre search: name and year of all movies in that genre.
4. Add: add title, actor, year, genre and rating.
5. Quit\n""")



def get_movie_list(movie_dict):
    for movie in movie_dict:
        title, year = movie.get('title'), movie.get('year')
        print(f'{title}, {year}.')
    print("\nThese are the movies in the database.\nWhat do you want to do next?")
    return SHOW_MENU_AGAIN


def get_actor_data(movie_dict):
    name = input('\nEnter the full name of the actor you are looking for: ')
    print_actor_data(movie_dict, name.title())
    return SHOW_MENU_AGAIN


def print_actor_data(movie_dict, name):
    for movie in movie_dict:
        for actors in movie.get('actors'):
            if name == actors:
                title, year = movie.get('title'), movie.get('year')
                print(f'{title}, {year}.')
    print(f"\nThese are the {name} movies in the database.\nWhat do you want to do next?")


def get_movies_by_genre(movie_dict):
    genre = input('\nEnter the name of the genre you are looking for: ')
    print_genre_data(movie_dict, genre.lower())
    return SHOW_MENU_AGAIN
    

def print_genre_data(movie_dict, genre):
    for movie in movie_dict:
        if genre == movie.get('genre'):
            title, year = movie.get('title'), movie.get('year')
            print(f'{title}, {year}.')
    print(f"\nThese are the {genre} movies in the database.\nWhat do you want to do next?")
    

def input_movies():
    new_movie = {}
    title = input('Please enter your title: ').capitalize()
    actors = input('Please enter the actors, separated by a comma: ').title().split(', ')
    year = int(input('Please enter the year: '))
    genre = input('Please enter the genre: ')
    rating = int(input('Please enter the rating: '))
    update_txtfile(title, actors, year, genre, rating)
    return title, actors, year, genre, rating, new_movie


def add_movies(movie_dict):
    title, actors, year, genre, rating, new_movie = input_movies()
    new_movie['title'] = title
    new_movie['actors'] = actors
    new_movie['year'] = year
    new_movie['genre'] = genre
    new_movie['rating'] = rating
    movie_dict.append(new_movie)
    return SHOW_MENU_AGAIN


def update_txtfile(title, actors, year, genre, rating):
    with open("movie_data.txt", 'a') as file:
        actors = ', '.join(actors)
        file.write(f'\n{title}\n{actors}\n{str(year)}\n{genre}\n{str(rating)}')


def opt_out(movie_dict):
    print()
    return DO_NOT_SHOW_MENU
    

def navigate_main_menu(movie_dict):
    main_choice = int(input('Enter your choice here: '))
    print()
    menu_list = [get_movie_list, get_actor_data, get_movies_by_genre, add_movies, opt_out]
    return menu_list[main_choice -1](movie_dict)


if __name__ == '__main__':
    main()