# hello_libtorch

## Dev Set Up

Requirements:

* Linux or macOS.
* A C and C++ compiler.
* Make.
* [LibTorch](https://pytorch.org/get-started/locally/).
  1. Download the LibTorch zip file for your OS.
  1. Uncompress the zip file.
  1. Move the uncompressed directory to the same directory as this README file,
  which is ignored by git.

If running on macOS, the LibTorch dylibs won't be able to be loaded by default
due to sandboxing issues. Fix with the following commands:

```
$ sudo xattr -d com.apple.quarantine libtorch/lib/libc10.dylib
$ sudo xattr -d com.apple.quarantine libtorch/lib/libtorch_cpu.dylib
$ sudo xattr -d com.apple.quarantine libtorch/lib/libomp.dylib
```

If running on macOS, the `torch_cpu.dylib` wrongly hardcodes the runtime path of
`libomp.dylib` and thus crashes the executable when running it. Fix with the
following command:

```
$ install_name_tool -change /opt/homebrew/opt/libomp/lib/libomp.dylib @rpath/libomp.dylib libtorch/lib/libtorch_cpu.dylib
```

## Building and Running

To build and run:

```
$ make
```

To build only:

```
$ make build
```

To clean build artifacts:

```
$ make clean
```
