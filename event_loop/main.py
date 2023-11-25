import time
import Petr_Viktorin_evet_loop as asynco_lib
import random

def print_blinkies(family):
    for blinky in family:
        print(blinky, end=' ')
    print(end='\r')

class Blinky():
    def __init__(self, family) -> None:
        self.face = '(o_o)'
        self.family = family 

    def __str__(self) -> str:
        return self.face
    
    async def show_face(self, new_face, delay):
        self.face = new_face
        print_blinkies(self.family)
        await asynco_lib.sleep(delay)
    async def run(self):
        while True:
            await self.show_face('(-_-)', 0.1)
            await self.show_face('o_o', random.uniform(0.1, 1.5))

family = []
family.extend(Blinky(family) for i in range(3))
async def run_all():
    tasks = []
    for blinky in family:
        tasks.append(asynco_lib.create_task(blinky.run()))
    for task in tasks:
        await task
asynco_lib.run(run_all())