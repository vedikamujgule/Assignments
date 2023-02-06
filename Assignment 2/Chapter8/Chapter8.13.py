def prefix(s1, s2):
    for i in range(len(s1)):
        s = s1[0:len(s1) - i]
        print(s)
        if str(s2).startswith(str(s)):
            return s
    return ""

def main():
    s1, s2 = input("Enter two strings: ").split()
    print(prefix(s1, s2))

main()