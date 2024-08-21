+++
title = "UART"
date = 2024-08-19
+++

# Chapter Two

## UART


First off, it really wasnt't that easy to find material on UART. I made everything using [this blog](https://www.lammertbies.nl/comm/info/serial-uart). Here I will summerize, which parts of these I needed.

### Why do I use UART?
For programming an operating system, I need to be able to communicate with it. For that, I need some form of output. Without output it is really hard to debug anything, so I dealt with this problem first. UART is a protocol for communication between devices. Since I use QEMU as my RISCV emulator and QEMU already supports UART, I just use UART as well. Besides, UART is less complicated to implement than other communication protocols. 

### What I did
UART operates with the 8 registers, found in this table ([source](https://www.lammertbies.nl/comm/info/serial-uart)):

| Address   | Read     | Write      |
|:----------|:---------|:-----------|
| base | RBR receiver buffer | THR transmitter holding |
| base+1 | IER interrupt enable | IER interrupt enable |
| base+2 | IIR interrupt identification | FCR FIFO control |
| base+3 | LCR line control | LCR line control |
| base+4 | MCR modem control| MCR modem control |
| base+5 | LSR line status | - |
| base+6 | MSR modem status | - |
| base+7 | SCR scratch | SCR scratch |

To access the registers, I need to know the base address of the UART-area in my 
