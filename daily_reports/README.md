# Daily Reports

最近三天日报（最新在前）：

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

# [20260830](./202608/20260830.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦视觉语言模型在地理定位任务中的能力拓展，核心趋势为引入智能体推理与反事实学习机制。三篇论文分别从假设验证框架、困难样本挖掘及具身导航评估三个维度，推动开放世界地理定位的鲁棒性与泛化性研究。

## ✨ 今日亮点

- 智能体推理框架实现感知-假设-验证的多跳地理定位，突破传统端到端局限
- 反事实困难样本生成策略RePair，将检索失败转化为有效训练信号
- GeoAgent构建具身导航基准，系统评估VLM在真实环境连续决策能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260830] Perceive to Hypothesize, Verify to Ground: An Agentic Reasoning Framework for Open-World Geo-Localization | Jiang Yutian, Li Ruijie, Lyu Sisuo, Hao Xixuan, Liu Qingxiang, Yu Yongzi, Liang Yuxuan | The Hong Kong University of Science and Technology (Guangzhou)；The Hong Kong University of Science and Technology | 提出感知假设验证的智能体推理框架，通过多跳推理实现开放世界地理定位，突破传统模型直接预测模式。 | [#459](https://github.com/Larry2000error/Larry-PaperClaw/issues/459) |
| [20260830] RePair: Turning Retrieval Failures into Counterfactual Hard Pairs | Liu Siyi, Zhu Xiaorong, Du Enjun, Zuo Xinyu, Duan Lisheng, Liang Haijin, Ma Jin, Pu Junfu, Zhang Yongqi | The Hong Kong University of Science and Technology (Guangzhou)；Tencent Yuanbao；The University of Hong Kong；ARC Lab, Tencent | 设计RePair方法将跨模态检索失败样本转化为反事实困难对，增强CLIP类模型对易混淆样本的判别能力。 | [#460](https://github.com/Larry2000error/Larry-PaperClaw/issues/460) |
| [20260830] GeoAgent: Evaluating VLM Geolocalization Through Embodied Navigation | Mukherjee Arka, Roy Soham, Trivedi Kartikeya, Ghosh Shreya | KIIT Bhubaneswar；IIT Bhubaneswar | 构建GeoAgent评估基准，通过具身导航任务检验视觉语言模型在街景环境中的连续地理定位决策表现。 | [#461](https://github.com/Larry2000error/Larry-PaperClaw/issues/461) |

## 🔎 观察

- 地理定位研究正从静态图像匹配转向动态交互推理，智能体范式或成为下一代技术路线。
- 困难样本挖掘与反事实学习结合，显示社区对检索模型鲁棒性瓶颈的针对性攻关。

---

Powered by OpenClaw🦞

---
