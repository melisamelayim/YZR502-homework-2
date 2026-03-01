import numpy as np
import matplotlib.pyplot as plt

def plot_workspace():
    # 1. Kol Uzunlukları
    L1 = 0.5
    L2 = 0.4
    L3 = 0.3

    # 2. Mafsal Limitleri (Radyan cinsinden)
    # Ödevde istendiği gibi limitleri burada belirliyoruz. 
    # Şu an hepsi tam tur (-pi ile +pi arası) dönebiliyor.
    q1_min, q1_max = -np.pi, np.pi
    q2_min, q2_max = -np.pi, np.pi
    q3_min, q3_max = -np.pi, np.pi

    # 3. Açı Kombinasyonları Oluşturma (Çözünürlük: her mafsal için 50 adım)
    # 50 * 50 * 50 = 125.000 farklı nokta hesaplanacak
    q1_vals = np.linspace(q1_min, q1_max, 50)
    q2_vals = np.linspace(q2_min, q2_max, 50)
    q3_vals = np.linspace(q3_min, q3_max, 50)

    # Meshgrid ile matrisleri oluştur (Hızlı hesaplama için vektörizasyon)
    Q1, Q2, Q3 = np.meshgrid(q1_vals, q2_vals, q3_vals)

    # 4. İleri Kinematik (FK) Denklemleri ile Pozisyon Hesaplama
    # Tüm 125.000 kombinasyon aynı anda hesaplanır
    Q12 = Q1 + Q2
    Q123 = Q1 + Q2 + Q3

    PX = L1 * np.cos(Q1) + L2 * np.cos(Q12) + L3 * np.cos(Q123)
    PY = L1 * np.sin(Q1) + L2 * np.sin(Q12) + L3 * np.sin(Q123)

    # 5. Görselleştirme (Matplotlib)
    plt.figure(figsize=(8, 8))
    
    # Noktaları çizdir (alpha değeri ile üst üste binen noktaların yoğunluğunu gösteriyoruz)
    plt.scatter(PX.flatten(), PY.flatten(), s=1, c='blue', alpha=0.05)
    
    # Orijini (Robotun tabanını) işaretle
    plt.plot(0, 0, 'ro', markersize=8, label='Robot Tabanı (Orijin)')

    # Grafik Ayarları (Akademik formata uygun)
    plt.title('3-DOF RRR Planar Robot Kolu Çalışma Alanı (Workspace)', fontsize=14)
    plt.xlabel('X Pozisyonu (m)', fontsize=12)
    plt.ylabel('Y Pozisyonu (m)', fontsize=12)
    
    # Eksenlerin oranını eşitle (Dairelerin elips gibi görünmesini engeller)
    plt.axis('equal') 
    
    # Maksimum erişim mesafesini eksen limitleri yap (L1+L2+L3 = 1.2m)
    plt.xlim([-1.3, 1.3])
    plt.ylim([-1.3, 1.3])
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

# Fonksiyonu çalıştır
plot_workspace()