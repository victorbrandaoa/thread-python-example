# thread-python-example

## How to run this code?

You'll need docker installed, then you can run the following commands.

```sh
docker build . --tag=thread-example

docker run thread-example
```

## Example explanation

In this example, I'm using the Bert pretrained model from huggingface for Portuguese to create embeddings for some texts.

The goal here is to optimize the creation of embeddings by using python threads to parallelize the process.
