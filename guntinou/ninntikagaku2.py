#認知科学の課題2
import numpy as np
import matplotlib.pyplot as plt

# 1. データの準備
# 横軸：刺激量
I = np.array([-7, -5, -3, 0, 3, 5, 7])
# 縦軸：評価値（今は仮のデータを入れています）
#S1 = np.array([50, 60, 50, 100, 110, 100, 180])
S1 = np.array([40,50,70,110,130,140,150])

#S2 = np.array([40,70,90,100,100,140,150])
S2 = np.array([30,50,60,100,130,140,150])

# 2. 線形回帰の計算
# 縦軸を対数（log10）に変換してから、1次関数として回帰
log_S1 = np.log10(S1)
log_S2 = np.log10(S2)

# 傾き(slope)と切片(intercept)を算出
slope1, intercept1 = np.polyfit(I, log_S1, 1)
slope2, intercept2 = np.polyfit(I, log_S2, 1)

# 3. 回帰直線用のデータ
# 対数軸上で「直線」として描画するための計算
S_fit_log1 = slope1 * I + intercept1
S_fit_log2 = slope2 * I + intercept2

# 4. グラフ描画
plt.figure(figsize=(8, 6))

# 評価値を〇でプロット
plt.scatter(I, S1, color='black', s=100, facecolors='none',
            edgecolors='black', label='Observed (○)')
plt.scatter(I, S2, color='black', s=100, marker='x', label='Observed (x)')

# 回帰直線の描画（10のべき乗に戻してプロットすると、対数軸上では直線になる）
plt.plot(I, 10**S_fit_log1, color='red', linewidth=2,
         label=f'Linear Regression (Log-Y)\nmusic1 (b) = {slope1:.4f}')
plt.plot(I, 10**S_fit_log2, color='blue', linewidth=2,
         label=f'Linear Regression (Log-Y)\nmusic2 (b) = {slope2:.4f}')

# 縦軸を対数スケールに設定
plt.yscale('log')

# 装飾
plt.title("ME Method: Log-Linear Regression", fontsize=14)
plt.xlabel("Presentation Number (Linear)", fontsize=12)
plt.ylabel("Evaluation Value (Log Scale)", fontsize=12)
plt.grid(True, which="both", ls=":", alpha=0.5)
plt.legend()

plt.show()

print(f"算出された回帰直線の傾き 音楽1 {slope1:.4f}")
print(f"算出された回帰直線の傾き 音楽2 {slope2:.4f}")