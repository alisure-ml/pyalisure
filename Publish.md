## 发布方法


### 1、注册账户

* 到官网注册用户：[https://pypi.org/](https://pypi.org/)

    ```
    邮箱：562282219@qq.com
    用户名：ALISURE
    密码：3/4
    ```

* 验证邮箱



### 2、准备`setup.py` 和 `README.rst`文件

* `setup.py`：[demo/setup.py](./demo/setup.py)，

* `README.rst`：该内容是显示在pypi包首页上。


### 3、打包

* 具体内容见[demo](./demo/pyalisuredemo)

* 打包

    * 源代码的包：在当前目录的dist文件夹下，就会多出一个以tar.gz结尾的包。
    
    ```
    python setup.py sdist build
    ```
    
    * 或者wheels格式的包：在dist文件夹下生成一个whl文件
    
    ```
    python setup.py bdist_wheel --universal
    ```

* 上传
    
    * 上传source包
    ```
    python setup.py sdist upload
    ```
    
    * 上传pre-compiled包
    ```
    python setup.py bdist_wheel upload
    ```
    
    * 或者使用twine上传，需要先安装`sudo pip install twine`
    ```
    twine upload dist/*
    ```


### 4、安装

可以在任何地方安装：

    ```
    sudo pip install pyalisuredemo
    ```

可以在任何地方更新：

    ```
    sudo pip install pyalisuredemo --upgrade
    ```

### 5、测试

```
import pyalisuredemo as alisuredemo
alisuredemo.pyhton11()
alisuredemo.pyhton22()
alisuredemo.pyhton11("aaaaa")
alisuredemo.pyhton22("bbbbb")
```


### 6、问题

* Upload failed (403)
    
    问题：
    ```
    Upload failed (403): Invalid or non-existent authentication information.
    error: Upload failed (403): Invalid or non-existent authentication information.
    ```
    
    解决方法：创建`～/.pypirc`文件
    ```
    [distutils]
    index-servers=pypi
    
    [pypi]
    repository = https://upload.pypi.org/legacy/
    username = <username>
    password = <password>
    ```
   
    
### 7. Inference

* [在Pypi上发布自己的Python包](https://www.cnblogs.com/sting2me/p/6550897.html)

* [reStructuredText](https://rest-sphinx-memo.readthedocs.io/en/latest/ReST.html)

* [发布你自己的轮子 - PyPI打包上传实践](https://segmentfault.com/a/1190000008663126)
