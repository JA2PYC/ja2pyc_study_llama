import numpy as np

data = np.array(
    [
        [[10, 12, 14], [16, 18, 20], [22, 24, 26]],
        [[101, 102, 103],[104, 105, 106],[107, 108, 109]],
        [[-5,-3,-1],[1,3,5],[7,9,11]]
    ]
)
print("data.shape : ", data.shape)
print("data.size : ", data.size)

for i in range(3):
    print(f"{i+1} : {data[i]}")

reshaped = data.reshape((3,9))

print("Reshaped")

for i in range (3):
    print(f"Reshaped {i+1} : {reshaped[i]}")