# Daily Reports

最近三天日报（最新在前）：

# [20261021](./202610/20261021.md)
## 📌 今日概况

今日共检索候选论文 38 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态大模型的精细化理解与检索能力。LocalAgent探索实例级一致性验证的协作智能体框架；ERCLIP针对小数据场景优化CLIP的长文本图像检索；pplx-embed-v2-late则推进多语言视觉文档嵌入与延迟交互建模，显示视觉-语言融合正从粗粒度对齐向细粒度、长上下文、多语言方向深化。

## ✨ 今日亮点

- LocalAgent提出协作式智能体验证框架，实现细粒度实例级多模态一致性判别
- ERCLIP突破CLIP小数据适配瓶颈，支持任意长度图文检索的对比学习优化
- pplx-embed-v2-late发布多语言视觉文档嵌入技术报告，强化延迟交互检索性能

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261021] LocalAgent: Collaborative Agentic Verification for Fine-Grained Instance-Level Consistency | Guo Jiachen, Zhu Xinshan, Wang Boyun, Liang Yanyan, Wan Jun, Lin Feng, Liu Ajian | Tianjin University；Chinese Academy of Sciences；Macau University of Science and Technology；Zhejiang University；University of Macau | LocalAgent通过多智能体协作验证机制，解决细粒度实例级跨模态一致性判断问题。 | [#650](https://github.com/Larry2000error/Larry-PaperClaw/issues/650) |
| [20261021] ERCLIP: Small-Data Adaptation of CLIP for Free-Length Image-Text Retrieval | Le Hoang-Bao, Tran Allie, Binh T. Nguyen, Zhou Liting, Gurrin Cathal | ADAPT Centre, School of Computing, Dublin City University；Ho Chi Minh University of Science, Vietnam National University | ERCLIP提出小数据场景下CLIP自适应方法，实现自由长度图文检索的对比学习优化。 | [#651](https://github.com/Larry2000error/Larry-PaperClaw/issues/651) |
| [20261021] pplx-embed-v2-late Technical Report | Krimmel Markus, Milliken Louis, Glazkova Ekaterina, Schall Maximilian, Chaffin Antoine, Eslami Sedigheh, Golde Jonas, Bykov Denis, Beamer Claire, Yang Jeremy, Wang Bo | Perplexity AI | pplx-embed-v2-late技术报告详述多语言视觉文档嵌入模型与延迟交互检索架构设计。 | [#652](https://github.com/Larry2000error/Larry-PaperClaw/issues/652) |

## 🔎 观察

- 细粒度实例级验证成为多模态大模型新焦点，协作智能体架构或成突破幻觉问题的关键路径
- 长文本理解与视觉文档检索同步演进，显示产业界对复杂场景多模态检索的工程化需求迫切

---

Powered by OpenClaw🦞

---

# [20261020](./202610/20261020.md)
## 📌 今日概况

今日共检索候选论文 46 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦视觉-语言模型在检索任务中的创新应用。行人重识别领域关注跨时段、换衣场景下的身份一致性建模；图像检索方向探索组合查询理解与重排序优化。多模态融合与测试时自适应成为提升检索精度的关键技术路径。

## ✨ 今日亮点

- MINER提出人际与个体内方差联合建模，解决换衣行人重识别难题
- PRAISE框架以属性为桥梁，实现查询条件子空间的几何约束检索
- 多模态重排序被重新定义为系统一决策问题，提升检索效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261020] MINER: Modeling Inter- and Intra-Person Variance for Reidentification | Nir Oron, Strugo Eliyahu, Shamir Ariel | Reichman University；Microsoft | MINER通过显式建模人际差异与个体内变化，结合困难样本挖掘，提升换衣场景下的行人重识别性能。 | [#645](https://github.com/Larry2000error/Larry-PaperClaw/issues/645) |
| [20261020] In PRAISE of Attributes: Grounding Retrieval Geometry with Query-Conditioned Subspaces for Person Re-Identification | Bhattacharya Rajarshi, Shukla Aryan, Murtaza Shakeeb, Desrosiers Christian, Dolz Jose, Heritier Maguelonne, Granger Eric | LIVIA, École de technologie supérieure；Genetec Inc. | PRAISE利用视觉-语言模型的属性语义，构建查询条件子空间，实现几何可解释的测试时自适应检索。 | [#646](https://github.com/Larry2000error/Larry-PaperClaw/issues/646) |
| [20261020] Less is More: Concise Retrieval and Critic-based Re-ranking for Composed Image Retrieval | Zheng Yuqian, Ahn Hyoju, Ahn Hyeongjin, Park Eunil | Sungkyunkwan University；Jaume I University | 提出简洁检索与基于评论家的重排序策略，以更少计算开销实现零样本组合图像检索。 | [#647](https://github.com/Larry2000error/Larry-PaperClaw/issues/647) |
| [20261020] Multimodal Reranking Is a System One Decision | Liu Zhuchenyang, Zhang Yao, Xiao Yu | Aalto University | 将多模态重排序形式化为系统一决策过程，揭示快速直觉判断在检索优化中的有效性。 | [#648](https://github.com/Larry2000error/Larry-PaperClaw/issues/648) |

## 🔎 观察

- 行人重识别正从单一视觉特征向属性-语义联合表征演进，换衣鲁棒性成为核心挑战
- 重排序环节的系统化设计（评论家机制、决策理论）成为提升检索质量的新突破口

---

Powered by OpenClaw🦞

---

# [20261019](./202610/20261019.md)
## 📌 今日概况

今日共检索候选论文 50 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究呈现多模态基础模型与高效检索技术的融合趋势。视觉语言模型向具身智能与3D场景理解延伸，同时训练无关方法与自适应表征优化成为降低计算成本的关键路径。跨域自适应与置信度引导策略持续推动无监督学习在视觉任务中的应用。

## ✨ 今日亮点

- 基础模型驱动光流估计，DINOv2与Depth Anything V2实现密集预测Transformer架构
- SpatialScout探索VLM智能体主动探索与3D场景建图的空间智能能力
- FlexVDR提出俄罗斯套娃表征预算动态分配，优化视觉文档检索效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261019] Foundation Model Driven Optical Flow | Chanda Praroop, Kumar Suryansh | Texas A&M University | 基于DINOv2与Depth Anything V2构建基础模型驱动的光流估计框架，采用密集预测Transformer实现端到端训练。 | [#639](https://github.com/Larry2000error/Larry-PaperClaw/issues/639) |
| [20261019] SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes? | Zhang Zhaoxi, Liang Hao, Wu Linxuan, Xu Yiming, Yuan Yifu, Liang Kun, Tang Chenming, Qiang Meiyi, Zhang Wentao, Li Weikang | Peking University；Tianjin University | SpatialScout验证视觉语言模型智能体在主动探索与3D场景建图任务中的空间推理与规划能力。 | [#640](https://github.com/Larry2000error/Larry-PaperClaw/issues/640) |
| [20261019] DCR-TSF: Dual-Level Compositional Reasoning with Triadic Spherical Fusion for Training-Free Zero-Shot Composed Image Retrieval | Na Gwang-Ho, Kim Ho-Joong, Lee Seong-Whan | Korea University | DCR-TSF通过三元球面融合与双层组合推理，实现无需训练的零样本组合图像检索。 | [#641](https://github.com/Larry2000error/Larry-PaperClaw/issues/641) |
| [20261019] Confidence-Guided Pseudo-Label Refinement for Unsupervised Cross-Domain Person Re-Identification | Iqbal Sundas, Ali Danish, Tian Qing, Zheng Yuhui, Gou Jianping, Ou Weihua | Tsinghua University；Chinese Academy of Sciences | 提出置信度引导的伪标签精修方法，提升无监督跨域行人重识别在目标域的适应性能。 | [#642](https://github.com/Larry2000error/Larry-PaperClaw/issues/642) |
| [20261019] FlexVDR: Learning to Allocate Matryoshka Representation Budgets for Visual Document Retrieval | Xiang Haowen, Yan Yibo, Zou Xin, Liu Shuliang, Cao Yi, Ou Mingdong, Hu Xuming | The Hong Kong University of Science and Technology (Guangzhou)；Alibaba Group；The Hong Kong University of Science and Technology | FlexVDR学习查询自适应的俄罗斯套娃表征预算分配策略，实现视觉文档检索的效率与精度权衡。 | [#643](https://github.com/Larry2000error/Larry-PaperClaw/issues/643) |

## 🔎 观察

- 训练无关（training-free）方法在检索与理解任务中快速涌现，反映领域对降低微调成本的迫切需求
- 视觉语言模型正从被动感知向主动交互演进，具身智能与空间智能成为下一代多模态系统的核心能力方向

---

Powered by OpenClaw🦞

---
