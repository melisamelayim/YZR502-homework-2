## 1. Robot Seçimi

Projede RRR Planar Kol seçilmiştir.

* Bağlantı Uzunlukları: L1 = 0.6 m, L2 = 0.5 m, L3 = 0.2 m
* Mafsal Limitleri: Hepsi için [-pi, pi]

## 2. Çalıştırma Talimatları

Sırasıyla:

1. Aşagıdaki kütüphaneleri kurun
pip install numpy matplotlib

2. İleri Kinematik analizi için
python forward-kinematics.py

3. Ters Kinematik analizi için:
python inverse-kinematics.py

4. Çalışma Alanı görselleştirmesi için:
python workspace.py

## 3. Kullanılan Kaynaklar

* Craig, J. J. (2005). Introduction to Robotics: Mechanics and Control (3rd ed.). Pearson Prentice Hall.
* Siciliano, B. et al. (2009). Robotics: Modelling, Planning and Control. Springer.
* Spong, M. W., Hutchinson, S., & Vidyasagar, M. (2006). Robot Modeling and Control. John Wiley and Sons.