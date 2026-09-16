# Daily Reports

最近三天日报（最新在前）：

# [20260913](./202609/20260913.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦多模态安全与高效推理两大方向。ViTeGate揭示视觉-语言检索增强生成中的知识投毒攻击风险，而多相机行人重识别框架则探索生成式AI与早退级联结合的低延迟方案。两者分别关注VLM的安全漏洞与实时性能优化，体现该领域攻防并进的发展态势。

## ✨ 今日亮点

- ViTeGate首次针对VLM检索增强生成场景设计视觉-文本触发式知识投毒攻击
- 多相机行人重识别框架整合生成式AI与早退级联机制实现低延迟推理
- 两篇论文均涉及视觉-语言模型，分别聚焦安全性与效率优化两个维度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260913] ViTeGate: Visual-Textual Triggered Knowledge Poisoning for Vision-Language Retrieval-Augmented Generation | Tan Xue, Zeng Xuandi, Shao Yu, Fang Zhongli, Luo Mingyu, Sun Xiaoyan, Chen Ping, Dai Jun | Fudan University；Guangdong University of Technology；Worcester Polytechnic Institute | ViTeGate提出视觉-文本触发知识投毒方法，揭示VLM检索增强生成系统在多模态对抗攻击下的安全漏洞。 | [#499](https://github.com/Larry2000error/Larry-PaperClaw/issues/499) |
| [20260913] A Generative AI Integrated Multimodal Framework for Low-Latency Multi-Camera Person Re-Identification | Fernando Leon, Dombawala C, Hettigoda P., Vanodhya G. Warnasooriya, Neranjana Ishara, Nawaratne Rashmika | University of Moratuwa；Zone24x7 (Pvt) Ltd；Chulalongkorn University；University of Colombo；La Trobe University | 该框架融合生成式AI与早退级联架构，构建面向多相机场景的低开销行人重识别系统。 | [#500](https://github.com/Larry2000error/Larry-PaperClaw/issues/500) |

## 🔎 观察

- VLM安全研究从传统对抗样本向检索增强生成等复杂场景延伸，知识投毒成为新兴威胁向量。
- 生成式AI与早退机制的跨架构整合，反映边缘实时应用对效率与精度的双重诉求。

---

Powered by OpenClaw🦞

---

# [20260907](./202609/20260907.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态文档智能与水下声学感知两大方向。文档理解领域呈现检索效率与长上下文建模并重的趋势，两篇工作分别从能力路由检索和查询感知令牌预算切入优化视觉文档问答与检索系统。水下声学识别则探索开放集场景下的船舶再识别，采用原始波形与选择性核注意力机制提升鲁棒性。

## ✨ 今日亮点

- 能力路由视觉检索与证据链构建，突破长文档问答的上下文瓶颈
- 原始波形选择性核网络SKANN，实现开放集水下船舶噪声再识别
- 查询感知令牌预算策略，优化Late-Interaction视觉文档检索效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260907] Capability-Routed Visual Retrieval and Evidence Threading for Long-Context Document Question Answering | Rahman Amirul, Karim Aisha, Nakamura Kenji, Ng Yi-Fan | University of Malaya | 提出能力路由视觉检索与证据线索方法，通过动态能力分配与视觉证据链构建处理长文档问答中的多模态长上下文挑战。 | [#492](https://github.com/Larry2000error/Larry-PaperClaw/issues/492) |
| [20260907] Open-Set Vessel Re-Identification from Underwater Ship-Radiated Noise with a Raw-Waveform Selective-Kernel Acoustic Neural Network (SKANN) and a Cross-Passage Evaluation Protocol | Tyagi Sunil | Institution unavailable | 设计原始波形选择性核声学神经网络SKANN，建立跨航道评估协议，解决开放集场景下水下船舶辐射噪声的再识别问题。 | [#493](https://github.com/Larry2000error/Larry-PaperClaw/issues/493) |
| [20260907] Query-Aware Token Budgeting for Efficient Late-Interaction Visual Document Retrieval | Rishi PS, Rajeev Ranjan Dwivedi, Vinod K Kurmi | Indian Institute of Science Education and Research Bhopal | 引入查询感知令牌预算机制，在Late-Interaction视觉文档检索中动态分配计算资源，平衡检索精度与推理效率。 | [#494](https://github.com/Larry2000error/Larry-PaperClaw/issues/494) |

## 🔎 观察

- Late-Interaction架构（如ColBERT系列）正成为视觉文档检索的主流范式，令牌级优化成为效率提升的关键突破口。
- 水下声学识别从封闭集向开放集演进，原始波形端到端学习取代传统手工特征，但跨域泛化仍是待解难题。

---

Powered by OpenClaw🦞

---

# [20260906](./202609/20260906.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦多模态图像匹配的核心挑战，西南交通大学与武汉大学联合团队提出辐射-旋转-尺度三重不变特征描述子。该工作针对异源传感器成像差异导致的匹配困难，通过几何与辐射联合建模提升跨模态配准鲁棒性，为遥感图像融合与变化检测提供基础支撑。

## ✨ 今日亮点

- 提出辐射-旋转-尺度三重不变特征描述子，突破多模态图像匹配瓶颈
- 联合几何变换与辐射畸变建模，增强异源遥感数据配准稳定性
- 西南交大与武大跨校合作，产学研结合推动遥感基础算法创新

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260906] Radiation, Rotation and Scale Invariant Feature Descriptor for Multimodal Image Matching | Ye Yuanxin, Tang Tengfeng, Peng Tao, Han Zhiqiang, Li Jiayuan, Wang Mi | Faculty of Geosciences and Engineering, Southwest Jiaotong University；School of Remote Sensing and Information Engineering, Wuhan University；State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University | Ye等提出辐射-旋转-尺度三重不变特征描述子，解决多模态遥感图像因传感器差异导致的匹配失效问题。 | [#490](https://github.com/Larry2000error/Larry-PaperClaw/issues/490) |

## 🔎 观察

- 多模态不变性联合建模正成为遥感图像匹配的主流技术路线，单一不变性已难以满足复杂应用场景需求
- 高校间跨机构合作频繁，特征描述子等基础算法研究需持续投入以支撑下游遥感智能解译应用

---

Powered by OpenClaw🦞

---
