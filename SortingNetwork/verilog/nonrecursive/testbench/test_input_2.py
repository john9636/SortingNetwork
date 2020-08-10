#!/usr/bin/env python

"""
Module Name: input_2.v
Created date: 08/10/2020
Last Modified: 08/10/2020
Description: 2 input comparing/sorting testbench
Author: John Zhang
Company: Shanghai Jiao Tong University

"""

from myhdl import *
import os

module = 'input_2'
testbench = 'test_%s' % module

srcs = []
srcs.append('../rtl/%s.v' % module)
srcs.append('%s.v' % testbench)

src = ' '.join(srcs) # ???
print(src)

build_cmd = 'iverilog -o %s.vvp %s' % (testbench, src)

def bench():

    # Parameters
    DATA_WIDTH = 8
    LABEL_WIDTH = 1
    SIGNED = 1
    ASCENDING = 1

    # Inputs
    clk = Signal(bool(0))
    rst = Signal(bool(0))
    x_valid = Signal(bool(0))
    x_0 = Signal(intbv(0)[DATA_WIDTH:])
    x_1 = Signal(intbv(0)[DATA_WIDTH:])
    x_label_0 = Signal(intbv(0)[LABEL_WIDTH:])
    x_label_1 = Signal(intbv(1)[LABEL_WIDTH:])

    # Outputs
    y_0 = Signal(intbv(0)[DATA_WIDTH:])
    y_1 = Signal(intbv(0)[DATA_WIDTH:])
    y_label_0 = Signal(intbv(0)[LABEL_WIDTH:])
    y_label_1 = Signal(intbv(1)[LABEL_WIDTH:])
    y_valid = Signal(bool(0))

    # DUT
    if os.system(build_cmd):
        raise Exception("Error running build command!")

    dut = Cosimulation(
        "vvp -m ../myhdl %s.vvp -lxt2" % testbench,
        clk = clk,
        rst = rst, 
        x_valid = x_valid,
        x_0 = x_0,
        x_1 = x_1,
        x_label_0 = x_label_0,
        x_label_1 = x_label_1,
        y_0 = y_0,
        y_1 = y_1,
        y_label_0 = y_label_0,
        y_label_1 = y_label_1,
        y_valid = y_valid
        )

    @always(delay(2))
    def clkgen():
        clk.next = not clk
    
    @always(clk.posedge)
    def set_input():
        if (rst == 0 and x_0 < 255):
            x_0.next = x_0 + 1
            x_valid.next = 1
        else:
            x_valid.next = 0

    @instance
    def rstctrl():  
        rst.next = 1
        yield delay(100)
        yield clk.posedge
        rst.next = 0
        yield clk.posedge
        yield delay(1024)
    
        raise StopSimulation

    return instances()

def test_bench():
    sim = Simulation(bench())
    sim.run()

if __name__ == '__main__':
    print("Running test...")
    test_bench()


