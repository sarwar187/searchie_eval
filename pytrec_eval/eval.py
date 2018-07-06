from pytrec_eval import TrecRun
from pytrec_eval import QRels
from pytrec_eval import evaluate
from pytrec_eval import metrics
from pytrec_eval import precisionAt

run = TrecRun("/home/smsarwar/PycharmProjects/deep-siamese-text-similarity/results/results_multitask.txt")
qrel = QRels('/home/smsarwar/PycharmProjects/deep-siamese-text-similarity/results/qrel.txt')
print(qrel)
print (evaluate(run, qrel, metrics.recall))
print (evaluate(run, qrel, metrics.precisionAt(10)))
print (evaluate(run, qrel, metrics.avgPrec))
#print(metrics.recall(run, qrel, detailed=True))
