import pandas as pd

# 1. Įkeliame duomenis
df = pd.read_csv("duomenys.csv")

print("=== Pradiniai duomenys ===")
print(df, "\n")

# 2. Vidutinio amžiaus skaičiavimas
vid_amzius = df["Amzius"].mean()
print(f"Vidutinis amžius: {vid_amzius:.1f} m.")

# 3. Vidutinis atlyginimas pagal miestą
print("\n=== Vidutinis atlyginimas pagal miestą ===")
print(df.groupby("Miestas")["Atlyginimas"].mean())

# 4. Filtras: žmonės, kurių atlyginimas > 1500
print("\n=== Žmonės su atlyginimu > 1500 ===")
print(df[df["Atlyginimas"] > 1500])

