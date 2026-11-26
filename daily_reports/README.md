# Daily Reports

最近三天日报（最新在前）：

# [20261123](./202611/20261123.md)
## 📌 今日概况

今日共检索候选论文 23 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日8篇论文集中于检索与定位主题：无人机视频-文本数据集、跨视角地理定位、行人重识别重排序与视频时刻检索占据主要篇幅。方法层面呈现证据对齐趋势，如查询自适应证据对齐、语义验证渐进细化，以及将评测协议效应与时空证据分离的反思性研究。同时，训练自由的智能体式检索和像素级统一嵌入表明多模态检索范式仍在快速演化。

## ✨ 今日亮点

- AirVT-15k发布万级无人机双语视频-文本数据集并配套查询自适应对齐网络
- RigidAnchor以迭代平面刚性对齐实现GNSS拒止下无人机跨视角定位
- 训练自由的智能体框架将视频语料时刻检索交给VLM与LLM协同规划

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261123] AirVT-15k: A Query-Diverse UAV Video-Text Dataset and Query-Adaptive Evidence Alignment Network for Retrieval | Chen Xi, Chen Xu, Jia Xiangyang, Gan Ting, Zhang Xu, Wei Shuquan | Institution unavailable | 提出AirVT-15k无人机视频-文本数据集，含多样查询双语描述，并用查询自适应证据对齐网络改进检索 | [#788](https://github.com/Larry2000error/Larry-PaperClaw/issues/788) |
| [20261123] SafeRank-ReID: Candidate-Conditioned Re-Ranking under Identity Conflicts for Multimodal Person Re-Identification | Wang Yizhi, Li Zixuan, Chen Zhuwen, Qin Feiwei | Hangzhou Dianzi University | 针对多模态行人重识别的身份冲突，用候选条件化重排序做证据仲裁并评估模态可靠性 | [#789](https://github.com/Larry2000error/Larry-PaperClaw/issues/789) |
| [20261123] RigidAnchor: Cross-View Geo-Localization for UAV via Iterative Planar Rigid Alignment | Wang Bo, Zhu Dekang, Li Jian, Meng Zhipeng, Wang Bo, Hu Dewen | National Innovation Institute of Defense Technology；College of Intelligence Science and Technology, National University of Defense Technology；School of Future Technology, National University of Defense Technology | 面向GNSS拒止的无人机导航，以迭代平面刚性对齐完成卫星影像跨视角地理定位 | [#790](https://github.com/Larry2000error/Larry-PaperClaw/issues/790) |
| [20261123] Separating Protocol Effects from Spatio-Temporal Evidence in Person Re-Identification Re-Ranking | Mochamad Rizal Fauzan, Doan Pham Thao Nhu, Konthoujam Jeslin, Hongjirakul Purit, Chawla Lakshay | National Taipei University of Technology | 将评估协议效应与时空证据分离，分析重排序中同摄像头惩罚等先验的真实贡献 | [#791](https://github.com/Larry2000error/Larry-PaperClaw/issues/791) |
| [20261123] Pixel as the Common Language: Unified Multimodal Embedding via Visual Rendering | Yuan Xu, Wu Pangjing, Fan Wenqi, Li Qing | The Hong Kong Polytechnic University | 以像素为通用语言，通过视觉渲染把多模态输入统一编码为共享嵌入用于检索 | [#792](https://github.com/Larry2000error/Larry-PaperClaw/issues/792) |
| [20261123] Bi-Refine: Semantic Verification-Guided Progressive Refinement for Moment Retrieval | Liu Mengnan, Zhou Sanping, Xia Kun, Lin Jiaxuan, Wu Yuxuan, Hua Gang | National Key Laboratory of Human-Machine Hybrid Augmented Intelligence, Xi'an Jiaotong University；School of Artificial Intelligence, Xi'an Jiaotong University；School of Computer Science and Technology, Xi'an Jiaotong University；Amazon Alexa AI | 用语义验证引导的渐进细化做视频时刻检索，双向迭代精化时序定位结果 | [#793](https://github.com/Larry2000error/Larry-PaperClaw/issues/793) |
| [20261123] Teaching How to Reason, Beyond What to Answer: Evidence-Faithful On-Policy Distillation for streaming video understanding | Liu Mengnan, Zhou Sanping, Xia Kun, Lin Jiaxuan, Hua Gang, Wang Le | Institution unavailable | 面向流式视频理解的在线策略蒸馏，强调证据忠实的推理过程而非仅答案本身 | [#794](https://github.com/Larry2000error/Larry-PaperClaw/issues/794) |
| [20261123] Towards Agentic Video Corpus Moment Retrieval | Xu Chenwei, Wu Shang, Pan Zhenyu, Zhang Jianshu, Maneriker Pranav, Lu Lie, Du Fan, Li Manling, Liu Han | Northwestern University；Dolby | 提出训练自由的智能体视频语料时刻检索框架，由VLM与LLM协同完成库级检索 | [#795](https://github.com/Larry2000error/Larry-PaperClaw/issues/795) |

## 🔎 观察

- 重排序研究开始反思评测协议本身，提示部分提升可能源于设定差异而非方法创新
- 无人机方向集中于图文检索与地理定位两条线，但机构信息与数据可复现性披露仍偏弱

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
