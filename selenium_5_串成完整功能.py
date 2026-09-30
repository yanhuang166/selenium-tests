"""
项目第一个测试：数名言
第二个测试：登录功能
第三个测试：翻页测试
封装起来
"""
import time
from selenium import webdriver # 创建接口
from selenium.webdriver.common.by import By # 定位找元素

driver = webdriver.Edge()  # 接口对象创建
driver.implicitly_wait(10)  # 隐式等待 找到元素为止：避免没加载出来就执行操作而报错
# 测试名言数
def test_quote_count():
    driver.get('https://quotes.toscrape.com')

    context_all = driver.find_elements(By.CLASS_NAME, 'quote')
    print(f'共有{len(context_all)}句名言')

    # 断言：数量和预期一致吗？
    if len(context_all) == 10:
        print('✅ PASS: 首页显示 10 条名言')
    else:
        print(f'❌ FAIL: 期望 10 条，实际 {len(context_all)} 条')

# 第二个测试：登录功能
def test_login():
    driver.get('https://quotes.toscrape.com/login')  # 直接访问登录页面

    time.sleep(1)
    driver.find_element(By.NAME, 'username').send_keys('acccc')  # 账号框查找+输入账号
    time.sleep(1)
    driver.find_element(By.NAME, 'password').send_keys('123456789')
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

    print(repr(driver.current_url))  # 'https://quotes.toscrape.com/'原来是/问题
    time.sleep(2)
    if driver.find_elements(By.LINK_TEXT, 'Logout'):  # 这个最可靠
        print('登录无异常✅')
    else:
        print("登录失败❌")


# 第三个测试：翻页测试
def test_paginationage():
    driver.get('https://quotes.toscrape.com/')  # 直接访问首页页面
    # ① 记录第一页第一条名言
    one_text = driver.find_element(By.CLASS_NAME, 'text').text
    time.sleep(3)  # 给跳转也加上睡眠以防网络延迟被current_url立即捕捉到还没跳转的旧网址
    # 修法 B：结构定位（推荐，不理会文字长啥样）⭐
    driver.find_element(By.CSS_SELECTOR, 'li.next a').click()# 点击翻页
    time.sleep(1)
    # 记录新页面第一条名言
    two_text = driver.find_element(By.CLASS_NAME, 'text').text

    # ④ 断言：两条不同 → PASS
    if two_text != one_text:
        print('翻页正常✅')
    else:
        print('第一页和第二页名言重复翻页失败❌')

test_quote_count()
test_login()
time.sleep(2)
test_paginationage()

driver.quit()  # 关闭浏览器会话
# 测试要对比期望和实际"就是断言的本质。
# 函数名带 test_ 前缀还有个好处：以后学 pytest 框架时，它能自动识别这些函数是测试用例——行业惯例。