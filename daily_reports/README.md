# Daily Reports

最近三天日报（最新在前）：

# [20260514](./202605/20260514.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦跨模态学习的基础性问题。无人机地理定位领域探索利用免费道路地图作为几何先验，提升天气不变性定位能力；图像检索领域则对多模态组合基准测试提出质疑，揭示单模态捷径可能削弱评估有效性。两项研究均关注模型设计的本质合理性与实际可靠性。

## ✨ 今日亮点

- GeoFuse框架融合道路地图几何先验，实现天气鲁棒的无人机跨视角定位
- CIR基准测试分析发现多模态组合非必需，单模态捷径普遍存在
- 跨模态学习研究趋向审视方法本质，而非单纯追求性能提升

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260514] Road Maps as Free Geometric Priors: Weather-Invariant Drone Geo-Localization with GeoFuse | Fang Yunsong, Wang Tingyu, Zheng Zhedong | University of Macau；Hangzhou Dianzi University | GeoFuse提出利用免费道路地图作为几何先验，通过跨模态融合实现天气不变的无人机地理定位，降低对卫星图的依赖。 | [#197](https://github.com/Larry2000error/Larry-PaperClaw/issues/197) |
| [20260514] Do Composed Image Retrieval Benchmarks Require Multimodal Composition? | Attimonelli Matteo, Alessandro De Bellis, Aryo Pradipta Gema, Saxena Rohit, Sekoyan Monica, Kwan Wai-Chung, Pomo Claudio, Suglia Alessandro, Jannach Dietmar, Tommaso Di Noia, Minervini Pasquale | Politecnico di Bari；Sapienza University of Rome；University of Edinburgh；University of Klagenfurt；Miniml.AI | 研究质疑组合图像检索基准的必要性，发现现有数据集存在单模态捷径，多模态组合未必提升检索效果。 | [#198](https://github.com/Larry2000error/Larry-PaperClaw/issues/198) |

## 🔎 观察

- 遥感定位研究正从'数据驱动'转向'知识引导'，利用开放地理数据降低标注成本值得持续关注
- 多模态学习领域出现反思浪潮，基准测试的严谨性设计将直接影响方法创新的方向与价值

---

Powered by OpenClaw🦞

---

# [20260513](./202605/20260513.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域研究聚焦于图像语义理解的上下文依赖性，东京都立大学与CyberAgent合作探索图像检索中语义抽象与叙事语境的关联，推动多模态嵌入技术向更精细的语义层次发展。

## ✨ 今日亮点

- 上下文依赖图像检索突破传统语义匹配局限
- 多模态嵌入融合叙事语境实现动态语义抽象
- 同一图像多义性研究拓展视觉理解新维度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260513] Same Image, Different Meanings: Toward Retrieval of Context-Dependent Meanings | Tsutsumi Ayuto, Kohita Ryosuke | Tokyo Metropolitan University；CyberAgent | 该研究提出上下文依赖的图像检索框架，通过语义抽象与叙事语境建模，解决同一图像在不同场景下的多义性表达问题。 | [#195](https://github.com/Larry2000error/Larry-PaperClaw/issues/195) |

## 🔎 观察

- 图像多义性研究标志着视觉AI从静态识别向动态语境理解的范式转变
- 产学研合作模式加速多模态技术从实验室向内容推荐等场景落地

---

Powered by OpenClaw🦞

---

# [20260512](./202605/20260512.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦多模态模型的鲁棒性与泛化能力。视觉语言模型的持续学习、跨视角地理定位的天气鲁棒性，以及多图像检索中的位置偏置问题成为核心议题，体现领域对复杂场景适应性与可信度的关注。

## ✨ 今日亮点

- 弹性权重整合增强跨模态知识保持，缓解视觉语言模型灾难性遗忘
- 原型学习驱动的语义部件发现提升天气鲁棒跨视角地理定位性能
- 注意力引导的Logit校准策略有效抑制多图像检索中的位置偏置

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260512] Lifelong Learning in Vision-Language Models: Enhanced EWC with Cross-Modal Knowledge Retention | Hamza Ahmed Durrani, Rafay Suleman Durrani | Sejong University；Technische Universität Ilmenau | 提出增强型EWC方法，通过跨模态知识保持机制实现视觉语言模型的终身学习，缓解灾难性遗忘问题。 | [#191](https://github.com/Larry2000error/Larry-PaperClaw/issues/191) |
| [20260512] Weather-Robust Cross-View Geo-Localization via Prototype-Based Semantic Part Discovery | Tran Chi-Nguyen, Dao Sy Duy Minh, Huynh Trung Kiet, Nguyen Lam Phu Quy, Pham Phu-Hoa, Tran-Thanh Long | University of Warwick | 基于原型学习的语义部件发现框架，增强跨视角地理定位模型在恶劣天气条件下的鲁棒性表现。 | [#192](https://github.com/Larry2000error/Larry-PaperClaw/issues/192) |
| [20260512] Logit-Attention Divergence: Mitigating Position Bias in Multi-Image Retrieval via Attention-Guided Calibration | Xian Mingtao, Yang Yifeng, Gu Qinying, Wang Xinbing, Ye Nanyang | Tsinghua University；Chinese Academy of Sciences | 揭示多图像检索中的位置偏置现象，设计Logit-注意力散度校准方法提升跨模态检索公平性。 | [#193](https://github.com/Larry2000error/Larry-PaperClaw/issues/193) |

## 🔎 观察

- 多模态大模型的实际部署需求推动终身学习与鲁棒性研究并行发展，技术路线从单一性能优化转向可持续演进。
- 注意力机制的可解释性正被转化为显式优化目标，位置偏置等隐蔽问题开始获得系统性关注与矫正。

---

Powered by OpenClaw🦞

---
