from itertools import permutations
chunk_size = 5

# def possible_permutations(my_list):
#     possibles = list(permutations(my_list))
#     for permutation in possibles:
#         print(permutation)

# possible_permutations([1, 2, 3, 4])

rank_order_list_straight = ['ace', '2', '3', '4', '5', '6', '7',
                   '8', '9', '10', 'jack', 'queen', 'king', 'ace']

for i in rank_order_list_straight:
    chunked_lists_ranks = [rank_order_list_straight[i:i + chunk_size] for i in range(0, len(rank_order_list_straight))]
    if len(chunked_lists_ranks) == 4:
        break

# print(chunked_lists_ranks)


for chunked_list in chunked_lists_ranks:
    possibles = list(permutations(chunked_list))
    for possible in possibles:
        print(list(possible))


# my_list = ['A', 'C', 'B']
# print(tuple(my_list))