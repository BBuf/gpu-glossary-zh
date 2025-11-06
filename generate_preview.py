#!/usr/bin/env python3
"""
快速生成英文原文预览版网站
不需要翻译，直接使用下载的原文
"""

import sys
from pathlib import Path

# 复用generate_website.py的代码
sys.path.insert(0, str(Path(__file__).parent))
from generate_website import WebsiteGenerator

def main():
    """使用英文原文生成预览网站"""
    print("=" * 60)
    print("GPU Glossary 预览版生成器")
    print("=" * 60)
    
    script_dir = Path(__file__).parent
    input_dir = script_dir / "content"  # 使用原文
    output_dir = script_dir / "website-preview"
    
    if not input_dir.exists():
        print(f"\n错误: 内容目录不存在: {input_dir}")
        print("请先运行 download_and_translate.py 下载文件")
        return
    
    print(f"\n使用英文原文生成网站...")
    print(f"输入目录: {input_dir}")
    print(f"输出目录: {output_dir}\n")
    
    generator = WebsiteGenerator(input_dir, output_dir)
    generator.generate_all()
    
    print("\n" + "=" * 60)
    print("提示:")
    print("  这是使用英文原文生成的预览版")
    print("  如需中文版，请先翻译文件后运行 generate_website.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
