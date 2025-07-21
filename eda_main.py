import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\n✅ Dataset loaded successfully.\n")
        print(df.head())
        return df
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return None

def handle_missing_values(df):
    print("\n🛠 Handling missing values...")
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna("Unknown")
        else:
            df[col] = df[col].fillna(df[col].median())
    print("✅ Missing values handled.\n")
    print("Remaining missing values:")
    print(df.isnull().sum())
    return df

def basic_eda(df):
    print("\n📊 Performing basic EDA...")
    print("\nSummary Statistics:")
    print(df.describe(include='all'))

    print("\nColumn Types:")
    print(df.dtypes)

    print("\nNull Values:")
    print(df.isnull().sum())

def generate_visuals(df):
    print("\n📈 Generating visualizations...")

    cat_cols = [col for col in df.columns if df[col].dtype == 'object' and df[col].nunique() < 20]
    for col in cat_cols[:5]:
        plt.figure(figsize=(8, 4))
        sns.countplot(y=col, data=df, order=df[col].value_counts().index)
        plt.title(f'Distribution of {col}')
        plt.tight_layout()
        plt.show()

    num_cols = df.select_dtypes(include='number').columns
    for col in num_cols[:5]:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col], kde=True, bins=30)
        plt.title(f'Distribution of {col}')
        plt.tight_layout()
        plt.show()

    if len(num_cols) > 1:
        plt.figure(figsize=(10, 6))
        sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

def run():
    file_path = input("📂 Enter path to your CSV file: ").strip()
    if not os.path.exists(file_path):
        print("❌ File does not exist.")
        return

    df = load_dataset(file_path)
    if df is None:
        return

    if input("🔧 Handle missing values? (y/n): ").lower() == 'y':
        df = handle_missing_values(df)

    if input("🔍 Perform basic EDA? (y/n): ").lower() == 'y':
        basic_eda(df)

    if input("🖼 Generate visualizations? (y/n): ").lower() == 'y':
        generate_visuals(df)

    print("\n✅ EDA process complete.")

if __name__ == "__main__":
    run()
