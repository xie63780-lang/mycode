# MyCode

本仓库用于练习 Git 分支、Pull Request、代码评审和合并。

## 运行问候程序

使用 Python 3.10 或更高版本，无需安装第三方依赖。

```powershell
python hello.py
```

默认输出：`你好，朋友！`

也可以在 Python 中调用 `greet("小明")`，输出：`你好，小明！`。

程序会去除姓名首尾的空白。如果传入空字符串或纯空白字符串，姓名会回退为“朋友”。

```python
greet("")          # 你好，朋友！
greet("   ")       # 你好，朋友！
greet("  小明  ")  # 你好，小明！
```
