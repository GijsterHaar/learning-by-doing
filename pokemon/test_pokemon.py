# grass is strong against water, weak against fire
# water is strong against fire, weak against grass
# fire is strong against grass, weak against water
import pokemon

def test_create_pokemon():
    assert pokemon.create(
        poke={},
        name='bulbasaur',
        type='grass',
        health=5)

def test_what_is_in_a_pokemon():
    squirtle = pokemon.create({}, 'squirtle', 'water', 5)
    result = squirtle['description']()
    assert result  == 'squirtle is a water type pokemon, with 5 health'

def test_what_is_in_a_pokemon_two():
    gijzemans = pokemon.create({}, 'gijzemans', 'fire', 5)
    result = gijzemans['description']()
    assert result  == 'gijzemans is a fire type pokemon, with 5 health'

def test_battle():
    shaams_pokemon = pokemon.create({}, 'bulbasaur', 'grass', 5)
    carlas_pokemon = pokemon.create({}, 'squirtle', 'water', 5)
    result = shaams_pokemon['battle'](carlas_pokemon)
    assert result == 'Yay! Your bulbasaur beat their squirtle!'

def test_battle_two():
    shaams_pokemon = pokemon.create({}, 'bulbasaur', 'grass', 5)
    carlas_pokemon = pokemon.create({}, 'charmander', 'fire', 5)
    result = shaams_pokemon['battle'](carlas_pokemon)
    assert result == "Oh no. Their charmander kicked bulbasaur's arse."

def test_battle_three():
    shaams_pokemon = pokemon.create({}, 'bulbasaur', 'grass', 5)
    carlas_pokemon = pokemon.create({}, 'charmander', 'fire', 5)
    result = carlas_pokemon['battle'](shaams_pokemon)
    assert result == "Yay! Your charmander beat their bulbasaur!"

def test_battle_four():
    gijs_pokemon = pokemon.create({}, 'gijzemans', 'fire', 5)
    carlas_pokemon = pokemon.create({}, 'squirtle', 'water', 5)
    result = gijs_pokemon['battle'](carlas_pokemon)
    assert result == "Oh no. Their squirtle kicked gijzemans's arse."
