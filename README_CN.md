# PetEcho 🐾

**宠物情感镜像**

> 你与毛孩子的每一个瞬间，都在诉说一个故事。PetEcho 倾听、理解、回应。

PetEcho 是一款 AI 驱动的情感陪伴工具，把你与宠物日常相处的点滴，转化为深度的情感洞察。不同于记录步数和热量的健康追踪器，PetEcho 关注真正重要的事——你与毛孩子之间的情感纽带。

## ✨ 功能特点

### 💭 情感智能
分享任何日常片段——一个古怪的行为、一个温柔的时刻、一个意外的笑料——PetEcho 会解读其中的情感脉络，帮你理解宠物真正在想什么。

### 📊 每周情感报告
AI 自动生成的周报，梳理你家宝贝的情绪变化轨迹、你们共度的难忘瞬间，以及加强情感连接的实用建议。

### 🎭 情绪标签
为每一次记录添加情绪标签。看久了，你会发现自己宠物情绪世界的规律，也让你们的关系被好好留存。

### 🔒 隐私优先
- 数据仅存储在你的设备上
- 无需注册账号
- 无追踪、不贩卖数据
- 设备ID隔离存储

## 🚀 快速开始

### 环境要求
- Python 3.8+
- OpenAI API Key

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/yourusername/pet-echo.git
cd pet-echo

# 安装依赖
pip install -r requirements.txt

# 配置 API Key
cp .env.example .env
# 编辑 .env 文件，填入你的 OpenAI API Key：
# OPENAI_API_KEY=sk-your-key-here
```

### 运行

```bash
python app.py
```

在浏览器中打开 [http://localhost:5000](http://localhost:5000)

### 环境变量说明

| 变量 | 说明 | 必须 |
|------|------|------|
| `OPENAI_API_KEY` | 你的 OpenAI API Key | 是 |
| `SECRET_KEY` | Flask 会话密钥 | 否（使用默认值）|
| `PORT` | 服务端口（默认：5000）| 否 |
| `FLASK_ENV` | 设为 `development` 开启调试模式 | 否 |

## 🏗️ 项目结构

```
pet-echo/
├── app.py              # Flask 主应用
├── prompts.py          # AI 情感分析提示词
├── requirements.txt   # Python 依赖
├── templates/
│   └── index.html     # 前端界面
├── static/            # 静态资源（CSS、JS、图片）
└── data/
    └── sample_entries.json  # 示例数据（仅供参考）
```

## 🎨 工作原理

1. **分享瞬间**：写下你与宠物的任何互动——一次散步、一个拥抱、一个意外的笑料
2. **AI 分析**：PetEcho 的情感智能从你的叙述中提取行为模式、情绪信号和情感连接指标
3. **获得洞察**：收到温暖、实用的洞察，了解宠物的情绪状态和你们的关系
4. **持续记录**：建立宠物日记合集，看着你们宝贝的情绪旅程慢慢展开

## 💡 产品理念

我们相信，关于你的宠物最重要的数据，不是步数，也不是热量——而是你们共度时光的品质。

PetEcho 的核心理念：**宠物主人本身就是最好的情感数据来源**。你的观察、你的叙述、你的感受，比任何传感器读数都更有价值。

这是一种全新的宠物科技：始于情感，而非硬件。

## 🔧 API 接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/` | GET | 首页 |
| `/api/journal` | POST | 创建新的日记条目 |
| `/api/journal/<device_id>` | GET | 获取设备的所有日记 |
| `/api/journal/<device_id>/weekly-summary` | GET | 获取 AI 周报 |
| `/api/moods` | GET | 获取可选的情绪标签 |

## 🌐 部署指南

### Docker 部署

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### Railway / Render / Fly.io

在部署平台的环境变量设置中配置 `OPENAI_API_KEY`，然后直接部署即可。

## 📖 相关文档

- [English Documentation](README.md)
- [中文文档](README_CN.md) ← 你在这里

## 🤝 参与贡献

欢迎提交 Pull Request！

## 📄 开源协议

MIT License - 可自由使用、修改和分发。

---

**用 💕 为每一位相信"毛孩子值得被理解"的宠物家长而作。**
