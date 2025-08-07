from pygtrie import Trie

class Homework(Trie):

    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Параметр 'pattern' має бути рядком")
        return sum(1 for key in self.keys() if ''.join(key).endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Параметр 'prefix' має бути рядком")
        return self.has_subtrie(prefix)


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie[word] = i

    # Тести
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    assert trie.has_prefix("app") is True
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True
    assert trie.has_prefix("ca") is True

    print("Vel det bra")