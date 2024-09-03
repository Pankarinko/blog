+++
title = "Chapter Two"
date = 2024-08-19
+++

## UART


First off, it really wasnt't that easy to find material on UART. I made everything using [this blog](https://www.lammertbies.nl/comm/info/serial-uart) and [this data sheet](http://byterunner.com/16550.html). Here I will summerize, which parts of these I needed.

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


To access the registers, I need to know the base address of the UART-area in my emulator. Forthe virt machine in QEMU it is address 0x10000000 as seen in the [official virt memory layout](https://github.com/qemu/qemu/blob/master/hw/riscv/virt.c). The memory layout is actuallay very important for me in general so I will paste it here:

```c

static const MemMapEntry virt_memmap[] = {
    [VIRT_DEBUG] =        {        0x0,         0x100 },
    [VIRT_MROM] =         {     0x1000,        0xf000 },
    [VIRT_TEST] =         {   0x100000,        0x1000 },
    [VIRT_RTC] =          {   0x101000,        0x1000 },
    [VIRT_CLINT] =        {  0x2000000,       0x10000 },
    [VIRT_ACLINT_SSWI] =  {  0x2F00000,        0x4000 },
    [VIRT_PCIE_PIO] =     {  0x3000000,       0x10000 },
    [VIRT_PLATFORM_BUS] = {  0x4000000,     0x2000000 },
    [VIRT_PLIC] =         {  0xc000000, VIRT_PLIC_SIZE(VIRT_CPUS_MAX * 2) },
    [VIRT_APLIC_M] =      {  0xc000000, APLIC_SIZE(VIRT_CPUS_MAX) },
    [VIRT_APLIC_S] =      {  0xd000000, APLIC_SIZE(VIRT_CPUS_MAX) },
    [VIRT_UART0] =        { 0x10000000,         0x100 },
    [VIRT_VIRTIO] =       { 0x10001000,        0x1000 },
    [VIRT_FW_CFG] =       { 0x10100000,          0x18 },
    [VIRT_FLASH] =        { 0x20000000,     0x4000000 },
    [VIRT_IMSIC_M] =      { 0x24000000, VIRT_IMSIC_MAX_SIZE },
    [VIRT_IMSIC_S] =      { 0x28000000, VIRT_IMSIC_MAX_SIZE },
    [VIRT_PCIE_ECAM] =    { 0x30000000,    0x10000000 },
    [VIRT_PCIE_MMIO] =    { 0x40000000,    0x40000000 },
    [VIRT_DRAM] =         { 0x80000000,           0x0 },
}
```

In the beginning I defined a bunch of macros for the addresses of the necessary UART registers to access them more easily. I need the registers *LCR, FCR, THR* and *LSR*.

I also saved the following values in macros:
```c
#define UART_LCR_8BIT 3
#define UART_FCR_FIFO_ENABLE 2
#define UART_FCR_14B 0xC0
#define UART_LSR_THR_EMPTY 32
```

After that I initialize the UART.\
\
For the initialization I need the *LCR* and *FCR* registers.\
Let's start with the *LCR*. This register is used solely for initialization. It can be set to transferring, 5,6,7 or 8 Bits at once. I thought setting it to the highest possible data rate -which is conviniently also the size of a byte- would be the best (or at least I think that was my thought process, I'm not sure, it was a while ago.) I also follow the recommendation from the website to use one stop bit and no parity bit. That means the value of LCR is set to 0x03.\
Now for the FCR: this controls the FIFO settings. I combined the two FCR macros from above for this one.

Outputting a single character is pretty straight-forward: I write the character into the *THR*.

Okay so now I can basically output anything. For printing a word, I just iterate thorugh all characters of the word and output the characters separately. This is the code snippet:
```c
void prints(char* word) {
  int char_count;
  while (*word != '\0') {
    char_count = 0;
    if (LSR != UART_LSR_THR_EMPTY) {
        while (char_count < 14) {
          output_UART((uint8) *word);
          word++;
          if (*word == '\0') return;
            }
        }
    }
}
```
That's it so far. As you might have noticed, I don't handle user input yet. I will deal with it when I need it.


