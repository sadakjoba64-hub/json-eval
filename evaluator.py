class Evaluator:
    def __init__(self,name,samples):
        self.name=name
        self.samples=samples
    def accuracy(self):
        count=0
        for sample in self.samples:
            if sample["pred"] == sample["truth"]:
                count=count+1
        return count/len(self.samples)
    def wrong_ids(self):
        wrong_labels = []
        for sample in self.samples:
            if sample["pred"] != sample["truth"]:
                wrong_labels.append(sample["id"])
        return wrong_labels




samples = [
    {"id": 1, "pred": "cup", "truth": "cup"},
    {"id": 2, "pred": "book", "truth": "cup"},
    {"id": 3, "pred": "phone", "truth": "phone"},
    {"id": 4, "pred": "pen", "truth": "bottle"},
]
ev = Evaluator("demo", samples)
print(ev.name)
print(ev.accuracy())
print(ev.wrong_ids())

ev2 = Evaluator("small", samples[:3])   # [:3] = 只取前 3 条
print(ev2.accuracy())