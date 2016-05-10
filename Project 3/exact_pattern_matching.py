import sys


class ExactPatternMatching(object):
    def __init__(self, string=None):
        self.string = string
        self.patterns_at = []

    def search(self, pattern, mode='naive-pattern-matching',  **kwargs):
        if kwargs:
            self.__init__(**kwargs)

        if mode == 'naive-pattern-matching':
            return self.naive_pattern_matching(pattern)
        elif mode == 'kmp-pattern-matching':
            print "not yet"

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
                if self.string[index + match_index] != pattern[match_index]:
                    break
        return self.patterns_at


if __name__ == "__main__":
    patterns_matcher = ExactPatternMatching('abbacbbbababacabbbba')
    print patterns_matcher.naive_pattern_matching('bbba')

