# 更新日志

## [1.0.0] - 2025-11-06

### ✨ 新增功能

- 🌐 完成 Modal GPU Glossary 全部 77 个页面的中文翻译
- 🚀 使用 SiliconFlow API (DeepSeek-V3) 进行高质量 AI 翻译
- 📱 响应式网站设计，支持桌面和移动端访问
- 🔗 修复所有内部链接，支持正确的页面跳转
- 🤖 GitHub Actions 自动部署到 GitHub Pages
- 🎨 暗色主题界面，符合开发者阅读习惯

### 🔧 技术实现

- **翻译引擎**: SiliconFlow API + DeepSeek-V3 模型
- **文档格式**: Markdown → HTML
- **静态网站生成**: Python + markdown 库
- **自动部署**: GitHub Actions
- **链接处理**: 自动转换 `/gpu-glossary/` 路径为相对路径

### 📝 翻译特色

- ✅ 专业术语保持一致性
- ✅ 首次出现术语使用"中文 (English)"格式
- ✅ 代码和 API 名称保持英文
- ✅ 保留原文 Markdown 格式和结构
- ✅ 77/77 文件翻译完成率 100%

### 🔒 安全改进

- 🔐 移除代码中的硬编码 API Key
- 🔐 使用环境变量管理敏感信息
- 🔐 提供 `.env.example` 配置示例
- 🔐 `.gitignore` 忽略敏感文件

### 📦 文件结构

```
gpu-glossary-zh/
├── .github/workflows/deploy.yml  # GitHub Actions 配置
├── .gitignore                    # Git 忽略规则
├── .env.example                  # 环境变量示例
├── LICENSE                       # MIT 许可证
├── README.md                     # 项目说明
├── CHANGELOG.md                  # 更新日志
├── requirements.txt              # Python 依赖
├── download_and_translate.py     # 下载脚本
├── translate_with_ai.py          # 翻译脚本（安全版本）
├── generate_website.py           # 网站生成（修复链接）
├── content/                      # 原始 Markdown
├── translated/                   # 中文翻译
└── website/                      # 生成的网站（自动生成）
```

### 🌟 主要贡献者

- 翻译：DeepSeek-V3 AI 模型
- 项目维护：BBuf

### 📚 相关链接

- 在线访问: https://bbuf.github.io/gpu-glossary-zh/
- GitHub 仓库: https://github.com/BBuf/gpu-glossary-zh
- 原始项目: https://github.com/modal-labs/gpu-glossary
