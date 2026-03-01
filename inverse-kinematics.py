import numpy as np
import math

def calculate_ik(x, y, z, phi_deg=0):
    L1 = 0.6
    L2 = 0.5
    L3 = 0.2
    
    # tuzak
    if z != 0:
        print(f"Calismaz. hedef Z={z}. RRR Planar robot sadece Z=0 duzleminde calisabilir.")
        return None
        
    phi = math.radians(phi_deg)
    
    # bilek noktasi hesabi
    xw = x - L3 * math.cos(phi)
    yw = y - L3 * math.sin(phi)
    
    # kosinus ile q2 icin D'yi hesapla
    r_sq = xw**2 + yw**2
    D = (r_sq - L1**2 - L2**2) / (2 * L1 * L2)
    
    if D > 1 or D < -1:
        print("Hedef nokta robotun erisim alani (workspace) disindadir!")
        return None
        
    # dirsek yukari ve dirsek asagi
    q2_up = math.acos(D)
    q2_down = -math.acos(D)
    
    # dirsek yukari icin q1 ve q3
    q1_up = math.atan2(yw, xw) - math.atan2(L2 * math.sin(q2_up), L1 + L2 * math.cos(q2_up))
    q3_up = phi - q1_up - q2_up
    
    # dirsek asagi icin q1 ve q3
    q1_down = math.atan2(yw, xw) - math.atan2(L2 * math.sin(q2_down), L1 + L2 * math.cos(q2_down))
    q3_down = phi - q1_down - q2_down
    
    # acilari dereceye cevir
    sol_up = [math.degrees(q1_up), math.degrees(q2_up), math.degrees(q3_up)]
    sol_down = [math.degrees(q1_down), math.degrees(q2_down), math.degrees(q3_down)]
    
    return sol_up, sol_down

print("Odevin hedefi: ")
calculate_ik(x=0.8, y=0.2, z=0.1)

print("\ngeçerli Z=0 noktasi icin test (x=0.8, y=0.2, z=0)")
solutions = calculate_ik(x=0.8, y=0.2, z=0.0, phi_deg=0)

if solutions:
    print(f"1. cozum dirsek yukari: q1={solutions[0][0]:.2f}°, q2={solutions[0][1]:.2f}°, q3={solutions[0][2]:.2f}°")
    print(f"2. cozum dirsek asagi):  q1={solutions[1][0]:.2f}°, q2={solutions[1][1]:.2f}°, q3={solutions[1][2]:.2f}°")