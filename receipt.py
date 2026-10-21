mehsul1_ad = "Kofe"
mehsul1_qiymet = 4.5

mehsul2_ad = "Çizkeyk"
mehsul2_qiymet = 6.0

mehsul3_ad = "Su"
mehsul3_qiymet = 1.0

cemi = mehsul1_qiymet + mehsul2_qiymet + mehsul3_qiymet
edv = cemi * 0.18
yekun = cemi + edv

print("------ KAFE ------")
print(f"{mehsul1_ad:<10} {mehsul1_qiymet} AZN")
print(f"{mehsul2_ad:<10} {mehsul2_qiymet} AZN")
print(f"{mehsul3_ad:<10} {mehsul3_qiymet} AZN")
print("-" * 20)
print(f"Cəmi:    {cemi} AZN")
print(f"ƏDV 18%: {edv:.2f} AZN")
print(f"Yekun:   {yekun:.2f} AZN")