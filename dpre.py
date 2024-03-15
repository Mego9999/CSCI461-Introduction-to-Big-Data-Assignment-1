import pandas as pd
import subprocess
import sys

def main(file_path):
    df = pd.read_csv(file_path)
    df.set_index(df.columns[0], inplace=True)
    df.drop(columns=['Cabin', 'Name', 'Ticket'], inplace=True)
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    most_frequent_value = df['Embarked'].value_counts().idxmax()
    df['Embarked'].fillna(most_frequent_value, inplace=True)
    df_cleaned = df.drop_duplicates()
    df_cleaned["Age"] = df_cleaned["Age"].astype(int)
    df_cleaned["Survived"] = df_cleaned["Survived"].astype(int)
    df_cleaned = pd.get_dummies(df_cleaned, columns=['Sex', 'Embarked'])
    df_cleaned.to_csv("res_dpre.csv", index=False)
    print("Preprocessed data saved to res_dpre.csv.")
    
    subprocess.run(["python3", "eda.py"])

if __name__ == "__main__":
    main(sys.argv[1])
