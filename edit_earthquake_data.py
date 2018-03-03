import pandas

data = pandas.read_csv("data.csv")

#replace missing ages with mean
data["Age"] = data["Age"].apply(lambda x: "25_39" if x=="don_t_know" or x=="refused" else x)

