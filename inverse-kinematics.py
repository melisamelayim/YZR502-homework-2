import numpy as np
import math

def calculate_ik(x, y, z, phi_deg=0):
    # Kol uzunlukları
    L1 = 0.5
    L2 = 0.4
    L3 = 0.3
    
    # 1. Tuzağı Kontrol Et
    if z != 0:
        print(f"HATA: Hedef Z={z}. RRR Planar robot sadece Z=0 düzleminde çalışabilir. Fiziksel olarak çözüm yoktur!")
        return None
        
    phi = math.radians(phi_deg)
    
    # 2. Bilek noktasını hesapla (x_w, y_w)
    xw = x - L3 * math.cos(phi)
    yw = y - L3 * math.sin(phi)
    
    # 3. Kosinüs teoremi ile q2 için D değerini bul
    r_sq = xw**2 + yw**2
    D = (r_sq - L1**2 - L2**2) / (2 * L1 * L2)
    
    if D > 1 or D < -1:
        print("HATA: Hedef nokta robotun erişim alanı (workspace) dışındadır!")
        return None
        
    # İki olası çözüm (Dirsek Yukarı ve Dirsek Aşağı)
    q2_up = math.acos(D)
    q2_down = -math.acos(D)
    
    # Dirsek Yukarı için q1 ve q3
    q1_up = math.atan2(yw, xw) - math.atan2(L2 * math.sin(q2_up), L1 + L2 * math.cos(q2_up))
    q3_up = phi - q1_up - q2_up
    
    # Dirsek Aşağı için q1 ve q3
    q1_down = math.atan2(yw, xw) - math.atan2(L2 * math.sin(q2_down), L1 + L2 * math.cos(q2_down))
    q3_down = phi - q1_down - q2_down
    
    # Açıları dereceye çevirerek dön (Okunması kolay olsun diye)
    sol_up = [math.degrees(q1_up), math.degrees(q2_up), math.degrees(q3_up)]
    sol_down = [math.degrees(q1_down), math.degrees(q2_down), math.degrees(q3_down)]
    
    return sol_up, sol_down

# Ödevdeki Hedef Nokta (Hata verecek)
print("--- Ödevdeki Hedef Nokta Testi ---")
calculate_ik(x=0.8, y=0.2, z=0.1)

# Geçerli bir Z=0 noktası ve Yatay yönelim (phi = 0) için test
print("\n--- Geçerli Z=0 Noktası İçin Test (x=0.8, y=0.2, z=0) ---")
solutions = calculate_ik(x=0.8, y=0.2, z=0.0, phi_deg=0)

if solutions:
    print(f"1. Çözüm (Dirsek Yukarı): q1={solutions[0][0]:.2f}°, q2={solutions[0][1]:.2f}°, q3={solutions[0][2]:.2f}°")
    print(f"2. Çözüm (Dirsek Aşağı):  q1={solutions[1][0]:.2f}°, q2={solutions[1][1]:.2f}°, q3={solutions[1][2]:.2f}°")