import re

file = "the-verdict.txt"

with open(file, "r", encoding="utf-8") as f:
    raw_text = f.read()
    
    print("Total number of character:", len(raw_text))
    print(raw_text[:99])

    preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = [item.strip() for item in preprocessed if item.strip()]
    print(preprocessed[:30])
    print(len(preprocessed))

    all_words = sorted(set(preprocessed))
    vocab_size = len(all_words)
    print(vocab_size)


