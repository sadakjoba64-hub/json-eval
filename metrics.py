def evaluate(samples):
    if len(samples) == 0:
        return {
            'accuracy': None,
            'wrong_ids':[]
        }

    correct = 0
    wrong_ids = []

    for sample in samples:
        if sample["pred"] == sample["truth"]:
            correct += 1
        else:
            wrong_ids.append(sample["id"])

    return {
        "accuracy": correct / len(samples),
        "wrong_ids": wrong_ids
    }
