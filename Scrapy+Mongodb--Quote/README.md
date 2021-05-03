## Scrapy爬取名人名言网

* 爬取网站：[http://quotes.toscrape.com/](http://quotes.toscrape.com/)

* 本项目是我学习[【拉钩教育】](https://kaiwu.lagou.com/cours)，上[崔庆才](https://cuiqingcai.com/)前辈的[52讲轻松搞定网络爬虫](https://kaiwu.lagou.com/course/courseInfo.htm?courseId=46#/detail/pc)课程中做的笔记，主要是通过本项目学习Scrapy爬虫的基本框架
* 本项目还参考了[Scrapy官网入门教程](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html#item)，从中获得了一些解决方法
* 博客地址：[Scrapy爬取名人名言网](https://daiera.github.io/2021/05/03/Scrapy%E7%88%AC%E5%8F%96%E5%90%8D%E4%BA%BA%E5%90%8D%E8%A8%80%E7%BD%91/)

---

1. 通过`scrapy startproject <project_name>`来创建项目
2.  通过`scrapy genspider <spider_name> <url>`创建一个继承了`scrapy.Spider`类的Spider
   * 举例：`scrapy genspider quotes quotes.toscrape.com`，发现scrapy文件夹中多了一个`quotes.py`
3. 创建`Item`，在`items.py`中添加一个`QuoteItem`类，此时`item.py`应该是如下，定义了需要爬取的容器
4. 在spider中引用创建的Item，并修改`parse`方法，`yield`每个item
5. 让parse自动爬取下一页
6. 如果想保存为json文件，可以直接使用`scrapy crawl <spider_name> -o items.json`
7. 通过`Item Pipeline`将爬取到的数据存入Mongodb
   1. 修改settings.py，设置管道优先级和数据库相关信息
   2. 修改`pipelines.py`添加类`quoteToMongo`，设置与Mongodb的交互
   3. 执行爬取，Mongodb中成功看到想要的数据