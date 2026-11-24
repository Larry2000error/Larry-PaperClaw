# Daily Reports

最近三天日报（最新在前）：

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

# [20261110](./202611/20261110.md)
## 📌 今日概况

今日共检索候选论文 27 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

11月10日的候选列表仅收录一篇论文，聚焦如何在不同传感器拍摄的遥感影像中找出同一场景。RS-JEPA将自监督学习与联合嵌入预测结合，通过改变同一图像中各图像块的读取顺序来构造训练视图，并让不同传感器共用同一个编码器。这项研究展示了如何利用读取顺序设计训练任务，但单篇论文不足以判断整个领域的研究走向。 ([arxiv.org](https://arxiv.org/abs/2611.14496?utm_source=openai))

## ✨ 今日亮点

- 研究聚焦跨传感器检索，目标是在不同遥感影像中找出同一场景。
- 同一图像保留原有像素，通过改变图像块的读取顺序构造不同视图。
- 不同传感器的影像共用视觉编码器，并以联合嵌入预测进行自监督训练。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261110] RS-JEPA: Remote Sensing Joint-Embedding Predictive Architecture with Scan-Path Views for Cross-Sensor Image Retrieval | Rachamalla Tanishq, Kaushik Srishti, Muhammad Attique Khan, Camps-Valls Gustau, Swalpa Kumar Roy | Prince Mohammad Bin Fahd University；Universitat de València；Tezpur University | RS-JEPA利用扫描路径视图进行自监督联合嵌入预测，用于跨传感器遥感影像检索。 | [#772](https://github.com/Larry2000error/Larry-PaperClaw/issues/772) |

## 🔎 观察

- 改变读取顺序就能构造不同视图，值得通过对照实验检验扫描路径本身的贡献。
- 无需人工标签不等于无需成对数据，训练仍依赖已配准的跨传感器影像。

---

Powered by OpenClaw🦞

---

# [20261109](./202611/20261109.md)
## 📌 今日概况

今日共检索候选论文 38 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

本期四篇候选中，两篇聚焦图像地理定位：一篇用位置表征和扩散模型预测坐标，另一篇融合图像序列特征，通过度量学习匹配不同视角。其余两篇分别研究零样本脑电到图像检索与无监督行人重识别，关注如何对齐不同模态的表征、如何缩小不同数据域的差异。就本期样本而言，地理定位是遥感相关主线，另外两篇可作为方法参考。

## ✨ 今日亮点

- 扩散定位研究将地理位置编码为潜空间表征，用于坐标预测。
- 跨视角定位结合注意力引导的序列特征融合与混合空间度量学习。
- 脑电检索与行人重识别分别关注跨模态对齐与跨域适应。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261109] X Marks the Spot: Diffusion for Image Geolocalization with Location Representations | Wei Brian, Hsu Chih-Chuan, Gao Tianyi, Cher Daniel, Xing Eric, Beaulieu Danielle, Jacobs Nathan | Washington University in St. Louis | 该研究将位置自编码器与潜空间扩散模型结合，用于从图像预测地理坐标。 | [#765](https://github.com/Larry2000error/Larry-PaperClaw/issues/765) |
| [20261109] Complementarity-Driven Dual-Teacher Hierarchical Alignment for Zero-Shot EEG-to-Image Retrieval | Wu Lukun, Li Jie, Ren Ziqi, Xia Ruiyang, Gao Yan, Gao Xinbo | p EncoderImage to combine their complementary visual representations for zero- EncoderTeacher centering softmax sg | 该研究通过双教师分层对齐利用互补视觉表征，用于零样本脑电到图像检索。 | [#766](https://github.com/Larry2000error/Larry-PaperClaw/issues/766) |
| [20261109] Attention-Guided Sequence Feature Fusion and Mixed-Space Metric Learning for Cross-View Image Sequence Geo-Localization | Wu Nan, Yang Chunfang, Li Jiangshan, Luo Xiangyang | Institution unavailable | 该研究以注意力融合序列特征，并在混合空间中学习匹配度量，用于跨视角图像序列地理定位。 | [#767](https://github.com/Larry2000error/Larry-PaperClaw/issues/767) |
| [20261109] MDA framework: multi-architecture domain adaptation for unsupervised person re-identification | Zhang Wei, Ye Peijun, Chen Dihu, Su Tao | School of Electronics and Information Technology, Sun Yat-sen University；Peng Cheng Laboratory；School of Integrated Circuits, Sun Yat-sen University | 该研究提出多架构域适应框架，旨在缩小无监督行人重识别中的域间差异。 | [#768](https://github.com/Larry2000error/Larry-PaperClaw/issues/768) |

## 🔎 观察

- 坐标预测与跨视角序列匹配的任务设定不同，比较两条路线前应先明确评估口径。
- 脑电检索与行人重识别可提供方法参考，但本期材料不足以判断这些方法能否迁移到遥感任务。

---

Powered by OpenClaw🦞

---
