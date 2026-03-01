import numpy as np
import matplotlib.pyplot as plt

def plot_workspace():
    # uzunluklar
    L1 = 0.6
    L2 = 0.5
    L3 = 0.2

    # mafsal limitleri
    q1_min, q1_max = -np.pi, np.pi
    q2_min, q2_max = -np.pi, np.pi
    q3_min, q3_max = -np.pi, np.pi

    # aci kombinasyonlari olusturma
    q1_vals = np.linspace(q1_min, q1_max, 50)
    q2_vals = np.linspace(q2_min, q2_max, 50)
    q3_vals = np.linspace(q3_min, q3_max, 50)

    # Meshgrid ile olusturulan matrisler
    Q1, Q2, Q3 = np.meshgrid(q1_vals, q2_vals, q3_vals)

    # forward kinematic denklemleri    
    Q12 = Q1 + Q2
    Q123 = Q1 + Q2 + Q3

    PX = L1 * np.cos(Q1) + L2 * np.cos(Q12) + L3 * np.cos(Q123)
    PY = L1 * np.sin(Q1) + L2 * np.sin(Q12) + L3 * np.sin(Q123)

    # matplotlib gorsellestirmesi
    plt.figure(figsize=(8, 8))
    
    # noktalar
    plt.scatter(PX.flatten(), PY.flatten(), s=1, c='blue', alpha=0.05)
    
    # orijin
    plt.plot(0, 0, 'ro', markersize=8, label='Robot Tabanı (Orijin)')

    # grafik ayarlari
    plt.title('3-DOF RRR Planar Robot Kolu Çalışma Alanı (Workspace)', fontsize=14)
    plt.xlabel('X Pozisyonu (m)', fontsize=12)
    plt.ylabel('Y Pozisyonu (m)', fontsize=12)
    
    # eksen esitligi
    plt.axis('equal') 
    
    # eksen limitleri
    plt.xlim([-1.3, 1.3])
    plt.ylim([-1.3, 1.3])
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

plot_workspace()