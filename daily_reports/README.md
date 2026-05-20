# Daily Reports

最近三天日报（最新在前）：

# [20260519](./202605/20260519.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域研究聚焦于视觉-语言模型的跨模态应用，特别是CLIP架构在遮挡场景下的行人重识别任务。研究者通过双提示学习与混合视觉编码器设计，探索提升模型对遮挡目标的鲁棒性表征能力，推动开放世界场景下的智能感知技术发展。

## ✨ 今日亮点

- 提出双提示CLIP架构，增强遮挡行人特征判别能力
- 混合视觉编码器设计，融合多尺度语义信息
- 提示学习机制优化，实现视觉-语言空间对齐

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260519] Dual-Prompt CLIP with Hybrid Visual Encoders for Occluded Person Re-Identification | Ji Zhangjian, Qiao Shaotong, Feng Kai, Wei Wei | School of Computer & Information Technology, Shanxi University；Key Laboratory of Computational Intelligence and Chinese Information Processing of Ministry of Education | 该研究提出双提示CLIP框架，结合混合视觉编码器解决遮挡行人重识别中的特征对齐与判别难题。 | [#207](https://github.com/Larry2000error/Larry-PaperClaw/issues/207) |

## 🔎 观察

- CLIP类预训练模型正加速向细粒度识别任务渗透，提示学习成为适配下游任务的关键技术路径
- 遮挡处理仍是行人重识别的核心挑战，混合编码器设计反映多尺度特征融合的持续演进趋势

---

Powered by OpenClaw🦞

---

# [20260518](./202605/20260518.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦于跨域视觉匹配与细粒度检索。电商场景下文本引导的隐式定位、空-地视角行人重识别、以及水产养殖中基于弱监督的鱼类再识别成为热点，体现视觉理解向实际应用落地的趋势。

## ✨ 今日亮点

- 快手提出TIGER-FG框架，实现电商图像的文本引导隐式细粒度定位检索
- 中山大学团队解决空-地跨视角行人重识别难题，提出视角感知语义对齐方法
- 挪威团队利用Patch集成与弱轨迹标签，实现养殖三文鱼的鲁棒再识别

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260518] TIGER-FG: Text-Guided Implicit Fine-Grained Grounding for E-commerce Retrieval | Sun Xinyu, Dai Huangyu, Mao Lingtao, Zheng Zexin, Liang Zihan, Chen Ben, Lei Chenyi, Ou Wenwu | Kuaishou Technology | TIGER-FG通过文本引导隐式学习，无需显式边界框即可实现电商图像的细粒度语义定位与检索。 | [#203](https://github.com/Larry2000error/Larry-PaperClaw/issues/203) |
| [20260518] View-Aware Semantic Alignment for Aerial-Ground Person Re-Identification | Zhang Quan, Cai Zeqiang, Zhao Peiming, Wu Jingze, Wu Cailun, Chen Hongbo, Lai Jianhuang | Sun Yat-sen University；Pazhou Lab (HuangPu)；Guangdong Province Key Laboratory of Information Security Technology；Key Laboratory of Machine Intelligence and Advanced Computing, Ministry of Education | View-Aware Semantic Alignment方法有效对齐无人机航拍与地面监控视角下的行人语义特征。 | [#204](https://github.com/Larry2000error/Larry-PaperClaw/issues/204) |
| [20260518] Patch Ensembles for Robust Salmon Re-Identification with Weak Trajectory Labels | Espen Uri Høgstedt, Schellewald Christian, Stahl Annette, Mester Rudolf | Department of Computer Science, Norwegian University of Science and Technology；SINTEF Ocean；Department of Engineering Cybernetics, Norwegian University of Science and Technology | Patch Ensembles结合弱轨迹监督，在标注受限条件下实现养殖环境中三文鱼的个体再识别。 | [#205](https://github.com/Larry2000error/Larry-PaperClaw/issues/205) |

## 🔎 观察

- 细粒度视觉理解正从显式标注向隐式学习演进，降低人工标注成本成为关键诉求。
- 农业水产等垂直场景的智能化需求推动计算机视觉技术向弱监督、低成本方向迁移。

---

Powered by OpenClaw🦞

---

# [20260515](./202605/20260515.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦自监督多模态表示学习，SOLAR框架通过联合学习优化对称多模态检索任务，采用对比学习实现图像-文本对齐，为遥感数据跨模态检索提供新思路。

## ✨ 今日亮点

- SOLAR提出自监督联合学习框架，统一处理对称多模态检索任务
- 采用对比学习机制优化图像-文本表征对齐效果
- 无需标注数据，降低遥感多模态应用的数据依赖门槛

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260515] SOLAR: Self-supervised Joint Learning for Symmetric Multimodal Retrieval | Yang Wenjie, Yu Hang, Guo Yuyu, Di Peng | Asymmetric Symmetric | SOLAR提出自监督联合学习框架，通过对称多模态检索优化图像-文本表征对齐，实现无需标注的遥感跨模态检索。 | [#200](https://github.com/Larry2000error/Larry-PaperClaw/issues/200) |

## 🔎 观察

- 自监督学习正成为降低遥感数据标注成本的主流技术路径
- 多模态检索的对称性设计或成提升跨模态一致性的关键方向

---

Powered by OpenClaw🦞

---
