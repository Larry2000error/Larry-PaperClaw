# Daily Reports

最近三天日报（最新在前）：

# [20260629](./202606/20260629.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦跨视角地理定位与低分辨率视觉理解两大方向。跨视角技术从2D匹配向3D几何感知演进，并拓展至行星表面探索场景；同时，跨分辨率语义迁移方法为监控场景下的文本-图像检索提供新思路，体现遥感AI向复杂环境适应的趋势。

## ✨ 今日亮点

- 单阶段几何感知框架统一跨视角目标定位，融合3D基础模型与多模态提示
- 跨分辨率语义迁移解决低分辨率监控场景下的文本-图像检索难题
- 行星表面跨视角定位方法将技术边界拓展至月球等地外环境

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260629] Beyond 2D Matching: A Unified Single-Stage Framework for Geometry-Aware Cross-View Object Geo-Localization | Wang Liyao, Wu Ruipu, Xu Haojun, Shi Lei, Huang Linjiang, Liu Si | Beihang University；Meituan | 提出统一单阶段框架，通过3D基础模型与几何感知机制实现跨视角目标地理定位，支持多模态提示输入。 | [#299](https://github.com/Larry2000error/Larry-PaperClaw/issues/299) |
| [20260629] Cross-Resolution Semantic Transfer for Robust Text-to-Image Retrieval in Low-Resolution Surveillance | Qian Wenjie, Yang Bin, Wang Xiao, Huang Wenke, Mei Ling, Xu Xin, Ye Mang | School of Computer Science and Technology, Wuhan University of Science and Technology；School of Computer Science, National Engineering Research Center for Multimedia Software, Wuhan University；Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System, Wuhan University of Science and Technology | 设计跨分辨率语义迁移策略，增强低分辨率监控视频中文本到图像检索的鲁棒性。 | [#300](https://github.com/Larry2000error/Larry-PaperClaw/issues/300) |
| [20260629] Learning Cross-view Correspondences for Geo-localization on Planetary Surfaces | Hong Minh Nguyen, Märtens Marcus, Chin Tat-Jun | Adelaide University | 面向行星表面探索场景，学习跨视角对应关系以实现月球等地外环境的视觉地理定位。 | [#301](https://github.com/Larry2000error/Larry-PaperClaw/issues/301) |

## 🔎 观察

- 跨视角定位技术正从地球场景向行星探测延伸，反映空间智能需求的增长
- 低分辨率与跨模态检索的结合显示监控AI对实际成像质量退化问题的关注

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
