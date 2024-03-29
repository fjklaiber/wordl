
class Secret:
    def __init__(self, word):
        self.word = word

    def check_word(self, tried_word):
        #print("Check word", tried_word, "with secret", self.word)
        if tried_word == self.word:
            return True, None
        def_cond = [("", "")]
        conditions = [5 * def_cond][0]
        rep_letters = dict()
        for l in self.word:
            rep_letters[l] = self.word.count(l)
        for i in range(5):
            if type(tried_word) is None or type(self.word) is None:
                print('problem')
            if tried_word[i] == self.word[i]:
                conditions[i] = (tried_word[i], "exact")
                rep_letters[tried_word[i]] -= 1
        for i in range(5):
            if type(tried_word) is None or type(self.word) is None:
                print('problem')
            elif tried_word[i] != self.word[i] and tried_word[i] in self.word and rep_letters[tried_word[i]] > 0:
                conditions[i] = (tried_word[i], "other")
                rep_letters[tried_word[i]] -= 1
            elif tried_word[i] != self.word[i]:
                conditions[i] = (tried_word[i], "not")

        return False, conditions


