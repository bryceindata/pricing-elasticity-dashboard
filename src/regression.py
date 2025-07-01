import pandas as pd
from sklearn.linear_model import LinearRegression

def calculate_elasticity(df):
    elasticity_scores = []

    for (sku, store), group in df.groupby(["SKU", "Store #"]):
        if group.shape[0] < 3:
            continue
        X = group[["Price"]].values
        y = group["UnitsSold"].values
        model = LinearRegression().fit(X, y)
        beta = model.coef_[0]

        avg_price = group["Price"].mean()
        avg_units = group["UnitsSold"].mean()
        elasticity = (beta) * (avg_price / avg_units)
        elasticity = round(elasticity, 2)

        # Determine Call to Action and Reasoning
        if elasticity < -1:
            action = "Consider price drop"
            reason = f"1. Elasticity score of {elasticity} indicates high sensitivity to price increases."
        elif -1 <= elasticity <= 0:
            action = "No action"
            reason = f"2. Elasticity score of {elasticity} shows price changes have low effect on volume."
        else:
            action = "Investigate pricing"
            reason = f"3. Elasticity score of {elasticity} is unexpected — possible data or price anomaly."

        elasticity_scores.append({
            "SKU": sku,
            "Store #": store,
            "ElasticityScore": elasticity,
            "Call to Action": action,
            "Reasoning": reason
        })

    return pd.DataFrame(elasticity_scores)
