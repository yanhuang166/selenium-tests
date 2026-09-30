# selenium-tests
基于 Selenium 的 Web 自动化测试项目
# selenium-tests

基于 Selenium 的 Web 自动化测试项目，测试 quotes.toscrape.com 的核心功能。

## 测试用例

| 测试 | 验证点 |
|------|--------|
| 名言数量测试 | 首页应显示 10 条名言 |
| 登录功能测试 | 登录后页面出现 Logout 链接 |
| 翻页功能测试 | 翻页后第一条名言与首页不同 |

## 技术栈

- Python 3
- Selenium 4（Edge 浏览器驱动）
- 隐式等待（implicitly_wait）

## 运行

```bash
pip install selenium
python test_quotes.py
