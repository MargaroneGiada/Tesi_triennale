from mpyc.runtime import mpc

async def main():

    await mpc.start()
    
    a = mpc.input(mpc.SecInt(16)(4))
    print("massimo (malicious)= ", await mpc.output(mpc.max(a)))
    print("a (malicious)= ", await mpc.output(a))
    
    await mpc.shutdown()
    

if __name__ == '__main__':
    mpc.run(main())