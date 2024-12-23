# 大学招生资讯爬虫项目

![](https://img.shields.io/badge/Language-python3-blue.svg)
![](https://img.shields.io/badge/license-Apache_2.0-green.svg)

## 项目描述

这个项目使用Scrapy框架开发，旨在爬取各大学的招生资讯，包括但不限于招生简章、重要日期、入学要求等信息。本项目旨在为学生提供最新的招生信息，帮助他们更好地进行学校选择和申请准备。

## 克隆项目代码

从GitHub克隆项目到本地环境：

```bash
git clone https://github.com/Weiliyoung/uninews_spider.git
cd uninews_spider
```

## 开发环境准备

以下是搭建和运行本项目所需的环境和步骤：

### 系统要求

- **操作系统**：Windows, Linux 或 macOS
- **Python 版本**：Python 3.6 或以上

### 安装 Python 和 pip

确保 Python 和 pip 已安装。可以通过在终端运行以下命令来检查版本：

```bash
python --version
pip --version
```

### 安装虚拟环境支持 (`venv`)

在Python 3中，`venv` 模块通常是预安装的。如果你的Python环境中没有包含 `venv`，可以通过以下命令安装：

```bash
pip install virtualenv
```

安装完成后，你可以使用 `virtualenv` 来创建虚拟环境，这与使用 `venv` 非常相似。

### 设置虚拟环境

为了避免污染全局Python环境，推荐使用虚拟环境。以下是如何使用`venv`模块（内置于Python 3中）设置虚拟环境：

1. 创建虚拟环境：

```bash
python -m venv venv
```

2. 激活虚拟环境：
    - Windows:
   ```bash
   .\venv\Scripts\activate
   ```
    - Linux 或 macOS:
   ```bash
   source venv/bin/activate

### 依赖安装

可以通过运行`pip install -r requirements.txt`来安装所有必要的包。

## 开发规范

### 代码风格

项目遵循Google代码风格指南。

### 文档

每个模块和函数都需要有适当的文档字符串，描述其功能和参数。

## 提交规范

为保持项目的清晰和可维护性，请遵循以下Git提交规范：

### 分支策略

- `main`：稳定版本，用于部署。
- `dev`：开发分支，用于日常开发。
- 功能分支：从`dev`分支检出，每个功能一个分支，完成后合并回`dev`。

### 拉取信息

拉取远程更改

```bash
git pull
```

### 提交信息

提交信息应该清晰描述改动的内容，例如：

```bash
git commit -m "添加了对某大学招生信息的爬取功能"
```

### 添加更改

```bash
git add .
git commit -m "描述提交的更改"
git push            --如果你的远程分支不是 origin，你需要指定远程分支的名称。git push origin main
```

### 解决拉取提交信息冲突

拉取远程更改。首先，执行命令来拉取远程仓库的更改到本地：

```bash
git pull origin main
```
这会将远程仓库的 main 分支上的更改拉取到本地仓库，并尝试自动合并。

```bash
解决冲突（如果有）： 如果 git pull 命令执行后提示发生了冲突，你需要手动解决这些冲突。打开冲突文件，手动编辑冲突内容，解决冲突后保存文件。
```

解决完冲突后，
使用 git add 命令将解决冲突后的文件添加到暂存区，然后使用 git commit 命令提交解决冲突的更改：

```bash
git add .
git commit -m "解决冲突"
```

推送更改： 最后，再次尝试推送你的更改到 GitHub：

```bash
git push origin main
```


## 运行项目

运行爬虫：

```bash
scrapy crawl spider_name
```

## 贡献指南

欢迎贡献！请确保你的提交符合我们的开发和提交规范。对于较大的更改，请先在issues中讨论。

## 许可证

本项目采用 [Apache 许可证](LICENSE)。

```

根据你的具体需求和项目细节，你可能需要进一步修改和填充上述内容。希望这个模板对你有帮助！如果你有其他问题或需要进一步的帮助，请随时告诉我。