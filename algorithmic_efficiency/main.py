import timeit


# Реалізація алгоритму Кнута-Морріса-Пратта (KMP)
def kmp_search(text, pattern):
    def compute_lps_array(pattern):
        length = 0
        lps = [0] * len(pattern)
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps_array(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


# Реалізація алгоритму Боєра-Мура
def boyer_moore_search(text, pattern):
    def bad_character_rule(pattern):
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    bad_char = bad_character_rule(pattern)
    s = 0
    while s <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1


# Реалізація алгоритму Рабіна-Карпа
def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    i = j = 0
    p = t = 0
    h = 1
    for i in range(M - 1):
        h = (h * d) % q
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == M:
                return i
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
    return -1


def main():
    # Приклад тексту та підрядків для пошуку
    text_example = "This is a simple example text for string searching."
    pattern_real = "simple"
    pattern_fake = "complex"

    # Вимірювання часу виконання кожного алгоритму
    results_real = {
        func.__name__: timeit.timeit(
            lambda: func(text_example, pattern_real), number=1000
        )
        for func in [kmp_search, boyer_moore_search, rabin_karp_search]
    }
    results_fake = {
        func.__name__: timeit.timeit(
            lambda: func(text_example, pattern_fake), number=1000
        )
        for func in [kmp_search, boyer_moore_search, rabin_karp_search]
    }

    # Виводимо результати
    print(f"Text: {text_example}")
    print(f"Real pattern: {pattern_real}")
    print(f"Fake pattern: {pattern_fake}")

    print("\nReal pattern:")
    for func, time in results_real.items():
        print(f"{func}: {time:.7f} seconds")

    print("\nFake pattern:")
    for func, time in results_fake.items():
        print(f"{func}: {time:.7f} seconds")


if __name__ == "__main__":
    main()
