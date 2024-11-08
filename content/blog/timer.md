+++
title = "Timer"
date = 2024-11-03
+++

I want to create timer interrupts. To test that I will write a small program to print a sentence every 5 seconds. 
I wasted a lot of time because I thought I need to look in the [RISCV ACLINT Specification](https://github.com/riscv/riscv-aclint/blob/main/riscv-aclint.adoc), which was an interesting read but made everything more compplicated. For a simple system, the privilidged ISA contains enaough information.

So, what we need to know is that there is a memory-mapped *mtime* register that contains the time and is increments at a constant frequency. 
There is also a memory-mapped *mtimecmp* register, which can hold a value that will be compared with *mtime*. If the value in *mtimecmp* is equal or less than the value in *mtime*, an interrupt will be triggered. This interrupt will be pending until *mtimecmp* is greater than *mtime* again. For this, interrupts need to be enabled.

First I will try to access *mtime* just by it's name, without finding out the address, as that's how I understand the example code in the specification.




