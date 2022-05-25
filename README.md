

> ## 项目简介

本项目为项目作者接触Python图片处理相关的练手项目

功能：**实现将大量图片按色块拟合拼接为指定的大图**

示例：
![2](https://raw.githubusercontent.com/fullstack-sake/MultiImgFit/main/doc/example.png)


> ## 使用手册

下载仓库`main.py`，并安装好`requirements.txt`的`python`库

运行 `python main.py [-h] [--i I] [--o O] [--s S] [--M M] [--N N] [--n N]`

![1](https://raw.githubusercontent.com/fullstack-sake/MultiImgFit/main/doc/example2.png)

参数含义：（带有--的参数为可选参数）

| 参数      | 含义                        | 备注                                                         |
| --------- | --------------------------- | ------------------------------------------------------------ |
| -h,--help | 显示帮助                    |                                                              |
| --i       | 输入图片绝对路径            | 默认为"D:/Project/example.jpg"                               |
| --o       | 输出图片路径                | 默认为"D:/Project/out.jpg"                                   |
| --s       | 源图库文件夹路径            | 默认为"D:/Project/source/"                                   |
| --M       | 像素块大小(每个像素放大M倍) | 默认大小50                                                   |
| --N       | 输入图片缩放倍数            | （该参数影响处理速度）原图如果尺寸大于500*500将会缩放，默认缩小为1/3 |
| --n       | 源图库图片缩放倍数          | （该参数影响输出图片大小）默认缩小为1/3                      |

> ### 注意事项

- 源图库图片颜色应多样化，否则无法准确匹配输入图片的色块，导致输出图片失真