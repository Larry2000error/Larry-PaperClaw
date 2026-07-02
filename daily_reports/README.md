# Daily Reports

最近三天日报（最新在前）：

# [20260624](./202606/20260624.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦于无人机位姿估计与视觉定位技术。ETH Zurich等机构提出OrthoTrack框架，利用公开正射影像实现连续六自由度轨迹估计，将传统SLAM与地理参考正射影像结合，为低成本无人机导航提供新思路，体现了视觉里程计向大规模、低成本方向发展的趋势。

## ✨ 今日亮点

- OrthoTrack首创以公开正射影像为锚点的6-DoF无人机轨迹估计框架
- 融合视觉里程计与地理参考影像，无需昂贵GNSS设备即可实现连续定位
- ETH Zurich、TUM、剑桥等多机构合作，代码已开源

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260624] OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos | Dhaouadi Oussema, Bauer Zuria, Johannes Michael Meier, Wysocki Olaf, Pollefeys Marc, Cremers Daniel | ETH Zurich；TU Munich；University of Cambridge；MCML；Microsoft | OrthoTrack提出以公开正射影像为锚点的连续6-DoF无人机轨迹估计方法，实现低成本高精度视觉定位。 | [#288](https://github.com/Larry2000error/Larry-PaperClaw/issues/288) |

## 🔎 观察

- 正射影像作为先验地图的利用方式，可能降低无人机导航对RTK-GNSS的依赖
- SLAM与地理空间数据融合正成为视觉定位领域的重要技术路线

---

Powered by OpenClaw🦞

---

# [20260623](./202606/20260623.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦跨场景视觉定位技术，上海交大联合多家机构提出ProteusVPR框架，针对船舶自主巡检中开放水域与封闭舱室的极端环境差异，融合几何-视觉特征实现鲁棒场景识别，推动海事机器人感知技术向实用化迈进。

## ✨ 今日亮点

- ProteusVPR实现水域到舱室的跨场景视觉定位，突破海事环境感知瓶颈
- 融合几何与视觉特征，解决开放与封闭空间的表征差异难题
- 产学研深度合作，上海交大联合中远海运等机构推动技术落地

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260623] From Open Waters to Enclosed Cabins: ProteusVPR for Cross-Scene Visual Place Recognition in Maritime Perception and Cabin Inspection | Chena Zexi, Huang Zitai, Gu Qiwen, Li Zhiqi, Dong Shengli, Wang Chenlei, Zhao Junqiao, Wang Hongdong, Han Bing | Shanghai Jiaotong University；COSCO SHIPPING Advanced Technology Institute；Shanghai Ship and Shipping Research Institute Co.LTD；Tongji University；Dalian Maritime University | ProteusVPR提出几何-视觉融合框架，实现开放水域至封闭舱室的跨场景视觉定位，支撑船舶自主巡检应用。 | [#285](https://github.com/Larry2000error/Larry-PaperClaw/issues/285) |

## 🔎 观察

- 海事场景视觉定位长期受限于环境剧烈变化，该工作通过多模态融合为行业提供可迁移的技术范式
- 产学研链条完整，体现国内智能船舶领域从算法创新到产业应用的加速闭环

---

Powered by OpenClaw🦞

---

# [20260622](./202606/20260622.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦视觉-语言模型的几何表征优化与隐私保护行人重识别。双曲几何被引入CLIP架构以改善否定语义理解，而Transformer结合匈牙利算法则在深度时序序列中实现隐私感知的人员匹配，体现多模态学习与隐私计算的交叉趋势。

## ✨ 今日亮点

- HANCLIP将双曲几何引入CLIP，通过角否定机制提升视觉-语言模型的否定理解能力
- 基于Transformer与匈牙利优化的隐私保护行人重识别，利用深度时序序列避免敏感生物特征暴露
- 两项研究均关注表征空间的结构优化，分别从几何性质与隐私约束角度拓展基础模型能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260622] HANCLIP: A Family of Hyperbolic Angular Negation Vision Language Models | Le Hoang-Bao, Durrant Aiden, Thai Son Mai, Binh T. Nguyen, Zhou Liting, Gurrin Cathal | ADAPT Centre；Dublin City University；University of East Anglia；Queen's University Belfast；University of Science；Vietnam National University | HANCLIP提出双曲角否定视觉-语言模型家族，通过双曲空间中的角否定机制改进CLIP的否定语义理解能力。 | [#282](https://github.com/Larry2000error/Larry-PaperClaw/issues/282) |
| [20260622] Privacy-Preserving Person Re-Identification from Temporal Sequences with Transformer and Hungarian Optimization | Delécluse Raphaël, Wannous Hazem, Guimas Laurent | IMT Nord Europe, University of Lille, CNRS UMR 9189 - CRIStAL；Explain | 该研究结合Transformer与匈牙利算法，从深度时序序列中实现隐私保护的人员重识别，避免使用可识别的RGB图像。 | [#283](https://github.com/Larry2000error/Larry-PaperClaw/issues/283) |

## 🔎 观察

- 视觉-语言模型正从欧氏空间向双曲等替代几何空间扩展，以更好捕捉层次化与否定语义结构
- 行人重识别领域出现从RGB向深度模态迁移的趋势，隐私保护需求驱动传感器与算法的协同创新

---

Powered by OpenClaw🦞

---
