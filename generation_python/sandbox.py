s = input()
left = s.find('h')
right = s.rfind('h')
print(s[:left] + s[right + 1:])