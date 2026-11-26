# Daily Reports

最近三天日报（最新在前）：

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

# [20261121](./202611/20261121.md)
## 📌 今日概况

今日共检索候选论文 25 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

2026年11月21日候选论文仅一篇，来自悉尼大学计算机学院，聚焦无配对视觉-语言对齐问题。该研究提出ConsensusAlign思路，以编码器集合替代单一编码器，借助集体共识与共享嵌入空间中的特征几何结构，提升跨模态对齐的可靠性。该方向与遥感场景相关：遥感图文配对数据稀缺，降低对成对监督的依赖具有实际价值。单日样本量有限，不足以判断更宏观的趋势走向。

## ✨ 今日亮点

- 提出ConsensusAlign：编码器集合支撑无配对视觉-语言对齐
- 从成对监督转向集体共识，缓解跨模态对齐对配对数据的依赖
- 利用共享嵌入空间的特征几何结构，提升无配对对齐可靠性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261121] From Pairwise to Collective: Encoder Collections Make Unpaired Vision-Language Alignment Reliable | Yin Xuanhua, Mao Shunqi, Xu Chuanzhi, Wei Boyu, Guo Wei, Cai Weidong | School of Computer Science, The University of Sydney | 提出ConsensusAlign，以编码器集合共识替代成对监督，实现可靠的无配对视觉-语言对齐 | [#780](https://github.com/Larry2000error/Larry-PaperClaw/issues/780) |

## 🔎 观察

- 今日候选仅一篇且偏基础方法研究，样本量过小，趋势性结论需谨慎对待
- 遥感图文配对天然稀缺，无配对对齐若可靠落地，可降低跨模态检索与解译的标注成本

---

Powered by OpenClaw🦞

---
