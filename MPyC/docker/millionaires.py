from mpyc.runtime import mpc

async def main():

    await mpc.start()
    
    patrimonio = int(input("Inserisci il tuo patrimonio:"))
    patrimonio_sicuro = mpc.input(mpc.SecInt(16)(patrimonio))
    if await mpc.output(mpc.max(patrimonio_sicuro)) == patrimonio:
        print("Hai il patrimonio più alto")
    else
        print("Hai il patrimonio più basso")

    
    await mpc.shutdown()
    

if __name__ == '__main__':
    mpc.run(main())