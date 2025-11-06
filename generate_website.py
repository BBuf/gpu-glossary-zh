#!/usr/bin/env python3
"""
生成 GPU Glossary 中文版静态网站
"""

import re
import markdown
from pathlib import Path
from typing import Dict, List, Tuple


class WebsiteGenerator:
    """静态网站生成器"""
    
    def __init__(self, input_dir: Path, output_dir: Path):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.nav_structure = self._build_nav_structure()
    
    def _build_nav_structure(self) -> List[Dict]:
        """构建导航结构"""
        return [
            {
                "title": "首页",
                "path": "readme",
                "children": []
            },
            {
                "title": "设备硬件",
                "path": "device-hardware",
                "children": [
                    {"title": "CUDA (设备架构)", "path": "device-hardware/cuda-device-architecture"},
                    {"title": "流式多处理器 (SM)", "path": "device-hardware/streaming-multiprocessor"},
                    {"title": "核心 (Core)", "path": "device-hardware/core"},
                    {"title": "特殊函数单元 (SFU)", "path": "device-hardware/special-function-unit"},
                    {"title": "加载/存储单元 (LSU)", "path": "device-hardware/load-store-unit"},
                    {"title": "Warp调度器", "path": "device-hardware/warp-scheduler"},
                    {"title": "CUDA核心", "path": "device-hardware/cuda-core"},
                    {"title": "Tensor核心", "path": "device-hardware/tensor-core"},
                    {"title": "Tensor内存加速器 (TMA)", "path": "device-hardware/tensor-memory-accelerator"},
                    {"title": "流式多处理器架构", "path": "device-hardware/streaming-multiprocessor-architecture"},
                    {"title": "纹理处理簇 (TPC)", "path": "device-hardware/texture-processing-cluster"},
                    {"title": "图形/GPU处理簇 (GPC)", "path": "device-hardware/graphics-processing-cluster"},
                    {"title": "寄存器文件", "path": "device-hardware/register-file"},
                    {"title": "L1数据缓存", "path": "device-hardware/l1-data-cache"},
                    {"title": "Tensor内存", "path": "device-hardware/tensor-memory"},
                    {"title": "GPU内存 (RAM)", "path": "device-hardware/gpu-ram"},
                ]
            },
            {
                "title": "设备软件",
                "path": "device-software",
                "children": [
                    {"title": "CUDA (编程模型)", "path": "device-software/cuda-programming-model"},
                    {"title": "流式汇编器 (SASS)", "path": "device-software/streaming-assembler"},
                    {"title": "并行线程执行 (PTX)", "path": "device-software/parallel-thread-execution"},
                    {"title": "计算能力", "path": "device-software/compute-capability"},
                    {"title": "线程 (Thread)", "path": "device-software/thread"},
                    {"title": "线程束 (Warp)", "path": "device-software/warp"},
                    {"title": "协作线程数组 (CTA)", "path": "device-software/cooperative-thread-array"},
                    {"title": "内核 (Kernel)", "path": "device-software/kernel"},
                    {"title": "线程块", "path": "device-software/thread-block"},
                    {"title": "线程块网格", "path": "device-software/thread-block-grid"},
                    {"title": "线程层次结构", "path": "device-software/thread-hierarchy"},
                    {"title": "内存层次结构", "path": "device-software/memory-hierarchy"},
                    {"title": "寄存器 (Registers)", "path": "device-software/registers"},
                    {"title": "共享内存", "path": "device-software/shared-memory"},
                    {"title": "全局内存", "path": "device-software/global-memory"},
                ]
            },
            {
                "title": "主机软件",
                "path": "host-software",
                "children": [
                    {"title": "CUDA (软件平台)", "path": "host-software/cuda-software-platform"},
                    {"title": "CUDA C++", "path": "host-software/cuda-c"},
                    {"title": "NVIDIA GPU 驱动", "path": "host-software/nvidia-gpu-drivers"},
                    {"title": "nvidia.ko", "path": "host-software/nvidia-ko"},
                    {"title": "CUDA 驱动 API", "path": "host-software/cuda-driver-api"},
                    {"title": "libcuda.so", "path": "host-software/libcuda"},
                    {"title": "NVIDIA 管理库 (NVML)", "path": "host-software/nvml"},
                    {"title": "libnvml.so", "path": "host-software/libnvml"},
                    {"title": "nvidia-smi", "path": "host-software/nvidia-smi"},
                    {"title": "CUDA 运行时 API", "path": "host-software/cuda-runtime-api"},
                    {"title": "libcudart.so", "path": "host-software/libcudart"},
                    {"title": "nvcc 编译器", "path": "host-software/nvcc"},
                    {"title": "NVRTC 运行时编译器", "path": "host-software/nvrtc"},
                    {"title": "CUPTI 性能分析接口", "path": "host-software/cupti"},
                    {"title": "Nsight Systems", "path": "host-software/nsight-systems"},
                    {"title": "CUDA 二进制工具", "path": "host-software/cuda-binary-utilities"},
                    {"title": "cuBLAS", "path": "host-software/cublas"},
                    {"title": "cuDNN", "path": "host-software/cudnn"},
                ]
            },
            {
                "title": "性能",
                "path": "perf",
                "children": [
                    {"title": "性能瓶颈", "path": "perf/performance-bottleneck"},
                    {"title": "屋顶线模型", "path": "perf/roofline-model"},
                    {"title": "计算受限", "path": "perf/compute-bound"},
                    {"title": "内存受限", "path": "perf/memory-bound"},
                    {"title": "算术强度", "path": "perf/arithmetic-intensity"},
                    {"title": "开销 (Overhead)", "path": "perf/overhead"},
                    {"title": "利特尔定律", "path": "perf/littles-law"},
                    {"title": "内存带宽", "path": "perf/memory-bandwidth"},
                    {"title": "算术带宽", "path": "perf/arithmetic-bandwidth"},
                    {"title": "延迟隐藏", "path": "perf/latency-hiding"},
                    {"title": "Warp执行状态", "path": "perf/warp-execution-state"},
                    {"title": "活跃周期", "path": "perf/active-cycle"},
                    {"title": "占用率 (Occupancy)", "path": "perf/occupancy"},
                    {"title": "流水线利用率", "path": "perf/pipe-utilization"},
                    {"title": "峰值速率", "path": "perf/peak-rate"},
                    {"title": "发射效率", "path": "perf/issue-efficiency"},
                    {"title": "SM利用率", "path": "perf/streaming-multiprocessor-utilization"},
                    {"title": "Warp分歧", "path": "perf/warp-divergence"},
                    {"title": "分支效率", "path": "perf/branch-efficiency"},
                    {"title": "内存合并", "path": "perf/memory-coalescing"},
                    {"title": "Bank冲突", "path": "perf/bank-conflict"},
                    {"title": "寄存器压力", "path": "perf/register-pressure"},
                ]
            },
        ]
    
    def _get_html_template(self, title: str, nav_html: str, content_html: str) -> str:
        """生成HTML模板"""
        return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GPU Glossary 中文版</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
            line-height: 1.6;
            color: #e0e0e0;
            background: #0d1117;
        }}
        
        .container {{
            display: flex;
            min-height: 100vh;
        }}
        
        .sidebar {{
            width: 280px;
            background: #161b22;
            border-right: 1px solid #30363d;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
            padding: 20px;
        }}
        
        .sidebar h1 {{
            color: #58a6ff;
            font-size: 1.5em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #30363d;
        }}
        
        .sidebar nav ul {{
            list-style: none;
        }}
        
        .sidebar nav > ul > li {{
            margin-bottom: 15px;
        }}
        
        .sidebar nav a {{
            color: #8b949e;
            text-decoration: none;
            display: block;
            padding: 5px 10px;
            border-radius: 6px;
            transition: all 0.2s;
        }}
        
        .sidebar nav a:hover {{
            background: #21262d;
            color: #58a6ff;
        }}
        
        .sidebar nav > ul > li > a {{
            font-weight: 600;
            color: #c9d1d9;
        }}
        
        .sidebar nav ul ul {{
            margin-left: 15px;
            margin-top: 5px;
        }}
        
        .sidebar nav ul ul li {{
            margin: 3px 0;
        }}
        
        .sidebar nav ul ul a {{
            font-size: 0.9em;
            padding: 3px 10px;
        }}
        
        .content {{
            flex: 1;
            margin-left: 280px;
            padding: 40px 60px;
            max-width: 900px;
        }}
        
        .content h1 {{
            color: #c9d1d9;
            font-size: 2.5em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #30363d;
        }}
        
        .content h2 {{
            color: #c9d1d9;
            font-size: 1.8em;
            margin-top: 30px;
            margin-bottom: 15px;
        }}
        
        .content h3 {{
            color: #c9d1d9;
            font-size: 1.3em;
            margin-top: 25px;
            margin-bottom: 10px;
        }}
        
        .content p {{
            margin-bottom: 15px;
            color: #c9d1d9;
        }}
        
        .content a {{
            color: #58a6ff;
            text-decoration: none;
        }}
        
        .content a:hover {{
            text-decoration: underline;
        }}
        
        .content code {{
            background: #161b22;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.9em;
            color: #79c0ff;
        }}
        
        .content pre {{
            background: #161b22;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            margin: 15px 0;
            border: 1px solid #30363d;
        }}
        
        .content pre code {{
            background: none;
            padding: 0;
            color: #c9d1d9;
        }}
        
        .content ul, .content ol {{
            margin-left: 25px;
            margin-bottom: 15px;
        }}
        
        .content li {{
            margin-bottom: 8px;
        }}
        
        .content blockquote {{
            border-left: 4px solid #58a6ff;
            padding-left: 15px;
            margin: 15px 0;
            color: #8b949e;
            font-style: italic;
        }}
        
        .content table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        
        .content th, .content td {{
            border: 1px solid #30363d;
            padding: 10px;
            text-align: left;
        }}
        
        .content th {{
            background: #161b22;
            font-weight: 600;
        }}
        
        .meta-info {{
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 15px;
            margin-bottom: 30px;
            font-size: 0.9em;
            color: #8b949e;
        }}
        
        .footer {{
            margin-top: 60px;
            padding-top: 20px;
            border-top: 1px solid #30363d;
            text-align: center;
            color: #8b949e;
            font-size: 0.9em;
        }}
        
        @media (max-width: 768px) {{
            .sidebar {{
                width: 100%;
                position: relative;
                height: auto;
                border-right: none;
                border-bottom: 1px solid #30363d;
            }}
            
            .content {{
                margin-left: 0;
                padding: 20px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <aside class="sidebar">
            <h1>GPU Glossary</h1>
            <p style="color: #8b949e; font-size: 0.9em; margin-bottom: 20px;">中文版</p>
            <nav>
                {nav_html}
            </nav>
        </aside>
        
        <main class="content">
            {content_html}
            
            <div class="footer">
                <p>原项目: <a href="https://modal.com/gpu-glossary" target="_blank">Modal GPU Glossary</a></p>
                <p>GitHub: <a href="https://github.com/modal-labs/gpu-glossary" target="_blank">modal-labs/gpu-glossary</a></p>
            </div>
        </main>
    </div>
</body>
</html>"""
    
    def _generate_nav_html(self, current_path: str = "") -> str:
        """生成导航HTML"""
        html = ["<ul>"]
        
        for item in self.nav_structure:
            path = item['path']
            title = item['title']
            is_current = (path == current_path)
            
            if item.get('children'):
                html.append(f'<li>')
                html.append(f'<a href="{path}.html">{title}</a>')
                html.append('<ul>')
                
                for child in item['children']:
                    child_path = child['path']
                    child_title = child['title']
                    is_child_current = (child_path == current_path)
                    style = ' style="color: #58a6ff; font-weight: bold;"' if is_child_current else ''
                    html.append(f'<li><a href="../{child_path}.html"{style}>{child_title}</a></li>')
                
                html.append('</ul>')
                html.append('</li>')
            else:
                style = ' style="color: #58a6ff; font-weight: bold;"' if is_current else ''
                html.append(f'<li><a href="{path}.html"{style}>{title}</a></li>')
        
        html.append("</ul>")
        return '\n'.join(html)
    
    def _markdown_to_html(self, md_content: str, current_file: Path) -> str:
        """将Markdown转换为HTML"""
        # 移除元信息注释
        md_content = re.sub(r'<!--.*?-->', '', md_content, flags=re.DOTALL)
        
        # 转换Markdown
        md = markdown.Markdown(extensions=[
            'extra',
            'codehilite',
            'toc',
            'tables',
            'fenced_code'
        ])
        
        html = md.convert(md_content)
        
        # 修复链接：将 /gpu-glossary/ 开头的链接转换为相对路径
        # 例如：/gpu-glossary/device-hardware/xxx -> ../device-hardware/xxx.html 或 device-hardware/xxx.html
        def fix_link(match):
            original_url = match.group(1)
            
            # 只处理 /gpu-glossary/ 开头的链接
            if original_url.startswith('/gpu-glossary/'):
                # 移除 /gpu-glossary/ 前缀
                relative_path = original_url.replace('/gpu-glossary/', '')
                
                # 计算当前文件的深度
                current_depth = len(current_file.relative_to(self.input_dir).parts) - 1
                
                # 添加 ../ 前缀
                if current_depth > 0:
                    prefix = '../' * current_depth
                    fixed_url = prefix + relative_path + '.html'
                else:
                    fixed_url = relative_path + '.html'
                
                return f'href="{fixed_url}"'
            
            return match.group(0)
        
        # 替换所有 href="/gpu-glossary/..." 的链接
        html = re.sub(r'href="(/gpu-glossary/[^"]+)"', fix_link, html)
        
        return html
    
    def generate_page(self, md_file: Path, html_file: Path):
        """生成单个HTML页面"""
        # 读取Markdown
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # 提取标题
        title_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
        title = title_match.group(1) if title_match else md_file.stem
        
        # 转换为HTML（传入当前文件路径用于修复链接）
        content_html = self._markdown_to_html(md_content, md_file)
        
        # 计算相对路径用于导航
        rel_path = md_file.relative_to(self.input_dir).with_suffix('')
        path_str = str(rel_path).replace('\\', '/')
        
        # 生成导航
        nav_html = self._generate_nav_html(path_str)
        
        # 生成完整HTML
        full_html = self._get_html_template(title, nav_html, content_html)
        
        # 保存
        html_file.parent.mkdir(parents=True, exist_ok=True)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(full_html)
        
        print(f"✓ 生成: {html_file.relative_to(self.output_dir)}")
    
    def generate_all(self):
        """生成所有页面"""
        md_files = list(self.input_dir.rglob("*.md"))
        print(f"\n找到 {len(md_files)} 个Markdown文件\n")
        
        for md_file in md_files:
            rel_path = md_file.relative_to(self.input_dir)
            html_file = self.output_dir / rel_path.with_suffix('.html')
            
            self.generate_page(md_file, html_file)
        
        # 创建index.html重定向到readme.html
        index_html = self.output_dir / "index.html"
        with open(index_html, 'w', encoding='utf-8') as f:
            f.write("""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=readme.html">
    <title>GPU Glossary 中文版</title>
</head>
<body>
    <p>跳转中... <a href="readme.html">点击这里</a></p>
</body>
</html>""")
        
        print(f"\n✓ 完成! 网站已生成到: {self.output_dir}")
        print(f"  打开 {index_html} 查看")


def main():
    """主函数"""
    print("=" * 60)
    print("GPU Glossary 网站生成器")
    print("=" * 60)
    
    script_dir = Path(__file__).parent
    input_dir = script_dir / "translated"
    output_dir = script_dir / "website"
    
    if not input_dir.exists():
        print(f"\n错误: 翻译文件目录不存在: {input_dir}")
        print("请先运行翻译脚本")
        return
    
    generator = WebsiteGenerator(input_dir, output_dir)
    generator.generate_all()


if __name__ == "__main__":
    main()
