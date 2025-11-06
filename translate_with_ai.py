#!/usr/bin/env python3
"""
GPU Glossary AI 翻译工具
使用 SiliconFlow API (DeepSeek-V3) 进行专业翻译
"""

import os
import time
from pathlib import Path
import requests


class AITranslator:
    """使用 SiliconFlow AI 进行翻译"""
    
    def __init__(self):
        """
        初始化翻译器，使用 SiliconFlow API
        """
        # 从环境变量读取 API Key，确保安全
        self.api_key = os.getenv("SILICONFLOW_API_KEY")
        if not self.api_key:
            raise ValueError(
                "未找到 SILICONFLOW_API_KEY 环境变量。\n"
                "请设置环境变量: export SILICONFLOW_API_KEY='your-api-key'"
            )
        self.base_url = "https://api.siliconflow.cn/v1"
        self.model = "Pro/deepseek-ai/DeepSeek-V3"
    
    def translate_markdown(self, content: str, context: str = "") -> str:
        """
        翻译 Markdown 内容
        
        Args:
            content: 要翻译的内容
            context: 上下文信息（文件路径等）
        
        Returns:
            翻译后的内容
        """
        system_prompt = """你是一位专业的技术文档翻译专家，特别擅长 GPU、CUDA 和并行计算相关的技术文档翻译。

翻译要求：
1. 保持 Markdown 格式完整，包括标题、链接、代码块等
2. 专业术语保持一致性，常见术语如下：
   - Streaming Multiprocessor → 流式多处理器 (SM)
   - Warp → 线程束
   - Thread Block → 线程块
   - Kernel → 内核
   - Compute Capability → 计算能力
   - Register → 寄存器
   - Shared Memory → 共享内存
   - Global Memory → 全局内存
   - Occupancy → 占用率
   - Latency Hiding → 延迟隐藏
   
3. 首次出现专业术语时，使用"中文翻译 (English)"格式
4. 代码、命令、API名称等保持英文不翻译
5. 链接地址不翻译，但链接文本要翻译
6. 保持技术准确性，不要过度意译
7. 语言要通顺自然，符合中文技术文档习惯
8. 保留所有的换行和段落结构

请直接返回翻译后的 Markdown 内容，不要添加任何解释。"""

        user_prompt = f"""请将以下 GPU Glossary 的 Markdown 文档翻译成中文：

{context}

---

{content}"""

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    "temperature": 0.3
                },
                timeout=120
            )
            
            response.raise_for_status()
            result = response.json()
            translated = result['choices'][0]['message']['content']
            return translated
            
        except Exception as e:
            print(f"翻译错误: {e}")
            print(f"响应内容: {response.text if 'response' in locals() else '无'}")
            return content
    
    def translate_file(self, file_path: Path, output_path: Path, context: str = "") -> bool:
        """
        翻译单个文件
        
        Args:
            file_path: 输入文件路径
            output_path: 输出文件路径
            context: 上下文信息
        
        Returns:
            是否成功
        """
        try:
            # 读取原文
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 翻译
            print(f"正在翻译: {file_path.name}")
            translated = self.translate_markdown(content, context)
            
            # 添加元信息
            header = f"""<!--
原文: {context}
翻译时间: {time.strftime('%Y-%m-%d %H:%M:%S')}
-->

"""
            translated = header + translated
            
            # 保存
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(translated)
            
            print(f"✓ 已保存: {output_path}")
            return True
            
        except Exception as e:
            print(f"✗ 处理文件失败 {file_path}: {e}")
            return False


def translate_directory(input_dir: Path, output_dir: Path, translator: AITranslator):
    """
    翻译整个目录
    
    Args:
        input_dir: 输入目录（包含原始markdown文件）
        output_dir: 输出目录
        translator: 翻译器实例
    """
    md_files = list(input_dir.rglob("*.md"))
    total = len(md_files)
    
    print(f"\n找到 {total} 个 Markdown 文件")
    print("=" * 60)
    
    success_count = 0
    
    for i, file_path in enumerate(md_files, 1):
        # 计算相对路径
        rel_path = file_path.relative_to(input_dir)
        output_path = output_dir / rel_path
        
        # 生成上下文信息
        github_path = str(rel_path).replace('\\', '/')
        context = f"文件路径: gpu-glossary/{github_path}"
        
        print(f"\n[{i}/{total}] {rel_path}")
        
        # 翻译
        if translator.translate_file(file_path, output_path, context):
            success_count += 1
        
        # 避免API限流
        if i < total:
            time.sleep(2)
    
    print("\n" + "=" * 60)
    print(f"完成! 成功翻译 {success_count}/{total} 个文件")
    print("=" * 60)


def main():
    """主函数"""
    print("=" * 60)
    print("GPU Glossary AI 翻译工具")
    print("使用 SiliconFlow API (DeepSeek-V3.2-Exp)")
    print("=" * 60)
    
    # 配置路径
    script_dir = Path(__file__).parent
    input_dir = script_dir / "content"
    output_dir = script_dir / "translated"
    
    # 检查输入目录
    if not input_dir.exists():
        print(f"\n错误: 输入目录不存在: {input_dir}")
        print("请先运行 download_and_translate.py 下载原始文件")
        return
    
    # 创建翻译器
    translator = AITranslator()
    
    # 翻译
    translate_directory(input_dir, output_dir, translator)
    
    print(f"\n翻译文件保存在: {output_dir}")


if __name__ == "__main__":
    main()
