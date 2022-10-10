from app.common.string import trie_utils


def test_iter_forms():
    trie = trie_utils.build_trie_from_dict(
        {
            'A': 97,
            'B': 98,
            'C': 99,
            'ABC': 979899,
        },
        to_lower=True
    )
    s = 'a B ABc'
    assert list(trie_utils.iter_forms(trie, s)) == [
        ('a', 0, 1),
        ('c', 6, 7),
    ]
    assert list(trie_utils.iter_forms(trie, s, whole_word=True)) == [
        ('a', 0, 1)
    ]
    assert list(trie_utils.iter_forms(trie, s, match_lower=True, whole_word=True)) == [
        ('a', 0, 1),
        ('B', 2, 3),
        ('ABc', 4, 7)
    ]
    assert list(trie_utils.iter_forms(trie, s, match_lower=True, whole_word=True, return_lower=True)) == [
        ('a', 0, 1),
        ('b', 2, 3),
        ('abc', 4, 7)
    ]
