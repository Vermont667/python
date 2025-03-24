st = 'I am learning Python. hello WORLD!'
print(st)
# print(st.find('h'))
# print(st.rfind('h'))
t = st[17:22]
ts = t[::-1]
st = 'I am learning Python. hello WORLD!'.split('h')
print(f'{st[0]}', ts, f'{st[2]}', sep='')
