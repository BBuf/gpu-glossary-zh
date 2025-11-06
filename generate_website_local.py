#!/usr/bin/env python3
"""
生成本地测试版网站（不带 GitHub Pages base path）
"""

import os
import sys

# 设置环境变量为空，生成本地测试版本
os.environ['GITHUB_PAGES_BASE'] = ''

# 导入并运行主脚本
from generate_website import main

if __name__ == "__main__":
    print("生成本地测试版网站...")
    main()
    print("\n提示: 使用以下命令启动本地服务器:")
    print("  cd website && python -m http.server 8000")
