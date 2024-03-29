from secret import Secret
from dictionary import words_set
from iteration import remove_words, find_next_word


words = words_set.copy()
MAXIMUM_ITERS = 20


def printInfo(text, log=False):
    if log:
        print("\t" + text)


def discover_word(hidden, log=False):
    cands = words.copy()
    secret = Secret(hidden)
    conditions = []
    # config = Config()
    n_iters = 0
    found = False
    tried_words = []
    got_conditions = []
    while len(cands) > 1 and n_iters < MAXIMUM_ITERS:
        #print("iter", n_iters)
        cands = remove_words(conditions, cands, tried_words)
        #if len(cands) < 10:
        #    print(len(cands), "cands:", cands)
        if len(cands) == 1:
            if n_iters > 5:
                print("FOUND:", list(cands)[0], "n iterations", n_iters)
            n_iters += 1
            found = True
            """if n_iters_dict.keys().__contains__(n_iters):
                n_iters_dict[n_iters] += 1
            else:
                n_iters_dict[n_iters] = 1"""
            #print("break 1")
            if n_iters > 6:
                settings = dict()
                settings["conditions"] = got_conditions
                settings["words"] = tried_words
                #print("writing ", hidden)
                #write_json(settings, os.path.join("data", "data_" + hidden + "_iters_" + str(n_iters)))
            break
        # ("number of candidates", len(cands))
        n_items, next_word = find_next_word(cands, words, tried_words, log)
        #print("Next word", next_word)
        if n_items > 1:
            #print('found more than one')
            for word in next_word:
                if not tried_words.__contains__(word):
                    next_word = word
                    #print("next word", next_word)
                    tried_words.add(word)
                    #print("break 2")
                    break
        tried_words.append(next_word)
        found, conditions = secret.check_word(next_word)
        got_conditions.append(conditions)
        #print(found, conditions)
        n_iters += 1
        if found:
            printInfo("FOUND: " + next_word + " n iters: " + n_iters, log)
            """if n_iters_dict.keys().__contains__(n_iters):
                n_iters_dict[n_iters] += 1
            else:
                n_iters_dict[n_iters] = 1"""
            #print("break 3")
            if n_iters > 6:
                settings = dict()
                settings["conditions"] = got_conditions
                settings["words"] = tried_words
                #print("writing ", hidden)
                #write_json(settings, os.path.join("data", "data_" + hidden + "_iters_" + str(n_iters)))

            break
        #print(len(cands), n_iters)
    #print()
    if not found:
        """if n_iters_dict.__contains__(MAXIMUM_ITERS):
            n_iters_dict[MAXIMUM_ITERS] += 1
        else:
            n_iters_dict[MAXIMUM_ITERS] = 1"""
        print("problems at word", hidden)
        print("used words", tried_words)
        print("used conditions", got_conditions)
        settings = dict()
        settings["conditions"] = got_conditions
        settings["words"] = tried_words
        #write_json(settings, os.path.join("data", "data_" + hidden + "_" + str(n_iters_dict[MAXIMUM_ITERS])
        #                                  + "_limit_iters_" + str(MAXIMUM_ITERS)))