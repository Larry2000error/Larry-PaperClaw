# Daily Reports

最近三天日报（最新在前）：

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

# [20261018](./202610/20261018.md)
## 📌 今日概况

今日共检索候选论文 18 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦高效视觉定位与多模态检索两大方向。LateMatch通过可缓存匹配机制突破交互瓶颈，推动边缘计算场景下的视觉定位效率；MEMORA则引入记忆增强的多模态委员会重排序架构，应对推理密集型检索任务。两者均体现模型架构创新与效率优化的双重追求。

## ✨ 今日亮点

- LateMatch提出可缓存匹配策略，显著降低视觉定位计算开销
- MEMORA构建记忆增强的多模态委员会，提升复杂推理检索精度
- 两篇论文均关注检索系统效率与精度的协同优化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261018] LateMatch: Breaking the Interaction Bottleneck via Cacheable Matching for Efficient Visual Localization | Omama Mohammad, Ashraf Aeyan, Chinchali Sandeep | The University of Texas at Austin；University of Massachusetts Amherst | LateMatch设计可缓存匹配机制，打破视觉定位中的交互瓶颈，实现边缘计算场景下的高效特征匹配。 | [#636](https://github.com/Larry2000error/Larry-PaperClaw/issues/636) |
| [20261018] MEMORA: A Memory-Enhanced Multimodal Committee Reranking Agent for Reasoning-Intensive Retrieval | Mahmoud Mohamed, Mostafa Farouk Senussi, Abdalla Mahmoud, Mahmoud SalahEldin Kasem, Abdallah Abdelrahman, Hyun Soo Kang | Chungbuk National University；University of Innsbruck | MEMORA提出记忆增强的多模态委员会重排序智能体，通过多专家协作与记忆机制强化推理密集型检索性能。 | [#637](https://github.com/Larry2000error/Larry-PaperClaw/issues/637) |

## 🔎 观察

- 特征匹配领域正从精度竞争转向效率与部署友好性并重，边缘计算需求驱动架构创新
- 多模态检索系统趋向引入显式记忆模块与委员会机制，以应对复杂推理场景的可解释性与稳定性挑战

---

Powered by OpenClaw🦞

---
