+++
title = "Chapter Three"
date = 2024-09-03
+++

## Timer

I want to create timer interrupts. To test that I will write a small program to print a sentence every 5 seconds. 
From the [RISCV ACLINT Specification](https://github.com/riscv/riscv-aclint/blob/main/riscv-aclint.adoc) I know that there is a timer device called MTIMER with one *mtime* register that counts up with fixed frequnecy. Additionally, MTIMER has *mtimecmp* registers (one per HART) to set the timer. The value in *mtime* is always compared to the *mtimecmp* regoster of the HART - if it is the same or greater, a timer interrupt is triggered. For signalling an interrupt, we have the *mip* register.

As for now: the specification says *mtime* and *mtimecmp* have different base addresses and I don't know yet where that is because it depends on the architecture so now I go through the code of virt to find it.