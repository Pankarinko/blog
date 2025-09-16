# Getting started

I wanted to continue my old RISCV OS - but I didn't have many features implemented anyway and some parts were not working properly because I had no idea what I was doing at the time. I wanted to refactor the little code I had anyway but I am also sick of C. Since I already struggled to keep to my original plan, I thought, why not make it even harder and rewrite it in Rust. Especially since this might be a good opportunity to get familar with unsafe Rust which I haven't used yet. So here it goes...


### Cross-compilation:

I first needed to figure out how I compile code for RISCV. In my original project, I aimed to write code that would work on both the 64 bit and 32 bit RISCV architectures with primary focus on 64 bit. I will probably do my new project similarly, but in the beginning I will just try to get 

