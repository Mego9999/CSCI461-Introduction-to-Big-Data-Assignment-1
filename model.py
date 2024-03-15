import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import subprocess

def main():
    df = pd.read_csv("res_dpre.csv")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_scaled)
    labels = kmeans.labels_
    cluster_counts = pd.Series(labels).value_counts()
    cluster_counts.to_csv("k.txt", header=None)
    print("Number of records in each cluster saved to k.txt.")
if __name__ == "__main__":
    main()
