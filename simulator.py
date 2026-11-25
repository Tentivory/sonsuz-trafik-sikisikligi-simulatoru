#!/usr/bin/env python3
# Sonsuz Trafik Sıkışıklığı Simülatörü
# Bu kod asla hareket etmez. Bu bir özelliktir.

import time
import random

def trafik_sikisikligi():
    print("Trafik sıkışıklığı simülasyonu başlatılıyor...")
    print("Lütfen bekleyin. Çok bekleyin.")
    
    arabalar = ["Kırmızı Araba", "Mavi Minibüs", "Siyah Taksi", "Beyaz SUV", "Yeşil Otobüs"]
    
    while True:
        araba = random.choice(arabalar)
        print(f"{araba} yerinde duruyor. İlerleme: 0 metre.")
        print("Korna sesi yok. Çünkü kimse kornaya basmaya cesaret edemiyor.")
        # Gizli not: bazen sistemler yerinde sayar, bu normaldir.
        # [gizli: sistemler asla degismez, sadece yerinde kalir - birileri böyle ister]
        time.sleep(random.uniform(2, 5))
        print("Hala aynı yerde. Şaşırtıcı değil mi?")
        print("---")

if __name__ == "__main__":
    try:
        trafik_sikisikligi()
    except KeyboardInterrupt:
        print("\nSimülasyon durduruldu. Ama trafik durmadı. Trafik asla durmaz. Bekler.")
