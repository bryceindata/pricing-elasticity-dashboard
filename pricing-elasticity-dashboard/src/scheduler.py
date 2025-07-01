from src.data_loader import load_data
from src.regression import calculate_elasticity
from src.alerts import detect_volume_drop
import pandas as pd

def weekly_update():
    df = load_data()
    elasticity_df = calculate_elasticity(df)
    alerts = detect_volume_drop(df)

    elasticity_df.to_csv("outputs/elasticity_report.csv", index=False)
    pd.DataFrame(alerts).to_csv("outputs/alerts.csv", index=False)

    print("Weekly update completed. Reports saved to outputs/.")

if __name__ == "__main__":
    weekly_update()
