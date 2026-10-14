import argparse
import json
from pathlib import Path
from collections import Counter
BASE_DIR = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description="程序说明")          # 1. 拿一张空白点菜单
parser.add_argument("--input", required=True, help="输入的是exam_a.json")    # 2. 印一栏，标明必填
args = parser.parse_args()                                        # 3. 收单：读命令行
print("这次的输入文件是：", args.input)
name = Path(args.input).stem
count=0
wrong_label=[]
w=Counter()
with open(BASE_DIR/ f"{name}.json", 'r', encoding='utf-8') as f:
    sampes = json.load(f)
print(len(sampes))
for sample in sampes:
    sample["prediction"]=sample["prediction"].strip()
    sample["label"]=sample["label"].strip()
    sample["prediction"] = sample["prediction"].lower()
    sample["label"] = sample["label"].lower()
    if sample["prediction"]== sample["label"]:
        count+=1
    else:
        wrong_label.append(sample)
        w[sample["label"]] += 1
total = len(sampes)
if total == 0:
    accuracy = 0
else:
    accuracy = count / total
print("总数:", total, "正确数:", count, "正确率:", accuracy)
print("错误的样本是:",wrong_label,"错误的个数是:",len(wrong_label))
with open(BASE_DIR/f"wrong_{name}.json", 'w', encoding='utf-8') as f:
    json.dump(wrong_label, f, ensure_ascii=False, indent=4)
print(dict(w))
report = {
    "total": total,               # 键 "total" → 变量 total 的值 10
    "correct": count,             # 键 "correct" → 变量 count 的值 5
    "accuracy": accuracy,         # 键 "accuracy" → 0.5
    "wrong_by_class": dict(w),    # 键 "wrong_by_class" → {'dog': 2, 'bird': 1, 'cup': 1, 'cat': 1}
}
with open(BASE_DIR/f"report_{name}.json", 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=4)






