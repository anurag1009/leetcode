def push(st,n):
    if(len(st)==n):
        print "Stack Overflow"
    else:
        n1=int()
        st.append(n1)

def pop(st):
    if(len(st)==0):
        print "Stack underflow"
    else:
        st.pop()

def isEmpty(st,n):
    if(len(st) == 0):
        return true

def isFull(st,n):
    if(len(st) == n):
        return true

n=int(input("Enter number"))
st=[]
for i in range(0,n):
    st.append(int(input()))
print "MENU"
print "1.PUSH"
print "2.POP"
print "3.ISEMPTY"
print "4.ISFULL"

i

