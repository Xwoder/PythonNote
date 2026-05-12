import pandas as pd
from pandas import DataFrame, Series
from tabulate import tabulate

df = pd.DataFrame({
    "team": ["A", "A", "B", "B"],
    "score": [10, 20, 30, 40]
})

df_agg: DataFrame | Series = df.groupby("team")["score"].agg("mean")
print(
    tabulate(df_agg.to_frame(), headers='keys', tablefmt='pretty')
)

df["team_mean"] = df.groupby("team")["score"].transform("mean")

df["zscore"] = (
    df.groupby("team")["score"]
    .transform(lambda x: (x - x.mean()) / x.std())
)

df["ratio"] = (
        df["score"] /
        df.groupby("team")["score"].transform("sum")
)

print(
    tabulate(df, headers='keys', tablefmt='pretty')
)
