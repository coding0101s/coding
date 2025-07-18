import os
import sys
import random
import time
import getpass

def main() :
    if len(sys.argv) >= 3 and sys.argv[1] == "--console":
        if sys.argv[2] == "DDos":
            if sys.argv[3] == "1":
                binarys_print(1)
            elif sys.argv[3] == "2":
                binarys_print(2)

def binarys_print(sysnum):
    os.system("color 0a")
    print_toggle = 0
    try:
        while True:
            for i in range(1, 18):
                if sysnum == 1:
                    print(f"\t0x{random.randint(0, 255):02X}", end="\t")
                elif sysnum == 2:
                    if print_toggle == 0:
                        print(f"\t0x{random.randint(0, 255):02X}", end="\t")
                        print_toggle = 1
                    elif print_toggle == 1:
                        print(f"0x{random.randint(0, 255):02X}", end="\t")
                        print_toggle = 0

            print("\n")
            
    #         print(" ".join("0x" + str(random.randint(0, 90)) for i in range(1, 109)), end=" ")
    #         time.sleep(0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
    except KeyboardInterrupt:
        while True:
            Y_or_N = input(f"\n\nDo you want to stop DDoS for Target {getpass.getuser()} (Y/N)? ")
            if Y_or_N == "Y":
                os.system("color 07")
                os.system("cls")
                os._exit(0)
                
            elif Y_or_N == "N":
                continue
            else :
                continue
            

if __name__ == "__main__":
    main()