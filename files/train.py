# a = 'https://klike.net/982-krasivye-kartinki-s-dnem-rozhdeniya-50-otkrytok.html'
# ext = a.split('.')[2].lower()
# ext1 = a.rsplit('.')
# print(ext,ext1)

# song = """When an eel grabs your arm,
# ... And it causes great harm,
# ... That's - a moray!"""

# a = song.replace(' moray', ' ray')

# print(a)

# g = 7
# num = 1

# while True:
#     if num < g:
#         print('too small')
#     elif num == g:
#         print('found it')
#         break
#     else:
#         print('imposible')
#     num += 1

# a = {1:'avd', 'a': 4}
# print(list(a))

# num = [i for i in range(10)]
# print(num)
# my = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
    
#     while low <= high:
#         mid = (low + high)//2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None

# print(binary_search(my, 6))

# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         elif item.is_a_key():
#             print('found')



# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index

# def selection_sort(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         smallest = find_smallest(arr)
#         new_arr.append(arr.pop(smallest))  
#     return new_arr

# print(selection_sort([5, 4, 7, 70, 2, 8, 1]))  


# def countdown(i):
#   # base case
#   if i <= 0:
#     return 0
#   # recursive case
#   else:
#     print(i)
#     return countdown(i-1)

# countdown(5)


# def greet2(name):
#     print('how are you, ', name) 
    
# def bye():
#     print('ok, bye')
    
# def greet(name):
#     print('hello, ', name)
#     greet2(name)
#     print('getting ready to say bye...')
#     bye()
    
# greet('ArturKing') 

# def fact(x):
#     if x == 1:
#         print('aga')
#         return 1
#     else:
#         print(x)
#         return x * fact(x-1)
    
# print(fact(4))


# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total

# print(sum([1, 2, 3, 4]))

# def quicksort(array):
#     if len(array) < 2:
#         print('wtf')
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(greater) + [pivot] + quicksort(less)
    
# print(quicksort([10, 5, 2, 3,6,8]))


# from collections import deque


# def person_is_seller(name):
#     return name[-1] == 'm' 

# graph = {}
# graph['you'] = ['alice', 'bob', 'claire']
# graph['bob'] = ['anuj', 'peggy']
# graph['alice'] = ['peggy']
# graph['claire'] = ['thom', 'jonny']
# graph['anuj'] = []
# graph['peggy'] = []
# graph['thom'] = []
# graph['jonny'] = []

# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
    
#     searched = set()
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if person_is_seller(person):
#                 print(person + ' is a mango seller')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.add(person)
#     return False

# search('you')


# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index


# arr = [i for i in range(10)]
# print(find_smallest([3, 5, 3, 1]))

# def end_zeros(num: int) -> int:
#     b = list(str(num))
#     c = b[::-1]
#     counter = 0
#     for i in c:
#         if int(i) != 0:
#             return counter
#         else:
#             counter += 1
            
#     return counter
    


# if __name__ == "__main__":
#     print("Example:")
#     #print(end_zeros(0))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     # assert end_zeros(0) == 1
#     # assert end_zeros(1) == 0
#     # assert end_zeros(10) == 1
#     # assert end_zeros(101) == 0
#     # assert end_zeros(245) == 0
#     assert end_zeros(100100) == 2
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# def backward_string(val: str) -> str:
#     a = val[::-1]
    
#     print(a)
#     return a


# if __name__ == '__main__':
#     print("Example:")
#     print(backward_string('val'))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert backward_string('val') == 'lav'
#     assert backward_string('') == ''
#     assert backward_string('ohho') == 'ohho'
#     assert backward_string('123456789') == '987654321'
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# a = 'vndhoinvdids'

# print(len('https://yandex.ru/images'))


# import unittest
# import sys
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver import ActionChains

# username = "khalikart" # Replace the username
# access_key = "ibXi9yAtGY7KtXT37mINyxUGpEHbwPRpuANSvyUZ0J4vX9BUxH" # Replace the access key

# class FirstSampleTest(unittest.TestCase):
   
#     def setUp(self):
#         desired_caps = {
#             "build": 'Lascana build', # Change your build name here
#             "name": 'Lascana_tests', # Change your test name here
#             "browserName": 'Chrome',
#             "version": '92.0',
#             "platform": 'Windows 10',
#             "resolution": '1920x1080',
#             "console": 'true', # Enable or disable console logs
#             "network": 'true'   # Enable or disable network logs
#         }
#         self.driver = webdriver.Remote(
#             command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
#             desired_capabilities= desired_caps)


