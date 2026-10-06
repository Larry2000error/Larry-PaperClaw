# Daily Reports

最近三天日报（最新在前）：

# [20261001](./202610/20261001.md)
## 📌 今日概况

今日共检索候选论文 56 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日两篇论文聚焦智能检索技术：一篇探索视觉语言模型驱动的多模态交互搜索，另一篇提出带召回率认证的度量空间近似最近邻搜索方法。研究趋势显示检索系统正向多模态融合与可量化性能保证方向发展。

## ✨ 今日亮点

- AiSearch实现图文视频统一交互检索，拓展VLM应用场景
- SOLO首创召回率认证机制，解决近似搜索可靠性难题
- 两篇工作分别从用户体验与理论保证角度推进检索技术

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261001] AiSearch: Interactive Multi-Modal Search with VLMs | Koksal Ali, Mei Chee Leong, Sintunata Vicky, Ching Ling Chin, Wee Teck Fong | Institute of Advanced Intelligence and Computing (IAIC)；Agency for Science, Technology and Research (A*STAR) | AiSearch提出基于视觉语言模型的交互式多模态搜索框架，支持图像、视频与文本的跨模态检索。 | [#541](https://github.com/Larry2000error/Larry-PaperClaw/issues/541) |
| [20261001] SOLO: Certified-Recall Metric Similarity Search with Scan-Only Sampled Inverted Lists | Chávez Édgar | CICESE | SOLO设计带召回率认证的度量相似性搜索算法，通过采样倒排列表实现仅需扫描的高效查询。 | [#542](https://github.com/Larry2000error/Larry-PaperClaw/issues/542) |

## 🔎 观察

- 多模态检索与VLM结合成为热点，但两篇论文均未涉及遥感数据，领域迁移潜力待挖掘
- 召回率认证机制对遥感大规模检索具有参考价值，可提升灾害应急等场景的可靠性

---

Powered by OpenClaw🦞

---

# [20260930](./202609/20260930.md)
## 📌 今日概况

今日共检索候选论文 69 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦跨模态智能与时空推理，涵盖视觉-语言模型在车辆重识别、视频地理定位、文本-视频检索及视觉空间导航等方向。学界正探索层级化图注意力、多维度显著性评估与多步嵌入检索等技术，以提升复杂场景下的跨视角匹配与推理能力。

## ✨ 今日亮点

- GeoGAT提出双向时序采样与层级图注意力，实现全球视频地理定位
- Front-to-Back构建非对称跨视角车辆重识别基准，评估视觉-语言模型零样本能力
- 文本-视频检索引入多维度显著性评估，缓解视觉冗余问题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260930] Front-to-Back: Benchmarking Vision-Language Models for Asymmetric Cross-View Vehicle Re-Identification | Mots'oehli Moseli, Babeli Thulani | MindForge AI；University of Hawai'i at Mānoa | 该研究建立非对称跨视角车辆重识别基准，系统评估视觉-语言模型的零样本跨视角匹配性能。 | [#536](https://github.com/Larry2000error/Larry-PaperClaw/issues/536) |
| [20260930] GeoGAT: Bidirectional Temporal Sampling Meets Hierarchical Graph Attention for Global Video Geo-localization | Cui Junchao, Ma Xuanzi, Shi Wenqi, Li Hangyu, Zhu Biru, Fu Chong, Luo Xiangyang | Information Engineering University；Zhengzhou University | GeoGAT融合双向时序采样与层级图注意力网络，实现基于时空特征的全局视频地理定位。 | [#537](https://github.com/Larry2000error/Larry-PaperClaw/issues/537) |
| [20260930] Text-Video Retrieval via Multi-Dimensional Saliency Assessment and Granularity-Aware Query Decomposition | Wei Shuquan, Chen Xi, Chen Xu, Jia Xiangyang | School of Computer Science, Wuhan University | 通过多维度显著性评估与粒度感知查询分解，提升文本-视频跨模态检索的精准度。 | [#538](https://github.com/Larry2000error/Larry-PaperClaw/issues/538) |
| [20260930] Learning to Route in Visual Space via Multi-Step Embedding Retrieval | Chen Tianyu, Zhou Mingyuan, Wu Jiaxing | The University of Texas at Austin；Google DeepMind | 基于强化学习的多步嵌入检索方法，使LLM智能体能够在视觉嵌入空间中自主导航寻路。 | [#539](https://github.com/Larry2000error/Larry-PaperClaw/issues/539) |

## 🔎 观察

- 跨模态对齐与时空推理成为核心趋势，图神经网络与注意力机制在地理定位任务中应用深化
- 视觉-语言模型正从静态图像向动态视频与复杂空间导航拓展，零样本与强化学习成为关键使能技术

---

Powered by OpenClaw🦞

---

# [20260929](./202609/20260929.md)
## 📌 今日概况

今日共检索候选论文 82 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI日报候选论文聚焦视觉-语言预训练与目标重识别领域。三篇论文分别探索扩散模型特征学习、视觉基础模型令牌路由机制，以及多模态意图表示优化，体现基础模型与多模态融合的持续深化趋势。

## ✨ 今日亮点

- DiffReID将扩散模型引入目标重识别，通过判别式扩散过程增强特征判别性
- FM-ReID基于DINOv3提出选择性竞争令牌路由，优化局部特征学习机制
- 零样本组合图像检索研究聚焦视觉-语言对齐中的视觉实例化修正问题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260929] DiffReID: Discriminative Diffusion Model for Object Re-Identification | Wang Yingquan, Zhang Pingping, Wang Dong, Lu Huchuan | Institution unavailable | DiffReID提出判别式扩散模型，通过CLIP引导的提示调优与扩散过程实现目标重识别的判别性特征学习。 | [#532](https://github.com/Larry2000error/Larry-PaperClaw/issues/532) |
| [20260929] FM-ReID: Selective Competitive Token Routing for Object Re-Identification | Li Zhiqi, Zhou Xiaowei, Sun Zeyuan, Gao Feng, Dong Junyu | Faculty of Information Science and Engineering, Ocean University of China；Sanya Oceanographic Institution, Ocean University of China | FM-ReID基于DINOv3视觉基础模型，设计选择性竞争令牌路由机制，动态筛选判别性局部令牌用于重识别。 | [#533](https://github.com/Larry2000error/Larry-PaperClaw/issues/533) |
| [20260929] Optimizing VLP-aligned Multimodal Intent Representation with Correct Visual Instantiation for Zero-Shot Composed Image Retrieval | Ge Xuri, Wang Chunhao, Fu Junchen, Wen Haokun, Xu Zhiwei, Zhou Ying, Chen Zhumin, Ren Pengjie, Ren Zhaochun, Xin Xin | School of Artificial Intelligence, Shandong University；School of Computer Science and Technology, Shandong University；School of Computing Science, University of Glasgow；School of Computer Science and Technology, Harbin Institute of Technology (Shenzhen)；Leiden University | 该研究针对零样本组合图像检索，提出视觉实例化修正方法优化VLP对齐的多模态意图表示。 | [#534](https://github.com/Larry2000error/Larry-PaperClaw/issues/534) |

## 🔎 观察

- 目标重识别领域正加速融合视觉基础模型，从CLIP向DINOv3演进体现技术迭代
- 多模态检索研究开始关注对齐质量的细粒度修正，而非仅追求模态间粗粒度对齐

---

Powered by OpenClaw🦞

---
