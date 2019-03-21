# 在包的__init__.py中使用__all__：导出包里的模块
import os
import sys
sys.path.append(os.path.split(str(__file__))[0])

# 定义 __all__，指定需要导出的内容
__all__ = ["python_1", "python_2", "python_11", "python_22"]

# 若要直接导出文件中的方法或者模块，需要导入：
from python_1 import python_11
from python_2 import python_22
