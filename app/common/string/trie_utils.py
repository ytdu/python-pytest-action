import ahocorasick
from .string_utils import is_whole_word


def build_trie_from_dict(str2value, to_lower=False):
    trie = ahocorasick.Automaton()
    for k, v in str2value.items():
        if to_lower:
            k = k.lower()
        trie.add_word(k, (k, v))
    trie.make_automaton()
    return trie


def get_values_by_prefix(trie, prefix):
    kvs = trie.values(prefix, '?', ahocorasick.MATCH_AT_LEAST_PREFIX)
    return [v for k, v in kvs]


def get_value_by_key(trie, key, default=None):
    k, v = trie.get(key, (key, default))
    return v


def iter_forms(trie, s, match_lower=False, whole_word=False, return_lower=False):
    if not trie or not s:
        return
    if match_lower:
        s_lower = s.lower()
        it = trie.iter(s_lower)
    else:
        it = trie.iter(s)
    for end, (k, v) in it:
        end = end + 1
        start = end - len(k)
        if whole_word and not is_whole_word(s, start, end):
            continue
        form = s[start: end]
        if return_lower:
            form = form.lower()
        yield form, start, end
