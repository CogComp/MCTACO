import torch
import os
from pytorch_pretrained_bert.file_utils import PYTORCH_PRETRAINED_BERT_CACHE
from pytorch_pretrained_bert.modeling import BertForSequenceClassification
from pytorch_pretrained_bert.tokenization import BertTokenizer
import numpy as np


class Annotator:

    def __init__(self, bert_model):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        cache_dir = os.path.join(str(PYTORCH_PRETRAINED_BERT_CACHE), 'distributed_{}'.format(-1))

        self.model = BertForSequenceClassification.from_pretrained(bert_model,
                                                        cache_dir=cache_dir).to(self.device)
        self.model.eval()
        self.tokenizer = BertTokenizer.from_pretrained(bert_model, do_lower_case=True)
        self.max_seq_length = 128

    def annotate(self, sentence, question, answer):
        tokens = sentence.lower().split() + question.lower().split()
        for i, _ in enumerate(tokens):
            if tokens[i].lower() not in self.tokenizer.vocab:
                tokens[i] = "[UNK]"

        answer = answer.lower().split()
        for i, _ in enumerate(answer):
            if answer[i].lower() not in self.tokenizer.vocab:
                answer[i] = "[UNK]"

        tokens = ["[CLS]"] + tokens + ["[SEP]"] + answer + ["[SEP]"]

        if len(tokens) > self.max_seq_length:
            print("ERROR: input sequence is too long.")
            return None

        segment_ids = [0] * len(tokens)
        input_ids = self.tokenizer.convert_tokens_to_ids(tokens)
        input_mask = [1] * len(input_ids)

        padding = [0] * (self.max_seq_length - len(input_ids))
        input_ids += padding
        input_mask += padding
        segment_ids += padding

        assert len(input_ids) == self.max_seq_length
        assert len(input_mask) == self.max_seq_length
        assert len(segment_ids) == self.max_seq_length

        input_ids = torch.tensor([input_ids], dtype=torch.long).to(self.device)
        input_mask = torch.tensor([input_mask], dtype=torch.long).to(self.device)
        segment_ids = torch.tensor([segment_ids], dtype=torch.long).to(self.device)

        with torch.no_grad():
            logits = self.model(
                input_ids, segment_ids, input_mask
            )

        outputs = np.argmax(logits, axis=1)
        prints = []
        for i in outputs:
            if i == 0:
                prints.append("yes")
            else:
                prints.append("no")
        return prints[0]
