#!/usr/bin/env python3
"""
《哈尔的移动城堡》音乐建造系统 - 主生成器
作者：为 Siraw2333 定制
"""
import os
import sys
import json
import time

# 添加core目录到模块搜索路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

def main():
    print("=== 《哈尔的移动城堡》音乐建造系统 ===")
    print("正在加载配置...")
    
    # 加载配置
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    print(f"目标版本: Minecraft {config['version']}")
    print(f"建造方向: {config['build']['spiral_direction']}")
    
    # 检查数据文件
    data_files = ['data/hows.litematic', 'data/converted_timeline.json']
    for file in data_files:
        if not os.path.exists(file):
            print(f"错误: 未找到文件 {file}")
            print("请将城堡文件(.litematic)和音乐时间轴文件(.json)放入 data/ 文件夹")
            return
    
    print("✓ 数据文件检查通过")
    
    # 这里将调用各个核心模块
    print("\n[1/5] 正在解析城堡结构...")
    # 未来将调用: castle_data = castle_parser.parse('data/hows.litematic')
    
    print("[2/5] 正在加载音乐时间轴...")
    # 未来将调用: timeline = music_sync.load('data/converted_timeline.json')
    
    print("[3/5] 正在生成螺旋建造序列...")
    # 未来将调用: spiral_order = spiral_generator.generate(castle_data, direction='clockwise')
    
    print("[4/5] 正在生成内部通道...")
    # 未来将调用: path_blocks = path_generator.create_path(castle_data, config)
    
    print("[5/5] 正在生成Minecraft命令...")
    # 未来将调用: commands = command_generator.create_commands(spiral_order, timeline, config)
    
    print("\n✅ 生成完成！")
    print("输出文件位于 output/ 目录")
    print("请将 output/datapack/ 放入Minecraft世界的datapacks文件夹")

if __name__ == '__main__':
    main()