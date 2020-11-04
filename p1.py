import re
import os

# directory which containes txt files
DATA_PATH = "dataset" 

def read_data(directory):
    """
    read text files into one variable and return combined string
    """
    raw_text = ""
    for entry in os.scandir(directory):
        if entry.is_file():
            f = open(entry, "r")
            raw_text += (f.read())
            f.close() 
    return raw_text

def clean_text(text):
    """ 
    remove all special sentences
    remove all non alphanumerica and non space chars
    """

    text = re.sub('<[^>]+>', '', text)
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)
    return text


def write_result(text):
    f = open("cleaned.txt", "w")
    f.write(text)
    f.close()

if __name__ == "__main__":
    text = read_data(DATA_PATH)
    text = clean_text(text)
    write_result(text)