# Daily Reports

最近三天日报（最新在前）：

# [20261125](./202611/20261125.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日候选论文聚焦数据稀缺、隐私约束与域外内容条件下的多模态检索，强调利用结构信息提升检索适应性。研究对象涵盖图表检索与文档版面分析，显示多模态系统正从依赖大规模同分布数据，转向关注有限数据、受限数据使用和分布变化下的稳健检索。不过今日仅有一篇候选，趋势判断仍需谨慎。

## ✨ 今日亮点

- 以结构感知方法回应多模态检索中的数据稀缺挑战
- 将隐私约束纳入检索问题，关注受限数据的可用边界
- 面向域外内容与文档版面，拓展图表检索研究场景

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261125] Structure-Aware Multimodal Retrieval Under Data Scarcity, Privacy Constraints and Out-of-Domain Content | Zafeiriou Argyrios, Koulouris Dionysios, Maglogiannis Ilias | University of Piraeus | 论文以结构信息增强多模态检索，集中讨论数据稀缺、隐私约束与域外内容带来的挑战。 | [#805](https://github.com/Larry2000error/Larry-PaperClaw/issues/805) |

## 🔎 观察

- 结构信息可作为低数据条件下的重要线索，但有效性仍需由具体实验结果验证。
- 同时考虑隐私与域外分布，说明检索研究正更重视真实部署中的约束。

---

Powered by OpenClaw🦞

---

# [20261124](./202611/20261124.md)
## 📌 今日概况

今日共检索候选论文 61 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日论文集中于多模态检索的可靠性、时序感知与系统演进：一类通过时序难负样本或组合可靠性学习，增强模型对时间约束和噪声对应的辨别；另一类以多向量证据表示、压缩索引和分阶段检索兼顾定位与效率；同时，兼容表示与增量重编码反映出检索系统持续升级、降低全量重建成本的工程需求。整体趋势是从单纯追求匹配精度，转向精度、鲁棒性、可解释证据与部署成本的协同优化。

## ✨ 今日亮点

- 时序难负样本用于强化视频检索的时间敏感性，同时保留通用能力
- CREDIT面向噪声三元组对应，学习组合语义与样本可靠性
- 多向量证据表示与兼容编码，分别回应可定位性和系统演进成本

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261124] Teaching Time Without Losing General Retrieval: Adapting Multimodal Embeddings for Time-Sensitive Video Retrieval | Oyama Toya, Lienhart Rainer, Satoh Shin'ichi | The University of Tokyo；National Institute of Informatics；University of Augsburg | 通过时序难负样本适配多模态嵌入，使视频检索理解时间条件并尽量保持通用检索能力。 | [#800](https://github.com/Larry2000error/Larry-PaperClaw/issues/800) |
| [20261124] CREDIT: Compositional Reliability Learning for Noisy Composed Image Retrieval | Zhou Tiancai, Li Yongxiang, Liu Suimei, Yuan Zhong, Peng Dezhong, Peng Xi, Wang Xu | College of Computer Science, Sichuan University；School of Computing and Artificial Intelligence, Southwest Jiaotong University；School of Artificial Intelligence, Sichuan University | CREDIT针对带噪组合图像检索，联合学习组合语义与对应关系的可靠性。 | [#801](https://github.com/Larry2000error/Larry-PaperClaw/issues/801) |
| [20261124] OmniEVIE: Evidence-Vector-Informed Embedding for Multi-modal Retrieval | Wang Zifei, Wen Wei, Ji Qiang, Zhang Qian-Wen, Qiao Ruizhi, Liu He, Sun Xing, Lin Qiang | Tencent IMA Product Center；Tencent Youtu Lab | OmniEVIE以证据向量丰富多模态嵌入，并结合压缩索引与三阶段检索。 | [#802](https://github.com/Larry2000error/Larry-PaperClaw/issues/802) |
| [20261124] RELAY: Learning Compatible Representations One Encoder at a Time | Wang Yu, Qin Chuan, Zhang Qiang | Qwen Business Unit of Alibaba | RELAY逐个训练兼容编码器，支持查询侧升级与文档表示的增量重编码。 | [#803](https://github.com/Larry2000error/Larry-PaperClaw/issues/803) |

## 🔎 观察

- 四篇工作均围绕检索表示展开，说明当前重点正由统一向量转向任务约束、证据粒度与表示兼容性。
- 候选论文未直接面向遥感场景，其方法价值主要在于为时序影像、噪声标注和大规模索引提供可迁移思路。

---

Powered by OpenClaw🦞

---

# [20261123](./202611/20261123.md)
## 📌 今日概况

今日共检索候选论文 62 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 11 篇。

今日论文以跨模态检索、视频时刻定位与行人重识别为主线，强调查询自适应、语义验证、候选重排序和时空先验等细粒度证据建模。遥感方向聚焦无人机视频文本检索及卫星—无人机跨视角地理定位；同时，统一像素表征、智能体式视频语料检索和医学图像数据构建，显示研究正由单一表征学习转向证据对齐、冲突处理与可解释评估。

## ✨ 今日亮点

- 无人机研究同时覆盖视频文本检索与无卫星导航信号下的跨视角定位
- 多项工作围绕重排序、时空先验与身份冲突提升行人重识别可靠性
- 视频检索从单次匹配转向语义验证、渐进细化和智能体式搜索

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261123] AirVT-15k: A Query-Diverse UAV Video-Text Dataset and Query-Adaptive Evidence Alignment Network for Retrieval | Chen Xi, Chen Xu, Jia Xiangyang, Gan Ting, Zhang Xu, Wei Shuquan | Institution unavailable | AirVT-15k面向多样查询构建双语无人机视频文本数据，并提出查询自适应证据对齐。 | [#788](https://github.com/Larry2000error/Larry-PaperClaw/issues/788) |
| [20261123] SafeRank-ReID: Candidate-Conditioned Re-Ranking under Identity Conflicts for Multimodal Person Re-Identification | Wang Yizhi, Li Zixuan, Chen Zhuwen, Qin Feiwei | Hangzhou Dianzi University | SafeRank-ReID针对多模态身份冲突，以候选条件重排序协调证据与模态可靠性。 | [#789](https://github.com/Larry2000error/Larry-PaperClaw/issues/789) |
| [20261123] RigidAnchor: Cross-View Geo-Localization for UAV via Iterative Planar Rigid Alignment | Wang Bo, Zhu Dekang, Li Jian, Meng Zhipeng, Wang Bo, Hu Dewen | National Innovation Institute of Defense Technology；College of Intelligence Science and Technology, National University of Defense Technology；School of Future Technology, National University of Defense Technology | RigidAnchor通过迭代平面刚性对齐，面向无人机与卫星影像的跨视角地理定位。 | [#790](https://github.com/Larry2000error/Larry-PaperClaw/issues/790) |
| [20261123] Separating Protocol Effects from Spatio-Temporal Evidence in Person Re-Identification Re-Ranking | Mochamad Rizal Fauzan, Doan Pham Thao Nhu, Konthoujam Jeslin, Hongjirakul Purit, Chawla Lakshay | National Taipei University of Technology | 该研究区分评测协议效应与时空证据，分析同摄像头惩罚对行人重识别重排序的影响。 | [#791](https://github.com/Larry2000error/Larry-PaperClaw/issues/791) |
| [20261123] Pixel as the Common Language: Unified Multimodal Embedding via Visual Rendering | Yuan Xu, Wu Pangjing, Fan Wenqi, Li Qing | The Hong Kong Polytechnic University | 该工作将不同模态渲染为像素输入，探索以视觉表征统一多模态检索嵌入。 | [#792](https://github.com/Larry2000error/Larry-PaperClaw/issues/792) |
| [20261123] Bi-Refine: Semantic Verification-Guided Progressive Refinement for Moment Retrieval | Liu Mengnan, Zhou Sanping, Xia Kun, Lin Jiaxuan, Wu Yuxuan, Hua Gang | National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Xi'an Jiaotong University；School of Artificial Intelligence, Xi'an Jiaotong University；School of Computer Science and Technology, Xi'an Jiaotong University；Amazon Alexa AI | Bi-Refine以语义验证引导渐进式细化，用于视频时刻检索与时间定位。 | [#793](https://github.com/Larry2000error/Larry-PaperClaw/issues/793) |
| [20261123] Teaching How to Reason, Beyond What to Answer: Evidence-Faithful On-Policy Distillation for streaming video understanding | Liu Mengnan, Zhou Sanping, Xia Kun, Lin Jiaxuan, Hua Gang, Wang Le | Institution unavailable | 该工作面向流式视频理解，以证据忠实的同策略蒸馏教授推理方式，而非仅拟合答案。 | [#794](https://github.com/Larry2000error/Larry-PaperClaw/issues/794) |
| [20261123] Towards Agentic Video Corpus Moment Retrieval | Xu Chenwei, Wu Shang, Pan Zhenyu, Zhang Jianshu, Maneriker Pranav, Lu Lie, Du Fan, Li Manling, Liu Han | Northwestern University；Dolby | 该研究探索无需训练的智能体式视频语料时刻检索，结合视觉语言模型与大语言模型。 | [#795](https://github.com/Larry2000error/Larry-PaperClaw/issues/795) |
| [20261123] A dataset of clinically similar image pairs from citation-linked case reports for medical image retrieval | Shmueli Guy, Keno K. Bressem, Hope Tom | School of Computer Science and Engineering, The Hebrew University of Jerusalem；National Center for Tumor Diseases West；Institute of Artificial Intelligence in Medicine, University Hospital Essen；Department of Diagnostic and Interventional Radiology, School of Medicine and Health, Technical University of Munich；Department of Diagnostic and Interventional Radiology and Neuroradiology, University Hospital Essen；Allen Institute for AI | 该数据集从引用关联病例报告中整理临床相似图像对，服务医学图像检索研究。 | [#797](https://github.com/Larry2000error/Larry-PaperClaw/issues/797) |
| [20261123] Intra-Class Diversity Loss for Person Re-Identification | Zhou Wei, Chen BaXian | Department of Artificial Intelligence, Guangzhou Huashang College | 该方法为行人重识别引入类内多样性损失，促进同一身份表征的多样性学习。 | [#798](https://github.com/Larry2000error/Larry-PaperClaw/issues/798) |
| [20261123] Where Compositionality Hides: Shared-Content Interference in Vision-Language Retrieval | Anudeep Chimata, Harsh Vardhan Poddar | BITS Pilani, K. K. Birla Goa Campus | 该研究分析视觉语言检索中的共享内容干扰，并以均值消除和嵌入投影探查组合性。 | [#799](https://github.com/Larry2000error/Larry-PaperClaw/issues/799) |

## 🔎 观察

- 今日方法普遍把性能瓶颈归因于证据组织与冲突处理，而非仅扩大模型或数据规模。
- 遥感相关论文数量有限但任务明确，集中在无人机检索与跨视角定位，尚不足以代表全领域趋势。

---

Powered by OpenClaw🦞

---
