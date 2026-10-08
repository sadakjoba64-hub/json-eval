import json
from pathlib import Path
from metrics import evaluate
BASE_DIR = Path(__file__).resolve().parent

names = ["samples", "samples_b","samples_c"]                # 要评估的数据文件名列表（不含 .json）
for name in names:                              # 每一轮从列表里取一个名字，放进变量 name

    with open(BASE_DIR / f"{name}.json", "r", encoding="utf-8") as file:
        samples = json.load(file)

    report = evaluate(samples)
    report["total"]=len(samples)
    print(report)

    with open(BASE_DIR/f"report_{name}.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"报告已保存到 report_{name}.json")

    wrong_samples = []

    for sample in samples:
        if sample["pred"] != sample["truth"]:
            wrong_samples.append(sample)

    with open(BASE_DIR/f"wrong_{name}.json", "w", encoding="utf-8") as file:
        json.dump(wrong_samples, file, indent=4)

    print(f"错误样本已保存到 wrong_{name}.json")