# pytest + allure + selenium + yaml + excel ---- UI自动化框架


1. allure：生成报告
- 使用Allure内置功能，实现用例执行结果统计、日志收集、错误截图等功能；
- 可生成精确到每一个测试步骤的详细测试报告，提高UI自动化测试过程中问题定位效率。
2. selenium：关键字封装
- 基于Selenium，使用PO模式对UI页面进行封装，将页面元素分类，使用excel或yaml文件进行集中管理，实现流程复用
3. pytest：用例控制管理
- 引用已封装好的关键字和业务流程，进行用例编写
- 基于Pytest,实现用例分组排序、失败重跑、用例跳过、前置后置等功能、使用pytest钩子函数实现异常截图
4. yaml + excel：数据管理
- 使用yaml、json、excel进行数据管理，包括pom页面分离出来的元素数据和用例数据



#### 框架目录结构
```
.
├── Data                            // 数据存放
│   ├── page_data                   // 页面元素数据
│   ├── testcase_data               // 测试用例数据
├── Data_Load                       // 数据加载
│   ├── case_data                   // 函数装饰器 ==》测试用例数据加载
│   ├── pom_data                    // 类装饰器   ==》页面对象 元素数据加载
├── KeyWord                         // 关键字封装
│   ├── Browser.py                  // selenium，浏览器操作封装
│   ├── Sql_base.py                 // pymysql，SQL数据库使用封装
├── Page                            // 页面对象存放
│   ├── project                     // 根据项目、前后台页面、自行分类存放
├── report_allure                   // allure生成报告位置
├── result                          // result  
├── TestCase                        // 测试用例存放
│   ├── project                     // 根据项目、模块等 自行安排存放位置
├── conftest.py                     // fixture前置后置操作、钩子函数实现异常截图
├── run.py                          // 运行入口  