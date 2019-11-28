import sys


def count_words(sentence):
    summary = {}
    word_docket = sentence.split()
    for first_word in word_docket:
        summary[first_word] = 0
        for diff_word in word_docket:
            if first_word == diff_word:
                summary[first_word] += 1
    return summary


if __name__ == '__main__':
    sentence = sys.argv[1]
    report = count_words(sentence)
    for word, count in report.items():
        print(f'{word}: {count}')
