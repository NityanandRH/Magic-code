####################################### Author:Nityanand.R.H ###################################
print('=======================================================================================')
print('Select and remember any character shown below')
print('a b c d e f g h i j k l m n o p q r s t u')
print('=======================================================================================')
s = 'abcdefghijklmnopqrstu'
print('a  h  o\nb  i  p\nc  j  q\nd  k  r\ne  l  s\nf  m  t\ng  n  u')
c1 = 'abcdefg'
c2 = 'hijklmn'
c3 = 'opqrstu'
t = input('Enter the column number as c1 or c2 or c3 that contains the character you selected: ')
if t == 'c1':
    s1 = c2 + c1 + c3
elif t == 'c2':
    s1 = c1 + c2 + c3
else:
    s1 = c1 + c3 + c2
s = s1
print(s)
print('========================================================================================')
print(s[0], s[1], s[2])
print(s[3], s[4], s[5])
print(s[6], s[7], s[8])
print(s[9], s[10], s[11])
print(s[12], s[13], s[14])
print(s[15], s[16], s[17])
print(s[18], s[19], s[20])
c1 = s[0] + s[3] + s[6] + s[9] + s[12] + s[15] + s[18]
c2 = s[1] + s[4] + s[7] + s[10] + s[13] + s[16] + s[19]
c3 = s[2] + s[5] + s[8] + s[11] + s[14] + s[17] + s[20]
t = input('Enter the column number as c1 or c2 or c3 that contains the character you selected: ')
if t == 'c1':
    s1 = c2 + c1 + c3
elif t == 'c2':
    s1 = c1 + c2 + c3
else:
    s1 = c1 + c3 + c2
s = s1
print('========================================================================================')
print('select the row now')
print(s[0], s[1], s[2])
print(s[3], s[4], s[5])
print(s[6], s[7], s[8])
print(s[9], s[10], s[11])
print(s[12], s[13], s[14])
print(s[15], s[16], s[17])
print(s[18], s[19], s[20])
c1 = s[0] + s[3] + s[6] + s[9] + s[12] + s[15] + s[18]
c2 = s[1] + s[4] + s[7] + s[10] + s[13] + s[16] + s[19]
c3 = s[2] + s[5] + s[8] + s[11] + s[14] + s[17] + s[20]
t = input('Enter the column number as c1 or c2 or c3 that contains the character you selected: ')
if t == 'c1':
    s1 = c2 + c1 + c3
elif t == 'c2':
    s1 = c1 + c2 + c3
else:
    s1 = c1 + c3 + c2
s = s1
print('=========================================================================================')
print('The character you remembered is:', s[10])
print('=========================================================================================')