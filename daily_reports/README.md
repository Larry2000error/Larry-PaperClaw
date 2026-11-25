# Daily Reports

最近三天日报（最新在前）：

# [20261122](./202611/20261122.md)
## 📌 今日概况

今日共检索候选论文 31 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

11月22日的四篇候选中，两篇直接涉及遥感定位：一篇关注改变点击位置后，跨视角物体定位能否保持一致；另一篇利用语义神经场连续估计无人机位姿。其余两篇分别研究多物种动物个体重识别和病理全切片图像的跨倍率来源核验。就这批候选而言，值得关注的是视角、提示或放大倍率变化后，模型如何判断自己是否仍指向同一目标或位置。

## ✨ 今日亮点

- 跨视角物体定位关注点击位置变化时，结果能否保持一致。
- 无人机地理定位利用语义神经场连续估计位置和姿态。
- 病理切片的跨倍率核验关注放大图像在原图中的来源位置。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261122] ApexID: Hierarchical Learning for Multi-Species Animal Re-Identification | Elkerdany Seifeldin, ElBassat Mohamed, Abouelhamd Gamal, Elkady Assem, Ghoneim Jana, Mahmood Matin, Abigail Allen Martin, Gerard de Melo, Rueda-Toicen Antonio | Made In Alexandria AI Team (M.I.A Robotics)；Alamein International University；Alexandria University；hyper3labs；Universidade Federal de Mato Grosso；Hasso Plattner Institute | 通过分层学习开展多物种动物个体重识别，并在检索时考虑观测信息。 | [#783](https://github.com/Larry2000error/Larry-PaperClaw/issues/783) |
| [20261122] Prompt-Consistent Cross-View Object Geo-Localization | Xing Lingyun, Hao Wenning, Jiang Kai, Jin Dawei, Zhang Xiaohan, Zhang Xiaoxiong | Institution unavailable | 研究跨视角物体地理定位中的点击提示一致性，关注提示敏感性与捷径学习。 | [#784](https://github.com/Larry2000error/Larry-PaperClaw/issues/784) |
| [20261122] ContinuLoc: Continuous Pose Inference over Neural Fields for UAV Geo-Localization | Zhou Weikun, Lin Jinliang, Zang Yu, Xie Lin, Fu Haiqing, Ao Sheng, Yu Shangshu, Luo Zhiming, Wang Cheng | Xiamen University；Northeastern University | 利用语义神经场连续估计无人机位姿，并进行四自由度位姿优化。 | [#785](https://github.com/Larry2000error/Larry-PaperClaw/issues/785) |
| [20261122] Can an Agent Trust Its Own Zoom? Cross-Magnification Provenance Verification for Whole-Slide Images | Wang Yan, Song Yiran, Gong Zizhuo, Qi Jianxiang, Xu Zhongxing, Qian Lingfei, Lin Minquan | Yale University；University of Minnesota – Twin Cities；Monash University | 研究视觉智能体如何跨倍率核验病理全切片图像中放大区域的来源位置。 | [#786](https://github.com/Larry2000error/Larry-PaperClaw/issues/786) |

## 🔎 观察

- 单次定位正确不代表结果对点击位置的变化不敏感，准确性和提示一致性值得分开评估。
- 病理图像的跨倍率核验与遥感图像的尺度对齐有相似之处，但方法能否迁移仍需验证。

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

# [20261120](./202611/20261120.md)
## 📌 今日概况

今日共检索候选论文 31 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

11月20日的三篇候选论文均聚焦细粒度视觉检索，分别研究如何从视频库中定位片段、从版面丰富的文档中检索相关区域，以及从外观近似的雕塑中找出同一实例。三篇论文的共同点是把匹配目标细化到片段、区域或实例，而不只判断整段视频、整页文档或物体类别是否相关。候选中没有明确面向遥感的研究，因此不能据此概括当天的遥感研究趋势。

## ✨ 今日亮点

- 视频片段检索结合多种评分方法，并用转录文本引导重排序。
- 版面丰富的文档按内容划分区域，再用多向量检索寻找相关区域。
- 雕塑检索以外观近似的对象为重点，关注能否识别同一实例。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261120] DiTraR: Diverse Scorers and Transcript-Guided Re-ranking for Video Corpus Moment Retrieval | Mohammad Alijanpour Shalmani, Alale Rezvani Boroujeni, Amini Ali | University of Central Florida；Kaunas University of Technology | 该研究结合查询拆解、多种评分方法和转录文本引导的重排序，从视频库中定位相关片段。 | [#770](https://github.com/Larry2000error/Larry-PaperClaw/issues/770) |
| [20261120] When Visually Rich Documents Meet Multi-Vector Retrieval for Region-level Retrieval-Augmented Generation | Yuan Xu, Ning Liangbo, Ding Yujuan, Li Qing, Fan Wenqi | The Hong Kong Polytechnic University | 该研究结合按内容划分区域与多向量检索，为版面丰富的文档开展区域级检索增强生成。 | [#771](https://github.com/Larry2000error/Larry-PaperClaw/issues/771) |
| [20261120] Which Dwarf Is This? Doppeldwarf-306 and Near-Identical Instance Retrieval | Turhan Can Kargin | Institution unavailable | 该研究使用视觉特征和近邻搜索，考察能否从外观近似的雕塑中检索到同一实例。 | [#773](https://github.com/Larry2000error/Larry-PaperClaw/issues/773) |

## 🔎 观察

- 片段和区域检索重在找对位置，近似实例检索重在找对对象，评估时应区分这两类错误。
- 文档区域检索可为大幅遥感影像的局部查询提供思路，但能否迁移仍需用遥感数据验证。

---

Powered by OpenClaw🦞

---
