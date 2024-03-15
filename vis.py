import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

def main():
    df = pd.read_csv("res_dpre.csv")
    sns.countplot(x='Pclass', hue='Survived', data=df)
    plt.title('Survival Rate by Passenger Class')
    plt.xlabel('Passenger Class')
    plt.ylabel('Count')
    plt.legend(title='Survived', labels=['No', 'Yes'])
    plt.savefig('vis.png')
    plt.show()
    print("Visualization saved as vis.png.")
    
    subprocess.run(["python3", "model.py"])

if __name__ == "__main__":
    main()
