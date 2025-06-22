import torch

device = None
if torch.cuda.is_available():
    print("Using the CUDA backend.")
    device = torch.device("cuda")
elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
    print("Using the Metal backend.")
    device = torch.device("mps")
else:
    print("Using the CPU.")

tensor = torch.rand(2, 3, device=device)

print(tensor)
