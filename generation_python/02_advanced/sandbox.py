n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

i = n + m - x - t  # books 1 and 2
j = m + k - y - t  # books 2 and 3
q = k + n - z - t  # books 3 and 1
only_two_books = i + j + q

only_first_book = n - q - t - i
only_second_book = m - i - t - j
only_third_book = k - q - t - j
only_one_book = only_first_book + only_second_book + only_third_book

no_one_books = a - only_one_book - only_two_books - t

print(only_one_book, only_two_books, no_one_books, sep="\n")
