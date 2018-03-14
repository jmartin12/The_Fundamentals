'''
Jacob Martin
3/11/2018


Context switching - Switching the CPU from the one process to the context of another. This can only be ran in kernal mode. Kernal mode is a
mode of the CPU in which only the kernal runs and has access to all memory locations and all system resources.

The context is the contents of a CPU's registers and program counters at a point in time. 

A Regiser is a small amount of very fast memory in the CPU that is used to speed the execution time of programs by providing quick access to 
commonly used values. 

The program counter is a special regester that indicats the position of the CPU in its instruction sequence (fetch, decode, execute) and the address
of the current or next instruction to be executed.

Context switching is an essential feature of multitasking OS's. Since context siwtching happens in rapid succession, very fast, without interfering
with processes, the illusion of concurrency is achieved. However, context switching is generally computationally intensive. It can often be
the most costly operation on an OS. For that reason, many modern OS try to avoid context switching. UNIX systems tend to do a good job at this.


'''