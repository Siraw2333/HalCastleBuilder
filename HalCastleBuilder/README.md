# 《哈尔的移动城堡》音乐同步建造系统

这是一个为Minecraft 1.21.1设计的自动建造系统，能将《哈尔的移动城堡》的结构与音乐《人生的旋转木马》的节拍同步，通过CommandFallingBlock模组实现方块从四面八方的螺旋飞来效果。

## 如何使用
1. 将你的 `hows.litematic` 和 `converted_timeline.json` 放入 `data/` 文件夹。
2. 安装依赖：`pip install -r requirements.txt`
3. 运行生成器：`python generate_castle.py`
4. 将 `output/datapack/` 文件夹放入Minecraft世界的datapacks文件夹。
5. 在游戏中放置黄金压力板并踩下以触发建造。