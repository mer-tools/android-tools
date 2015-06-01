# Makefile for fastboot; from https://heiher.info/2227.html

SRCS+= bootimg.c
SRCS+= engine.c
SRCS+= fastboot.c
SRCS+= protocol.c
SRCS+= usb_linux.c
SRCS+= util_linux.c
SRCS+=util.c
SRCS+=fs.c

VPATH+= ../libzipfile
SRCS+= centraldir.c
SRCS+= zipfile.c

VPATH+= ../libsparse
SRCS+= backed_block.c
SRCS+= sparse_crc32.c
SRCS+= sparse.c
SRCS+= sparse_read.c
SRCS+= sparse_err.c
SRCS+= output_file.c

VPATH+= ../../extras/ext4_utils/
SRCS+= make_ext4fs.c
SRCS+= crc16.c
SRCS+= ext4_utils.c
SRCS+= ext4_sb.c
SRCS+= indirect.c
SRCS+= allocate.c
SRCS+= contents.c
SRCS+= uuid.c
SRCS+= extent.c
SRCS+= wipe.c
SRCS+= sha1.c

CPPFLAGS+= -I.
CPPFLAGS+= -I../include
CPPFLAGS+= -I../mkbootimg
CPPFLAGS+= -I../../extras/ext4_utils/
CPPFLAGS+= -I../../extras/f2fs_utils/
CPPFLAGS+= -I../libsparse/include/
CPPFLAGS+= -DHAVE_OFF64_T=1
CPPFLAGS+= -std=gnu99

LIBS+= -lz -lselinux

OBJS= $(SRCS:.c=.o)

all: fastboot

fastboot: $(OBJS)
	$(CC) -o $@ $(LDFLAGS) $(OBJS) $(LIBS)

clean:
	rm -rf $(OBJS) fastboot
