# Daily Reports

最近三天日报（最新在前）：

# [20261119](./202611/20261119.md)
## 📌 今日概况

今日共检索候选论文 54 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

11月19日的四篇候选主要关注视觉内容的检索与探索，没有直接面向遥感场景的论文。三篇检索研究分别考察预训练接触与动作和物体匹配的关系，梳理历史图像检索中的任务级偏差，以及学习更具区分性的通用多模态表示。另一篇从交互入手，用分层可视化支持视频探索。这组研究不只关注能否找得准，也关注模型理解了什么、检索存在哪些偏差，以及用户如何找到所需内容。

## ✨ 今日亮点

- 第一视角视频检索表现提升，不代表模型更懂得动作与物体的搭配。
- 历史图像检索按任务梳理偏差，通用多模态检索则关注表示的区分能力。
- 分层可视化用于交互式视频探索，帮助用户浏览并定位感兴趣的内容。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261119] Better Retrieval, Not Better Binding: Pretraining Exposure in Egocentric Video Retrieval | Guo Yuqi, Wray Michael | University of Bristol | 考察预训练接触对第一视角视频文本检索的影响，发现检索改善不等于动词与名词绑定能力提升。 | [#711](https://github.com/Larry2000error/Larry-PaperClaw/issues/711) |
| [20261119] A Task-Level Bias Taxonomy for Historical Image Retrieval | Gavali Omkar, Sebastian Ratan, Rippe Christoph, Ewerth Ralph, Hoppe Anett | Philipps-Universität Marburg；TIB – Leibniz Information Centre for Science and Technology；L3S Research Center, Leibniz University Hannover；Goethe University Frankfurt, University Library；Hessian Center for Artificial Intelligence (hessian.AI) | 提出历史图像检索的任务级偏差分类框架，用于梳理不同检索任务中可能出现的偏差。 | [#712](https://github.com/Larry2000error/Larry-PaperClaw/issues/712) |
| [20261119] DiLE: Discrimination-Aware Latent-Space Learning for Universal Multimodal Embeddings | Kang Ben, Wang Junda, Yuan Yuxuan, Li Hang, Liu Yuhan, Chen Xin, Geng Wanting, Lin Tong, Fu Pei, Wang Dong, Luan Jian, Lu Huchuan | Dalian University of Technology；Peking University；Xiaomi Inc；City University of Hong Kong | 提出注重区分能力的潜在空间学习方法，旨在构建适用于多种检索任务的通用多模态嵌入。 | [#722](https://github.com/Larry2000error/Larry-PaperClaw/issues/722) |
| [20261119] VideoTrail: Interactive Video Foraging Through Hierarchical Visualization | Yeh Catherine, Wang Bryan, Viégas Fernanda, Wattenberg Martin | Harvard University；Adobe Research | 提出基于分层可视化的交互系统，帮助用户在视频中浏览并寻找相关内容。 | [#724](https://github.com/Larry2000error/Larry-PaperClaw/issues/724) |

## 🔎 观察

- 整体检索得分不能替代对组合语义的专项评估，找对视频不等于理解其中的动作与物体关系。
- 历史图像检索的偏差分类可为遥感检索提供参考，但哪些偏差会重现仍需在遥感任务中验证。

---

Powered by OpenClaw🦞

---

# [20261118](./202611/20261118.md)
## 📌 今日概况

今日共检索候选论文 51 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

十一月十八日的四篇候选论文集中讨论如何利用不同来源的信息完成视觉理解、检索与定位。视频研究通过后训练探索跨视角理解，视觉检索研究尝试兼顾整体结构与局部细节，神经信号检索引入频域先验和自适应监督，定位研究则考察已知参考图像位姿时，学习式三维模型还能提供什么。对遥感而言，多视角影像匹配和影像检索是值得验证的方向，但候选条目未提供遥感验证结果。

## ✨ 今日亮点

- 视频编码器以后训练为切入点，探索如何理解不同视角下的内容。
- 两项检索研究分别关注图像特征融合与神经信号到图像的匹配。
- 无地图视觉定位研究聚焦学习式三维模型在已有位姿参考时的额外作用。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261118] MV-JEPA: Post-Training Video Encoders for Cross-View Understanding | Zhao Yangchen, Payani Ali, Ding Caiwen | University of Minnesota, Twin Cities；Cisco | 该研究以掩码潜表示预测对视频编码器进行多视角后训练，旨在改善跨视角理解。 | [#706](https://github.com/Larry2000error/Larry-PaperClaw/issues/706) |
| [20261118] One Affinity, Two Axes: Bidirectional Slot Attention for Iterative Aggregation across the Structure--Detail Spectrum in Visual Retrieval | Wang Zihang, Zhu Wenkai, Kong Lingdong, Yan Teng, Liang Alan, Li Shuyuan, Chen Xieyuanli, Kong Dong, Zong Guanyu | Southeast University；National University of Singapore；The Hong Kong University of Science and Technology (Guangzhou)；Shanghai Innovation Institute；Shandong University of Science and Technology；National University of Defense Technology | 该研究用双向槽注意力迭代聚合整体结构和局部细节，构建用于视觉检索的全局描述符。 | [#707](https://github.com/Larry2000error/Larry-PaperClaw/issues/707) |
| [20261118] Stabilizing Neural-to-Image Retrieval with Frequency-Domain Priors and Adaptive Supervision | Liu YaoYang, Tang ZhuoShi, Lai Haopeng, Sun Weijun, Fang Xiaozhao, Wen Jie | Institution unavailable | 该研究引入频域先验和自适应监督，旨在提高从脑电或脑磁信号检索图像的稳定性。 | [#708](https://github.com/Larry2000error/Larry-PaperClaw/issues/708) |
| [20261118] What Do Learned 3D Models Add to Localization from Posed References? | Kim Jaehyun, Kang Wonseok, Lee Jeongmin, Kim Tae-Wan | Seoul National University；DeepFine Co., Ltd. | 该研究考察参考图像位姿已知时，学习式三维模型能为无地图视觉定位提供哪些额外信息。 | [#709](https://github.com/Larry2000error/Larry-PaperClaw/issues/709) |

## 🔎 观察

- 跨视角视频理解与视觉定位都涉及视角变化，但理解同一场景不等于能准确估计相机位姿。
- 遥感可先验证这些方法能否用于同一传感器的多视角影像，再检验其能否跨传感器迁移。

---

Powered by OpenClaw🦞

---

# [20261117](./202611/20261117.md)
## 📌 今日概况

今日共检索候选论文 49 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

2026年11月17日的8篇候选论文以视觉定位和多模态检索为主。定位研究关注如何利用颜色与几何信息估计相机位姿，以及如何提高视觉地点识别效率。检索研究则关注图像局部区域、对话情绪和跨模态模型的向后兼容，并在手术视频和电商商品场景提出评测基准。候选中未见明确以遥感数据为对象的研究，因此这些主题只能作为相关方法参考，不能代表遥感领域的整体趋势。

## ✨ 今日亮点

- 视觉定位研究用颜色线索寻找位置，再通过几何配准细化位姿。
- 局部图文检索使用冻结的视觉语言模型，无需额外训练。
- 两项检索基准分别面向多域手术视频和需要推理的电商商品检索。

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261117] CARE: Conversational Affective Response Retrieval for Internet Memes | Li Jiajun, Zhang Leihan, Zhang Teng, Zhang Le, Yan Qiang | Beijing University of Posts and Telecommunications；Beijing Key Laboratory of Multimodal Data Intelligent Perception and Governance；Beijing Information Science and Technology University | 结合情绪增强的视觉语言模型与门控融合，为对话检索情绪相符的网络梗图。 | [#699](https://github.com/Larry2000error/Larry-PaperClaw/issues/699) |
| [20261117] Kolibri: Color Finds the Place, Refinement Sets the Pose for RGB-D Localization in Colored Point Clouds | Aguilar Leonel, Tuncay Bartu, Hoelscher Christoph | Chair of Cognitive Science, ETH Zürich | 借助颜色线索在彩色点云中寻找位置，再通过几何配准细化相机位姿。 | [#700](https://github.com/Larry2000error/Larry-PaperClaw/issues/700) |
| [20261117] OVET-Consensus: Rank-Preserving Counterfactual Event Verification for Video Moment Grounding | Osmanli Alibay, Gong Shaogang | Queen Mary University of London | 结合反事实事件验证与保序重排，利用时序证据定位视频中的目标片段。 | [#701](https://github.com/Larry2000error/Larry-PaperClaw/issues/701) |
| [20261117] SurgCBVR: A Multi-Domain Benchmark for Content-Based Surgical Video-to-Video Retrieval | Eslami Mohammad, Moradi Mousa, Ghamsarian Negin, Zebardast Nazlee, Jennifer L Lindsey, Sophia Y. Wang, Sobrin Lucia, Rishi P Singh, Elze Tobias | Harvard Medical School；Stanford University；University of Bern | 提出基于内容的多域手术视频检索基准，覆盖手术场景与手术流程检索。 | [#702](https://github.com/Larry2000error/Larry-PaperClaw/issues/702) |
| [20261117] EfficientVPR: Toward Efficient Visual Place Recognition via Scene-Aware Prompt Tuning and Adaptive Feature Enhancement | Tang Wenjing, Yang Chuanguang, An Zhulin, Huang Libo, Xu Yongjun | State Key Laboratory of AI Safety, Institute of Computing Technology, Chinese Academy of Sciences；University of Chinese Academy of Sciences | 结合场景感知提示调优与自适应局部特征增强，旨在提高视觉地点识别效率。 | [#703](https://github.com/Larry2000error/Larry-PaperClaw/issues/703) |
| [20261117] LoCaR: Localized Canvas Retrieval With Frozen Vision-Language Model | Hossain Rahim, Saha Dipanwita, Mishra Ashirbad, Shu Xinxin, Strunjas Svetlana, Li Binbin | eBay Inc.；Binghamton University | 使用冻结的视觉语言模型与候选图像区域，实现无需额外训练的局部图文检索。 | [#704](https://github.com/Larry2000error/Larry-PaperClaw/issues/704) |
| [20261117] VIBRA: Backward-Compatible Cross-Modal Retrieval with Consensus Barycenters | Yang Shubing, Liu Xutong, Zhao Dongfang | University of Washington | 利用共识重心与共识蒸馏，处理跨模态检索模型更新时的向后兼容问题。 | [#715](https://github.com/Larry2000error/Larry-PaperClaw/issues/715) |
| [20261117] MIPR: A Benchmark for Reasoning-Intensive Multimodal Intent-to-Product Retrieval with Multi-Category Solutions | Li Qiang, Lu Xuan, Ruan Jian, Lin Manxi, Chen Jiacheng, Shen Wen, Wei Zhihua, Shen Xiaoyu, Ou Dan, Kong Xiangheng, Zheng Junjun | Tongji University；Taobao & Tmall Group of Alibaba；Eastern Institute of Technology, Ningbo | 提出电商检索基准，评估从多模态意图出发、经推理检索多个品类商品的能力。 | [#717](https://github.com/Larry2000error/Larry-PaperClaw/issues/717) |

## 🔎 观察

- 局部图文检索和视频片段定位都把匹配粒度细化，但分别依赖空间区域和时间线索。
- 视觉定位方法可为遥感影像匹配提供思路，但能否适应视角与尺度变化，仍需在遥感数据上验证。

---

Powered by OpenClaw🦞

---
