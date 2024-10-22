import math

#lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r*r
jari_jari = 7
#menghitung luas
area = luas_lingkaran(jari_jari)
#mencetak hasil dengan format desimal
print(f"Luas Lingkaran dengan jari jari {jari_jari} adalah {area:.2f}")