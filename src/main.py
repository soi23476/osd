import matplotlib.pyplot as plt

# 수정연습(src 수정과제)

# 1. 데이터 불러오기
left_vals = []
right_vals = []

with open('data.txt', 'r') as f:
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 2:
            try:
                left_vals.append(float(parts[0]))
                right_vals.append(float(parts[1]))
            except:
                continue

# 2. 그래프 그리기
plt.figure(figsize=(10,5))
plt.plot(left_vals, label='Left sensor(L)', color='blue')
plt.plot(right_vals, label='Right sensor(R)', color='red')
plt.title('result')
plt.xlabel('number')
plt.ylabel('distances(cm)')
plt.legend()
plt.grid(True)
plt.show()

wear_left = max(left_vals) - min(left_vals)
wear_right = max(right_vals) - min(right_vals)

print(f"left interval: {wear_left:.2f} cm")
print(f"right interval: {wear_right:.2f} cm")
