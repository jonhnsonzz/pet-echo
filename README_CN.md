[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

# PetEcho 🐾 — 宠物异常助手

**"宠物不对劲了，是不是该立刻去医院？还是再观察一下？"**

> 凌晨2点，猫拉稀了。你不确定是紧急情况还是可以在家观察。上网搜，出来的全是宠物医院的广告。PetEcho 告诉你：可能是什么原因、什么时候该就医、在家可以观察什么。

[English Version](README.md)

---

## 😰 你是不是遇到过这些情况

- 宠物拉稀/呕吐了，但精神还行——该不该半夜冲医院？
- 猫狗突然不爱吃饭——是挑食还是真的不舒服？
- 半夜宠物出状况，宠物医院关门了——你能做点什么？
- 想去医院但怕被宰，想观察又怕拖严重了

**PetEcho 就是为这些时刻设计的——帮你做一个更有信息的判断。**

## ✨ 功能

- **症状评估** — 描述宠物情况，给出严重程度判断
- **居家护理指导** — 在家可以做什么、观察什么、什么时候必须就医
- **趋势追踪** — 持续记录，让异常模式清晰可见
- **减少焦虑** — 不是所有突发状况都需要半夜跑急诊

## 📱 适用设备

手机浏览器即可使用——**微信、Chrome、Safari** 均支持。不需要下载 App，不需要注册账号。

## 🔒 隐私保护

- 数据仅存储在**你的设备本地**，不上传到任何服务器
- 不需要手机号、邮箱、账号
- 不追踪、不贩卖数据

---

## 🚀 快速开始

### 环境要求

- Python 3.8+
- OpenAI API Key

### 安装

```bash
git clone https://github.com/jonhnsonzz/pet-echo.git
cd pet-echo
pip install -r requirements.txt
```

### 配置

```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 OpenAI API Key
# OPENAI_API_KEY=你的密钥
```

### 运行

```bash
python app.py
```

手机浏览器打开 `http://localhost:5000` 即可使用。

---

## 📂 项目结构

```
pet-echo/
├── app.py              # Flask 主应用
├── prompts.py          # AI 分析提示词
├── requirements.txt    # Python 依赖
├── templates/
│   └── index.html     # 前端界面（手机适配）
└── data/
    └── sample_entries.json  # 示例数据
```

---

## 💡 产品理念

你才是宠物最好的观察者——你每天都和它在一起，你最了解它正常的样子。

你缺的不是一个医学专家，而是一座**连接你的观察和正确判断的桥**。

PetEcho 不是医疗器械，不能替代兽医。它的作用是：**在你犹豫要不要去医院的时候，帮你做一个更有信息的决定。**

---

## 🤝 参与贡献

欢迎提交 Issue 或 Pull Request！

## 📄 许可证

MIT License — 可自由使用，包括商用。

---

**为爱宠操心的你设计的。** 🐶🐱
