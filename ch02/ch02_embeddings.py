import torch
from utils import create_dataloader_v1

input_ids = torch.tensor([2, 3, 5, 1])

torch.manual_seed(123)

# for test
vocab_size = 6
output_dim = 3
embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
print(embedding_layer.weight)
print(embedding_layer(torch.tensor([3])))
print(embedding_layer(input_ids))
#print(embedding_layer(torch.tensor([13])))

# token embedding layer
vocab_size = 50257
output_dim = 256
token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
print(token_embedding_layer.weight)
print(token_embedding_layer(torch.tensor([3])))
print(token_embedding_layer(input_ids))

# position embedding layer
max_length = 4
context_length = max_length
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)

file = "the-verdict.txt"
with open(file, "r", encoding="utf-8") as f:
    raw_text = f.read()

    dataloader = create_dataloader_v1(
        raw_text, batch_size=8, max_length=max_length,
        stride=max_length, shuffle=False
    )
    data_iter = iter(dataloader)
    inputs, targets = next(data_iter)

    print("Token IDs:\n", inputs)
    print("\nInputs shape:\n", inputs.shape)

    token_embeddings = token_embedding_layer(inputs)
    print(token_embeddings.shape)

    pos_embeddings = pos_embedding_layer(torch.arange(max_length))
    print(pos_embeddings.shape)

    input_embeddings = token_embeddings + pos_embeddings
    print(input_embeddings.shape)
