#!/usr/bin/env python

"""
Module Name: input_4.v
Created date: 08/10/2020
Last Modified: 08/10/2020
Description: 4 input comparing/sorting testbench
Author: John Zhang
Company: Shanghai Jiao Tong University

"""

from myhdl import *
import os

module_1 = 'input_4'
module_2 = 'input_2'
module_3 = 'input_4_bitonic_required'
testbench = 'test_%s' % module_1

srcs = []
srcs.append('../rtl/%s.v' % module_1)
srcs.append('../rtl/%s.v' % module_2)
srcs.append('../rtl/%s.v' % module_3)
srcs.append('%s.v' % testbench)

src = ' '.join(srcs) 

build_cmd = 'iverilog -o %s.vvp %s' % (testbench, src)

def bench():

    # Parameters
    DATA_WIDTH = 8
    LABEL_WIDTH = 2
    SIGNED = 1
    ASCENDING = 0

    # Inputs
    clk = Signal(bool(0))
    rst = Signal(bool(0))
    x_valid = Signal(bool(0))
    x_0 = Signal(intbv(0)[DATA_WIDTH:])
    x_1 = Signal(intbv(0)[DATA_WIDTH:])
    x_2 = Signal(intbv(0)[DATA_WIDTH:])
    x_3 = Signal(intbv(0)[DATA_WIDTH:])
    x_label_0 = Signal(intbv(0)[LABEL_WIDTH:])
    x_label_1 = Signal(intbv(0)[LABEL_WIDTH:])
    x_label_2 = Signal(intbv(0)[LABEL_WIDTH:])
    x_label_3 = Signal(intbv(0)[LABEL_WIDTH:])

    # Outputs
    y_0 = Signal(intbv(0)[DATA_WIDTH:])
    y_1 = Signal(intbv(0)[DATA_WIDTH:])
    y_2 = Signal(intbv(0)[DATA_WIDTH:])
    y_3 = Signal(intbv(0)[DATA_WIDTH:])
    y_label_0 = Signal(intbv(0)[LABEL_WIDTH:])
    y_label_1 = Signal(intbv(1)[LABEL_WIDTH:])
    y_label_2 = Signal(intbv(0)[LABEL_WIDTH:])
    y_label_3 = Signal(intbv(1)[LABEL_WIDTH:])
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
        x_2 = x_2,
        x_3 = x_3,
        x_label_0 = x_label_0,
        x_label_1 = x_label_1,
        x_label_2 = x_label_2,
        x_label_3 = x_label_3,
        y_0 = y_0,
        y_1 = y_1,
        y_2 = y_2,
        y_3 = y_3,
        y_label_0 = y_label_0,
        y_label_1 = y_label_1,
        y_label_2 = y_label_2,
        y_label_3 = y_label_3,
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
            x_1.next = 16
            x_2.next = 32
            x_3.next = 64
            x_label_0.next = 0
            x_label_1.next = 1
            x_label_2.next = 2
            x_label_3.next = 3
        else:
            x_valid.next = 0

    @instance
    def rstctrl():  
        rst.next = 1
        yield delay(100)
        yield clk.posedge
        rst.next = 0
        yield clk.posedge
        yield delay(1050)
    
        raise StopSimulation

    return instances()

def test_bench():
    sim = Simulation(bench())
    sim.run()

if __name__ == '__main__':
    print("Running test...")
    test_bench()


