import tiktoken

file = "the-verdict.txt"

with open(file, "r", encoding="utf-8") as f:
    raw_text = f.read()
    
    print("Total number of character:", len(raw_text))
    print(raw_text[:99])

    tokenizer = tiktoken.get_encoding("gpt2")

    ids = tokenizer.encode(raw_text, allowed_special={"<|endoftext|>"})
    print(raw_text == tokenizer.decode(ids))

    # sliding window
    enc_text = tokenizer.encode(raw_text)
    print(len(enc_text))
    enc_sample = enc_text[50:]

    context_size = 4

    x = enc_sample[:context_size]
    y = enc_sample[1:context_size+1]

    print(f"x: {x}")
    print(f"y:      {y}")

    for i in range(1, context_size+1):
        context = enc_sample[:i]
        desired = enc_sample[i]

        print(context, "---->", desired)
        print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))


    