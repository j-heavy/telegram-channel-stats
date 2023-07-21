import sys
import json

def expand_mess(mess):
    if type(mess) == str:
        return mess
    elif type(mess) == list:
        return ''.join(list(map(expand_mess, mess)))
    elif type(mess) == dict and 'text' in mess:
        return expand_mess(mess['text'])

def main(result_filename):
    data = json.load(open(result_filename, encoding='utf8'))
    messages = list(map(expand_mess, data['messages']))
    full = '\n'.join(messages)
    words = full.split()
    uniq_words = set(words)

    n_messages = len(messages)
    total_length = len(full)
    total_n_words = len(words)
    total_n_uniq_words = len(uniq_words)
    avg_lentgh_of_message = total_length / n_messages
    avg_n_words_in_message = total_n_words / n_messages

    print('Number of messages:', n_messages)
    print('Total length of all messages:', total_length)
    print('Total number of words in all messages:', total_n_words)
    print('Total number of unique words from all messages:', total_n_uniq_words)
    print('Average length of message:', avg_lentgh_of_message)
    print('Average number of words in message:', avg_n_words_in_message)
    print()

    print('The most frequent words:')
    words_by_freq = { word: words.count(word) for word in uniq_words }
    words_by_freq = { k: v for k, v in sorted(words_by_freq.items(), key=lambda item: item[1], reverse=True) }
    for word in list(words_by_freq.keys())[:15]:
        print(word, '-', words_by_freq[word])
    print()

    print('The longest words:')
    words_by_length = { word: len(word) for word in uniq_words }
    words_by_length = { k: v for k, v in sorted(words_by_length.items(), key=lambda item: item[1], reverse=True) }
    for word in list(words_by_length.keys())[:15]:
        print(word if len(word) < 40 else word[:40] + ' ...', '-', words_by_length[word])
    print()

result_filename = sys.argv[1] if len(sys.argv) > 1 else './result.json'
main(result_filename)
