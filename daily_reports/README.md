# Daily Reports

最近三天日报（最新在前）：

# [20260422](./202604/20260422.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦跨模态检索与组合式视觉检索两大方向。武汉大学与BIGAI团队提出两阶段跨模态检索框架，山东大学与哈工深则针对噪声问题与零样本场景展开攻关，显示该领域正从单一模态对齐向复杂场景鲁棒性演进。

## ✨ 今日亮点

- Fast-then-Fine框架实现粗到细的多粒度跨模态对齐
- ConeSep网络通过锥形结构解决硬噪声对应学习难题
- UniCVR首次统一零样本组合图像与视频检索任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260422] Fast-then-Fine: A Two-Stage Framework with Multi-Granular Representation for Cross-Modal Retrieval in Remote Sensing | Chen Xi, Chen Xu, Jia Xiangyang, Zhang Xu, Wei Shuquan, Wang Wei | Wuhan University；Beijing Institute for General Artificial Intelligence (BIGAI) | Fast-then-Fine采用快速粗筛与精细对齐两阶段策略，提升遥感图像-文本检索效率与精度。 | [#18](https://github.com/Larry2000error/Larry-PaperClaw/issues/18) |
| [20260422] ConeSep: Cone-based Robust Noise-Unlearning Compositional Network for Composed Image Retrieval | Li Zixu, Hu Yupeng, Chen Zhiwei, Zhang Mingyu, Fu Zhiheng, Nie Liqiang | Shandong University；Harbin Institute of Technology (Shenzhen) | ConeSep提出锥形噪声遗忘网络，专门处理组合图像检索中的噪声三元组对应问题。 | [#19](https://github.com/Larry2000error/Larry-PaperClaw/issues/19) |
| [20260422] UniCVR: From Alignment to Reranking for Unified Zero-Shot Composed Visual Retrieval | Wen Haokun, Song Xuemeng, Zhang Haoyu, Zhao Xiangyu, Guan Weili, Nie Liqiang | Harbin Institute of Technology (Shenzhen)；Southern University of Science and Technology；City University of Hong Kong；Pengcheng Laboratory | UniCVR基于多模态大语言模型，实现零样本组合视觉检索从对齐到重排序的统一框架。 | [#20](https://github.com/Larry2000error/Larry-PaperClaw/issues/20) |

## 🔎 观察

- 组合式检索成为热点，三篇中有两篇聚焦该任务，反映用户对精细化视觉搜索需求上升。
- 噪声鲁棒性与零样本能力成关键挑战，显示实际部署中数据质量与泛化性瓶颈亟待突破。

---

Powered by OpenClaw🦞

---

# [20260421](./202604/20260421.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦多模态智能与推理增强范式。组合图像检索领域探索知识内化与噪声标签鲁棒性，行人重识别引入强化推理与思维链机制，体现视觉任务向认知推理深度演进趋势。

## ✨ 今日亮点

- Air-Know提出仲裁校准知识内化网络，解决组合图像检索中噪声标签与知识融合难题
- Thinking Before Matching首创强化推理范式，以思维链机制提升行人重识别泛化能力
- 多模态大模型与强化学习成为视觉理解任务的关键赋能技术

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260421] Air-Know: Arbiter-Calibrated Knowledge-Internalizing Robust Network for Composed Image Retrieval | Fu Zhiheng, Hu Yupeng, Yang Qianyun, Zhang Shiqi, Chen Zhiwei, Li Zixu | Shandong University | Air-Know通过仲裁器校准机制实现知识内化，构建噪声鲁棒的组合图像检索网络。 | [#1](https://github.com/Larry2000error/Larry-PaperClaw/issues/1) |
| [20260421] Thinking Before Matching: A Reinforcement Reasoning Paradigm Towards General Person Re-Identification | Zhang Quan, Wu Jingze, Wang Jialong, Xie Xiaohua, Lai Jianhuang, Chen Hongbo | Sun Yat-sen University；Alibaba Cloud Computing | Thinking Before Matching将强化学习与思维链结合，使模型在匹配前进行身份推理。 | [#2](https://github.com/Larry2000error/Larry-PaperClaw/issues/2) |

## 🔎 观察

- 视觉检索任务正从特征匹配向认知推理跃迁，思维链与强化学习成为新范式
- 噪声标签学习与知识内化结合，反映实际应用场景对模型鲁棒性的迫切需求

---

Powered by OpenClaw🦞

---

# [20260420](./202604/20260420.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦于组合检索任务的鲁棒性提升，山东大学团队连续贡献三项工作，覆盖图像与视频跨模态场景。核心趋势为噪声抑制与渐进学习：通过不变表示学习、证据驱动校准等机制，解决查询-目标对齐中的干扰问题，推动检索系统向复杂真实场景适配。

## ✨ 今日亮点

- 组合检索噪声抑制：INTENT提出不变性与判别性联合优化框架
- 渐进学习新范式：HABIT构建时序协同的鲁棒训练机制
- 视频检索突破：ReTrack以证据驱动实现双流方向锚点校准

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260420] INTENT: Invariance and Discrimination-aware Noise Mitigation for Robust Composed Image Retrieval | Chen Zhiwei, Hu Yupeng, Fu Zhiheng, Li Zixu, Huang Jiale, Huang Qinlei, Wei Yinwei | School of Software, Shandong University | INTENT针对组合图像检索中的噪声干扰，联合优化不变表示与判别性学习以增强鲁棒性。 | [#4](https://github.com/Larry2000error/Larry-PaperClaw/issues/4) |
| [20260420] HABIT: Chrono-Synergia Robust Progressive Learning Framework for Composed Image Retrieval | Li Zixu, Hu Yupeng, Chen Zhiwei, Zhang Shiqi, Huang Qinlei, Fu Zhiheng, Wei Yinwei | School of Software, Shandong University | HABIT提出时序协同的渐进学习框架，提升组合图像检索在多模态噪声下的训练稳定性。 | [#5](https://github.com/Larry2000error/Larry-PaperClaw/issues/5) |
| [20260420] ReTrack: Evidence-Driven Dual-Stream Directional Anchor Calibration Network for Composed Video Retrieval | Li Zixu, Hu Yupeng, Chen Zhiwei, Huang Qinlei, Qiu Guozhi, Fu Zhiheng, Liu Meng | School of Software, Shandong University；School of Computer Science and Technology, Shandong Jianzhu University | ReTrack面向组合视频检索，以证据驱动双网络流实现方向锚点动态校准。 | [#6](https://github.com/Larry2000error/Larry-PaperClaw/issues/6) |

## 🔎 观察

- 同一团队同日三连发，显示组合检索已成为跨模态学习的热点攻坚方向，噪声鲁棒性成关键瓶颈。
- 从图像到视频的范式延伸表明，动态时序建模与静态空间对齐的技术融合需求正在凸显。

---

Powered by OpenClaw🦞

---
