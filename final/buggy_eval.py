# D 部分：修常见报错
# 这个程序本来想做的事：
#   1. 打印第一条样本的真实答案（应该印出 cat）
#   2. 算 exam_a.json 的正确率（不做清理，应该印出 正确率: 0.5）
# 里面埋了 3 个 bug。运行一次只会看到一个报错，修好一个再运行，看下一个。

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
count=0

with open(BASE_DIR / "exam_a.json", "r", encoding="utf-8") as f:
    samples = json.load(f)
    w=samples[0]
    a=w["label"]
print("第一条样本的真实答案:", a)
for sample in samples:
    if sample["prediction"] == sample["label"]:
        count += 1

accuracy = count / len(samples)
print("正确率: " , accuracy)
