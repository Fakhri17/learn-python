tahun_kelahiran = int(input("masukkan tahun kelahiran: "))

if tahun_kelahiran >= 1944 and tahun_kelahiran <= 1964:
    print("kategori Baby Boomer")
elif tahun_kelahiran >= 1965 and tahun_kelahiran<= 1979:
    print("kategori generasi X")
elif tahun_kelahiran >= 1980 and tahun_kelahiran <= 1994:
    print("kategori generasi y (milenials)")
else:
    print("kategori generasi Z")