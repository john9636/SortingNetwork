# User guide

## Design

The sorting network is implemented in both recursion form and non-recursion form. After synthesis and implementation, they should have the same hardware architecture. 

It is more readable and understandable to implement in non-recursion form. But as the amount of inputs growing, the amount of the codes is too huge. I just implement the 16-input sorting network in non-recursion form.

So, it is necessary to implement it in recursion way if the amount of the inputs is over 32. And you only need 4 verilog files to implement any amount of inputs, as long as you have enough resources in your FPGA.

## Parameters

DATA_WIDTH: Needless to explain.

LABEL_WIDTH: Mostly, we want to get the sorted output with their input index or something. To be flexible, make the index width or label width adjustable.

SIGNED: If the input data are signed, then assign it with 1; if the input data are unsigned, assign it with 0.

ASCENDING: If you want the output data ascending, assign it with 1; otherwise, 0.

LOG_INPUT_NUM: Only available in recursion form. In recursion form, the input is adjustable. So it must be specified that how many inputs are there. If LOG_INPUT_NUM = n, then there're 2^n inputs. If you want to implement some number of inputs, but the number is not a 2^n, the simplest way is to complement 0s to the rest inputs.


## Delay and Resources

It's not hard to figure out that the delay of a k-input bitonic sorting network is __(log⁡K*(log⁡K+1))/2__ cycles. The base of log is 2.

And it needs (log⁡K*(log⁡K+1))/2 * K/2 = __(K*logK*(log⁡K+1))/4__   2-input comparators.

## Tools

To do the simulation as efficiently as possible, I use several tools. They are [Icarus](http://iverilog.icarus.com/), [myHDL](http://www.myhdl.org/) and [gtkwave](http://gtkwave.sourceforge.net/). I use them on a ubuntu 16.04 computer with python 3. Actually they are not necessary. If the goal is just to implement the sorting network on an FPGA with some IDE, like Vivado, just put the rtl codes into the IDE and set the parameters as you want. 

I use myHDL and Icarus in order to write the testbench with python. And then use GTKWave to check the output test waveforms. It's not difficult to use them if you install them properly.

