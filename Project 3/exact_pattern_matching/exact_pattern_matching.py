from border_array.border_array import make_border_array

class ExactPatternMatching(object):
    def __init__(self, string=None):
        self.string = string
        self.patterns_at = []
        self.pattern = None

    def search(self, pattern, mode='naive-pattern-matching',  **kwargs):
        if kwargs:
            self.__init__(**kwargs)

        if mode == 'naive-pattern-matching':
            return self.naive_pattern_matching(pattern)
        elif mode == 'kmp-pattern-matching':
            return self.kmp_pattern_matching(pattern)
        elif mode == 'ba-pattern-matching':
            return self.ba_pattern_matching(pattern)


    def ba_pattern_matching(self, pattern):#psx_ba=None): #exact pattern matching with border arrays

    #if psx_ba==None:
    #    psx_ba = make_border_array(pattern+"$"+x)
        m = len(pattern)
        psx_ba = make_border_array(pattern+"$"+self.string)
        for index, val in enumerate(psx_ba):
            if val == m:
                print index-2*m

    def naive_pattern_matching(self, pattern):
        """Naive implementation for an exact pattern matching algorithm"""
        self.patterns_at = []
        pattern_length = len(pattern)
        string_length = len(self.string)
        # loops through the string
        for index in range(string_length):
            #  loops through the pattern
            for match_index in range(pattern_length + 1):
                # checks if the whole pattern has been checked
                if match_index == pattern_length:
                    self.patterns_at.append(index)
                    break
                # checks if the character is equal
                if index+match_index >= len(self.string):
                    break
                if self.string[index + match_index] != pattern[match_index]:
                    break
        return self.patterns_at


    def __border_preprocessing__(self, pattern):
        n = len(pattern)
        res = [None] * n
        res_ = [0] * (n + 1)
        res[0] = 0

        for i in range(0, n - 1):
            b = res[i]
            while b > 0 and (pattern[i + 1] != pattern[b]):
                b = res[b - 1]
            if pattern[i + 1] == pattern[b]:
                res[i + 1] = b + 1
            else:
                res[i + 1] = 0

        for i in range(1, n + 1):
            res_[i] = res[i-1] + 1
        return res, res_


    def __match__(self, string_index, pattern_index, pattern_length):
        while self.string[string_index] == self.pattern[pattern_index]:
            string_index += 1
            pattern_index += 1
            if pattern_index == pattern_length:
                break
        return string_index, pattern_index


    def kmp_pattern_matching(self, pattern):
        self.pattern = pattern
        self.string = self.string
        self.patterns_at = []
        pattern_length = len(self.pattern)
        string_length = len(self.string)
        b, b_ = self.__border_preprocessing__(pattern)

        string_index, pattern_index = 0, 0


        while string_index <= string_length - pattern_length + pattern_index :

            string_index, pattern_index = self.__match__(string_index, pattern_index, pattern_length)

            if pattern_index == pattern_length:
                self.patterns_at.append(string_index - pattern_length)
            if pattern_index == 0:
                string_index += 1
            else:
                pattern_index = b_[pattern_index] - 1

        return self.patterns_at




if __name__ == "__main__":
    patterns_matcher = ExactPatternMatching('abbacbbbababacabbbba')
    print patterns_matcher.naive_pattern_matching('bbba')
    print patterns_matcher.kmp_pattern_matching('bbba')

