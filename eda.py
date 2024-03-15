import pandas as pd
import subprocess

def main():
    df = pd.read_csv("res_dpre.csv")
    insights = [
        "Insight 1: The mean value of Age is {}.".format(df['Age'].mean()),
        "Insight 2: The Survived count are {}.".format((df['Survived'] == 1).sum()),
        "Insight 3: There are {} unique categories in Pclass.".format(df['Pclass'].nunique())
    ]
    for i, insight in enumerate(insights, start=1):
        with open(f"eda-in-{i}.txt", "w") as file:
            file.write(insight)
    print("Insights saved to text files.")
    
    subprocess.run(["python3", "vis.py"])

if __name__ == "__main__":
    main()
