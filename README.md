# SPP
**This is a tiny tool made for assemblers that don't support .equ directives.**

I found it a bit annoying that we cannot use constants (.equ directives) to make our assembly more readable/debuggable. So I created a python script and a *pseudo*-language called **spp** (s++) that allows .equ directives and compiles into **.s** files.

To use this, simply create a **.spp** file with .equ directives and run the command
`python3 spp.py programs/public/os/yourprogram.spp`
which will output a file `yourprogram.s` with all the constants replaced.

Example .spp file:
```asm
.equ MAGIC_NUMBER = 0x100
.equ TEST = 400
_start:
    li t0, MAGIC_NUMBER
    li t1, TEST
    mul t0, t0, t1
```
It will compile into:
```asm
_start:
    li t0, 0x100
    li t1, 400
    mul t0, t0, t1
```
It might be important to compile and remove the .spp files before submitting.

**The software is provided "as is" and there is no guarantee that it will work as intended and any possible problems caused by this is your responsibility. Use at your own risk!**