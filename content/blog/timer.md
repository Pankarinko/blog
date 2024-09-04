+++
title = "Chapter Three"
date = 2024-09-03
+++

## Timer

I want to create timer interrupts. To test that I will write a small program to print a sentence every 5 seconds. 
From the [RISCV ACLINT Specification](https://github.com/riscv/riscv-aclint/blob/main/riscv-aclint.adoc) I know that there is a timer device called MTIMER with one *mtime* register that counts up with fixed frequnecy. Additionally, MTIMER has *mtimecmp* registers (one per HART) to set the timer. The value in *mtime* is always compared to the *mtimecmp* register of the HART - if it is the same or greater, a timer interrupt is triggered. For signalling an interrupt, we have the *mip* register.

The specification says *mtime* and *mtimecmp* have different base addresses and these depend on the architecture. So I looked through the whole [QEMU code](https://github.com/qemu/qemu) to find these addresses.

This is what I found: in `include/hw/intc/riscv_aclint.h`: 
```c
75:    RISCV_ACLINT_DEFAULT_MTIMECMP      = 0x0,
76:    RISCV_ACLINT_DEFAULT_MTIME         = 0x7ff8,
```

which is perfect because it corresponds to the Table 3 and 4 in the RISCV ACLINT Specification. That means that the *mtime* register is mapped to right after the *mtimecmp* registers.