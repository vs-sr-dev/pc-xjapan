"""X JAPAN Virtual Shock 001's .DGT pictures to PNG.

    python tools/dgt.py build/extract build/dgt           # every .DGT in a folder
    python tools/dgt.py build/extract/TITLE.DGT out.png

A .DGT is a 6-byte header, "DC" then the width and the height (16-bit,
big-endian), then width x height 16-bit big-endian pixels in the Saturn's
RGB format (bit 15 set: opaque; bits 14-10 blue, 9-5 green, 4-0 red); a
pixel with bit 15 clear is transparent. Checked on all 78 files of the
disc: every size is 6 + 2 x width x height.
"""
import os
import struct
import sys


def decode(data):
    """(width, height, RGBA bytes) of a .DGT."""
    if data[:2] != b"DC":
        raise ValueError("not a .DGT (no 'DC')")
    w, h = struct.unpack(">HH", data[2:6])
    if len(data) != 6 + 2 * w * h:
        raise ValueError("size %d is not 6 + 2 x %d x %d" % (len(data), w, h))
    px = struct.unpack(">%dH" % (w * h), data[6:])
    out = bytearray(4 * w * h)
    for i, p in enumerate(px):
        r, g, b = p & 31, (p >> 5) & 31, (p >> 10) & 31
        out[4 * i:4 * i + 4] = bytes(((r << 3) | (r >> 2), (g << 3) | (g >> 2), (b << 3) | (b >> 2), 255 if p & 0x8000 else 0))
    return w, h, bytes(out)


def to_png(src, dst):
    from PIL import Image
    w, h, rgba = decode(open(src, "rb").read())
    Image.frombytes("RGBA", (w, h), rgba).save(dst)
    return w, h


def main():
    src, dst = sys.argv[1], sys.argv[2]
    if os.path.isdir(src):
        os.makedirs(dst, exist_ok=True)
        for f in sorted(os.listdir(src)):
            if f.upper().endswith(".DGT"):
                w, h = to_png(os.path.join(src, f), os.path.join(dst, f[:-4] + ".png"))
                print("%-14s %3d x %3d" % (f, w, h))
    else:
        print("%d x %d" % to_png(src, dst))


if __name__ == "__main__":
    main()
