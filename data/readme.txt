This dataset (MCTACO) is a dataset which aims to evaluate a system's ability to acquire and understand *temporal commonsense* knowledge.

=====================
DIRECTORY STRUCTURE
=====================
├── data
│   ├── dev_3783.tsv
│   └── test_9442.tsv
└── readme.txt

=============
DATASET FILES
=============
The dataset files are:
 * dev_3783.tsv : the dev set, containing 561 questions and 3783 candidate answers.
 * test_9442.tsv : the test set, containing 1332 questions and 9442 candidate answers.

Note there is no training data, and we provide the dev set as the only source of supervision. Please see details in the paper.

In each file (dev_3783.tsv and test_9442.tsv), there are lines of tab-separated data, each line representing an instance of a question-answer pair.
Specifically, the format is as the following:

sentence \t  question \t  answer \t label \t category 

 * sentence: a sentence where the question is based on.
 * question: a question querying some temporal knowledge.
 * answer: a potential answer to the question. all lowercase. 
 * label: whether the answer is a correct (likely) answer. "yes" indicates the answer is likely, "no" otherwise.
 * category: the temporal category the question belongs to one of Event Ordering, Event  Duration", Frequency, Stationarity, or Typical Time. 

===========
EVALUATION
===========
Each question corresponds to multiple candidate answers, and each question can have no "likely" answer or many.
During the test time, the system should only see one question-answer pair at a time, and the gold label/category should not be used if compared with the baselines.
For evaluation metrics, please refer to the paper.


=========
REFERENCE
=========
Zhou et al., “Going on a vacation” takes longer than “Going for a walk”: A Study of Temporal Commonsense Understanding, EMNLP 2019.
