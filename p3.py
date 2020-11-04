import pandas as pd

# utility for speed
from collections import Counter


CLEANED_FILEPATH = "cleaned.txt"
VOCAB_FILEPATH = "vocab.txt"

def read_data(filepath):
    """ read cleaned text """
    
    f = open(filepath, "r")
    cleaned_text = (f.read())
    f.close() 

    return cleaned_text

def prob_matrix(cleaned_text, vocab_data):
    """
    read data and populate matrix
    """
    cleaned_text = cleaned_text.lower()

    # calculate bigrams
    bigrams = [x for x in zip(cleaned_text.split()[:-1], cleaned_text.split()[1:])] 

    # if counter allow, much faster
    bigrams_freq = dict(Counter(bigrams))

    # take first 1000 words from vocab
    vocab_data = vocab_data.split("\n")[:1000]
    vocab_dict = {}
    for line in vocab_data:
        key, value = line.split(",")
        vocab_dict[key] = int(value)
    words = vocab_dict.keys()
    
    # n by n matrix 
    table = []
    for word in words:
        row = []
        for w in words:
            key = (word, w)

            # if counter allowed, much faster
            if (key in bigrams_freq):
                row.append(bigrams_freq[key])
            else:
                row.append(0)

            # if counter not allowed, slower
            # row.append(bigrams.count((word, w)))
 
        table.append(row)
    
    # convert to prob
    df = pd.DataFrame(table, columns=words, index=words)
    df['freq_count'] = vocab_dict.values()
    df = (df[words] + 1) / (df['freq_count'] + len(words))
    df = df.transpose()

    # return pandas df
    return df

def write_df(df):
    """ write model to csv """
    df.to_csv("model.csv")


if __name__ == "__main__":
    cleaned_text = read_data(CLEANED_FILEPATH)
    vocab_data = read_data(VOCAB_FILEPATH)
    df = prob_matrix(cleaned_text, vocab_data)
    write_df(df)
