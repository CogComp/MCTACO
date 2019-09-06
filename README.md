# MC-TACO 🌮
Dataset and code for “Going on a vacation” takes longer than “Going for a walk”: A Study of Temporal Commonsense Understanding, EMNLP 19

## Dataset
We provide the dev/test split as specified in the paper, along with a detailed readme.txt file under `data/`

## Experiments (WIP)
At this point, we provide the outputs of the ESIM/BERT baselines. 

To run BERT baseline: 

First install required packages with `pip install -r experiments/bert/requirements.txt`

`sh experiments/bert/run_bert_baseline.sh`
- This will produce results by default under ./bert_output, which you can further evaluate with

`python experiments/evaluator.py eval --test_file data/test_9442.tsv --prediction_file bert_output/eval_outputs.txt`

ESIM baseline: Releasing soon after some polish

## Citation
See the following paper:

```
@inproceedings{ZKNR19,
    author = {Ben Zhou, Daniel Khashabi, Qiang Ning and Dan Roth},
    title = {“Going on a vacation” takes longer than “Going for a walk”: A Study of Temporal Commonsense Understanding },
    booktitle = {EMNLP},
    year = {2019},
}
```
