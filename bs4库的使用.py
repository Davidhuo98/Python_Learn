from bs4 import BeautifulSoup

html_string = """
<html>
<head>
<title>Simple test</title>
</head>
<body>
<p id='China'>中国,<b>你好!</b>. </p>
<p id='World'>世界,<b>大同!</b>. </p>
</body>
</html>
"""

soup = BeautifulSoup(html_string, 'html.parser')

# 提取并打印所有的中文字符
for string in soup.stripped_strings:
    # 判断字符串中是否包含中文字符
    if any(ord(char) >= 0x4e00 and ord(char) <= 0x9fff for char in string):
        print(string)


