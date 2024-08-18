<link rel="stylesheet" href="blog.css" />
<link rel="stylesheet" media="screen" href="https://fontlibrary.org//face/neomatrixcode" type="text/css"/> 

# OS Blog

I set out to write a simple operating system for RISCV just for fun. This blog describes all the steps (and missteps) I took

## How I got started

Since I only came up with the idea of this blog after I already did some things - mainly to motivate myself - I will try to remember and summarize what I did.

### Linker Script

This was the first and unfortunately most fucked up part of the whole thing so far. Here is the code I have so far in teh *script.ld* file:

```{.c}
ENTRY(asm_entry)
OUTPUT_ARCH(riscv)

MEMORY {

    RAM (rwx) : org = 0x80000000, len = 1M
}

PHDRS {
  text PT_LOAD;
}

SECTIONS {
 .text : {
    . = ALIGN(8);
    PROVIDE(startkernel = .);
    *(.text)
    *(.text*)
    PROVIDE(endkernel = .);
 } > RAM : text
}
```

#### Now the explanation:
The first line tells the linker that the code starts at the label *asm_entry (found in entry.S)*
The second line the architecture to RISCV.

In the **MEMORY** section, I define all addressess above 0x80000000 as RAM. This is the address from which the RISCV architecture allows the OS and user space programs to use memory - everything smaller than this address is mapped to some device. My RAM is readable, writable and executable (rwx) however at this point I know I will probably need to define a new memory section that is not writable for the kernel, because kernel code shouldn't reside in writable memory.

**PHDRS** defines ELF program headers *(see also [here](https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_node/ld_23.html)*. I only have one memory segment so far, *.text*. *PT_LOAD* means, that this segment has to be loaded from a file.

The **SECTIONS** part describes all the segments our memory will have. Again, at this point I only have some kernel code so I only have the *.text* segment, where the kernel code is.  The address of the beginning of this segment is saved into the variable *startkernel*, the address of the end is saved into the variable *endkernel*. These variables will be used in the C-code later. The segment is aligned by 8 Bytes because I write this OS for RISCV64. *.text* will be placed in the RAM memory section.
