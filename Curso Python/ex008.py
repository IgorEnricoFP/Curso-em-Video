d = float(input("Digite uma distância em metros: "))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print(f"A medida de {d:.1f} corresponde a")
print(f"{km:.3f}km \n{hm:.2f}hm \n{dam:.1f}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm")
