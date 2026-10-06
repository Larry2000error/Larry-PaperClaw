# Daily Reports

最近三天日报（最新在前）：

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

# [20260928](./202609/20260928.md)
## 📌 今日概况

今日共检索候选论文 84 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦跨模态匹配与多模态学习，涵盖无监督可见光-红外行人重识别、野生动物保护中的多模态动物重识别，以及视觉文档重排序。研究趋势显示语义补偿、环境元数据融合与高效轻量模型成为关键方向。

## ✨ 今日亮点

- 无监督跨模态行人重识别提出语义模态补偿机制，缓解非配对场景下的模态差异
- 野生动物保护研究整合视觉特征与环境元数据，推动多模态动物个体识别
- RidgeRank以岭回归浅层读出实现高效视觉文档重排序，降低计算开销

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260928] Semantic Modality Compensation for Unsupervised Visible-Infrared Person Re-identification under Unpaired Settings | Chen Duanning, He Ke, Yang Bin, Yao Yongxiang | Wuhan University | 提出语义模态补偿网络，在无监督非配对设置下缩小可见光与红外图像的模态鸿沟。 | [#525](https://github.com/Larry2000error/Larry-PaperClaw/issues/525) |
| [20260928] Advancing Wildlife Conservation through Multimodal Animal Re-Identification with Environmental Metadata | Li Yuzhuo, Zhao Di, Qiao Tingrui, Wu Yihao, Pang Bo, Yun Sing Koh | School of Computer Science, University of Auckland | 构建融合环境元数据的多模态框架，提升野外场景下动物重识别的鲁棒性与可解释性。 | [#526](https://github.com/Larry2000error/Larry-PaperClaw/issues/526) |
| [20260928] RidgeRank: Efficient Visual Document Reranking via Score Fusion and a Shallow Linear Readout | Yang Shubing, Zhao Dongfang | University of Washington | 设计基于分数融合与岭回归浅层读出的轻量重排序方法，优化视觉文档检索效率。 | [#527](https://github.com/Larry2000error/Larry-PaperClaw/issues/527) |

## 🔎 观察

- 跨模态重识别研究正从配对数据向非配对、无监督设置迁移，降低标注成本成为核心诉求
- 环境元数据与视觉模态的融合或将成为生态监测领域的新范式，但数据异质性挑战仍待解决

---

Powered by OpenClaw🦞

---
