# Daily Reports

最近三天日报（最新在前）：

# [20260903](./202609/20260903.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究呈现跨模态检索与农业智能监测两大方向。跨模态生成式检索通过动态扩展策略优化信息不对称为核心创新；农业领域聚焦牲畜个体识别，利用背部标记解决养殖场景下的重识别与追踪难题，体现AI技术向垂直场景的深度渗透。

## ✨ 今日亮点

- 跨模态生成检索引入动态通配符推理，缓解自回归解码中的信息瓶颈
- 猪只重识别创新采用背部标记分类，适配侧视摄像头养殖场景
- 农业计算机视觉研究融合多机构资源，推动精准畜牧业发展

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260903] WIDE: Wildcard Inference with Dynamic Expansion for Cross-Modal Generative Retrieval | Guo Teng, Wang Xin, Xu Jiayou, Zhou Keying, Shen Jifeng, Ruan Haoxin | Jilin University；Jiangsu University | WIDE提出动态扩展通配符推理机制，通过优化束搜索策略解决跨模态生成检索中的信息非对称问题。 | [#471](https://github.com/Larry2000error/Larry-PaperClaw/issues/471) |
| [20260905] BMCTrack-d: Pig re-identification and tracking via back marks in challenging camera settings | Brunner David, Oczak Maciej, Bordes Marie, Rault Jean-Loup, Stephan M. Winkler, Dorfer Viktoria | Bioinformatics Research Group, PLFDoc, University of Applied Sciences Upper Austria；Computer Vision Lab, TU Wien；Precision Livestock Farming Hub, The University of Veterinary Medicine Vienna；Animal Welfare Science Unit, The University of Veterinary Medicine Vienna | BMCTrack-d开发基于背部标记的猪只重识别与跟踪系统，针对挑战性相机设置下的养殖场景实现个体精准辨识。 | [#472](https://github.com/Larry2000error/Larry-PaperClaw/issues/472) |

## 🔎 观察

- 生成式检索正从静态编码向动态推理演进，自回归模型的信息损耗问题成为优化焦点
- 农业AI研究呈现精细化趋势，牲畜个体识别从群体分析迈向单只追踪，标记辅助策略降低环境干扰

---

Powered by OpenClaw🦞

---

# [20260902](./202609/20260902.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦于视觉语言模型幻觉抑制与图像检索优化两大方向。前者通过稀疏解码与跨模态检索机制提升大模型可靠性，后者融合流形学习与排序聚合改进检索精度，均体现多技术融合趋势。

## ✨ 今日亮点

- RVSD提出检索视觉稀疏解码，有效缓解大视觉语言模型幻觉问题
- 邻居嵌入投影与基于排序的流形学习结合，优化图像检索性能
- 跨模态语义空间对齐与UMAP降维技术成为关键方法支撑

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260902] RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models | Liu Canjie, Kang Jiawen, Wen Jinbo, Zhong Zishao | School of Automation, Guangdong University of Technology；Department of Computer Science, City University of Hong Kong；The Second Affiliated Hospital of Guangzhou University of Chinese Medicine | RVSD通过检索增强的稀疏解码机制，在生成阶段抑制大视觉语言模型的视觉幻觉现象。 | [#468](https://github.com/Larry2000error/Larry-PaperClaw/issues/468) |
| [20260902] Aggregating Neighbor Embedding Projection and Rank-Based Manifold Learning for Image Retrieval | Vinicius Atsushi Sato Kawai, Gustavo Rosseto Leticio, Lucas Pascotti Valem, Daniel Carlos Guimarães Pedronette | São Paulo State University (UNESP)；University of São Paulo (USP) | 提出邻居嵌入投影与排序流形学习融合方法，提升基于内容的图像检索准确性。 | [#469](https://github.com/Larry2000error/Larry-PaperClaw/issues/469) |

## 🔎 观察

- 视觉语言模型幻觉治理从训练后干预转向生成过程控制，稀疏解码成为新范式
- 传统流形学习方法与排序聚合结合，显示经典算法在深度学习时代的重构价值

---

Powered by OpenClaw🦞

---

# [20260901](./202609/20260901.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日两篇论文聚焦视觉表征学习新范式。AutoConcept提出无需训练的概念引导重排序方法，解决组合图像检索中元数据利用不足问题；ViTAMINS则系统探索合成难负样本在自监督Vision Transformer训练中的作用，为对比学习优化提供实证依据。

## ✨ 今日亮点

- AutoConcept首创训练-free概念引导重排序，突破组合图像检索后处理瓶颈
- ViTAMINS揭示合成难负样本对ViT自监督学习的增益机制与边界条件
- 两研究分别从检索系统优化与表征学习基础角度推进视觉AI发展

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260901] AutoConcept: Training-Free Concept-Guided Reranking for Metadata-Available Composed Image Retrieval | Wang Tianyu, Wu Tianjiao | School of Computer Science and Technology, Soochow University；INSTITUT NATIONAL DES SCIENCES APPLIQUEES DE LYON | AutoConcept提出无需训练的概念引导重排序框架，利用元数据概念实现组合图像检索的精准后处理，在FashionIQ数据集验证有效性。 | [#465](https://github.com/Larry2000error/Larry-PaperClaw/issues/465) |
| [20260901] ViTAMINS: An Empirical Study of Training Self-Supervised Vision Transformers with Synthetic Hard Negatives | Giakoumoglou Nikos, Floros Andreas, Papadopoulos Kleanthis-Marios, Stathaki Tania | Imperial College London | ViTAMINS系统实证合成难负样本对自监督Vision Transformer训练的影响，为对比学习中的负样本选择策略提供指导。 | [#466](https://github.com/Larry2000error/Larry-PaperClaw/issues/466) |

## 🔎 观察

- 训练-free方法成为检索任务新趋势，降低部署成本同时提升可解释性
- 难负样本合成技术从NLP向视觉迁移，自监督学习正经历精细化设计阶段

---

Powered by OpenClaw🦞

---
