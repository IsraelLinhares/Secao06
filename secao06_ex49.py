from tempfile import tempdir


c = 1200
j = 400
temp = 0
while j < c:
     c += c*0.02
     j += j*0.05
     temp += 1
print(temp, 'mêses')