#2. Заменить символ "#" на символ "/" в строке:www.my_site.com#about
# 1 вариант
old_text = 'www.my_site.com#about'
new_text = 'www.my_site.com/about'
print(new_text)

# 2 вариант
text = 'www.my_site.com#about'
text = text.replace('#','/')
print(text)