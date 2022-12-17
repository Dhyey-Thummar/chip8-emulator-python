import asyncio
import os
import subprocess
import sys
import random

NREG = 16
NMEM = 4096
USERMEM = 512
SCREEN_X = 64
SCREEN_Y = 32
STACK_SIZE = 16

def drawGraphics(screen):
    for y in range(SCREEN_Y):
        for x in range(SCREEN_X):
            if screen[y][x] == 1:
                sys.stdout.write(chr(0x2588))
            else:
                sys.stdout.write(" ")
        sys.stdout.write("\n")


def clearScreen():
    for y in range(SCREEN_Y):
        sys.stdout.write("\n")


# drawGraphics(test)


def setupGraphics():
    sys.stdout.write("\x1b[2J\x1b[H")

async def mainloop():
    for i in range(50):
        test = [[random.randint(0, 1) for x in range(SCREEN_X)]
            for y in range(SCREEN_Y)]
        drawGraphics(test)
        await asyncio.sleep(0.5)
        
if __name__ == "__main__":
    asyncio.run(mainloop())
