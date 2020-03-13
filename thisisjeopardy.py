import pandas as pd

jeopardy_data = pd.read_csv('./jeopardy_starting/jeopardy.csv')

pd.set_option('display.max_colwidth', len(jeopardy_data.columns))

word_list = [" King ", " England "]


def is_word_in_sentence(sentence, lst):
    for word in lst:
        if sentence.lower().find(word.lower(), 0, len(sentence)) < 0:
            return False
    return True


def string_to_float(string):
    return string.sub_string(1, len(string))


new_df = jeopardy_data[jeopardy_data[" Question"].apply(lambda x: is_word_in_sentence(x, word_list))]


def strin(num):
    if num == "one":
        print("what?")
    num = num[1:]

    for i, c in enumerate(num):
        if c == ',':
            num = num[:i] + "" + num[i + 1:]

    return float(num)


a = jeopardy_data[" Value"].apply(lambda x: strin(x))
#
a = jeopardy_data[" Value"]
print(a)

# print(b)
