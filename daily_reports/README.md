# Daily Reports

最近三天日报（最新在前）：

# [20260710](./202607/20260710.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦跨视角匹配与重识别技术，涵盖动物、行人及室内导航场景。研究趋势显示：一是视觉-语言模型与参数高效微调结合，利用元数据增强泛化能力；二是双曲空间表征与自训练策略成为解决跨域、跨视角对齐问题的新方向。

## ✨ 今日亮点

- CLIP参数高效适配结合连续元数据条件，提升动物重识别泛化性
- 双曲层级表征融合多粒度特征，解决航拍-地面行人跨视角匹配难题
- 弹性匹配与自适应净化机制稳定自训练，优化无监督跨视角地理定位

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260710] Parameter-Efficient Vision-Language Adaptation with Continuous Metadata Conditioning for Animal Re-Identification | Anil Osman Tur, Tonje Knutsen Sordalen, Kim Tallaksen Halvorsen, Beyan Cigdem | Department of Computer Science, University of Verona；Institute of Marine Research；University of Agder, Centre for Coastal Research | 提出连续元数据条件化的参数高效视觉-语言适配方法，用于动物重识别任务。 | [#328](https://github.com/Larry2000error/Larry-PaperClaw/issues/328) |
| [20260710] REMIND: RE-Identification with Memory for INDoor Navigation | Diaz-Pereda Pablo, Rodriguez-Ramos Alejandro, Perez-Saura David, Campoy Pascual | Institution unavailable | REMIND框架融合视觉记忆与DINOv3特征，支持室内导航中的多目标跟踪与重识别。 | [#329](https://github.com/Larry2000error/Larry-PaperClaw/issues/329) |
| [20260710] HiHR: Hierarchical Hyperbolic Representation for Aerial-Ground Person Re-Identification | Yang Qiwei, Zhang Pingping | Dalian University of Technology | HiHR构建层级双曲表征空间，实现航拍与地面视角下行人的跨视图精准匹配。 | [#330](https://github.com/Larry2000error/Larry-PaperClaw/issues/330) |
| [20260710] STEAM: Stable Self-Training with Elastic Matching and Adaptive Purification | Wang Shaoxiang, Zhang Kejia, Pan Haiwei, Zhang Lan | Harbin Engineering University, School of Computer Science and Technology；Northeast Forestry University, School of Computer and Artificial Intelligence | STEAM通过弹性匹配与自适应净化稳定自训练过程，提升无监督跨视图地理定位性能。 | [#331](https://github.com/Larry2000error/Larry-PaperClaw/issues/331) |

## 🔎 观察

- 重识别任务正从单一模态向视觉-语言融合演进，元数据驱动成为提升域泛化的关键路径。
- 双曲几何与自训练技术的引入，反映领域对复杂跨视角几何关系建模与标签噪声鲁棒性的双重关注。

---

Powered by OpenClaw🦞

---

# [20260709](./202607/20260709.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日研究聚焦多查询车辆重识别领域，提出增强视图专家混合架构。该工作通过对比学习与跨视图融合技术，结合大规模基准数据集构建，推动智能交通监控系统中车辆身份匹配技术的实用化进展。

## ✨ 今日亮点

- 提出增强视图专家混合网络，实现多查询条件下的鲁棒车辆重识别
- 构建大规模多查询车辆重识别基准数据集，填补领域数据空白
- 融合对比学习与跨视图特征融合，提升复杂场景下的识别精度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260709] Mixture of Enhanced-View Experts for Multi-Query Vehicle ReID and A Large-Scale Benchmark | Zheng Aihua, Zhen Jie, Li Chenglong, Wang Jiaxiang, Tang Jin | Institution unavailable | 该研究提出增强视图专家混合架构，结合多查询学习与跨视图融合，解决车辆重识别中视角变化与遮挡难题，并发布大规模基准数据集。 | [#326](https://github.com/Larry2000error/Larry-PaperClaw/issues/326) |

## 🔎 观察

- 多查询学习范式正成为车辆重识别的新方向，反映实际监控场景对非理想输入的适应性需求
- 专家混合架构与对比学习的结合显示，模块化设计在跨域视觉任务中仍具显著潜力

---

Powered by OpenClaw🦞

---

# [20260707](./202607/20260707.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 3 篇。

今日遥感AI相关研究聚焦跨模态检索与不确定性量化，涵盖遥感图像-文本检索、细粒度图像哈希及多模态推荐。证据学习、频率感知与关系建模成为关键技术路径，显示领域对检索精度与可靠性的双重追求。

## ✨ 今日亮点

- 证据学习首次引入遥感跨模态检索，实现不确定性显式建模
- RFHNet融合关系建模与频率感知，突破细粒度食品图像哈希瓶颈
- 时序重排机制优化视频-音乐推荐，强化语义-时序联合对齐

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260707] RFHNet: Relational and Frequency-Aware Hashing Network for Large-Scale Fine-Grained Food Image Retrieval | Wang Junsong, Min Weiqing, Sheng Guorui, Yao Tao, Wang Lili, Jiang Shuqiang | College of Computer Science and Artificial Intelligence, Ludong University；Institute of Computing Technology, Chinese Academy of Sciences；University of Chinese Academy of Sciences | RFHNet通过关系与频率感知哈希网络，解决大规模细粒度食品图像检索中的特征判别性不足问题。 | [#322](https://github.com/Larry2000error/Larry-PaperClaw/issues/322) |
| [20260707] Uncertainty-Aware Cross-Modal Remote Sensing Image-Text Retrieval via Evidential Learning | Wang Zhuoyue, Wang Xueqian, Li Gang, Li Chengxi, Liu Yongpan, Ban Yifang | Institution unavailable | 基于证据学习的遥感图像-文本检索方法，首次在跨模态匹配中引入不确定性量化，提升检索可靠性。 | [#323](https://github.com/Larry2000error/Larry-PaperClaw/issues/323) |
| [20260707] Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal Reranking | Doh Seungheon, Lee Minhee, Lee Sangmoon, Ben Sangbae Chon, Nam Juhan | Korea Advanced Institute of Science and Technology；Kakao Entertainment Corp. | 多模态视频-音乐推荐系统采用语义检索与时序重排两阶段策略，实现音视频内容精准对齐。 | [#324](https://github.com/Larry2000error/Larry-PaperClaw/issues/324) |

## 🔎 观察

- 证据学习从计算机视觉基础任务向遥感专用场景渗透，反映领域对模型可信度评估的迫切需求
- 细粒度检索与跨模态任务持续涌现频率域与时序维度创新，表明特征空间扩展成为提升性能的关键方向

---

Powered by OpenClaw🦞

---
