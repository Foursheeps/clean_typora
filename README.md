# Typora资源清理工具

这是一个用于清理Typora编辑器中未使用图片资源的Python工具。它可以帮助您自动识别并删除目录下所有`.assets`文件夹中在Markdown文件中未被引用的图片文件，保持项目文件夹整洁。

## 功能特点

- 自动扫描目录下所有.md文件中的图片引用
- 支持多种图片引用语法（`![]()` 和 `<img>` 标签）
- 识别并清理未使用的图片文件
- 提供详细的清理统计信息
- 支持相对路径和绝对路径的图片引用
- 递归搜索所有子目录中的.md文件和.assets文件夹
- 支持批量处理多个项目目录

## 系统要求

- Python 3.x
- 操作系统：Windows/macOS/Linux
- 磁盘空间：至少100MB（用于程序运行）

## 使用场景

1. 清理Typora文档中未使用的图片
2. 整理项目文档中的冗余资源
3. 批量处理多个Markdown项目
4. 在提交代码前清理无用资源

## 使用方法

### 方法一：直接运行Python脚本

1. 确保您的目录中有.md文件和对应的.assets文件夹
2. 运行脚本：
   ```bash
   # 处理当前目录
   python clean_typora_assets.py

   # 处理指定目录
   python clean_typora_assets.py /path/to/your/project

   # 处理多个目录
   python clean_typora_assets.py /path1 /path2 /path3
   ```

3. 程序执行完成后会显示清理统计信息，按回车键退出。

### 方法二：使用打包后的可执行文件

1. 下载发布版本中的 `clean_typora_assets.exe`
2. 双击运行，或在命令行中执行：
   ```bash
   # 处理当前目录
   clean_typora_assets.exe

   # 处理指定目录
   clean_typora_assets.exe "D:\My Projects\Documentation"
   ```

## 打包说明

如果您想自己打包成可执行文件，请按以下步骤操作：

1. 安装PyInstaller：
   ```bash
   pip install pyinstaller
   ```

2. 在项目目录下执行打包命令：
   ```bash
   # 生成单个可执行文件
   pyinstaller --onefile clean_typora_assets.py

   # 生成带控制台窗口的可执行文件
   pyinstaller --onefile --console clean_typora_assets.py

   # 生成无控制台窗口的可执行文件
   pyinstaller --onefile --noconsole clean_typora_assets.py
   ```

3. 打包完成后，可执行文件将在 `dist` 目录中生成

## 示例

### 示例1：基本项目结构
```
project/
├── docs/
│   ├── guide.md
│   └── assets/
│       ├── image1.png
│       └── image2.jpg
├── README.md
└── assets/
    ├── image3.png
    └── image4.jpg
```

如果 `guide.md` 引用了 `image1.png`，`README.md` 引用了 `image3.png`，运行脚本后将删除 `image2.jpg` 和 `image4.jpg`。

### 示例2：复杂项目结构
```
project/
├── docs/
│   ├── api/
│   │   ├── reference.md
│   │   └── assets/
│   │       ├── api-diagram.png
│   │       └── old-diagram.png
│   ├── guide.md
│   └── assets/
│       ├── guide-image.png
│       └── unused-image.jpg
├── README.md
└── assets/
    ├── logo.png
    └── banner.jpg
```

脚本会递归搜索所有目录，清理所有未使用的图片。

## 注意事项

- 脚本会扫描目录下所有的.md文件
- 支持的图片格式：PNG、JPG、JPEG、GIF、BMP、WEBP
- 建议在运行脚本前备份重要文件
- 删除的文件无法恢复，请谨慎操作
- 如果图片路径包含中文，请确保系统支持UTF-8编码
- 建议在运行前先使用 `--dry-run` 模式测试（如果支持）

## 常见问题

1. **Q: 为什么有些图片没有被删除？**  
   A: 可能是因为图片在Markdown文件中的引用路径使用了不同的格式或相对路径。

2. **Q: 如何恢复误删的图片？**  
   A: 建议在运行脚本前先备份整个项目目录。

3. **Q: 支持哪些图片引用格式？**  
   A: 支持标准的Markdown图片语法 `![alt](path)` 和HTML的 `<img>` 标签。

## 贡献

欢迎提交问题和改进建议！如果您发现了bug或有新功能建议，请提交Issue或Pull Request。

## 许可证

MIT License
