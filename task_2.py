from pygtrie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not strings or not all(isinstance(s, str) for s in strings):
            return ""

        self.clear()

        for word in strings:
            self[word] = True

        # Візьмемо найкоротше слово, бо префікс не може бути довшим за нього
        shortest = min(strings, key=len)
        prefix = ""

        for i in range(len(shortest)):
            char = shortest[i]
            prefix_candidate = shortest[:i + 1]
            # Перевіряємо: чи всі слова мають цей префікс
            if all(s.startswith(prefix_candidate) for s in strings):
                prefix = prefix_candidate
            else:
                break

        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""