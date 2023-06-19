# pytest + allure + selenium + yaml + excel ---- UI自动化框架

### 框架分层介绍
1. 报告层：allure
- 使用Allure内置功能，实现用例执行、结果统计、日志收集、错误截图等功能；
- 能生成精确到每一个测试步骤的详细测试报告，提高UI自动化测试过程中问题定位效率。
2. 关键字封装层：selenium
- 基于Selenium，使用PO模式对UI页面进行封装，将页面元素分类
- 使用excel或yaml文件对元素定位数据进行集中管理
3. 用例管理控制层：pytest
- 引用已封装好的关键字和业务流程，进行用例编写
- 基于Pytest,实现用例分组排序、失败重跑、用例跳过、前置后置等功能、使用pytest钩子函数实现异常截图
4. 数据管理：yaml 、 excel 、 json
- 使用yaml、json、excel进行数据管理，包括pom页面分离出来的元素数据和用例数据
5. 其他
- 对pymysql进行封装===访问数据库
- 使用pyautogui第三方库，解决文件上传等操作



### 框架目录结构
```
.
├── Data                            // 数据存放
│   ├── page_data                   // 页面元素数据
│   ├── testcase_data               // 测试用例数据
├── Data_Load                       // 数据加载
│   ├── case_data                   // 测试用例数据加载
│   ├── pom_data                    // 类装饰器   ==》页面对象 元素数据加载
├── KeyWord                         // 关键字封装
│   ├── Browser.py                  // selenium，浏览器操作封装
│   ├── Sql_base.py                 // pymysql，SQL数据库使用封装
├── Page                            // 页面对象存放
│   ├── project                     // 根据项目、前后台页面、自行分类存放
├── PyAutoGui                       // pyautogui第三方库使用：OS层面进行鼠标、键盘相关操作
│   ├── location.py                 // 网上找的代码==输出鼠标的坐标
│   ├── pyautogui_use.py            // pyautogui的一些基础用法
│   ├── file_uploader.py            // layUI==尝试在OS层面进行单图片上传
├── report_allure                   // allure生成报告位置
├── result                          // result  
├── TestCase                        // 测试用例存放
│   ├── project                     // 根据项目、模块等 自行安排存放位置
├── conftest.py                     // fixture前置后置操作、钩子函数实现异常截图
├── run.py                          // 运行入口  