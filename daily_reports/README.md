# Daily Reports

最近三天日报（最新在前）：

# [20261125](./202611/20261125.md)
## 📌 今日概况

今日共检索候选论文 66 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日论文集中呈现多模态检索、跨视角理解与遥感数据基础设施三条主线。多项工作关注数据稀缺、隐私、域外内容及语义偏差下的稳健匹配，并尝试借助结构信息、潜在知识和人类判断改善对齐。研究还延伸至跨视角佩戴者定位、开放世界航拍目标搜索，以及复杂成像差异下的多分辨率SAR配准，显示真实场景泛化与评测基准正同步受到重视。

## ✨ 今日亮点

- 稳健多模态检索成为主线，结构约束与语义校准用于应对复杂数据条件。
- 开放世界航拍搜索引入免训练智能体，拓展视觉语言模型的遥感应用边界。
- SAR配准新数据集聚焦跨轨、视角变化与多分辨率成像差异。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261125] Structure-Aware Multimodal Retrieval Under Data Scarcity, Privacy Constraints and Out-of-Domain Content | Zafeiriou Argyrios, Koulouris Dionysios, Maglogiannis Ilias | University of Piraeus | 面向数据稀缺、隐私与域外内容，研究探索结构感知的多模态及图表检索。 | [#805](https://github.com/Larry2000error/Larry-PaperClaw/issues/805) |
| [20261125] Towards Closing the Performance Gap in Cross-Modal Place Recognition | Idan Ofer, Badur Dan, Shavit Yoli | Bar-Ilan University | 研究聚焦跨模态地点识别中的细粒度匹配，旨在缩小现有方法的性能差距。 | [#808](https://github.com/Larry2000error/Larry-PaperClaw/issues/808) |
| [20261125] Who Is Ego? Scaling Cross-View Camera Wearer Identification and Segmentation beyond Humans | Jin Yifan, Zhang Zheng, Qian Tianwen, Wang Dong, Zhao Bo, Fu Yanwei, Fu Yuqian | Central South University；Fudan University；East China Normal University；Shanghai AI Laboratory；Shanghai Jiao Tong University；Shanghai Innovation Institute；KAUST | 将跨视角相机佩戴者识别与分割扩展至非人类对象，并关注极线几何线索。 | [#809](https://github.com/Larry2000error/Larry-PaperClaw/issues/809) |
| [20261125] SPARC: Semantic Calibration with Latent Multimodal Knowledge for Robust Image-Text Retrieval | Mao Zhongkuan, Zhao Wenzhuo, Chen Haidong, Li Shangze, Wang Yidong, Bi Jinhe, Ma Yunpu, Fang Junfeng, Shen Fei, Chua Tat-Seng | Sichuan University；North China University of Technology；Nanjing University of Science and Technology；Peking University；National University of Singapore；Ludwig-Maximilians-Universität München | SPARC利用潜在多模态知识进行语义校准，增强图文检索的稳健匹配能力。 | [#810](https://github.com/Larry2000error/Larry-PaperClaw/issues/810) |
| [20261125] A Simple Yet Effective Agent for Open-World Aerial Object Search | Hao Jitai, Yang Liangxing, Li Zhenyang, Liu Fan, Huang Qiang, Yu Jun | Harbin Institute of Technology；Hong Kong Polytechnic University；Southeast University | 提出面向开放世界航拍目标搜索的免训练智能体，结合视觉语言模型开展导航搜索。 | [#811](https://github.com/Larry2000error/Larry-PaperClaw/issues/811) |
| [20261125] MOVR-SAR: A Multi-resolution SAR Registration Dataset under Orbit-crossing and View-variant Imaging Differences | Pu Yuchi, Qi Bosong, Shi Pengcheng, Li Jiayuan | School of Remote Sensing and Information Engineering, Wuhan University；Hubei Luojia Laboratory | MOVR-SAR构建跨轨、视角变化与多分辨率条件下的SAR影像配准数据集。 | [#812](https://github.com/Larry2000error/Larry-PaperClaw/issues/812) |
| [20261125] Aligned Machine: A Benchmark for Evaluating Multimodal Embedding Similarity via Human Comparative Judgements | Li Jiechen, Groos Hannah, Bent Brinnae | Duke University | 以人类比较判断评估多模态嵌入相似度，重点考察模型与人类语义认知的对齐。 | [#813](https://github.com/Larry2000error/Larry-PaperClaw/issues/813) |

## 🔎 观察

- 研究重心正从封闭集精度转向数据受限、域偏移与开放世界条件下的可靠泛化。
- 数据集与人类对齐基准并进，说明能力比较越来越依赖贴近真实需求的评测。

---

Powered by OpenClaw🦞

---

# [20261124](./202611/20261124.md)
## 📌 今日概况

今日共检索候选论文 71 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日论文集中于多模态检索的可靠性、时序理解与系统演进：研究一方面通过时间敏感训练、决策模型强化长视频中的证据定位，另一方面处理组合图像检索的噪声对应问题。同时，多向量嵌入、压缩索引和分阶段检索关注精度与效率平衡，兼容表示与增量重编码则面向编码器更新时的存量索引复用。整体趋势是从单一相似度匹配走向更细粒度、可扩展且具证据意识的检索框架。

## ✨ 今日亮点

- 时间敏感训练与决策模型共同推进长视频证据检索
- 可靠性学习用于缓解组合图像检索中的噪声对应
- 兼容表示和压缩索引兼顾系统更新成本与检索效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261124] Teaching Time Without Losing General Retrieval: Adapting Multimodal Embeddings for Time-Sensitive Video Retrieval | Oyama Toya, Lienhart Rainer, Satoh Shin'ichi | The University of Tokyo；National Institute of Informatics；University of Augsburg | 通过时间敏感适配与时间硬负样本，在保留通用能力下改进视频检索。 | [#800](https://github.com/Larry2000error/Larry-PaperClaw/issues/800) |
| [20261124] CREDIT: Compositional Reliability Learning for Noisy Composed Image Retrieval | Zhou Tiancai, Li Yongxiang, Liu Suimei, Yuan Zhong, Peng Dezhong, Peng Xi, Wang Xu | College of Computer Science, Sichuan University；School of Computing and Artificial Intelligence, Southwest Jiaotong University；School of Artificial Intelligence, Sichuan University | 以组合可靠性学习评估噪声三元组中的语义可信度，提升组合图像检索。 | [#801](https://github.com/Larry2000error/Larry-PaperClaw/issues/801) |
| [20261124] OmniEVIE: Evidence-Vector-Informed Embedding for Multi-modal Retrieval | Wang Zifei, Wen Wei, Ji Qiang, Zhang Qian-Wen, Qiao Ruizhi, Liu He, Sun Xing, Lin Qiang | Tencent IMA Product Center；Tencent Youtu Lab | 利用证据向量、多向量嵌入与三阶段流程，兼顾证据定位和压缩索引。 | [#802](https://github.com/Larry2000error/Larry-PaperClaw/issues/802) |
| [20261124] RELAY: Learning Compatible Representations One Encoder at a Time | Wang Yu, Qin Chuan, Zhang Qiang | Qwen Business Unit of Alibaba | 采用逐个编码器学习兼容表示，并以增量重编码降低跨模态检索更新负担。 | [#803](https://github.com/Larry2000error/Larry-PaperClaw/issues/803) |
| [20261124] Searching Ultra-Long Videos with Decision Models | Zhang Ce, Li Baiqi, Ha Seongsu, Bertasius Gedas | University of North Carolina at Chapel Hill | 将决策模型用于超长视频搜索，通过多模态推理定位与查询相关的证据。 | [#807](https://github.com/Larry2000error/Larry-PaperClaw/issues/807) |

## 🔎 观察

- 本批论文高度集中于检索基础设施与表示学习，遥感场景应用并非主要议题。
- 研究评价应同时关注召回效果、索引成本及编码器升级后的兼容性。

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
