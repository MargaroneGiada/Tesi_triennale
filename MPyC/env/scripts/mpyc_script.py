
from mpyc.runtime import mpc
import random


async def main():

    await mpc.start()
    i = random.randint(0, 100)
    
    a = mpc.input(mpc.SecInt(16)(i))
    print("sum a = ", await mpc.output(mpc.sum(a)))
    b = mpc.input(mpc.SecInt(16)(10))
    
    print("sum b = ", await mpc.output(mpc.sum(b)))
    print("b = ", await mpc.output(b))
    print("a = ", await mpc.output(a))
    await mpc.shutdown()
    

if __name__ == '__main__':
    mpc.run(main())