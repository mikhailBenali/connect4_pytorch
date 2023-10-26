import torch
import numpy as np

data = np.array([[1, 2, 3],[4, 5, 6]])
x_data = torch.tensor(data)

np_array = np.array(data)
x_np = torch.from_numpy(np_array)

x_ones = torch.ones_like(x_data)
x_rand = torch.rand_like(x_data, dtype=torch.float)

rand_tensor = torch.rand(3,4)
ones_tensor = torch.ones(3,4)
zeros_tensor = torch.zeros(3,4)

print(f"Random Tensor shape: {rand_tensor.shape} \n")
print(f"Random Tensor datatype : {rand_tensor.dtype} \n")
print(f"Zeros Tensor device: {zeros_tensor.device} \n")

#Standard numpy-like indexing and slicing

tensor = torch.ones(4, 4)

print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:, 0]}")
print(f"Last column: {tensor[..., -1]}")
tensor[:,1] = 0

print(tensor)