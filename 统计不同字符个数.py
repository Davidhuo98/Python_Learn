#统计不同字符的个数
character = input('请输入任意字符：')
i = number = space = other = letter = 0
for i in range(len(character )):
    if 'a' <= character [i] <= 'z' or 'A' <= character [i] <= 'Z':
        letter += 1
    elif '0' <= character [i] <= '9':
        number += 1
    elif character [i] == ' ':
        space += 1
    else:
        other += 1
print("字母个数为：",letter,'\t',"数字个数为：",number,'\t',"空格个数为：",space,'\t',"其他字符个数为：",other)