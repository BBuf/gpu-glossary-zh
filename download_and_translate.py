#!/usr/bin/env python3
"""
GPU Glossary 中文翻译工具
从 GitHub 下载所有 markdown 文件并翻译成中文
"""

import os
import re
import time
from pathlib import Path
from typing import Dict, List, Tuple
import requests
from urllib.parse import urljoin

# GitHub 仓库配置
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/modal-labs/gpu-glossary/main/gpu-glossary/"
GITHUB_API_BASE = "https://api.github.com/repos/modal-labs/gpu-glossary/contents/gpu-glossary"

# 输出目录
OUTPUT_DIR = Path(__file__).parent / "content"


class GitHubDownloader:
    """从 GitHub 下载文件"""
    
    def __init__(self, base_url: str, api_url: str):
        self.base_url = base_url
        self.api_url = api_url
        self.session = requests.Session()
    
    def get_directory_contents(self, path: str = "") -> List[Dict]:
        """获取目录内容"""
        url = f"{self.api_url}/{path}" if path else self.api_url
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def download_file(self, file_path: str) -> str:
        """下载单个文件"""
        url = urljoin(self.base_url, file_path)
        response = self.session.get(url)
        response.raise_for_status()
        return response.text
    
    def download_all_markdown_files(self, base_path: str = "") -> Dict[str, str]:
        """递归下载所有 markdown 文件"""
        files = {}
        
        try:
            contents = self.get_directory_contents(base_path)
            
            for item in contents:
                if item['type'] == 'file' and item['name'].endswith('.md'):
                    file_path = item['path'].replace('gpu-glossary/', '', 1)
                    print(f"下载: {file_path}")
                    content = self.download_file(file_path)
                    files[file_path] = content
                    time.sleep(0.5)  # 避免请求过快
                    
                elif item['type'] == 'dir':
                    subdir_path = item['path'].replace('gpu-glossary/', '', 1)
                    print(f"进入目录: {subdir_path}")
                    sub_files = self.download_all_markdown_files(item['path'].replace('gpu-glossary/', '', 1))
                    files.update(sub_files)
                    
        except Exception as e:
            print(f"错误: {e}")
        
        return files


