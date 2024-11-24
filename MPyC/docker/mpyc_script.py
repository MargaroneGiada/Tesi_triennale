from mpyc.runtime import mpc

async def main():

    await mpc.start()
    
    a = mpc.input(mpc.SecInt(16)(2))
    print("massimo = ", await mpc.output(mpc.max(a)))
    
    await mpc.shutdown()
    

if __name__ == '__main__':
    mpc.run(main())