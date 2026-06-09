# Daily Reports

最近三天日报（最新在前）：

# [20260606](./202606/20260606.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究呈现跨模态智能与时空图神经网络两大主线。GeoGNN聚焦时序地理定位，通过双塔图神经网络融合时空表征；IMAGINE则探索自适应图式-意象增强的组合视频检索，推动跨模态语义对齐技术发展。

## ✨ 今日亮点

- GeoGNN提出双塔图神经网络架构，实现时序数据与地理空间的联合嵌入学习
- IMAGINE创新引入图式-意象增强机制，提升组合视频检索的语义理解能力
- 两研究分别来自Emory-橡树岭-南加大联盟与山东大学团队，体现产学研协同

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260606] GeoGNN: Time Series Geo-Localization using Two-Tower Graph Neural Networks | Tran Toan, Abebe Waqwoya, Potnis Abhishek, Chinthavali Supriya, Shahabi Cyrus, Xiong Li, Lunga Dalton | Emory University；Oak Ridge National Laboratory；University of Southern California | GeoGNN构建双塔图神经网络，联合学习时序数据的空间嵌入与时间表示，用于精确地理定位任务。 | [#253](https://github.com/Larry2000error/Larry-PaperClaw/issues/253) |
| [20260606] IMAGINE: Adaptive Schema-Imagery Enhanced Composition for Composed Video Retrieval | Huang Jiale, Li Zixu, Chen Zhiwei, Fu Zhiheng, Wang Chunxiao, Hu Yupeng | Shandong University；Qilu University of Technology (Shandong Academy of Sciences) | IMAGINE提出自适应图式-意象增强组合框架，通过多模态原型学习实现复杂视频语义检索。 | [#254](https://github.com/Larry2000error/Larry-PaperClaw/issues/254) |

## 🔎 观察

- 图神经网络正成为遥感时空建模的核心工具，双塔架构设计或成地理定位新范式
- 跨模态检索从简单对齐迈向深层语义组合，图式认知理论的引入值得关注

---

Powered by OpenClaw🦞

---

# [20260605](./202606/20260605.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI相关研究聚焦于视觉感知与智能检索两大方向。多目标跟踪领域探索外观特征与3D点云融合的新范式；零样本图像检索则致力于构建更真实的跨模态基准测试体系，推动视觉语言模型的泛化能力评估。

## ✨ 今日亮点

- 3D多行人跟踪中系统验证外观特征对重识别任务的增益效果
- 构建首个真实零样本组合图像检索基准，解决训练-测试数据泄露问题
- 基于视频源的一致性数据集设计，提升跨模态检索评估可靠性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260605] Does Appearance Help? A Systematic Study of Image-Based Re-Identification in Online 3D Multi-Pedestrian Tracking | Borges Eduardo, Garrote Luís, Urbano J. Nunes | Institution unavailable | 该研究系统评估了图像外观特征在在线3D多行人跟踪重识别任务中的作用，为LiDAR与视觉融合策略提供实证依据。 | [#250](https://github.com/Larry2000error/Larry-PaperClaw/issues/250) |
| [20260605] Never Seen Before: Benchmarking Genuine Zero-Shot Composed Image Retrieval with Consistent Video-Sourced Datasets | Yang Zhenyu, Du Zemin, Qian Shengsheng, Xu Changsheng | Institution unavailable | 论文提出全新零样本组合图像检索基准，通过视频源数据集构建避免训练测试重叠，更真实反映模型泛化性能。 | [#251](https://github.com/Larry2000error/Larry-PaperClaw/issues/251) |

## 🔎 观察

- 多模态融合正从简单特征拼接转向系统性的增益量化分析，方法论趋于严谨
- 零样本学习领域开始正视基准测试的数据泄露隐患，数据集构建范式面临革新

---

Powered by OpenClaw🦞

---

# [20260604](./202606/20260604.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究呈现两大趋势：一是跨视角地理定位向非城市环境拓展，融合度量-语义原语匹配实现无GNSS导航；二是多模态大语言模型的可解释性研究，通过识别核心注意力头揭示功能稀疏性机制。两项工作分别从机器人定位鲁棒性与模型内部机理层面推进技术边界。

## ✨ 今日亮点

- Meridian提出度量-语义原语匹配框架，突破城市环境限制实现空地跨视角定位
- CoRe Heads机制揭示多模态LLM功能稀疏性，为模型压缩与效率优化提供新思路
- MIT与丰田研究院合作推动无GNSS导航技术，拓展地面机器人野外作业能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260604] Meridian: Metric-Semantic Primitive Matching for Cross-View Geo-Localization Beyond Urban Environments | Peterson Mason, Li Qingyuan, Jia Yixuan, Cladera Fernando, Nieto-Granda Carlos, Camillo Jose Taylor, Jonathan P. How | Massachusetts Institute of Technology；University of Pennsylvania；Toyota Research Institute | Meridian通过度量-语义原语匹配，将跨视角地理定位从城市拓展至野外等非结构化环境，支持无GNSS条件下的地面机器人定位。 | [#247](https://github.com/Larry2000error/Larry-PaperClaw/issues/247) |
| [20260604] Mechanistic Insights into Functional Sparsity in Multimodal LLMs via CoRe Heads | Sun Ruoxi, Qiu Quantong, Li Juntao, Tang Zecheng, Lou Yihang, Zhang Min | Soochow University；Peking University | 该研究提出CoRe Heads识别多模态LLM中承担跨模态检索的核心注意力头，揭示功能稀疏性机制并验证其可解释性价值。 | [#248](https://github.com/Larry2000error/Larry-PaperClaw/issues/248) |

## 🔎 观察

- 跨视角定位从城市向野外延伸，反映自动驾驶与野外机器人对无GNSS导航的迫切需求，语义-几何联合表征成为关键突破口。
- 多模态LLM可解释性研究从现象描述走向机制定位，核心子结构识别为模型轻量化与可信部署提供工程化路径。

---

Powered by OpenClaw🦞

---
