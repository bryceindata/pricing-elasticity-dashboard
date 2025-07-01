import pandas as pd
from sklearn.linear_model import LinearRegression

def calculate_elasticity(df):
    elasticity_scores = []

    for sku, group in df.groupby("SKU"):
        if group.shape[0] < 3:
            continue
        X = group[["Price"]].values
        y = group["UnitsSold"].values
        model = LinearRegression().fit(X, y)
        beta = model.coef_[0]

        avg_price = group["Price"].mean()
        avg_units = group["UnitsSold"].mean()
        elasticity = (beta) * (avg_price / avg_units)
        elasticity_scores.append({"SKU": sku, "ElasticityScore": round(elasticity, 2)})

    return pd.DataFrame(elasticity_scores)
