@echo off
echo 正在安装必要的包...
pip install pyinstaller

echo 正在打包程序...
pyinstaller --onefile --name clean_typora_assets clean_typora_assets.py

echo 打包完成！
echo 可执行文件位于 dist 目录中
pause 