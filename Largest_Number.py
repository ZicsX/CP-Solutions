N = input()
K = int(input())
st = []
for d in N:
    while K > 0 and st and st[-1] < d:
        st.pop()
        K -= 1
    st.append(d)

while K > 0 and st:
    st.pop()
    K -= 1

res = ""
while st:
    res = st.pop() + res

print(res)
