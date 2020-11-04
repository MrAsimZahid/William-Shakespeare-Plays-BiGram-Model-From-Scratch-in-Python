import matplotlib.pyplot as plt
import pandas as pd

# utility for speed
from collections import Counter

CLEANED_FILEPATH = "cleaned.txt"

def get_word_freq(text):
    text = text.lower()
    word_list = text.split()

    # if Counter allowed, much fatser 
    word_freq = dict(Counter(word_list))
    
    # if Counter not allowed, slower 
    # word_freq = {}
    # unique_words = set(word_list)
    # for w in unique_words:
    #     word_freq[w] = word_list.count(w)
    
    # reverse sort by freq
    word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return word_freq

def read_data(filepath):
    """ read cleaned text """
    
    f = open(filepath, "r")
    cleaned_text = (f.read())
    f.close() 

    return cleaned_text

def write_vocab(word_freq):
    """ write word, freq line by line """

    f = open("vocab.txt", "w")
    for k, v in word_freq:
        f.writelines(f"{k}, {v}\n")
    f.close()


def plot_graph_1(word_freq):
        df = pd.DataFrame(word_freq[:100], columns=['words', 'freq'])
        df.plot.bar(x='words', y='freq')
        plt.show()

def plot_graph_2(word_freq):
        df = pd.DataFrame(word_freq, columns=['words', 'freq'])
        df = df.groupby(['freq']).size().reset_index(name="counts")
        df = df[df.freq <= 250]
        df.plot.bar(y='freq', x='counts', fontsize="6")
        plt.show()
        

if __name__ == "__main__":
    text = read_data(CLEANED_FILEPATH)
    word_freq = get_word_freq(text)
    write_vocab(word_freq)
    plot_graph_1(word_freq)
    plot_graph_2(word_freq)