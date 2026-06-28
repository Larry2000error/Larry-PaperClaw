# Daily Reports

最近三天日报（最新在前）：

# [20260624](./202606/20260624.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦无人机定位与导航技术，ETH Zurich等机构提出OrthoTrack系统，创新性地将公开正射影像作为定位锚点，实现连续六自由度轨迹估计。该方法突破传统SLAM依赖局部建图的局限，为低成本无人机导航提供新思路。

## ✨ 今日亮点

- OrthoTrack以公开正射影像为全局锚点，解决无人机定位漂移问题
- 实现连续6-DoF位姿估计，无需昂贵传感器或预先构建地图
- 融合SLAM与视觉里程计，拓展无人机在GNSS拒止环境应用

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260624] OrthoTrack: Continuous 6-DoF UAV Trajectory Estimation Anchored in Public Orthophotos | Dhaouadi Oussema, Bauer Zuria, Johannes Michael Meier, Wysocki Olaf, Pollefeys Marc, Cremers Daniel | ETH Zurich；TU Munich；University of Cambridge；MCML；Microsoft | ETH Zurich等提出OrthoTrack，利用公开正射影像实现无人机连续六自由度轨迹估计，为低成本高精度导航提供新方案。 | [#288](https://github.com/Larry2000error/Larry-PaperClaw/issues/288) |

## 🔎 观察

- 正射影像作为先验地图的利用方式，可能推动众包地理数据在机器人定位中的价值重估
- 该方法对影像更新时效性和分辨率存在隐性依赖，实际部署需权衡成本与精度

---

Powered by OpenClaw🦞

---

# [20260623](./202606/20260623.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦视觉位置识别（VPR）在特殊场景的应用拓展。上海交大联合多家航运机构提出ProteusVPR，针对海上感知与舱室检测的跨场景定位难题，融合几何与视觉信息，推动自主航运机器人从开放水域向封闭舱室的作业能力升级。

## ✨ 今日亮点

- 跨场景VPR新框架，打通海上与舱室两种极端环境
- 产学研深度融合，航运巨头与高校联合攻关
- 几何-视觉融合策略，应对 Maritime 领域光照与结构挑战

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260623] From Open Waters to Enclosed Cabins: ProteusVPR for Cross-Scene Visual Place Recognition in Maritime Perception and Cabin Inspection | Chena Zexi, Huang Zitai, Gu Qiwen, Li Zhiqi, Dong Shengli, Wang Chenlei, Zhao Junqiao, Wang Hongdong, Han Bing | Shanghai Jiaotong University；COSCO SHIPPING Advanced Technology Institute；Shanghai Ship and Shipping Research Institute Co.LTD；Tongji University；Dalian Maritime University | ProteusVPR提出跨场景视觉位置识别方法，解决海上开放水域与封闭舱室间的定位迁移难题，支持自主船舶感知与舱室巡检。 | [#285](https://github.com/Larry2000error/Larry-PaperClaw/issues/285) |

## 🔎 观察

- VPR技术正从城市自动驾驶向垂直工业场景渗透，海事领域成为新蓝海
- 航运企业与高校联合研发模式凸显，行业数据壁垒或成关键竞争要素

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
