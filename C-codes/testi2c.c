#include <stdio.h>
#include <wiringPi.h>
#include <wiringPiI2C.h>
#include <unistd.h>

int main (void)
{
   int fd0,fd1, ctl, val, hByte, lByte;
   const int dac0 = 0x4c; // Could be 0x4d
   const int dac1 = 0x4d; // Could be 0x4d
   const int maxval = 0xffff; // max = 2^16 -1 = 65535
   int chan = 0; // first chan varies from 0 to 3
   int err;
   ctl = 0x10 | ((chan & 3) << 1) ; // control byte, see Bob's python code io_board_subs.py

   fd0 = wiringPiI2CSetup (dac0) ;
   printf("fd0 = %04x\n",fd0);
   fd1 = wiringPiI2CSetup (dac1) ;
   printf("fd1 = %04x\n",fd1);
      err = wiringPiI2CWrite (fd0, dac0) ; // Device address
      usleep(10);
      printf("err1: %04x\n",err);
      err = wiringPiI2CWrite (fd0, ctl); // Control Byte
      usleep(10);
      printf("err2: %04x\n",err);
   for (val=0x0000;val<=maxval;val++)  
   {
      hByte = (val>>8) & 0xff; // MS Byte, see Bob's python code io_board_subs.py
      lByte = val & 0xff; // LS Byte, see Bob's python code io_board_subs.py
//        printf("%04x %04x %04x %04x %04x\n",i2cAddress, ctl, val,hByte,lByte);
//      err = wiringPiI2CWrite (fd0, dac0) ; // Device address
//      usleep(10);
//      printf("err1: %04x\n",err);
//      err = wiringPiI2CWrite (fd0, ctl); // Control Byte
//      usleep(10);
//      printf("err2: %04x\n",err);
      err = wiringPiI2CWrite (fd0, hByte); // MS Byte
      usleep(10);
      printf("err3: %04x  hByte: %02x\n",err,hByte);
      err = wiringPiI2CWrite (fd0, lByte); // LS Byte
      usleep(10);
      printf("err4: %04x  lByte: %02x\n",err,lByte);
      usleep(200000);
      
   }
}
