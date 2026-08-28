# Daily Reports

最近三天日报（最新在前）：

# [20260819](./202608/20260819.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦多模态检索与智能体决策两大方向。检索任务呈现从单一视觉匹配向知识增强、时序建模、判别推理演进的趋势；同时，强化学习驱动的主动地理定位探索了无人机场景下的好奇心奖励机制，体现遥感智能体研究的深化。

## ✨ 今日亮点

- 实体对齐检索突破视觉相似性局限，融合外部知识提升视觉问答能力
- 正交子空间建模实现历史图像时序表征，支持组合式跨时段检索
- 好奇心驱动奖励塑形优化无人机主动地理定位的探索效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260819] Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual Question Answering | Xu Hangrui, Wu Zhengxian, Yu Yunyao, Chen Zhuohong, Cong Rui, Deng Xiangwen, Liu Zhifang, Jiao Peng, Wang Haoqian | Shenzhen International Graduate School, Tsinghua University；University of Arizona | 提出实体对齐检索框架，通过知识图谱实体关联替代纯视觉匹配，解决知识型视觉问答中的语义鸿沟问题。 | [#432](https://github.com/Larry2000error/Larry-PaperClaw/issues/432) |
| [20260819] Composed Historical Image Retrieval by Modeling Temporal Representations | Adrià Molina Rodríguez, Oriol Ramos Terrades, Josep Lladós Canet | Centre de Visió per Computador；Universitat Autònoma de Barcelona；Computer Science Department | 构建时序正交子空间分解历史图像表征，实现时间条件与视觉内容的组合式检索，支持灵活的历史图像查询。 | [#433](https://github.com/Larry2000error/Larry-PaperClaw/issues/433) |
| [20260819] DynCur-Geo: Dynamic Curiosity Reward Shaping for Multimodal Active Geo-Localization | Sun Yiming, Zhang Yang, Zhu Pengfei | School of Automation, Southeast University | 设计动态好奇心奖励机制，引导无人机在主动地理定位中高效探索未知区域，提升定位成功率与效率。 | [#434](https://github.com/Larry2000error/Larry-PaperClaw/issues/434) |
| [20260819] UMER: Unifying Embedding and Ranking via Pair-Aware Discriminative Reasoning for Universal Multimodal Retrieval | Chen Libiao, Liu Xiyang, Wei Yanheng, Wang Tao, Tang Zhenyu | Beihang University | 统一嵌入学习与排序任务，通过成对判别推理与思维链增强多模态检索的泛化性与可解释性。 | [#435](https://github.com/Larry2000error/Larry-PaperClaw/issues/435) |

## 🔎 观察

- 多模态检索正从表征对齐迈向推理增强，链式思维与判别式学习的引入标志着检索任务认知深度的提升。
- 无人机主动地理定位与好奇心机制的结合，反映出遥感智能体研究从被动感知向主动决策的范式转变。

---

Powered by OpenClaw🦞

---

# [20260817](./202608/20260817.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦视觉定位与跨模态识别两大方向。视觉定位领域呈现从静态图像向视频序列、从粗粒度匹配向渐进式细粒度对齐的发展趋势；跨模态学习则关注可见光-红外场景下的行人重识别，强调多尺度特征分解与注意力机制的结合。数据集构建与真实环境适应性仍是关键挑战。

## ✨ 今日亮点

- YILDIZ-VPR发布密集覆盖、多环境条件的行人视角视觉定位数据集
- X²Localizer提出跨粒度渐进式跨视角视频地理定位框架
- 多尺度分解卷积网络优化可见光-红外跨模态行人重识别性能

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260817] YILDIZ-VPR: A Novel Dataset with Dense Coverage Under Diverse Environmental Conditions for Visual Place Recognition | Yildiz Serdar, Memiş Abbas, Varli Songül | Yildiz Technical University；Istanbul University；BILGEM, TUBITAK | YILDIZ-VPR构建了涵盖多样环境条件的密集覆盖行人视角视觉定位数据集，为VPR研究提供更贴近实际应用的基准。 | [#427](https://github.com/Larry2000error/Larry-PaperClaw/issues/427) |
| [20260817] X$^2$Localizer: Cross-grained Alignment for Progressive Cross-view Video Geo-localization | Zeng Zichao, Fan Weijia, Chen Yufan, June Moh Goo, Zheng Junwei, Liu Ruiping, Peng Kunyu, Zhang Jiaming, Stiefelhagen Rainer, Boehm Jan | University College London；Karlsruhe Institute of Technology；Hunan University；University of Alberta；Shenzhen University | X²Localizer通过跨粒度对齐机制实现渐进式跨视角视频地理定位，在有限时间预算下平衡检索效率与定位精度。 | [#428](https://github.com/Larry2000error/Larry-PaperClaw/issues/428) |
| [20260817] Multi-scale Decomposed Convolution Refinement Network for Visible-Infrared Person Re-Identification | Zheng Mingsheng, Jiang Zirui, Liu Bo, Chen Yupeng, Zhang Jun, Zhao Kai | School of Computer Science and Technology, Xinjiang University；Joint International Research Laboratory of Silk Road Multilingual Cognitive Computing, Xinjiang University | 多尺度分解卷积细化网络针对可见光-红外行人重识别任务，利用注意力机制与度量学习缓解模态差异问题。 | [#429](https://github.com/Larry2000error/Larry-PaperClaw/issues/429) |

## 🔎 观察

- 视觉定位研究正从单帧图像检索向时序视频理解演进，时间信息与渐进式推理成为提升定位精度的关键路径
- 跨模态行人重识别持续依赖多尺度特征学习与注意力机制，但现有方法在极端光照变化下的鲁棒性仍需验证

---

Powered by OpenClaw🦞

---

# [20260816](./202608/20260816.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究呈现两大方向：一是视觉语言基础模型的对齐优化，AlignJEPA提出预测式对齐新范式；二是面向体育视频的无训练多目标跟踪，强调相机运动补偿与重识别技术。整体趋势显示基础模型架构创新与特定场景高效推理并重。

## ✨ 今日亮点

- AlignJEPA融合JEPA预测架构与对比学习，实现遥感视觉语言基础模型的高效对齐
- 无训练长期多目标跟踪方案，通过相机运动补偿降低体育场景标注依赖
- ISRO与IIT Bombay等机构联合推进遥感大模型，强化印度空间技术自主能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260816] Training-Free Long-Term Multi-Object Tracking for Sports Video Analytics | Stanczyk Tomasz, Yoon Seongro, Bremond Francois | Inria；Université Côte d'Azur | 提出无需训练的长期多目标跟踪框架，结合相机运动补偿与重识别技术，专为体育视频分析设计。 | [#424](https://github.com/Larry2000error/Larry-PaperClaw/issues/424) |
| [20260816] AlignJEPA: Predictive Vision-Language Alignment for Remote Sensing Foundation Models | Md Aminur Hossain, Vaghasiya Omkumar, Rajeev Ranjan Dwivedi, Kurmi Vinod, Banerjee Biplab | Space Applications Centre, ISRO；CSRE, Indian Institute of Technology Bombay；Indian Institute of Science Education and Research (IISER) Bhopal | AlignJEPA将JEPA预测机制引入遥感视觉语言对齐，通过掩码预测与对比学习联合优化基础模型表征。 | [#425](https://github.com/Larry2000error/Larry-PaperClaw/issues/425) |

## 🔎 观察

- JEPA架构正从自然图像向遥感领域迁移，预测式学习或成为多模态遥感模型的新基线范式
- 无训练跟踪方案虽降低标注成本，但体育场景的剧烈相机运动对补偿算法鲁棒性提出更高要求

---

Powered by OpenClaw🦞

---
