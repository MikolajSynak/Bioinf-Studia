# import torch library
import torch

# create tensors with requires_grad = true
x = torch.tensor(3.0, requires_grad = True)
y = torch.tensor(4.0, requires_grad = True)

# print the tensors
print("x:", x)
print("y:", y)

# define a function z of above created tensors
z = x**x
print("z:", z)

# call backward function for z to compute the gradients
z.backward()

# Access and print the gradients w.r.t x, and y
dx = x.grad
dy = y.grad
print("x.grad :", dx)
print("y.grad :", dy)
