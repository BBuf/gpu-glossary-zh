# GPU Glossary 中文版

这是 [Modal GPU Glossary](https://modal.com/gpu-glossary) 的中文翻译项目。

## 📖 在线访问

**中文版网站**: https://bbuf.github.io/gpu-glossary-zh/

## ℹ️ 原项目信息

- **原始网站**: https://modal.com/gpu-glossary
- **GitHub 仓库**: https://github.com/modal-labs/gpu-glossary
- **许可证**: MIT License

## 📁 项目结构

```
gpu-glossary-zh/
├── .github/workflows/           # GitHub Actions 配置
│   └── deploy.yml              # 自动部署到 GitHub Pages
├── download_and_translate.py   # 下载原始 Markdown 文件
├── translate_with_ai.py         # 使用 AI 翻译（SiliconFlow API）
├── generate_website.py          # 生成静态网站
├── requirements.txt             # Python 依赖
├── content/                     # 原始 Markdown 文件
├── translated/                  # 翻译后的 Markdown 文件
└── website/                     # 生成的 HTML 网站（GitHub Actions 自动生成）
```

## 🚀 使用方法

### 1. 克隆仓库

```bash
git clone https://github.com/BBuf/gpu-glossary-zh.git
cd gpu-glossary-zh
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 下载原始文件（可选）

如果需要重新下载原始文件：

```bash
python download_and_translate.py
```

这会从 GitHub 下载所有 markdown 文件到 `content/` 目录。

### 4. 翻译文件（可选）

> **⚠️ 注意**: 翻译需要 API Key，仓库中已包含翻译后的文件，通常不需要重新翻译。

如需重新翻译，首先设置 SiliconFlow API Key:

```bash
export SILICONFLOW_API_KEY='your-api-key-here'
```

然后运行翻译脚本:

```bash
python translate_with_ai.py
```

翻译后的文件会保存到 `translated/` 目录。

**注意**: 翻译会调用 SiliconFlow API，可能产生费用。

### 5. 生成 HTML 网站

#### 生成本地测试版本（推荐）

```bash
python generate_website_local.py
```

这会生成不带 GitHub Pages base path 的版本，适合本地测试。

#### 生成 GitHub Pages 版本

```bash
python generate_website.py
```

这会生成带有 `/gpu-glossary-zh/` base path 的版本，适合 GitHub Pages 部署。

生成的静态网站会保存到 `website/` 目录。

### 6. 查看网站

启动本地服务器:

```bash
cd website
python -m http.server 8000
```

然后访问 http://localhost:8000

> **注意**: 如果使用 `generate_website.py` 生成的版本，本地查看时导航链接会失效，这是正常的，因为它是为 GitHub Pages 优化的。使用 `generate_website_local.py` 生成本地测试版本即可。

## 🌐 GitHub Pages 部署

本项目使用 GitHub Actions 自动部署到 GitHub Pages。

### 部署步骤

1. **Fork 或推送到你的仓库**
2. **启用 GitHub Pages**:
   - 进入仓库 Settings → Pages
   - Source 选择 "GitHub Actions"
3. **推送代码到 main 分支**，GitHub Actions 会自动:
   - 运行 `generate_website.py` 生成网站
   - 部署到 GitHub Pages

### 手动触发部署

在 Actions 标签页中，选择 "部署 GPU Glossary 中文版到 GitHub Pages"，点击 "Run workflow"。

## 📝 翻译说明

### 翻译技术栈

- **翻译 API**: SiliconFlow API
- **翻译模型**: DeepSeek-V3
- **文档格式**: Markdown
- **网站生成**: Python + markdown 库

### 术语翻译规范

为保持术语一致性，主要技术术语翻译如下：

| 英文 | 中文 | 缩写 |
|------|------|------|
| Streaming Multiprocessor | 流式多处理器 | SM |
| Warp | 线程束 | - |
| Thread Block | 线程块 | - |
| Kernel | 内核 | - |
| Compute Capability | 计算能力 | - |
| Register | 寄存器 | - |
| Shared Memory | 共享内存 | - |
| Global Memory | 全局内存 | - |
| Occupancy | 占用率 | - |
| Latency Hiding | 延迟隐藏 | - |
| Special Function Unit | 特殊函数单元 | SFU |
| Load/Store Unit | 加载/存储单元 | LSU |
| Tensor Core | Tensor核心 | - |
| CUDA Core | CUDA核心 | - |

### 翻译原则

1. **准确性**: 保持技术概念的准确性
2. **一致性**: 相同术语使用相同翻译
3. **可读性**: 符合中文技术文档习惯
4. **保留**: 代码、API名称、命令等保持英文
5. **首次说明**: 专业术语首次出现时使用"中文 (English)"格式

## 自定义配置

### 使用不同的翻译API

编辑 `translate_with_ai.py`，修改API配置:

```python
translator = AITranslator(
    api_key="your-api-key",
    base_url="https://your-api-endpoint.com/v1"  # 可选
)
```

### 调整翻译模型

在 `translate_with_ai.py` 中修改模型参数:

```python
"model": "gpt-4",  # 或 gpt-4-turbo, gpt-3.5-turbo
"temperature": 0.3,  # 降低随机性
```

### 自定义网站样式

编辑 `generate_website.py` 中的CSS样式部分。

## 离线翻译

如果不想使用AI翻译或没有API Key，可以:

1. 运行 `download_and_translate.py` 下载原始文件
2. 手动翻译 `content/` 目录中的文件
3. 将翻译结果放到 `translated/` 目录
4. 运行 `generate_website.py` 生成网站

## 批量翻译建议

翻译整个项目可能需要较多API调用。建议:

1. **测试**: 先翻译几个文件测试效果
2. **成本**: 估算API调用成本（约100+个文件）
3. **限流**: 脚本中已添加延迟避免限流
4. **检查**: 翻译完成后检查质量
5. **备份**: 保留原始文件以便重新翻译

## 贡献

欢迎提交Issue和Pull Request改进翻译质量！

## 许可证

本翻译项目遵循原项目的MIT许可证。

## 致谢

感谢 [Modal Labs](https://modal.com) 创建了这个优秀的GPU文档资源！
