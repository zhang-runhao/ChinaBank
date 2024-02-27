# 以下为第二题解答
s = input("string:")
num = input("num:")
num = int(num)
tong = [0 for i in range(256)] #构建一个数组，记录每个字符在该字符前10个中是否出现过，出现一次就+1
ans = ""
for i in range(len(s)):
    if tong[ord(s[i])] > 0:
        ans += '-'
    else:
        ans += s[i]

    if i > 9:
        tong[ord(s[i])] += 1
        tong[ord(s[i - 10])] -= 1 #将10个以前的记录抹去
    else:
        tong[ord(s[i])] += 1

print(ans)