#     def tearDown(self):
#         self.driver.quit()

    # def test_authentification_user(self):
    #     user_name = 'Алла'
    #     user_mail ='alla@mail.com'
    #     user_password ='alla1234'
    
    #     driver = self.driver
    #     driver.get("https://lascana.ru/")

    #     user_icon = driver.find_element(by=By.CSS_SELECTOR, value='.header-links__account')
    #     user_icon.click()

    #     email = driver.find_element(by=By.XPATH, value='//*[@id="auth_form"]/label[1]/input')
    #     email.send_keys(user_mail)

    #     password = driver.find_element(by=By.XPATH, value='//*[@id="auth_form"]/label[2]/div/input')
    #     password.send_keys(user_password)
        
    #     auth_submit_button = driver.find_element(by=By.XPATH, value='//*[@id="auth_form"]/div/input')
    #     auth_submit_button.click()
    #     time.sleep(2)
        
    #     name_on_the_header = driver.find_element(by=By.CSS_SELECTOR, value='.header-links__name').text
    #     self.assertEqual(name_on_the_header, user_name)
        
    # def test_registration_new_user(self):
    #     user_name = 'Алла'
    #     user_last_name = 'Аллова'
    #     user_mail = 'alla@email.com'
    #     user_password = 'alla1234'
        
    #     driver = self.driver
    #     driver.get("https://lascana.ru/")

    #     user_icon = driver.find_element(by=By.CSS_SELECTOR, value='.header-links__account')
    #     user_icon.click()

    #     regis_link = driver.find_element(by=By.XPATH, value='//*[@id="auth_form"]/div/div[2]/a')
    #     regis_link.click()
        
    #     last_name = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[1]/input')
    #     last_name.send_keys(user_last_name)
        
    #     name = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[2]/input')
    #     name.send_keys(user_name)
        
    #     email = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[4]/input')
    #     email.send_keys(user_mail)
        
    #     password = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[5]/input')
    #     password.send_keys(user_password)
        
    #     password_confirm  = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/label[6]/input')
    #     password_confirm.send_keys(user_password)
        
    #     agreement_box = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/div[3]/label/span')
    #     agreement_box.click()
        
    #     cookies = driver.find_element(by=By.CSS_SELECTOR, value='body > div.cookie-popup > div')
    #     driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element);""", cookies)
        
    #     regis_button = driver.find_element(by=By.XPATH, value='//*[@id="register_form"]/div[4]')
    #     regis_button.click()
    #     time.sleep(5)
        
    #     current_url = driver.current_url
    #     self.assertEqual(current_url, "https://lascana.ru/auth/index.php" )
        
    # def test_adding_into_favorites(self):
        
    #     driver = self.driver
    #     driver.get("https://lascana.ru/")
        
    #     kupalniki_tab = driver.find_element(by=By.CSS_SELECTOR, value='li.navigation-menu__item:nth-child(4) > a:nth-child(1)')
    #     kupalniki_tab.click()
        
    #     first_picture = driver.find_element(by=By.XPATH, value='/html/body/section/div[4]/div/div/div[1]/a/div[1]')
    #     first_picture.click()
        
    #     icon_add_to_favorite = driver.find_element(by=By.XPATH, value='//*[@id="bx_117848907_7527"]/div[2]/div[4]/a[3]')
    #     icon_add_to_favorite.click() 
        
    #     uniq_product_article = driver.find_element(by=By.ID ,value='product__article').text
        
    #     header_link_into_favorites = driver.find_element(by=By.CSS_SELECTOR, value='.header-links__favourites')
    #     header_link_into_favorites.click()
    #     time.sleep(2)
        
    #     current_url = driver.current_url
    #     self.assertEqual(current_url, "https://lascana.ru/personal/favorite/" )
        
    #     favorites_item_image = driver.find_element(by=By.CSS_SELECTOR, value='.personal__favorite--item_image')
    #     favorites_item_image.click()
        
    #     product_article_in_favorites = driver.find_element(by=By.ID ,value='product__article').text
    #     self.assertEqual(uniq_product_article, product_article_in_favorites )
        
#     def test_adding_into_favorites(self):
        
#         driver = self.driver
#         driver.get("https://lascana.ru/")     
        

# if __name__ == "__main__":
#     unittest.main()

import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        if not data:
            # Клиент отключился
            break
        client_sock.sendall(data)

    client_sock.close()