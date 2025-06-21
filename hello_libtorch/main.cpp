#include <iostream>
#include <torch/torch.h>

int main() {
  // Create a 2x3 tensor with random uniform values.
  torch::Tensor tensor = torch::rand({2, 3});
  std::cout << tensor << std::endl;
  return 0;
}
