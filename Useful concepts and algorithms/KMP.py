# KMP (Knuth-Morris-Pratt) Algorithm for Pattern Matching

def compute_lps(pattern):
    """
    Builds the Longest Prefix Suffix (LPS) array used by KMP algorithm.
    """
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length > 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
                
    return lps


def kmp_search(text, pattern):
    """
    Searches for the pattern in the text using the KMP algorithm.
    Returns the starting index of the first match, or -1 if not found.
    """
    n, m = len(text), len(pattern)
    if m == 0:
        return 0

    lps = compute_lps(pattern)

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - m  # match found
        else:
            if j > 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


# --- Example usage ---

if __name__ == "__main__":
    text = "abxabcabcaby"
    pattern = "abcaby"
    
    print(f"Given text '{text}', find pattern '{pattern}'.")

    index = kmp_search(text, pattern)
    if index != -1:
        print(f"Pattern found at index {index}")
    else:
        print("Pattern not found")
