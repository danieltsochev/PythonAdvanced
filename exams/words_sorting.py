def words_sorting(*args):
    words = {}
    result = ''
    sort_dict = {}

    all_value_sum = 0
    for word in args:
        sum_ascii = 0
        for letter in word:
            sum_ascii += ord(letter)
            all_value_sum += ord(letter)
        words[word] = sum_ascii

    if all_value_sum % 2 == 0:
        sort_dict = dict(sorted(words.items(), key=lambda x: x[0]))
    else:
        sort_dict = dict(sorted(words.items(), key=lambda x: -x[1]))

    for key, value in sort_dict.items():
        result += f"{key} - {value}\n"

    return result


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))