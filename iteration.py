from dictionary import words_set

WORDS_LENGTH = 5

def check_word_contains(letter, word):
    return letter in word


def check_letter_in_position(position, letter, word):
    return word[position] == letter


def correct_double_letters(conditions):
    letters = set()
    repeated = ""
    for cond in conditions:
        if letters.__contains__(cond[0]):
            repeated += cond[0]
        else:
            letters.add(cond[0])
    if len(repeated) == 0:
        return conditions
    new_conds = conditions.copy()
    for i in range(len(new_conds)):
        for rep in repeated:
            #print(rep)
            if rep == new_conds[i][0] and new_conds[i][1] == "not":
                new_conds[i] = (new_conds[i][0]*(repeated.count(rep)+1), "notMultiple")
    return new_conds


def check_letter(check_type, position, letter, word):
    if check_type == "exact":
        #print
        return check_letter_in_position(position, letter, word)
    if check_type == "other":
        if not check_word_contains(letter, word):
            return False
        return not check_letter_in_position(position, letter, word)
    if check_type == "not":
        return not check_word_contains(letter, word)
    if check_type == "notMultiple":
        if word.count(letter[0]) >= len(letter):
            return False
    return True


def remove_words(conditions, candidates, used_words=[]):
    conditions = correct_double_letters(conditions)
    next_candidates = candidates.copy()
    for cand in candidates:
        if cand in used_words:
            next_candidates.remove(cand)
            continue
        for index, cond in enumerate(conditions):
            if not check_letter(cond[1], index, cond[0], cand):
                next_candidates.remove(cand)
                break
    return next_candidates


def printInfo(text, log=False):
    if log:
        print("\t" + text)


def find_next_word(current_candidates, words_set_iter=words_set.copy(), tried_words=set(), log=False):
    printInfo("Current candidates: " + str(len(current_candidates)), log)
    all_words = words_set_iter.copy()
    for word in tried_words:
        all_words.remove(word)
    letters_repetition = dict()
    letters_repetition_pos = []
    for i in range(WORDS_LENGTH):
        letters_repetition_pos.append(dict())
    for word in current_candidates:
        ind_letters = set()
        for index, letter in enumerate(word):
            ind_letters.add(letter)
            if letter in letters_repetition_pos[index]:
                letters_repetition_pos[index][letter] += 1
            else:
                letters_repetition_pos[index][letter] = 1
        for letter in ind_letters:
            for i in range(1, word.count(letter)+1):
                if i*letter in letters_repetition.keys():
                    letters_repetition[i*letter] += 1
                else:
                    letters_repetition[i*letter] = 1

    #print("letters repetition", sorted(letters_repetition, key=letters_repetition.get, reverse=True))
    #print("letters repetition", letters_repetition)
    for lr in letters_repetition.keys():
        letters_repetition[lr] /= len(current_candidates)
        letters_repetition[lr] = abs(letters_repetition[lr] - 0.5)
    sorted_letters = sorted(letters_repetition, key=letters_repetition.get)
    #print("letters utility (inverse)", letters_repetition)
    input_candidates = all_words.copy()
    #print("sorted letters", sorted_letters)
    #print("letter repetition per position")
    #for pos in letters_repetition_pos:
    #    print(pos)
    for letter in sorted_letters:
        #print("candidates for input before letter", letter, ":", len(input_candidates))
        #if len(input_candidates) < 10:
        #    print(input_candidates)
        cur_input_candidates = input_candidates.copy()
        if len(letter) == 1:
            for word in input_candidates.copy():
                if letter not in word:
                    cur_input_candidates.remove(word)
            if len(cur_input_candidates) > 1:
                input_candidates = cur_input_candidates
            elif len(cur_input_candidates) == 1:
                printInfo("Next word: " + list(cur_input_candidates)[0], log)
                return 1, list(cur_input_candidates)[0]
        else:
            for word in input_candidates.copy():
                if word.count(letter[0]) < len(letter):
                    cur_input_candidates.remove(word)
            if len(cur_input_candidates) > 1:
                input_candidates = cur_input_candidates
            elif len(cur_input_candidates) == 1:
                printInfo("Next word: " + list(cur_input_candidates)[0], log)
                return 1, list(cur_input_candidates)[0]

    if len(input_candidates) > 1:
        #printInfo("multiple candidates", log)
        current_max = -1
        current_word = None
        for word in input_candidates:
            cur_val = 0
            for index, letter in enumerate(word):
                if letter in letters_repetition_pos[index].keys():
                    cur_val += letters_repetition_pos[index][letter]
            #printInfo("Value of word " + word + " " + str(cur_val), log)
            if cur_val > current_max:
                current_max = cur_val
                current_word = word
        printInfo("Next word: " + current_word, log)
        return 1, current_word
        # return len(input_candidates), current_word
    else:
        print("not set", len(input_candidates))
    return 0, None


def compute_conditions(settings, all_words):
    current_candidates = all_words.copy()
    for conditions in settings["conditions"]:
        used = ""
        if len(settings["words"]) > 0:
            used = settings["words"].pop()
        current_candidates = remove_words(conditions, current_candidates, used)
        print(used)
        print(current_candidates)
    return current_candidates


