
file1 = "../data/mzdata/result/trecqalist_90.1_1000.test.result"
file2 = "../data/mzdata/result_sydney/trecqalist_90.1_1000.test.result"

goulburn = set()
sydney = set()
for line in open(file1):
    a = line.split()
    goulburn.add(int(a))


#goulburn.add(10000000)

for line in open(file2):
    a = line.strip()
    sydney.add(int(a))

print(len(sydney))
print(len(goulburn))
print(sydney ^ goulburn)
