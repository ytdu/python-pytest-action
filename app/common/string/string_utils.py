def to_caps(s):
    ret = s
    for symbol in [' ', '\t', '-', '–']:
        parts = ret.split(symbol)
        cap_parts = []
        for s in parts:
            if s:
                cap_parts.append(s[0].upper() + s[1:])
            else:
                cap_parts.append(s)
        ret = symbol.join(cap_parts)
    return ret


def is_whole_word(s, start, end):
    is_word_sep_left = (start == 0 or is_word_sep(s[start - 1]))
    is_word_sep_right = (end >= len(s) or is_word_sep(s[end]))
    return is_word_sep_left and is_word_sep_right


def is_word_sep(c):
    return not c.isalnum()


def str2bool(s):
    s = s.strip()
    if s.lower() in {'y', 'yes', '1', 'true', 't'}:
        return True
    elif s.lower() in {'n', 'no', '0', 'false', 'f'}:
        return False
    else:
        raise ValueError('cannot convert to bool', s)
