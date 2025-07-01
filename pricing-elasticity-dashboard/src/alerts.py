def detect_volume_drop(df):
    alerts = []

    df = df.sort_values(["SKU", "Date"])
    for sku, group in df.groupby("SKU"):
        group = group.reset_index(drop=True)
        for i in range(1, len(group)):
            price_diff = group.loc[i, "Price"] - group.loc[i-1, "Price"]
            units_diff = (group.loc[i, "UnitsSold"] - group.loc[i-1, "UnitsSold"]) / group.loc[i-1, "UnitsSold"]

            if price_diff > 0 and units_diff < -0.10:
                alerts.append({
                    "SKU": sku,
                    "Date": group.loc[i, "Date"],
                    "Price": group.loc[i, "Price"],
                    "UnitsSold": group.loc[i, "UnitsSold"],
                    "VolumeDrop%": round(units_diff * 100, 2),
                    "Alert": "Price ↑ + Volume ↓ >10%"
                })
    return alerts
