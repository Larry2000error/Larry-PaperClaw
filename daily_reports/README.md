# Daily Reports

最近三天日报（最新在前）：

# [20261119](./202611/20261119.md)
## 📌 今日概况

今日共检索候选论文 54 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

11月19日的两篇候选都关注视觉检索，但考察的问题不同。第一篇聚焦第一视角视频与文本检索，考察预训练接触的影响，指出检索表现改善并不意味着模型更能正确匹配动作与对象。第二篇面向文化遗产场景，从任务层面梳理历史图像检索中的偏差，议题涉及元数据补充。两篇均未直接研究遥感，不能据此概括遥感领域的整体趋势。

## ✨ 今日亮点

- 第一视角视频与文本检索表现改善，不代表动词与名词的绑定能力增强。
- 历史图像检索研究以任务为单位梳理偏差，涉及文化遗产场景。
- 两篇分别关注预训练接触与任务偏差，均未直接研究遥感影像。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261119] Better Retrieval, Not Better Binding: Pretraining Exposure in Egocentric Video Retrieval | Guo Yuqi, Wray Michael | University of Bristol | 研究考察预训练接触对第一视角视频与文本检索的影响，发现检索改善未伴随动词与名词绑定能力提升。 | [#711](https://github.com/Larry2000error/Larry-PaperClaw/issues/711) |
| [20261119] A Task-Level Bias Taxonomy for Historical Image Retrieval | Gavali Omkar, Sebastian Ratan, Rippe Christoph, Ewerth Ralph, Hoppe Anett | Philipps-Universität Marburg；TIB – Leibniz Information Centre for Science and Technology；L3S Research Center, Leibniz University Hannover；Goethe University Frankfurt, University Library；Hessian Center for Artificial Intelligence (hessian.AI) | 研究为文化遗产场景中的历史图像检索提出任务层面的偏差分类，议题涉及元数据补充。 | [#712](https://github.com/Larry2000error/Larry-PaperClaw/issues/712) |

## 🔎 观察

- 整体检索指标不足以判断模型能否正确匹配动作与对象，组合语义理解应单独评估。
- 遥感检索评估可借鉴任务级偏差分类，但元数据偏差是否影响结果，仍需用遥感数据验证。

---

Powered by OpenClaw🦞

---

# [20261118](./202611/20261118.md)
## 📌 今日概况

今日共检索候选论文 51 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

11月18日入选的四项研究涵盖跨视角视频理解、视觉检索、神经信号到图像检索和无地图视觉定位。前三项分别从多视角预测、结构与细节的迭代聚合、频域先验与自适应监督入手，探讨如何学习或对齐表征。定位研究则关注参考图像位姿已知时，学习式三维模型能提供哪些额外信息。这些研究可为遥感中的多视角分析与检索提供方法参考，但候选信息未报告遥感场景的验证结果。

## ✨ 今日亮点

- 多视角预测用于视频编码器后训练，面向跨视角理解。
- 两项检索研究分别关注结构与细节聚合、神经信号与图像对齐。
- 定位研究考察已知参考图像位姿时，学习式三维模型的额外作用。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261118] MV-JEPA: Post-Training Video Encoders for Cross-View Understanding | Zhao Yangchen, Payani Ali, Ding Caiwen | University of Minnesota, Twin Cities；Cisco | 通过多视角预测开展视频编码器后训练，以掩码潜在表征预测支持跨视角理解。 | [#706](https://github.com/Larry2000error/Larry-PaperClaw/issues/706) |
| [20261118] One Affinity, Two Axes: Bidirectional Slot Attention for Iterative Aggregation across the Structure--Detail Spectrum in Visual Retrieval | Wang Zihang, Zhu Wenkai, Kong Lingdong, Yan Teng, Liang Alan, Li Shuyuan, Chen Xieyuanli, Kong Dong, Zong Guanyu | Southeast University；National University of Singapore；The Hong Kong University of Science and Technology (Guangzhou)；Shanghai Innovation Institute；Shandong University of Science and Technology；National University of Defense Technology | 采用双向槽注意力迭代聚合结构与细节特征，构建用于视觉检索的全局描述符。 | [#707](https://github.com/Larry2000error/Larry-PaperClaw/issues/707) |
| [20261118] Stabilizing Neural-to-Image Retrieval with Frequency-Domain Priors and Adaptive Supervision | Liu YaoYang, Tang ZhuoShi, Lai Haopeng, Sun Weijun, Fang Xiaozhao, Wen Jie | Institution unavailable | 结合频域先验与自适应监督，旨在提高从神经信号到图像检索的稳定性。 | [#708](https://github.com/Larry2000error/Larry-PaperClaw/issues/708) |
| [20261118] What Do Learned 3D Models Add to Localization from Posed References? | Kim Jaehyun, Kang Wonseok, Lee Jeongmin, Kim Tae-Wan | Seoul National University；DeepFine Co., Ltd. | 考察在参考图像位姿已知时，学习式三维模型能为无地图视觉定位提供什么。 | [#709](https://github.com/Larry2000error/Larry-PaperClaw/issues/709) |

## 🔎 观察

- 跨视角理解与无地图定位都涉及视角变化，但前者关注视频表征，后者关注几何位姿估计。
- 两项检索研究处理的问题不同：一项要兼顾图像结构与细节，另一项要对齐神经信号与图像。

---

Powered by OpenClaw🦞

---

# [20261117](./202611/20261117.md)
## 📌 今日概况

今日共检索候选论文 49 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

11月17日的六篇候选论文主要围绕视觉定位、内容检索和视频时刻定位展开。定位方向分别关注彩色点云中的位姿精炼，以及通过场景感知提示和局部特征增强改善地点识别效率。检索任务涉及对话中的表情包、手术视频和图像局部区域，另有研究用反事实事件验证核查视频时刻定位的证据。清单未明确列出以遥感影像为对象的研究。

## ✨ 今日亮点

- 视觉定位研究分别关注彩色点云中的位姿估计与视觉地点识别效率。
- 手术视频检索引入多领域基准，覆盖手术场景和流程两类任务。
- 视频时刻定位引入反事实事件验证，局部图像检索采用冻结的视觉语言模型。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261117] CARE: Conversational Affective Response Retrieval for Internet Memes | Li Jiajun, Zhang Leihan, Zhang Teng, Zhang Le, Yan Qiang | Beijing University of Posts and Telecommunications；Beijing Key Laboratory of Multimodal Data Intelligent Perception and Governance；Beijing Information Science and Technology University | 面向对话中的表情包检索，结合情感增强的视觉语言模型与门控融合。 | [#699](https://github.com/Larry2000error/Larry-PaperClaw/issues/699) |
| [20261117] Kolibri: Color Finds the Place, Refinement Sets the Pose for RGB-D Localization in Colored Point Clouds | Aguilar Leonel, Tuncay Bartu, Hoelscher Christoph | Chair of Cognitive Science, ETH Zürich | 利用彩色点云中的颜色信息识别地点，再通过几何精炼估计相机位姿。 | [#700](https://github.com/Larry2000error/Larry-PaperClaw/issues/700) |
| [20261117] OVET-Consensus: Rank-Preserving Counterfactual Event Verification for Video Moment Grounding | Osmanli Alibay, Gong Shaogang | Queen Mary University of London | 用反事实事件验证核查视频时刻定位的时间证据，并以保留原有排序为重排原则。 | [#701](https://github.com/Larry2000error/Larry-PaperClaw/issues/701) |
| [20261117] SurgCBVR: A Multi-Domain Benchmark for Content-Based Surgical Video-to-Video Retrieval | Eslami Mohammad, Moradi Mousa, Ghamsarian Negin, Zebardast Nazlee, Jennifer L Lindsey, Sophia Y. Wang, Sobrin Lucia, Rishi P Singh, Elze Tobias | Harvard Medical School；Stanford University；University of Bern | 构建多领域手术视频检索基准，涵盖基于视频内容的手术场景与流程检索。 | [#702](https://github.com/Larry2000error/Larry-PaperClaw/issues/702) |
| [20261117] EfficientVPR: Toward Efficient Visual Place Recognition via Scene-Aware Prompt Tuning and Adaptive Feature Enhancement | Tang Wenjing, Yang Chuanguang, An Zhulin, Huang Libo, Xu Yongjun | State Key Laboratory of AI Safety, Institute of Computing Technology, Chinese Academy of Sciences；University of Chinese Academy of Sciences | 采用场景感知提示微调与自适应局部特征增强，旨在提高视觉地点识别效率。 | [#703](https://github.com/Larry2000error/Larry-PaperClaw/issues/703) |
| [20261117] LoCaR: Localized Canvas Retrieval With Frozen Vision-Language Model | Hossain Rahim, Saha Dipanwita, Mishra Ashirbad, Shu Xinxin, Strunjas Svetlana, Li Binbin | eBay Inc.；Binghamton University | 利用冻结的视觉语言模型与候选图像区域，实现无需额外训练的局部文本到图像检索。 | [#704](https://github.com/Larry2000error/Larry-PaperClaw/issues/704) |

## 🔎 观察

- 地点识别回答在哪里，位姿估计还需确定朝向，两类任务不宜仅按识别效率比较。
- 区域检索和时刻定位都依赖局部证据，但仅凭候选信息尚无法判断这些方法能否迁移到遥感场景。

---

Powered by OpenClaw🦞

---
