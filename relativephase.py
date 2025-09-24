import numpy as np
import matplotlib.pyplot as plt
import invkinematics

def normalize(x):
    return (x-np.mean(x)) / np.std(x)

def compute_relative_phase(theta1, theta2):
    from scipy.signal import savgol_filter
    # 平滑化（window_lengthとpolyorderはデータに応じて調整）
    theta1_smooth = savgol_filter(theta1, window_length=11, polyorder=3)
    theta2_smooth = savgol_filter(theta2, window_length=11, polyorder=3)

    dtheta1 = np.gradient(theta1_smooth)
    dtheta2 = np.gradient(theta2_smooth)

    theta1_n = normalize(theta1_smooth)
    theta2_n = normalize(theta2_smooth)
    dtheta1_n = normalize(dtheta1)
    dtheta2_n = normalize(dtheta2)

    phi1 = np.arctan2(dtheta1_n, theta1_n)
    phi2 = np.arctan2(dtheta2_n, theta2_n)

    rel_phase = phi1 - phi2
    return rel_phase

def get_rellist(l):
    shoulder = []
    elbow = []
    
    for i in range(len(l)):
        t1,t2,_,_ = invkinematics.calc_theta(l[i])
        shoulder.append(t1)
        elbow.append(t2)
    
    rel_phase = compute_relative_phase(shoulder,elbow)
    return rel_phase

   
if __name__ == "__main__":
    l = np.load("good.npy")
    rel_phase = get_rellist(l)
    print(l.shape)

    plt.plot(range(len(l)), rel_phase)
    plt.xlabel("time")
    plt.ylabel("relative phase (radian)")
    plt.grid()
    plt.show()

    l2 = np.load("bad2.npy")
    rel_phase2 = get_rellist(l2)

    fig = plt.figure()
    fig.suptitle("relative phase")

    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)

    ax1.plot(range(len(l)), rel_phase)
    ax2.plot(range(len(l2)), rel_phase2)

    plt.show()


