# site =input("사이트를 입력")
# print(site[7:10]+ str(len(site[7:12]))+ str(site.count("e")) + "!" )

url = "http://naver.com"
my_str = url.replace("http://", "") 

my_str = my_str[:my_str.index(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))