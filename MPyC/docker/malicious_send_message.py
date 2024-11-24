from mpyc.runtime import mpc
import random


async def main():

    await mpc.start()
    
    a = mpc.input(mpc.SecInt(32)(2))
    print(mpc.pid)
    def _send_message( peer_pid, share):
        if peer_pid == 0:  
            share = b"000000000000000000" 

    print(" a = ", _send_message(peer_pid=0, share=a))
    
    
    await mpc.shutdown()


if __name__ == '__main__':
    mpc.run(main())
