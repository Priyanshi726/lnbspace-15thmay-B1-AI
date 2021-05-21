s = input("Enter your string : ")
m = {i:s.count(i) for i in s}
m_length = len(m)
m_value = list(m.values())
m_max = max(m_value)
m_new = [m_max - m_value[i] for i in range(m_length)]


if(m_new.count(0)==m_length or m_new.count(1)==1):
    print("This is My String")

else:
    print("This Is not my string")
