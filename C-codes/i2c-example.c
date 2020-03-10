/*
 * Simple I2C example
 *
 * Copyright 2017 Joel Stanley <joel@jms.id.au>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 */

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



int main(int argc, char **argv)
{
	uint8_t data, addr = 0x4c, reg = 0x98;
	const char *path = argv[1];
	int file, rc;

	if (argc == 1)
		errx(-1, "path [i2c address] [register]");

	if (argc > 2)
		addr = strtoul(argv[2], NULL, 0);
	if (argc > 3)
		reg = strtoul(argv[3], NULL, 0);

	file = open(path, O_RDWR);
	if (file < 0)
		err(errno, "Tried to open '%s'", path); 

	rc = ioctl(file, I2C_SLAVE, addr);
	if (rc < 0)
		err(errno, "Tried to set device address '0x%02x'", addr);

	data = i2c_smbus_read_byte_data(file, reg);

	printf("%s: device 0x%02x at address 0x%02x: 0x%02x\n",
			path, addr, reg, data);

}

