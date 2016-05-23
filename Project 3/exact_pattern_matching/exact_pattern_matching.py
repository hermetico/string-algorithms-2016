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
        self.patterns_at = []
    #if psx_ba==None:
    #    psx_ba = make_border_array(pattern+"$"+x)
        m = len(pattern)
        psx_ba = make_border_array(pattern+"$"+self.string)
        for index, val in enumerate(psx_ba):
            if val == m:
                self.patterns_at.append(index-2*m)

        return self.patterns_at[:]

    def naive_pattern_matching(self, pattern):
        """Naive implementation for an exact pattern matching algorithm"""
        self.patterns_at = []
        pattern_length = len(pattern)
        string_length = len(self.string)
        # loops through the string
        for index in range((string_length - pattern_length) + 1):
            #  loops through the pattern
            match_index = 0

            while match_index < pattern_length and pattern[match_index] == self.string[index]:
                match_index += 1
                index += 1
            if match_index == pattern_length:
                self.patterns_at.append(index - pattern_length)

        return self.patterns_at[:]

    def __border_preprocessing__(self, pattern):
        """
        Computes a border array and a modified version for the kmp
        :param pattern: the string to compute
        :return: <border-array>, <modified border-array>
        """
        n = len(pattern)
        res = make_border_array(pattern)
        res_ = [0] * (n + 1)
        for i in range(1, n + 1):
            res_[i] = res[i-1] + 1
        return res, res_


    def __match__(self, string_index, pattern_index, pattern_length):
        """
        Loops through the string and the pattern until it's the end of the pattern or
        string and pattern differ
        :param string_index:
        :param pattern_index:
        :param pattern_length:
        :return:
        """
        while pattern_index != pattern_length and self.string[string_index] == self.pattern[pattern_index]:
            string_index += 1
            pattern_index += 1

        return string_index, pattern_index

    def kmp_pattern_matching(self, pattern):
        """
        Computes the kmp pattern matching
        :param pattern:
        :return:
        """
        self.pattern = pattern
        self.string = self.string
        self.patterns_at = []
        pattern_length = len(self.pattern)
        string_length = len(self.string)
        b, b_ = self.__border_preprocessing__(pattern)

        string_index, pattern_index = 0, 0


        while string_index <= string_length - pattern_length + pattern_index :

            # trying to avoid overhead...
            # string_index, pattern_index = self.__match__(string_index, pattern_index, pattern_length)
            while pattern_index != pattern_length and self.string[string_index] == self.pattern[pattern_index]:
                string_index += 1
                pattern_index += 1

            if pattern_index == pattern_length:
                self.patterns_at.append(string_index - pattern_length)
            if pattern_index == 0:
                string_index += 1
            else:
                pattern_index = b_[pattern_index] - 1

        return self.patterns_at[:]

if __name__ == "__main__":

    pattern = 'ana'
    string = 'banana'
    patterns_matcher = ExactPatternMatching(string)
    print "String: %s\nPattern: %s" %(string, pattern)
    print  "Naive algorithm"
    print patterns_matcher.naive_pattern_matching(pattern)
    print "BA algorithm"
    print patterns_matcher.ba_pattern_matching(pattern)
    print "KMP algorithm"
    print patterns_matcher.kmp_pattern_matching(pattern)

    pattern = 'bbba'
    string = 'abbacbbbababacabbbba'
    patterns_matcher = ExactPatternMatching(string)
    print "String: %s\nPattern: %s" % (string, pattern)
    print  "Naive algorithm"
    print patterns_matcher.naive_pattern_matching(pattern)
    print "BA algorithm"
    print patterns_matcher.ba_pattern_matching(pattern)
    print "KMP algorithm"
    print patterns_matcher.kmp_pattern_matching(pattern)


    """
    print patterns_matcher.search(pattern, mode='naive-pattern-matching', string=string)
    print patterns_matcher.search(pattern, mode='kmp-pattern-matching', string='abaababaabaababaababaabaababaabaababaababaabaababa')

    print "change"
    pattern  = "aaa"
    string = "".join(['a'] * 50)
    patterns_matcher = ExactPatternMatching(string)
    print patterns_matcher.ba_pattern_matching(pattern)
    print patterns_matcher.search(pattern, mode='naive-pattern-matching', string=string)
    print patterns_matcher.kmp_pattern_matching(pattern)
    """