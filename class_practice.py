class Sample:
    def __init__(self, sample_id,pred,truth):
        self.sample_id = sample_id
        self.pred = pred
        self.truth = truth



    def is_correct(self):  # 动作 1：判断对不对
        return self.pred == self.truth


    def describe(self):  # 动作 2：拼一句说明文字
        return f"样本 {self.sample_id}：预测 {self.pred}，真实 {self.truth}"

s1 = Sample(1, "cup", "cup")
s2 = Sample(2, "book", "cup")
s3 = Sample(3, "pen", "phone")
print(s3.is_correct())
print(s3.describe())
print(s3.is_correct)