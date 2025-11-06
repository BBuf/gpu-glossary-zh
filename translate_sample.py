#!/usr/bin/env python3
"""
示例：翻译单个文件或几个文件
适合测试翻译效果
"""

import os
from pathlib import Path
from translate_with_ai import AITranslator

def translate_samples():
    """翻译几个示例文件测试效果"""
    
    # 检查API Key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("\n⚠️  未设置 OPENAI_API_KEY 环境变量")
        print("\n提示: 如果您没有OpenAI API Key，可以:")
        print("  1. 使用其他翻译服务（如Claude、DeepL等）")
        print("  2. 手动翻译markdown文件")
        print("  3. 跳过翻译，直接使用英文原文生成网站\n")
        return
    
    script_dir = Path(__file__).parent
    input_dir = script_dir / "content"
    output_dir = script_dir / "translated"
    
    # 选择几个示例文件进行翻译
    sample_files = [
        "readme.md",
        "device-hardware/cuda-core.md",
        "device-software/warp.md",
        "perf/occupancy.md",
    ]
    
    print("=" * 60)
    print("翻译示例文件")
    print("=" * 60)
    print(f"\n将翻译以下文件:")
    for f in sample_files:
        print(f"  - {f}")
    print()
    
    translator = AITranslator(api_key=api_key)
    
    for i, file_name in enumerate(sample_files, 1):
        input_file = input_dir / file_name
        output_file = output_dir / file_name
        
        if not input_file.exists():
            print(f"[{i}/{len(sample_files)}] ⚠️  文件不存在: {file_name}")
            continue
        
        print(f"[{i}/{len(sample_files)}] 翻译: {file_name}")
        context = f"文件路径: gpu-glossary/{file_name}"
        
        success = translator.translate_file(input_file, output_file, context)
        
        if success:
            print(f"  ✓ 完成")
        else:
            print(f"  ✗ 失败")
        
        # 延迟避免限流
        if i < len(sample_files):
            import time
            time.sleep(2)
    
    print("\n" + "=" * 60)
    print(f"完成！翻译文件保存在: {output_dir}")
    print("\n查看翻译结果:")
    for f in sample_files:
        output_file = output_dir / f
        if output_file.exists():
            print(f"  {output_file}")
    print("=" * 60)

if __name__ == "__main__":
    translate_samples()
