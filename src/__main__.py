import pandas as pd
from sentence_transformers import SentenceTransformer
from threading import Thread, Lock

from util import BERT, STEP, DATA_PATH


def encode_document(bert_model, data, lock, result):
	embeddings = bert_model.encode(data)
	lock.acquire()
	result.extend(embeddings)
	lock.release()


def main():
	data = pd.read_csv(DATA_PATH)
	text_column = data['text']
	bert_model = SentenceTransformer(BERT)

	threads = []
	result = []
	lock = Lock()
	for i in range(0, text_column.shape[0], STEP):
		threads.append(
			Thread(
				target=encode_document,
				args=(
					bert_model,
					text_column[i:(i+STEP)].tolist(),
					lock,
					result
				)
			)
		)

	[t.start() for t in threads]
	[t.join() for t in threads]


if __name__ == '__main__':
	main()
