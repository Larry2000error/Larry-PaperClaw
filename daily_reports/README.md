# Daily Reports

最近三天日报（最新在前）：

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

# [20260806](./202608/20260806.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦多模态检索的鲁棒性与持续学习能力。一方面，通过硬负样本与思维链机制提升检索失败案例的学习效率；另一方面，针对遥感图像-文本检索的增量场景，探索双适配器架构与排序感知蒸馏的结合，以缓解灾难性遗忘。

## ✨ 今日亮点

- 硬负样本驱动的检索中心思维链，统一多模态检索框架
- 双适配器架构服务遥感图像-文本持续检索任务
- 排序感知蒸馏机制缓解跨模态对齐中的知识遗忘

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260806] Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval | Sun Zelong, Wang Jun, Yang Kaicheng, Gu Tiancheng, Feng Ziyong, Lu Zhiwu | Glint Lab | 提出检索中心思维链方法，利用硬负样本构建失败感知反馈机制，增强多模态检索的统一性与鲁棒性。 | [#399](https://github.com/Larry2000error/Larry-PaperClaw/issues/399) |
| [20260806] DARAD: Dual Adapters and Ranking-Aware Distillation for Continual Remote Sensing Image-Text Retrieval | Chen Xi, Chen Xu, Jia Xiangyang, Wang Wei, Zhang Xu, Sun Zhenyuan | School of Computer Science, Wuhan University；Beijing Institute for General Artificial Intelligence (BIGAI) | 设计双适配器与排序感知蒸馏框架，解决遥感图像-文本检索在持续学习场景下的灾难性遗忘问题。 | [#400](https://github.com/Larry2000error/Larry-PaperClaw/issues/400) |

## 🔎 观察

- 遥感多模态检索正从静态任务转向动态持续学习，增量场景下的跨模态对齐稳定性成为关键瓶颈
- 硬负样本挖掘与思维链推理的结合，或为提升检索模型失败案例学习能力提供通用范式

---

Powered by OpenClaw🦞

---
