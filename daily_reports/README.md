# Daily Reports

最近三天日报（最新在前）：

# [20260630](./202606/20260630.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦无人机智能应用与跨模态视觉理解两大方向。UAV技术涵盖野生动物追踪与地理定位，体现从感知到决策的自主化升级；视觉-语言模型研究则关注检索效率与零样本推理能力，通过哈希对齐与策略规划降低数据依赖。

## ✨ 今日亮点

- 无人机自主导航实现野生动物个体重识别，结合YOLOv11提升追踪精度
- 无监督跨模态哈希检索通过全局-邻域对齐降低标注需求
- 零样本组合图像检索引入策略规划与自我批评机制增强鲁棒性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260630] Autonomous UAV Navigation for Individual Wildlife Re-Identification | Sun Claire, Berger-Wolf Tanya, Kline Jenna | The Ohio State University | 提出自主无人机导航系统，基于YOLOv11实现野生动物个体重识别，支持野外动态追踪任务。 | [#304](https://github.com/Larry2000error/Larry-PaperClaw/issues/304) |
| [20260630] Unsupervised Data-Efficient Cross-Modal Retrieval with Global-Neighborhood Alignment Hashing | Li Runhao, Ma Xiaoxu, Weng Zhenyu, Zhang Yue, Luo Guibo, Zhuang Huiping, Lin Zhiping, Tan Yap-Peng | School of Electrical and Electronic Engineering, Nanyang Technological University；Shien-Ming Wu School of Intelligent Engineering, South China University of Technology；College of Computer and Information Engineering, Henan Normal University；Guangdong Provincial Key Laboratory of Ultra High Definition Immersive Media Technology, Peking University Shenzhen Graduate School；VinUniversity | 设计无监督全局-邻域对齐哈希方法，以少量数据实现高效跨模态检索，无需配对标注。 | [#305](https://github.com/Larry2000error/Larry-PaperClaw/issues/305) |
| [20260630] Thinking Before Retrieving: Robust Zero-Shot Composed Image Retrieval via Strategic Planning and Self-Criticism | Jung Gunho, Park Jeong-Woo, Seon Bin Kim, Lee Seong-Whan | Department of Artificial Intelligence, Korea University | 引入策略规划与自我批评机制，通过多阶段推理提升零样本组合图像检索的鲁棒性。 | [#307](https://github.com/Larry2000error/Larry-PaperClaw/issues/307) |
| [20260630] PiLoT v2: Pixel-to-Orthogonal Map Alignment for Free-view UAV Geo-localization | Liu Xinyi, Cheng Xiaoya, Wu Rouwan, Wang Zhaochen, Yan Shen, Zhang Maojun, Liu Yu | National University of Defense Technology | PiLoT v2实现像素到正射影像对齐，利用神经配准解决无人机自由视角地理定位问题。 | [#308](https://github.com/Larry2000error/Larry-PaperClaw/issues/308) |

## 🔎 观察

- 无人机研究从单一遥感感知向自主决策闭环演进，野生动物保护场景成为技术验证热点
- 视觉-语言检索研究呈现效率与泛化并重趋势，无监督与零样本方法持续压缩人工标注成本

---

Powered by OpenClaw🦞

---

# [20260629](./202606/20260629.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦跨视角地理定位技术突破，涵盖地球与行星表面场景。北航与美团团队提出单阶段几何感知框架，突破传统2D匹配局限；阿德莱德大学将跨视角定位拓展至月球等行星表面；武汉科大等则关注低分辨率监控场景下的文本-图像检索，体现技术向极端条件与实用化延伸的趋势。

## ✨ 今日亮点

- 单阶段几何感知框架统一跨视角目标定位，融合3D基础模型与多模态提示
- 跨视角地理定位技术首次系统应用于行星表面探索，拓展月球等地外场景
- 低分辨率监控场景下实现跨分辨率语义迁移，提升文本-图像检索鲁棒性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260629] Beyond 2D Matching: A Unified Single-Stage Framework for Geometry-Aware Cross-View Object Geo-Localization | Wang Liyao, Wu Ruipu, Xu Haojun, Shi Lei, Huang Linjiang, Liu Si | Beihang University；Meituan | 北航与美团提出单阶段几何感知框架，通过3D基础模型与多模态提示实现跨视角目标地理定位，超越传统2D匹配范式。 | [#299](https://github.com/Larry2000error/Larry-PaperClaw/issues/299) |
| [20260629] Cross-Resolution Semantic Transfer for Robust Text-to-Image Retrieval in Low-Resolution Surveillance | Qian Wenjie, Yang Bin, Wang Xiao, Huang Wenke, Mei Ling, Xu Xin, Ye Mang | School of Computer Science and Technology, Wuhan University of Science and Technology；School of Computer Science, National Engineering Research Center for Multimedia Software, Wuhan University；Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System, Wuhan University of Science and Technology | 武汉科大等提出跨分辨率语义迁移方法，解决低分辨率监控场景下文本-图像检索的语义鸿沟问题。 | [#300](https://github.com/Larry2000error/Larry-PaperClaw/issues/300) |
| [20260629] Learning Cross-view Correspondences for Geo-localization on Planetary Surfaces | Hong Minh Nguyen, Märtens Marcus, Chin Tat-Jun | Adelaide University | 阿德莱德大学开发行星表面跨视角地理定位方法，针对月球等地外环境建立俯视与透视图像对应关系。 | [#301](https://github.com/Larry2000error/Larry-PaperClaw/issues/301) |

## 🔎 观察

- 跨视角定位正从地球场景向行星探测延伸，反映空间智能技术的战略拓展需求
- 单阶段统一框架取代多阶段流水线，显示遥感AI模型向高效端到端架构演进

---

Powered by OpenClaw🦞

---

# [20260624](./202606/20260624.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录一篇研究，聚焦无人机轨迹估计与正射影像融合。该工作将SLAM/视觉里程计与公开正射影像结合，实现6自由度连续位姿估计，体现遥感与机器人导航交叉趋势，强调低成本高精度定位方案。

## ✨ 今日亮点

- 正射影像锚定：利用公开正射影像作为全局参考，解决无人机定位漂移问题
- 6-DoF连续估计：实现完整位姿轨迹重建，兼顾精度与计算效率
- 跨机构合作：ETH、TUM、剑桥、微软等多单位联合，产学研结合

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260624] OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos | Dhaouadi Oussema, Bauer Zuria, Johannes Michael Meier, Wysocki Olaf, Pollefeys Marc, Cremers Daniel | ETH Zurich；TU Munich；University of Cambridge；MCML；Microsoft | OrthoTrack提出以公开正射影像为锚点的无人机6-DoF连续轨迹估计方法，融合视觉里程计与地理参考影像实现全局一致定位。 | [#288](https://github.com/Larry2000error/Larry-PaperClaw/issues/288) |

## 🔎 观察

- 正射影像作为先验地图的利用方式，可能降低无人机测绘对GNSS的依赖，拓展拒止环境应用
- 单一论文收录反映当日遥感AI领域产出稀疏，或存在预印本平台数据抓取延迟

---

Powered by OpenClaw🦞

---
