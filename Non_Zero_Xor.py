for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    xor1 = 0
    st = []
    st.append(0)
    for i in range(n):
        xor1 ^= a[i]
        if xor1 in st:
            st.clear()
            cnt += 1
            st.append(0)
            xor1 = 0
        st.append(xor1)
    print(cnt)
