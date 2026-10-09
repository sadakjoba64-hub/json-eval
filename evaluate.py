import json
import argparse                   # Python 自带：读取命令行参数
from pathlib import Path
from metrics import evaluate, count_wrong_by_class
BASE_DIR = Path(__file__).resolve().parent

parser = argparse.ArgumentParser(description="评估 JSON 数据的正确率")   # 创建一个“参数解析器”
parser.add_argument("--input", required=True, help="要评估的 JSON 文件名，例如 samples.json")   # 规定程序接受 --input，而且必须给
args = parser.parse_args()        # 真正去读运行时写在命令行里的参数，结果放进 args
print("这次的输入文件是：", args.input)   # args.input 就是 --input 后面写的那个值

names = [Path(args.input).stem]   # .stem = 去掉扩展名的文件名："samples_b.json" → "samples_b"
#names = ["samples", "samples_b","samples_c"]                # 要评估的数据文件名列表（不含 .json）
for name in names:                              # 每一轮从列表里取一个名字，放进变量 name

    with open(BASE_DIR / f"{name}.json", "r", encoding="utf-8") as file:
        samples = json.load(file)

    report = evaluate(samples)
    report["total"]=len(samples)
    report["wrong_by_class"] = count_wrong_by_class(samples)
    print(report)

    #print("按类别的错误数：", count_wrong_by_class(samples))
    print("按类别的错误数：", report["wrong_by_class"])   # 从 report 里取，不重新算
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

