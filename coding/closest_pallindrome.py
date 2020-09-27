def change_bit(num):
    if len(str(num+1))!=len(str(num)):
        return 1
    elif len(str(num-1))!=len(str(num)) or num==1:
        return -1
    else:
        return 0

def find_min(s,m,m_lo,m_hi):
    print(m,m_lo,m_hi)
    m_diff=abs(int(s)-int(m))
    m_lo_diff=abs(int(s)-int(m_lo))
    m_hi_diff=abs(int(s)-int(m_hi))
    print(m_diff,m_lo_diff,m_hi_diff)
    if (m_diff<= m_hi_diff):
        if (m_lo_diff <= m_diff):
            return m_lo
        else:
            return m
    else:
        if (m_lo_diff<= m_hi_diff):
            return m_lo
        else:
            return m_hi
def nearestpallindrome(s):
    n=len(s)
    if n<2:
        return str(int(s)-1)
    if n%2==0:
        f1=s[:n//2]
        m=f1+f1[::-1]
        lo=str(int(f1)-1)
        m_lo=lo+lo[::-1]
        hi=str(int(f1)+1)
        m_hi=hi+hi[::-1]
    if n%2!=0:
        f1=s[:n//2+1]
        m=f1+f1[::-1][1:]
        lo=str(int(f1)-1)
        m_lo=lo+lo[::-1][1:]
        hi=str(int(f1)+1)
        m_hi=hi+hi[::-1][1:]

    if m==s:
        m='0'
    if change_bit(int(f1))==1:
        m_hi='1'+(n-1)*'0'+'1'
    if change_bit(int(f1))==-1:
        m_lo=(n-1)*'9'

    return (find_min(s,m,m_lo,m_hi))


print(nearestpallindrome(("121")))

# 100--99
# 20002--19991