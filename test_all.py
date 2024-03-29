from discover import discover_word
from dictionary import words_set

n_iters_dict = dict()
words = words_set.copy()

for index, hidden in enumerate(words):
    discover_word(hidden)

    if index % 20 == 0:
        print("n_iters", n_iters_dict, "at index", index)
print(n_iters_dict)
