import movie_data
"""
This program will import the movie data, and then provide a menu of options to the user.
The user can select an option, the program will do it, and afterwards the program should return to the main menu. The options are:
    1. *List :* List the name and year of all movies, separated by a comma.
    2. *Actor Search :* Prompt for an actor's name, then list the name and year of all their movies.
    3. *Genre Search :* Prompt for a genre name, then list the name and year of every movie in that genre.
    4. *Add :* Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. This new movie should show up in the other searches.
    5. *Quit :* Ends the program.
"""

def main():
    start_message()
    main_choice = enter_main_menu()
    print()
    navigate_main_menu(main_choice)

def start_message():
    print("""\n   Movie Database. You can enter your choice of action.
===========================================================
1. List: name and year of all movies.
2. Actor search by name: name and year of all their movies.
3. Genre search: name and year of all movies in that genre.
4. Add: add title, actor, year, genre and rating.
5. Quit\n""")

def enter_main_menu():
    return int(input('Enter your choice here: '))

def get_movie_list():
    movie_library = movie_data.movies
    for movie in movie_library:
        title, year = movie.get('title'), movie.get('year')
        print(f'{title}, {year}.')
    print("\nThese are the movies in the database.\nWhat do you want to do next?")
    main()

def get_actor_data():
    movie_library = movie_data.movies
    name = input('Enter the name of the actor you are looking for: ')
    print_actor_data(movie_library, name.title())
    main()
    
def print_actor_data(movie_library, name):
    for movie in movie_library:
        for actors in movie.get('actors'):
            if name == actors:
                title, year = movie.get('title'), movie.get('year')
                print(f'{title}, {year}.')
    print(f"\nThese are the {name} movies in the database.\nWhat do you want to do next?")

def get_movies_by_genre():
    movie_library = movie_data.movies
    genre = input('Enter the name of the genre you are looking for: ')
    print_genre_data(movie_library, genre.lower())
    main()

def print_genre_data(movie_library, genre):
    for movie in movie_library:
        if genre == movie.get('genre'):
            title, year = movie.get('title'), movie.get('year')
            print(f'{title}, {year}.')
    print(f"\nThese are the {genre} movies in the database.\nWhat do you want to do next?")

def login():
    user, userpass = 'user', 'userpass'
    logname = input('\nLog in please.\nPlease enter your username: ')
    logpass = input('Please enter your password: ')
    if user == logname and userpass == logpass:
        return
    login_fail()
    
def login_fail():
    next_action = int(input("\nWell, that didn't work.\nPress 1 for login or 2 for main menu: "))
    if next_action == 1:
        login()
    else:
        main()

def input_movies():
    title = input('Please enter your title: ')
    actors = input('Please enter the actors, separated by a comma: ')
    actors = actors.title().replace(' ', '').split(',')
    year = int(input('Please enter the year: '))
    genre = input('Please enter the genre: ')
    rating = int(input('Please enter the rating: '))
    return title, actors, year, genre, rating

def add_input_to_database(title, actors, year, genre, rating):
    movie_library = movie_data.movies
    movie = {'title': title, 'actors': actors, 'year': year, 'genre': genre, 'rating': rating}
    movie_library.append(movie)
    return movie_library


def add_movies():
    login()
    title, actors, year, genre, rating = input_movies()
    movie_library = add_input_to_database(title, actors, year, genre, rating)
    movie_data.movies = movie_library
    main()

def opt_out():
    print()
    quit()

def navigate_main_menu(main_choice):
    menu_list = [get_movie_list, get_actor_data, get_movies_by_genre, add_movies, opt_out]
    return menu_list[main_choice -1]()


if __name__ == '__main__':
    main()