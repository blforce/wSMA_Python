#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>

int writeDac(int fd, int dac, int chan, int val) {

int ctl, hByte, lByte ;

/* See Bob's Python code */
      ctl = 0x10 | ((chan & 3) << 1) ; 
      hByte = (val>>8) & 0xff; 
      lByte = val & 0xff; 

      //printf("%d \n",fd);
      wiringPiI2CWrite (fd, dac) ; // Device address
      wiringPiI2CWrite (fd, ctl); // Control Byte
      wiringPiI2CWrite (fd, hByte); // MS Byte
      wiringPiI2CWrite (fd, lByte); // LS Byte

}

int main (void) {

int val, fd0, fd1;
const int dac0 = 0x4c; 
const int dac1 = 0x4d; 
const int maxval = 0xffff; // max = 2^16 -1 = 65535
int chan = 0; // first chan varies from 0 to 3


fd0 = wiringPiI2CSetup (dac0) ;
fd1 = wiringPiI2CSetup (dac1) ;
writeDac(fd0, dac0, 2, 32767);
writeDac(fd1, dac1, 2, 32767);


for (val=0x0000;val<=0xffff;val++) {

writeDac(fd0, dac0, 0, val);
writeDac(fd0, dac0, 1, val);
writeDac(fd0, dac0, 3, val);
writeDac(fd1, dac1, 0, val);
writeDac(fd1, dac1, 1, val);
writeDac(fd1, dac1, 3, val);
//sleep(0.2);



}

}
