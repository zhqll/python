# 拼接字符串的方法

# 1.使用+拼接字符串
print("李白", "青莲居士")
print("李白" + "青莲居士")
name = "杜甫"
hao = "草堂居士"
print(name + hao)
n = "456"
m = "123"
print(n + m)
# 2. 使用占位符 %s，%d，%f
book = "钢铁是怎样炼成的"
publish_year = 1933
price = 26.5
print("书名：%s,出版日期：%d, 价格：%.2f" % (book, publish_year, price))
# 3.使用format（），函数拼接字符串，在拼接的位置写{}
# 1）"{}".format()
print("{} - {} - {}".format(book, publish_year, price))
# 2) 在{}中写入位置顺序，从0开始
print("{0} - {1} - {2}".format(book, publish_year, price))
# 3) 在{}中写入一个形象，在format（）中用形参=实参进行传值
print("{pub}-{book}-{price}".format(pub=publish_year, book=book, price=price))
print("{pub}-{book}-{price}".format(price=price, pub=publish_year, book=book))
# 4) 特别简单的用法，在字符串前边添加符f，{}直接写变量
print(f"{book} {publish_year} {price}")

