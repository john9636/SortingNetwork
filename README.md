# FPGA Sorting Network
Implement a bitonic sorting network on FPGA
## Motivation
Sometimes, it's necessary to implement a sorting module on FPGA. And those sorting algorithms which work well on CPU are not that suitable for FPGA. A usual method to sort a fixed amount of inputs is to use a sorting network. So, here, I implement a bitonic sorting network with verilog. 
## Bitonic sorting network
Just as its name implies, bitonic sorting network is a sorting network which could sort two groups of sorted data. And the two groups of sorted data, or inputs, should have opposite ascending features. To be more specific, please check out the introduction on [wiki](https://en.wikipedia.org/wiki/Bitonic_sorter).

Briefly, the structure is as the figure below. It's from [wiki](https://en.wikipedia.org/wiki/Bitonic_sorter) as well.


![Test Image 3](https://github.com/john9636/SortingNetwork/blob/master/SortingNetwork/bitonic_sorting.png)





