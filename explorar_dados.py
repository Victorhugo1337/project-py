import pandas as pd

df = pd.read_csv("dados/students_habits_perfomance")

print("Prévia do dataset:")
print(df.head())

print("\nInformação do dataset:")
print(df.info())
