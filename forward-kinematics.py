import numpy as np

def calculate_fk(q1, q2, q3):
    L1 = 0.5
    L2 = 0.4
    L3 = 0.3
    
    q12 = q1 + q2
    q123 = q1 + q2 + q3
    
    px = L1 * np.cos(q1) + L2 * np.cos(q12) + L3 * np.cos(q123)
    py = L1 * np.sin(q1) + L2 * np.sin(q12) + L3 * np.sin(q123)
    pz = 0.0
    
    R = np.array([
        [np.cos(q123), -np.sin(q123), 0],
        [np.sin(q123),  np.cos(q123), 0],
        [0, 0, 1]
    ])
    
    T = np.eye(4)
    T[0:3, 0:3] = R
    T[0, 3] = px
    T[1, 3] = py
    T[2, 3] = pz
    
    return T, px, py, pz, R

q_test = [0, np.pi/4, np.pi/2]
T_res, px_res, py_res, pz_res, R_res = calculate_fk(q_test[0], q_test[1], q_test[2])

print("Hesaplanan x konumu (px):", round(px_res, 4))
print("Hesaplanan y konumu (py):", round(py_res, 4))
print("Hesaplanan z konumu (pz):", round(pz_res, 4))