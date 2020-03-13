import pandas as pd

jeopardy_data = pd.read_csv('./jeopardy_starting/jeopardy.csv')

pd.set_option('display.max_colwidth', len(jeopardy_data.columns))

print(jeopardy_data.head(20))

print("columns = ", jeopardy_data.columns)

word_list = [" King ", " England "]


def is_word_in_sentence(sentence, lst):
    for word in lst:
        if sentence.lower().find(word.lower(), 0, len(sentence)) < 0:
            return False
    return True


# def string_to_float(string):
#
#     return string.sub_string(1,len(string))
#
# new_df = jeopardy_data[jeopardy_data[" Question"].apply(lambda x: is_word_in_sentence(x, word_list))]
# print(len(new_df))
#
def string_to_float(str):

    pass


jeopardy_data[" Value"] = jeopardy_data[" Value"].apply(lambda x: string_to_float(x))
