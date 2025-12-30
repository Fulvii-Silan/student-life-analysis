import pandas as pd
pd.options.display.max_columns = 9999


data = [
    {
        "student_id": 1,
        "day": 1,
        "sleep": 7,
        "sport": 1,
        "fun": 5,
        "exam": 1,
        "weather": "bad",
        "math": 5,
        "eng": 5,
        "cs": 3,
        "soc": 5,
        "rus": 4,
    },
    {
        "student_id": 1,
        "day": 2,
        "sleep": 6,
        "sport": 0,
        "fun": 4,
        "exam": 0,
        "weather": "good",
        "math": 4,
        "eng": 5,
        "cs": 4,
        "soc": 5,
        "rus": 5,
    }
]


df = pd.DataFrame(data)



df["raw_burnout"] = (
    (12 - df["sleep"]) + 
    df["exam"] * 3 +
    (df["fun"] > 4).astype(int) * 2 -
    df["sport"] * 2
)

df["burnout"] = pd.cut(
   df["raw_burnout"],
   bins = [-100, 3, 6, 9, 12, 100],
   labels = [1, 2, 3, 4, 5]
)


print(df)



print(df[["sleep", "sport", "fun", "exam", "raw_burnout"]].corr())

df["avg_grade"] = df[["math", "eng", "cs", "soc", "rus"]].mean(axis = 1)

print(df[["avg_grade", "burnout"]])