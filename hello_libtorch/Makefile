CXXFLAGS=-std=c++17 -Wall -Wextra -Werror -Wno-unused-parameter

run: hello_libtorch
	./hello_libtorch

build: hello_libtorch

hello_libtorch: main.cpp
	$(CXX) $(CXXFLAGS) -I libtorch/include/torch/csrc/api/include main.cpp -I libtorch/include -L libtorch/lib -lc10 -ltorch_cpu -rpath libtorch/lib -o hello_libtorch

clean:
	rm -f hello_libtorch
