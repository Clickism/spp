# SPP
**This is a tiny tool made for assemblers that don't support .equ directives.**

I found it a bit annoying that we cannot use constants (.equ directives) to make our assembly more readable/debuggable. 
So I created a python script and a preprocessor called **spp** (s++) that allows .equ directives and compiles into **.s** assembly files.

### Usage

To use this, simply create a **.spp** or **.spp.s** (so that IDEs can recognize the file as assembly) file with .equ directives and run the command
`python3 spp.py yourprogram.spp.s`
which will output a file `yourprogram.s` with all the constants replaced.

Example `.spp`/`.spp.s` file:
```asm
.equ MAGIC_NUMBER = 0x100
.equ TEST = 400
main:
    li t0, MAGIC_NUMBER
    li t1, TEST
    mul t0, t0, t1
```
It will compile into:
```asm
main:
    li t0, 0x100
    li t1, 400
    mul t0, t0, t1
```

### Extra Features
- **Nested constants:** You can use previously defined constants in new ones. For example:
```asm
.equ BASE = 0x100
.equ DATA_NAME = BASE
```
- **Evaluation:** You can evaluate expressions by surrounding them with parentheses. For example:
```asm
.equ RESULT = (0xFF00 + 0x100)
.equ ANOTHER = (RESULT * 2)

.equ BASE_ADDRESS = 0x0000
.equ DATA_AGE = (BASE_ADDRESS + 4)
.equ DATA_COUNT = (BASE_ADDRESS + 8)
```
**__Note:__** Evaluation is only supported for numbers. After evaluation, the result will be converted to **hexadecimal**.

**The software is provided "as is" and there is no guarantee that it will work as intended and any possible problems caused by this is your responsibility. Use at your own risk!**