from mpyc.runtime import mpc

async def main():

    await mpc.start()
    
    a = mpc.input(mpc.SecInt(16)(4))
    print("a = ", await mpc.output(a))
    print("a = ", await mpc.output(a))
    print("sum a = ", await mpc.output(mpc.sum(a)))
    
    await mpc.shutdown()
    

if __name__ == '__main__':
    mpc.run(main())