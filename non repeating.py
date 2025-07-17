from collections import OrderedDict

def first_non_repeating_char(s):
    freq = OrderedDict()

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in freq:
        if freq[ch] == 1:
            return ch

    return None  # or -1 or ''

# Example
print(first_non_repeating_char("aabbcdeff"))  # "c"


