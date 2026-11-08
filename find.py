import sys, os
sigs = {
    b'ANDROID!': 'Android boot image',
    b'$OS$': 'Intel OSIP header',
    b'HdrS': 'Linux bzImage header',
    b'\x1f\x8b\x08': 'gzip',
    b'\x89LZO': 'lzo',
    b'\xfd7zXZ': 'xz',
}
for f in sys.argv[1:]:
    d = open(f, 'rb').read()
    nz = sum(1 for b in d if b != 0)
    print(f"== {f}: размер {len(d)} байт, ненулевых байт {nz}")
    print("первые 64 байта:", d[:64].hex())
    for s, name in sigs.items():
        i = -1
        n = 0
        while True:
            i = d.find(s, i + 1)
            if i < 0 or n >= 5:
                break
            print(f"  {name} ({s!r}) по смещению {i}")
            n += 1
