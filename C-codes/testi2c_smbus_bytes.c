#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <err.h>
#include <errno.h>

#include <linux/types.h>
#include <linux/i2c-dev.h>

#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


int writeDac(int fd, int dac, int chan, int val) {

int ctl, hByte, lByte ;

/* See Bob's Python code */
      ctl = 0x10 | ((chan & 3) << 1) ; 
      hByte = (val>>8) & 0xff; 
      lByte = val & 0xff; 

      i2c_smbus_write_byte(fd, (__u8)dac);
      i2c_smbus_write_byte(fd, (__u8)ctl);
      i2c_smbus_write_byte(fd, (__u8)hByte);
      i2c_smbus_write_byte(fd, (__u8)lByte);

}


int main (void) {

int val, fd, ii;
const int dac0 = 0x4c; 
const int dac1 = 0x4d; 
const int maxval = 0xffff; // max = 2^16 -1 = 65535
int chan = 0; // first chan varies from 0 to 3

fd = open( "/dev/i2c-1", O_RDWR );

ioctl( fd, I2C_SLAVE, dac0 );
writeDac(fd, dac0, 2, 32767);
ioctl( fd, I2C_SLAVE, dac1 );
writeDac(fd, dac1, 2, 32767);


//while(1) {
for (ii=0x0000;ii<=0xffff;ii++) {

val = ii;
ioctl( fd, I2C_SLAVE, dac0 );
writeDac(fd, dac0, 0, val);
writeDac(fd, dac0, 1, val);
writeDac(fd, dac0, 3, val);
ioctl( fd, I2C_SLAVE, dac1 );
writeDac(fd, dac1, 0, val);
writeDac(fd, dac1, 1, val);
writeDac(fd, dac1, 3, val);



}
//}

}
