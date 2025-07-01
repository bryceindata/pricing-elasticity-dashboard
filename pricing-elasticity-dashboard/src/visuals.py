import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_elasticity_by_store(elasticity_csv="outputs/elasticity_report.csv"):
    df = pd.read_csv(elasticity_csv)

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x="Store #", y="ElasticityScore")
    plt.axhline(-1, color="red", linestyle="--", label="Elastic Threshold")
    plt.title("Price Elasticity Distribution by Store")
    plt.ylabel("Elasticity Score")
    plt.legend()
    plt.tight_layout()
    os.makedirs("outputs/visuals", exist_ok=True)
    plt.savefig("outputs/visuals/elasticity_by_store.png")
    plt.close()

def plot_alert_counts(alert_csv="outputs/alerts.csv"):
    df = pd.read_csv(alert_csv)

    alert_counts = df.groupby("Store #").size().reset_index(name="AlertCount")

    plt.figure(figsize=(10, 6))
    sns.barplot(data=alert_counts, x="Store #", y="AlertCount", palette="Reds")
    plt.title("Volume Drop Alerts by Store")
    plt.ylabel("Number of Alerts")
    plt.tight_layout()
    os.makedirs("outputs/visuals", exist_ok=True)
    plt.savefig("outputs/visuals/alerts_by_store.png")
    plt.close()