class MarkdownTranslator:
    """翻译 Markdown 内容"""
    
    # 术语翻译映射表
    TERM_MAPPING = {
        # 硬件相关
        "Streaming Multiprocessor": "流式多处理器",
        "SM": "流式多处理器",
        "Core": "核心",
        "CUDA Core": "CUDA核心",
        "Tensor Core": "Tensor核心",
        "Special Function Unit": "特殊函数单元",
        "SFU": "特殊函数单元",
        "Load/Store Unit": "加载/存储单元",
        "LSU": "加载/存储单元",
        "Warp Scheduler": "Warp调度器",
        "Tensor Memory Accelerator": "Tensor内存加速器",
        "TMA": "Tensor内存加速器",
        "Texture Processing Cluster": "纹理处理簇",
        "TPC": "纹理处理簇",
        "Graphics Processing Cluster": "图形处理簇",
        "GPU Processing Cluster": "GPU处理簇",
        "GPC": "图形/GPU处理簇",
        "Register File": "寄存器文件",
        "L1 Data Cache": "L1数据缓存",
        "Tensor Memory": "Tensor内存",
        "GPU RAM": "GPU内存",
        
        # 软件相关
        "Thread": "线程",
        "Warp": "线程束",
        "Cooperative Thread Array": "协作线程数组",
        "CTA": "协作线程数组",
        "Kernel": "内核",
        "Thread Block": "线程块",
        "Thread Block Grid": "线程块网格",
        "Thread Hierarchy": "线程层次结构",
        "Memory Hierarchy": "内存层次结构",
        "Registers": "寄存器",
        "Shared Memory": "共享内存",
        "Global Memory": "全局内存",
        
        # CUDA工具
        "CUDA Driver API": "CUDA驱动API",
        "CUDA Runtime API": "CUDA运行时API",
        "NVIDIA Management Library": "NVIDIA管理库",
        "NVML": "NVIDIA管理库",
        "Streaming ASSembler": "流式汇编器",
        "SASS": "流式汇编器",
        "Parallel Thread eXecution": "并行线程执行",
        "PTX": "并行线程执行",
        "Compute Capability": "计算能力",
        
        # 性能相关
        "Performance Bottleneck": "性能瓶颈",
        "Roofline Model": "屋顶线模型",
        "Compute-bound": "计算受限",
        "Memory-bound": "内存受限",
        "Arithmetic Intensity": "算术强度",
        "Overhead": "开销",
        "Little's Law": "利特尔定律",
        "Memory Bandwidth": "内存带宽",
        "Arithmetic Bandwidth": "算术带宽",
        "Latency Hiding": "延迟隐藏",
        "Warp Execution State": "Warp执行状态",
        "Active Cycle": "活跃周期",
        "Occupancy": "占用率",
        "Pipe Utilization": "流水线利用率",
        "Peak Rate": "峰值速率",
        "Issue Efficiency": "发射效率",
        "Streaming Multiprocessor Utilization": "流式多处理器利用率",
        "Warp Divergence": "Warp分歧",
        "Branch Efficiency": "分支效率",
        "Memory Coalescing": "内存合并",
        "Bank Conflict": "Bank冲突",
        "Register Pressure": "寄存器压力",
    }
    
    def __init__(self):
        """初始化翻译器"""
        pass
    
    def translate_content(self, content: str, file_path: str) -> str:
        """
        翻译markdown内容
        注意：这是一个基础实现，实际使用时建议集成翻译API
        """
        print(f"翻译: {file_path}")
        
        # 这里需要实际的翻译逻辑
        # 可以集成 OpenAI API, Google Translate API 等
        # 为了示例，这里返回带有翻译标记的内容
        
        translated = content
        
        # 添加翻译说明
        header = f"""---
原文链接: https://modal.com/gpu-glossary/{file_path.replace('.md', '').replace('readme', '')}
翻译状态: 待翻译
---

"""
        translated = header + translated
        
        return translated
    
    def update_links(self, content: str) -> str:
        """更新内部链接"""
        # 将 Modal 网站链接转换为本地链接
        content = re.sub(
            r'https://modal\.com/gpu-glossary/([^\)]+)',
            r'../\1.html',
            content
        )
        return content


def main():
    """主函数"""
    print("=" * 60)
    print("GPU Glossary 中文翻译工具")
    print("=" * 60)
    
    # 创建输出目录
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # 下载文件
    print("\n步骤 1: 下载 markdown 文件...")
    downloader = GitHubDownloader(GITHUB_RAW_BASE, GITHUB_API_BASE)
    files = downloader.download_all_markdown_files()
    
    print(f"\n共下载 {len(files)} 个文件")
    
    # 保存原始文件
    print("\n步骤 2: 保存文件...")
    for file_path, content in files.items():
        output_path = OUTPUT_DIR / file_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"保存: {output_path}")
    
    # 翻译（当前仅添加翻译标记）
    print("\n步骤 3: 准备翻译...")
    translator = MarkdownTranslator()
    
    translated_dir = OUTPUT_DIR.parent / "translated"
    translated_dir.mkdir(parents=True, exist_ok=True)
    
    for file_path, content in files.items():
        translated_content = translator.translate_content(content, file_path)
        output_path = translated_dir / file_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
    
    print("\n" + "=" * 60)
    print("完成！")
    print(f"原始文件保存在: {OUTPUT_DIR}")
    print(f"翻译文件保存在: {translated_dir}")
    print("=" * 60)
    
    # 生成文件清单
    print("\n文件清单:")
    for file_path in sorted(files.keys()):
        print(f"  - {file_path}")


if __name__ == "__main__":
    main()
