
# Cross-compilation

## Choosing the target

First, I needed to figure out how I compile code for RISCV. In my original project, I aimed to write code that would work on both the 64 bit and 32 bit RISCV architectures with primary focus on 64 bit. I will probably do my new project similarly, but in the beginning I will just try to get it to run. 

Rust already supports cross-compilation to [multiple RISCV architectures](https://doc.rust-lang.org/beta/rustc/platform-support.html).

 Since my aim is to write an operating system, I don't want to have one already - so I choose <code class="keyword">none</code> as operating system. I don't need any standard library support at the moment becasue I suspect that adhering to any ABI would just make the beginning more complicated (also the only other option is <code class="keyword">musl</code> anyway) - so I use <code class="keyword">elf</code>, which specifies the object file format, but in this case, basically means no ABI. 

 With all this, it seems like I have two options:
 <code class="keyword">riscv64gc-unknown-none-elf</code> and <code class="keyword">riscv64imac-unknown-none-elf</code>. The only difference between the two architectures is that RISCV64GC supports floating point arithmetic and RISCV64IMAC doesn't. I will probably not need floating points for my code but the userspace programs might, so I will support both architectures (I think this should be fairly easy to do).

 By the way, though irrelevant in this case, I found out that <code class="keyword">unknown</code> here represents the chip/OS vendor if relevant (this wasn't so easy to find, big thanks to [mcyoung](https://mcyoung.xyz/2025/04/14/target-triples/)).

## Building the project

Now that I know my compilation target, I need to get rust toolchain to compile the project for this target. For that, I need to install the target first. Installing a new platform to rustc's compilation targets is actually very simple - with the command <code class="keyword">rustup target add TARGET</code>, where I replace <code class="keyword">TARGET</code> with <code class="keyword">riscv64gc-unknown-none-elf</code>. 

The [rustup book](https://rust-lang.github.io/rustup/cross-compilation.html) will tell you that you can compile for RISCV64 by building the project with an extra target flag. This is however too much work for the amount of compilations I want to do. So I will make my job easier. There are two ways I can do that. 

The first option is to write a bash script with a shorter name (even shorter than cargo build) that simply contains the command with the right target flag, as such:

```bash
#! /bin/bash

cargo build --target=riscv64gc-unknown-none-elf
```

 This is practical since I might want to compile my code for RISCV64GC, RISCV64IMAC and some kind of RISCV32 respectively and I could put all necessary commands in the same bash script.

The second option is to change the default target by modifying <code class="keyword">.cargo/config.toml</code> like this:

```rs
[build]
target = "riscv64gc-unknown-none-elf"
```

This looks more elegant in my opinion, but I would still probably need to write a bash script if I want to build for multiple platforms. 
I am not sure which one will be more practical in the future, but I will go with the script for now since I chose a conveniently short name for it.

## Compiling for qemu

I currently use [qemu](https://github.com/qemu), a well-known system emulator, as a hardware alternative. In qemu-RISCV64, the starting code is placed at address 0x80000000. I copied the linker code and Assemnbler entry code I had from my previous project in C (more on thos in the restective chapters) which already manages this part for me. 





