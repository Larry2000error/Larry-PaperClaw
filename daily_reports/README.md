# Daily Reports

最近三天日报（最新在前）：

# [20260519](./202605/20260519.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI领域研究聚焦于视觉-语言模型与3D点云理解两大方向。CLIP架构持续演进，通过双提示学习与混合编码器提升遮挡场景下的行人重识别性能；同时，2D-3D跨模态对齐取得进展，Tango3D在全局检索与局部密集匹配上实现统一，为3D基础模型发展提供新思路。

## ✨ 今日亮点

- CLIP双提示机制结合混合视觉编码器，有效缓解遮挡行人重识别中的特征混淆问题
- Tango3D提出全局-局部联合对齐框架，突破2D-3D对应关系中尺度不一致的瓶颈
- 高校与产业界协同创新，腾讯混元团队参与3D基础模型关键技术攻关

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260519] Dual-Prompt CLIP with Hybrid Visual Encoders for Occluded Person Re-Identification | Ji Zhangjian, Qiao Shaotong, Feng Kai, Wei Wei | School of Computer & Information Technology, Shanxi University；Key Laboratory of Computational Intelligence and Chinese Information Processing of Ministry of Education | 山西大学团队提出双提示CLIP架构，以混合视觉编码器与可学习提示优化遮挡行人重识别，实现视觉-语言特征协同对齐。 | [#207](https://github.com/Larry2000error/Larry-PaperClaw/issues/207) |
| [20260519] Tango3D: Towards Alignment for Global and Local 2D-3D Correspondence | He Zebin, Yang Mingxin, Yang Shuhui, Sun Hanxiao, Han Xintong, Guo Chunchao, Luo Wenhan | HKUST；Tencent Hunyuan | 港科大与腾讯混元联合发布Tango3D，通过全局-局部联合对齐机制统一2D-3D对应任务，提升点云理解与跨模态检索性能。 | [#209](https://github.com/Larry2000error/Larry-PaperClaw/issues/209) |

## 🔎 观察

- 提示学习正成为CLIP下游适配的主流范式，但双提示设计对计算开销的影响需进一步验证
- 2D-3D对齐从分离式走向统一框架，或加速3D基础模型在开放场景中的实用化部署

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
