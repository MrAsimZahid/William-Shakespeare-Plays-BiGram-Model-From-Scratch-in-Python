import pandas as pd

MODEL_FILEPATH = "model.csv"

def load_model(path):
    """ load probablity matrix for inference """

    df = pd.read_csv(path, index_col=0)
    return df

def predict_next(df, stmt):
    ''' predict net word which highest prob '''

    stmt_words = reversed(stmt.split())
    for w in stmt_words:
        if w in df.columns:
            return df[w].idxmax()
        else:
            print("..out of vocab, trying previous word")
    return "out of vocab"
    

def take_input():
    ''' propmt user for input '''
    sentence = str(input("Enter your stmt: "))
    sentence = sentence.strip()
    return sentence


if __name__ == "__main__":
    df = load_model(MODEL_FILEPATH)
    stmt = take_input()
    print("suggested word = ", predict_next(df, stmt))

