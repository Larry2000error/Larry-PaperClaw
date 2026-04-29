# Daily Reports

最近三天日报（最新在前）：

# [20260424](./202604/20260424.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦多模态学习与视觉-语言模型的优化应用。联邦学习框架下的跨模态检索解决数据孤岛与模态缺失问题，CLIP特征聚合策略的重新设计则提升行人重识别在遮挡场景下的鲁棒性，体现从全局表征向局部细粒度建模的演进趋势。

## ✨ 今日亮点

- 联邦跨模态检索通过语义路由与个性化适配器解决模态缺失难题
- CLIP特征聚合从全局平均转向局部感知，增强遮挡行人识别能力
- 视觉-语言模型在检索与重识别任务中的特征工程持续深化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260424] Federated Cross-Modal Retrieval with Missing Modalities via Semantic Routing and Adapter Personalization | Zhou Hefeng, Liu Xuan, Chen Sicheng, Zhang Wutong, Yan Wu, Lou Jiong, Wu Chentao, Xue Guangtao, Zhao Wei, Li Jie | Shanghai Jiao Tong University；Shenzhen Univ of Advanced Technology；Hohai University | 提出语义路由与适配器个性化机制，实现联邦环境下缺失模态的跨模态检索，平衡全局知识共享与本地数据隐私。 | [#156](https://github.com/Larry2000error/Larry-PaperClaw/issues/156) |
| [20260424] From Global to Local: Rethinking CLIP Feature Aggregation for Person Re-Identification | Zheng Aotian, Sun Winston, Alattar Bahaa, Ablavsky Vitaly, Hwang Jenq-Neng | Department of Electrical and Computer Engineering, University of Washington；Applied Physics Laboratory, University of Washington | 重新设计CLIP特征聚合策略，从全局平均池化转向局部细粒度建模，显著提升遮挡场景下的行人重识别性能。 | [#157](https://github.com/Larry2000error/Larry-PaperClaw/issues/157) |

## 🔎 观察

- 跨模态检索正从集中式训练向联邦范式迁移，数据隐私与异构性成为核心挑战
- CLIP等视觉-语言模型的下游适配研究，正从直接应用转向特征聚合机制的精细化改造

---

Powered by OpenClaw🦞

---

# [20260423](./202604/20260423.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态检索的鲁棒性与对齐问题。三篇论文分别针对组合图像检索中的多修改场景、通用多模态检索的视觉模态坍缩，以及跨模态视频行人重识别的时序建模，核心共性在于通过新型对齐机制提升跨模态表征的稳定性与语义一致性。

## ✨ 今日亮点

- TEMA提出锚定图像-跟随文本策略，解决多修改组合检索中的实体映射难题
- MiMIC设计模态交互机制，在缓解视觉坍缩的同时避免语义错位
- 时序原型与层级对齐框架实现无监督跨模态视频行人重识别

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260423] TEMA: Anchor the Image, Follow the Text for Multi-Modification Composed Image Retrieval | Li Zixu, Hu Yupeng, Fu Zhiheng, Chen Zhiwei, Li Yongqi, Nie Liqiang | School of Software, Shandong University；Department of Computing, Hong Kong Polytechnic University；School of Computer Science and Technology, Harbin Institute of Technology (Shenzhen) | TEMA通过图像锚定与文本跟随的双流设计，处理组合图像检索中多属性修改的复杂查询对齐问题。 | [#152](https://github.com/Larry2000error/Larry-PaperClaw/issues/152) |
| [20260423] MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment | Li Juan, Ding Chuanghao, Zhang Xujie, Nguyen Cam-Tu | State Key Laboratory for Novel Software Technology, Nanjing University；School of Artificial Intelligence, Nanjing University | MiMIC提出模态交互约束与语义保持损失，在通用多模态检索中同时抑制视觉模态坍缩和跨模态语义偏移。 | [#153](https://github.com/Larry2000error/Larry-PaperClaw/issues/153) |
| [20260423] Temporal Prototyping and Hierarchical Alignment for Unsupervised Video-based Visible-Infrared Person Re-Identification | Li Zhiyong, Jiang Wei, Liu Haojie, Wang Mingyu, Xu Wanchong, Mao Weijie | Harbin Institute of Technology | 基于时序原型构建与层级特征对齐，实现无监督场景下可见光-红外视频行人重识别的跨模态身份关联。 | [#154](https://github.com/Larry2000error/Larry-PaperClaw/issues/154) |

## 🔎 观察

- 多模态检索正从单一查询向复杂组合查询演进，对细粒度语义对齐提出更高要求
- 视觉模态坍缩与语义错位成为通用多模态系统的关键瓶颈，需联合优化表征空间结构

---

Powered by OpenClaw🦞

---

# [20260422](./202604/20260422.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦跨模态检索与组合式视觉检索两大方向。武汉大学与BIGAI团队提出两阶段跨模态检索框架，山东大学与哈工深则针对噪声问题与零样本场景展开攻关，显示该领域正从单一模态对齐向复杂场景鲁棒性演进。

## ✨ 今日亮点

- Fast-then-Fine框架实现粗到细的多粒度跨模态对齐
- ConeSep网络通过锥形结构解决硬噪声对应学习难题
- UniCVR首次统一零样本组合图像与视频检索任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260422] Fast-then-Fine: A Two-Stage Framework with Multi-Granular Representation for Cross-Modal Retrieval in Remote Sensing | Chen Xi, Chen Xu, Jia Xiangyang, Zhang Xu, Wei Shuquan, Wang Wei | Wuhan University；Beijing Institute for General Artificial Intelligence (BIGAI) | Fast-then-Fine采用快速粗筛与精细对齐两阶段策略，提升遥感图像-文本检索效率与精度。 | [#18](https://github.com/Larry2000error/Larry-PaperClaw/issues/18) |
| [20260422] ConeSep: Cone-based Robust Noise-Unlearning Compositional Network for Composed Image Retrieval | Li Zixu, Hu Yupeng, Chen Zhiwei, Zhang Mingyu, Fu Zhiheng, Nie Liqiang | Shandong University；Harbin Institute of Technology (Shenzhen) | ConeSep提出锥形噪声遗忘网络，专门处理组合图像检索中的噪声三元组对应问题。 | [#19](https://github.com/Larry2000error/Larry-PaperClaw/issues/19) |
| [20260422] UniCVR: From Alignment to Reranking for Unified Zero-Shot Composed Visual Retrieval | Wen Haokun, Song Xuemeng, Zhang Haoyu, Zhao Xiangyu, Guan Weili, Nie Liqiang | Harbin Institute of Technology (Shenzhen)；Southern University of Science and Technology；City University of Hong Kong；Pengcheng Laboratory | UniCVR基于多模态大语言模型，实现零样本组合视觉检索从对齐到重排序的统一框架。 | [#20](https://github.com/Larry2000error/Larry-PaperClaw/issues/20) |

## 🔎 观察

- 组合式检索成为热点，三篇中有两篇聚焦该任务，反映用户对精细化视觉搜索需求上升。
- 噪声鲁棒性与零样本能力成关键挑战，显示实际部署中数据质量与泛化性瓶颈亟待突破。

---

Powered by OpenClaw🦞

---
