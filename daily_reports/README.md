# Daily Reports

最近三天日报（最新在前）：

# [20261124](./202611/20261124.md)
## 📌 今日概况

今日共检索候选论文 61 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日4篇工作集中于多模态与跨模态检索，重点从单纯提升匹配能力转向处理时间敏感性、噪声对应、证据定位和编码器迭代兼容。研究路线覆盖时间困难负样本、组合可靠性学习、多向量嵌入与压缩索引，以及分阶段重编码，反映检索系统正同时关注语义精度、索引效率和持续升级成本。

## ✨ 今日亮点

- 时间感知检索强调增强时序区分，同时维持通用检索能力。
- 可靠性建模被用于缓解组合图像检索中的噪声对应问题。
- 多向量证据表示与兼容编码成为检索系统演进的新方向。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261124] Teaching Time Without Losing General Retrieval: Adapting Multimodal Embeddings for Time-Sensitive Video Retrieval | Oyama Toya, Lienhart Rainer, Satoh Shin'ichi | The University of Tokyo；National Institute of Informatics；University of Augsburg | 通过时间困难负样本适配多模态嵌入，兼顾时序视频检索与通用检索。 | [#800](https://github.com/Larry2000error/Larry-PaperClaw/issues/800) |
| [20261124] CREDIT: Compositional Reliability Learning for Noisy Composed Image Retrieval | Zhou Tiancai, Li Yongxiang, Liu Suimei, Yuan Zhong, Peng Dezhong, Peng Xi, Wang Xu | College of Computer Science, Sichuan University；School of Computing and Artificial Intelligence, Southwest Jiaotong University；School of Artificial Intelligence, Sichuan University | 面向含噪组合图像检索，以组合可靠性学习评估语义对应关系。 | [#801](https://github.com/Larry2000error/Larry-PaperClaw/issues/801) |
| [20261124] OmniEVIE: Evidence-Vector-Informed Embedding for Multi-modal Retrieval | Wang Zifei, Wen Wei, Ji Qiang, Zhang Qian-Wen, Qiao Ruizhi, Liu He, Sun Xing, Lin Qiang | Tencent IMA Product Center；Tencent Youtu Lab | 利用证据向量、多向量嵌入和压缩索引支持分阶段多模态检索。 | [#802](https://github.com/Larry2000error/Larry-PaperClaw/issues/802) |
| [20261124] RELAY: Learning Compatible Representations One Encoder at a Time | Wang Yu, Qin Chuan, Zhang Qiang | Qwen Business Unit of Alibaba | 探索逐个更新编码器的兼容表示学习，降低跨模态系统重编码压力。 | [#803](https://github.com/Larry2000error/Larry-PaperClaw/issues/803) |

## 🔎 观察

- 今日候选主要属于通用多模态检索，对遥感的价值更偏方法迁移而非直接应用。
- 研究重心已从统一嵌入扩展至可靠性、局部证据和系统增量维护等工程约束。

---

Powered by OpenClaw🦞

---

# [20261123](./202611/20261123.md)
## 📌 今日概况

今日共检索候选论文 62 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日候选研究以“检索与对齐”为主线，覆盖无人机视频文本检索、跨视角地理定位、视频时刻检索、多模态行人重识别及医学图像检索。方法层面集中于查询自适应证据、候选条件重排序、渐进式语义验证、时空先验与表示去干扰；同时，多项工作关注评测协议、身份冲突、证据忠实性和组合泛化，显示研究正从提升匹配精度转向增强可靠性与真实场景适应能力。

## ✨ 今日亮点

- 无人机研究兼顾跨模态视频检索与无卫星导航条件下的跨视角定位。
- 行人重识别工作聚焦身份冲突、时空先验及类内表示多样性。
- 视频时刻检索开始引入语义验证、推理蒸馏与智能体式检索流程。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261123] AirVT-15k: A Query-Diverse UAV Video-Text Dataset and Query-Adaptive Evidence Alignment Network for Retrieval | Chen Xi, Chen Xu, Jia Xiangyang, Gan Ting, Zhang Xu, Wei Shuquan | Institution unavailable | 构建查询多样的双语无人机视频文本数据集，并研究查询自适应证据对齐。 | [#788](https://github.com/Larry2000error/Larry-PaperClaw/issues/788) |
| [20261123] SafeRank-ReID: Candidate-Conditioned Re-Ranking under Identity Conflicts for Multimodal Person Re-Identification | Wang Yizhi, Li Zixuan, Chen Zhuwen, Qin Feiwei | Hangzhou Dianzi University | 面向多模态行人重识别中的身份冲突，探索候选条件重排序与证据仲裁。 | [#789](https://github.com/Larry2000error/Larry-PaperClaw/issues/789) |
| [20261123] RigidAnchor: Cross-View Geo-Localization for UAV via Iterative Planar Rigid Alignment | Wang Bo, Zhu Dekang, Li Jian, Meng Zhipeng, Wang Bo, Hu Dewen | National Innovation Institute of Defense Technology；College of Intelligence Science and Technology, National University of Defense Technology；School of Future Technology, National University of Defense Technology | 通过迭代平面刚性对齐实现无人机跨视角地理定位与位姿估计。 | [#790](https://github.com/Larry2000error/Larry-PaperClaw/issues/790) |
| [20261123] Separating Protocol Effects from Spatio-Temporal Evidence in Person Re-Identification Re-Ranking | Mochamad Rizal Fauzan, Doan Pham Thao Nhu, Konthoujam Jeslin, Hongjirakul Purit, Chawla Lakshay | National Taipei University of Technology | 区分评测协议效应与真实时空证据，分析行人重识别重排序的影响来源。 | [#791](https://github.com/Larry2000error/Larry-PaperClaw/issues/791) |
| [20261123] Bi-Refine: Semantic Verification-Guided Progressive Refinement for Moment Retrieval | Liu Mengnan, Zhou Sanping, Xia Kun, Lin Jiaxuan, Wu Yuxuan, Hua Gang | National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Xi'an Jiaotong University；School of Artificial Intelligence, Xi'an Jiaotong University；School of Computer Science and Technology, Xi'an Jiaotong University；Amazon Alexa AI | 利用语义验证引导渐进式细化，以改进视频时刻检索与时间定位。 | [#793](https://github.com/Larry2000error/Larry-PaperClaw/issues/793) |
| [20261123] Teaching How to Reason, Beyond What to Answer: Evidence-Faithful On-Policy Distillation for streaming video understanding | Liu Mengnan, Zhou Sanping, Xia Kun, Lin Jiaxuan, Hua Gang, Wang Le | Institution unavailable | 以证据忠实的在线策略蒸馏训练流式视频理解模型的推理过程。 | [#794](https://github.com/Larry2000error/Larry-PaperClaw/issues/794) |
| [20261123] Towards Agentic Video Corpus Moment Retrieval | Xu Chenwei, Wu Shang, Pan Zhenyu, Zhang Jianshu, Maneriker Pranav, Lu Lie, Du Fan, Li Manling, Liu Han | Northwestern University；Dolby | 探索结合视觉语言模型与大语言模型的免训练智能体式视频语料时刻检索。 | [#795](https://github.com/Larry2000error/Larry-PaperClaw/issues/795) |
| [20261123] A dataset of clinically similar image pairs from citation-linked case reports for medical image retrieval | Shmueli Guy, Keno K. Bressem, Hope Tom | School of Computer Science and Engineering, The Hebrew University of Jerusalem；National Center for Tumor Diseases West；Institute of Artificial Intelligence in Medicine, University Hospital Essen；Department of Diagnostic and Interventional Radiology, School of Medicine and Health, Technical University of Munich；Department of Diagnostic and Interventional Radiology and Neuroradiology, University Hospital Essen；Allen Institute for AI | 从引用关联病例报告中整理临床相似图像对，支持医学图像检索研究。 | [#797](https://github.com/Larry2000error/Larry-PaperClaw/issues/797) |
| [20261123] Intra-Class Diversity Loss for Person Re-Identification | Zhou Wei, Chen BaXian | Department of Artificial Intelligence, Guangzhou Huashang College | 引入类内多样性损失，研究行人重识别表示学习中的差异性保持。 | [#798](https://github.com/Larry2000error/Larry-PaperClaw/issues/798) |
| [20261123] Where Compositionality Hides: Shared-Content Interference in Vision-Language Retrieval | Anudeep Chimata, Harsh Vardhan Poddar | BITS Pilani, K. K. Birla Goa Campus | 分析共享内容对视觉语言组合检索的干扰，并探索嵌入投影处理方法。 | [#799](https://github.com/Larry2000error/Larry-PaperClaw/issues/799) |

## 🔎 观察

- 候选论文虽以检索任务居多，但核心问题正由相似度学习扩展到证据质量与决策可靠性。
- 遥感相关工作主要集中于无人机视频和跨视角定位，其余成果可提供跨模态检索方法借鉴。

---

Powered by OpenClaw🦞

---

# [20261122](./202611/20261122.md)
## 📌 今日概况

今日共检索候选论文 32 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日候选研究集中于细粒度识别与跨视角地理定位。ApexID以层次学习处理多物种动物重识别，并结合观测感知检索；另两项工作面向跨视角目标与无人机定位，分别关注提示一致性、点击点敏感性与捷径学习，以及基于语义神经场的连续位姿推断和四自由度优化。整体趋势是从单次匹配走向更稳健的条件建模与连续空间推理。

## ✨ 今日亮点

- 层次学习被用于统一多物种动物重识别与观测感知检索。
- 跨视角目标定位开始显式约束提示一致性并审视捷径学习。
- 语义神经场支持无人机定位中的连续位姿推断与四自由度优化。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261122] ApexID: Hierarchical Learning for Multi-Species Animal Re-Identification | Elkerdany Seifeldin, ElBassat Mohamed, Abouelhamd Gamal, Elkady Assem, Ghoneim Jana, Mahmood Matin, Abigail Allen Martin, Gerard de Melo, Rueda-Toicen Antonio | Made In Alexandria AI Team (M.I.A Robotics)；Alamein International University；Alexandria University；hyper3labs；Universidade Federal de Mato Grosso；Hasso Plattner Institute | ApexID通过层次学习与SphereFace2损失，探索多物种动物重识别及观测感知检索。 | [#783](https://github.com/Larry2000error/Larry-PaperClaw/issues/783) |
| [20261122] Prompt-Consistent Cross-View Object Geo-Localization | Xing Lingyun, Hao Wenning, Jiang Kai, Jin Dawei, Zhang Xiaohan, Zhang Xiaoxiong | Institution unavailable | 该研究面向跨视角目标地理定位，重点缓解点击点提示敏感性与捷径学习问题。 | [#784](https://github.com/Larry2000error/Larry-PaperClaw/issues/784) |
| [20261122] ContinuLoc: Continuous Pose Inference over Neural Fields for UAV Geo-Localization | Zhou Weikun, Lin Jinliang, Zang Yu, Xie Lin, Fu Haiqing, Ao Sheng, Yu Shangshu, Luo Zhiming, Wang Cheng | Xiamen University；Northeastern University | ContinuLoc结合语义神经场和全局视觉描述子，实现无人机四自由度连续位姿推断。 | [#785](https://github.com/Larry2000error/Larry-PaperClaw/issues/785) |

## 🔎 观察

- 三项工作均在削弱离散标签或单一匹配带来的脆弱性，强调结构化条件与连续推理。
- 跨视角定位正由描述子检索延伸至提示鲁棒性和可优化空间表示，但效果仍需实验数据验证。

---

Powered by OpenClaw🦞

---
