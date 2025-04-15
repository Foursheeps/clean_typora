# Typora资源清理工具

这是一个用于清理Typora编辑器中未使用图片资源的Python工具。它可以帮助您自动识别并删除**同级目录**./`assets`文件夹中在Markdown文件中未被引用的图片文件，保持项目文件夹整洁。

## 功能特点

- 自动扫描README.md文件中的图片引用
- 支持多种图片引用语法（`![]()` 和 `<img>` 标签）
- 识别并清理未使用的图片文件
- 提供详细的清理统计信息
- 支持相对路径和绝对路径的图片引用

## 系统要求

- Python 3.x
- 操作系统：Windows/macOS/Linux

## 使用方法

### 方法一：直接运行Python脚本

1. 确保您的项目目录中有 `README.md` 文件
2. 运行脚本：
   ```bash
   python clean_typora_assets.py [目录路径]
   ```
   
   如果不指定目录路径，脚本将在当前目录下执行。

3. 程序执行完成后会显示清理统计信息，按回车键退出。

### 方法二：使用打包后的可执行文件

1. 下载发布版本中的 `clean_typora_assets.exe`
2. 双击运行，或在命令行中执行：
   ```bash
   clean_typora_assets.exe [目录路径]
   ```

## 打包说明

如果您想自己打包成可执行文件，请按以下步骤操作：

1. 安装PyInstaller：
   ```bash
   pip install pyinstaller
   ```

2. 在项目目录下执行打包命令：
   ```bash
   pyinstaller --onefile clean_typora_assets.py
   ```

3. 打包完成后，可执行文件将在 `dist` 目录中生成

## 示例

假设您的项目结构如下：
```
project/
├── README.md
└── assets/
    ├── image1.png
    ├── image2.jpg
    └── image3.png
```

如果 `README.md` 中只引用了 `image1.png`，运行脚本后将删除 `image2.jpg` 和 `image3.png`。

## 注意事项

- 脚本默认只处理 `README.md` 文件中的图片引用
- 支持的图片格式：PNG、JPG、JPEG、GIF、BMP、WEBP
- 建议在运行脚本前备份重要文件
- 删除的文件无法恢复，请谨慎操作

## 贡献

欢迎提交问题和改进建议！

## 许可证

MIT License
# clean_typora
# clean_typora
# clean_typora
