# README

The `dgx-utils` package contains various functions for use on the DGX computing cluster at ORNL. Version 0.1 contains two functions: `GetLowestGPU()` and `GetFileNames`

* **`GetLowestGPU()`:** This function returns the GPU with the lowest memory use on the cluster. Returns a device string (e.g. 'cuda:0' or 'cpu' if no cuda devices).

* **`GetFileNames`:** This function returns a list of file names with a given extension from the specified directory.