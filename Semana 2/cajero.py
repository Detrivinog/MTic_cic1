retiro = int(input())

b100 = retiro // 100000
b50 = (retiro - b100*100000) // 50000
b20 = (retiro - b100*100000 - b50*50000) // 20000
b10 = (retiro - b100*100000 - b50*50000 - b20*20000) // 10000

print(str(b100) + " x $100000")
print(str(b50) + " x $50000")
print(str(b20) + " x $20000")
print(str(b10) + " x $10000")