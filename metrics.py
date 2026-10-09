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



def count_wrong_by_class(samples):
    counts = {}                                    # 空字典：真实类别 → 错了几次
    for sample in samples:                         # 从列表里一条条取样本（每条是字典）
        if sample["pred"] != sample["truth"]:      # 只数错的
            label = sample["truth"]                # 取这条的真实类别，例如 "cup"
            counts[label] = counts.get(label, 0) + 1
    return counts                                  # 把记账本交回去