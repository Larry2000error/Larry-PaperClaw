# Daily Reports

最近三天日报（最新在前）：

# [20260810](./202608/20260810.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦跨视角地理定位与无人机视觉理解两大方向。前者致力于消除卫星-地面图像间的几何形变干扰，后者探索细粒度跨模态对齐技术。两项工作均体现特征空间学习与多源数据融合的持续深化趋势。

## ✨ 今日亮点

- 无变形跨视角地理定位：在特征空间共识挖掘替代传统几何校正
- 无人机细粒度理解：粒度感知区域对齐联合语义原型学习
- 中科院空天院主导无人机视觉-语言导航新框架

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260810] Warp-free Cross-view Geo-localization via Feature-space Consensus Mining | Song Zhuo, Xu Lian, Jiang Runqing, Zhang Yongjian, Li Kunhong, Zhang Ye, Guo Yulan | Sun Yat-sen University；The University of Western Australia | 中山大学团队提出特征空间共识挖掘方法，无需显式几何变形校正即可实现跨视角地理定位。 | [#411](https://github.com/Larry2000error/Larry-PaperClaw/issues/411) |
| [20260810] GRASP: Granularity-Aware Region Alignment and Semantic Prototype Learning for Fine-Grained Cross-Modal Understanding in Drone Views | Cui Jiahui, Zhao Yan, Wei Kan, Zhu Enze, Zhang Peirong, Wang Lei, Wang Yiru | Aerospace Information Research Institute, Chinese Academy of Sciences；Key Laboratory of Target Cognition and Application Technology (TCAT)；University of Chinese Academy of Sciences；School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences | 中科院空天院提出GRASP框架，通过粒度感知区域对齐与语义原型学习提升无人机细粒度跨模态理解能力。 | [#412](https://github.com/Larry2000error/Larry-PaperClaw/issues/412) |

## 🔎 观察

- 跨视角任务正从几何显式建模转向特征隐式对齐，降低对先验配准精度的依赖
- 无人机视觉-语言研究向细粒度区域级理解演进，支撑更复杂的导航与交互应用

---

Powered by OpenClaw🦞

---

# [20260808](./202608/20260808.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦跨视角地理定位的时序建模创新。SeqLoc突破单帧限制，针对特征稀疏场景提出序列聚合机制，结合测试时自适应技术提升定位鲁棒性，为卫星-地面图像匹配开辟新路径。

## ✨ 今日亮点

- SeqLoc提出序列聚合策略，解决特征稀疏场景下的跨视角定位难题
- 融合测试时自适应技术，增强模型对未知环境的泛化能力
- 基于OpenStreetMap构建验证框架，推动实际场景应用落地

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260808] SeqLoc: Beyond the Single Frame for Cross-View Geo-Localization in Feature-Sparse Scenes | Zheng Junwei, Huang Yun, Dai Ruize, Liu Ruiping, Chen Yufan, Peng Kunyu, Yang Kailun, Zhang Jiaming, Wang Guangming, Wysocki Olaf, Stiefelhagen Rainer | Karlsruhe Institute of Technology；Hunan University；University of Cambridge | SeqLoc通过序列聚合与测试时自适应，突破单帧限制，显著提升特征稀疏场景下的跨视角地理定位精度。 | [#408](https://github.com/Larry2000error/Larry-PaperClaw/issues/408) |

## 🔎 观察

- 时序信息利用正成为跨视角定位的新趋势，单帧方法面临性能瓶颈
- 测试时自适应与开放地图数据结合，或成提升模型泛化性的关键路径

---

Powered by OpenClaw🦞

---

# [20260807](./202608/20260807.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦于细粒度图像检索与跨模态重识别两大方向。前者针对执法场景中的刀具识别提出结构化局部表征方法，后者探索双空间模态一致性学习以实现通用跨模态匹配，均体现视觉理解任务向精细化、鲁棒化发展的趋势。

## ✨ 今日亮点

- KnifeHunter提出CoRe-Net网络，通过结构化局部表征提升刀具细粒度检索精度
- 双空间模态一致性学习框架，联合优化空间嵌入与频域特征实现跨模态统一
- 两研究分别面向执法取证与通用重识别场景，推动视觉检索技术实用化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260807] KnifeHunter: Structured Local Representation Learning for Fine-Grained Knife Image Retrieval in Law Enforcement | Syed Sameed Husain, Ong Eng-Jon, Simpson Stephen, Hamshere Trevor, Turner Matt, Bober Miroslaw | JOURNAL OF LATEX CLASS FILES | KnifeHunter提出结构化局部表征学习方法CoRe-Net，用于执法场景中的细粒度刀具图像检索与取证识别。 | [#405](https://github.com/Larry2000error/Larry-PaperClaw/issues/405) |
| [20260807] Dual-Space Modality Consistency Learning for Universal Cross-Modal Re-Identification | Zhao Yujian, Zhao Yukang, Liu Hankun, Xu Haoxuan, Li Bo, Wan Hanzi, Niu Guanglin | Harbin Institute of Technology | 提出双空间模态一致性学习框架，联合空间嵌入与频域特征实现通用跨模态重识别。 | [#406](https://github.com/Larry2000error/Larry-PaperClaw/issues/406) |

## 🔎 观察

- 细粒度检索与跨模态匹配正成为视觉识别核心挑战，局部结构与多域融合是关键技术路径
- 应用场景驱动明显：执法安全需求推动刀具识别研究，智能监控需求催生跨模态统一框架

---

Powered by OpenClaw🦞

---
