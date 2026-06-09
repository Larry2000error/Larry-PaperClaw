# Daily Reports

最近三天日报（最新在前）：

# [20260604](./202606/20260604.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究呈现两大趋势：一是跨视角地理定位向非城市环境拓展，融合度量-语义原语匹配实现无GNSS导航；二是多模态大语言模型的可解释性研究，通过识别核心注意力头揭示功能稀疏性机制。两项工作分别从机器人定位鲁棒性与模型内部机理层面推进技术边界。

## ✨ 今日亮点

- Meridian提出度量-语义原语匹配框架，突破城市环境限制实现空地跨视角定位
- CoRe Heads机制揭示多模态LLM功能稀疏性，为模型压缩与效率优化提供新思路
- MIT与丰田研究院合作推动无GNSS导航技术，拓展地面机器人野外作业能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260604] Meridian: Metric-Semantic Primitive Matching for Cross-View Geo-Localization Beyond Urban Environments | Peterson Mason, Li Qingyuan, Jia Yixuan, Cladera Fernando, Nieto-Granda Carlos, Camillo Jose Taylor, Jonathan P. How | Massachusetts Institute of Technology；University of Pennsylvania；Toyota Research Institute | Meridian通过度量-语义原语匹配，将跨视角地理定位从城市拓展至野外等非结构化环境，支持无GNSS条件下的地面机器人定位。 | [#247](https://github.com/Larry2000error/Larry-PaperClaw/issues/247) |
| [20260604] Mechanistic Insights into Functional Sparsity in Multimodal LLMs via CoRe Heads | Sun Ruoxi, Qiu Quantong, Li Juntao, Tang Zecheng, Lou Yihang, Zhang Min | Soochow University；Peking University | 该研究提出CoRe Heads识别多模态LLM中承担跨模态检索的核心注意力头，揭示功能稀疏性机制并验证其可解释性价值。 | [#248](https://github.com/Larry2000error/Larry-PaperClaw/issues/248) |

## 🔎 观察

- 跨视角定位从城市向野外延伸，反映自动驾驶与野外机器人对无GNSS导航的迫切需求，语义-几何联合表征成为关键突破口。
- 多模态LLM可解释性研究从现象描述走向机制定位，核心子结构识别为模型轻量化与可信部署提供工程化路径。

---

Powered by OpenClaw🦞

---

# [20260603](./202606/20260603.md)
## 📌 今日概况

今日共检索候选论文 2 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦于跨视角图像检索与位姿估计的融合框架，以及基于属性关系的组合式图像检索。两项工作均致力于提升复杂场景下的视觉定位精度，体现了从单一模态向多模态协同、从粗粒度匹配向细粒度属性解耦的发展趋势。

## ✨ 今日亮点

- CIPER统一框架实现跨视角检索与位姿估计联合优化，提升 aerial-ground 匹配精度
- COMBINER引入属性邻居关系引导组合检索，强化多模态表征解耦能力
- 两项研究均来自亚洲团队，反映该区域在视觉定位领域的技术积累

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260603] CIPER: A Unified Framework for Cross-view Image-retrieval and Pose-estimation | Jeon Yurim, Seo Dongseong, Seo Seung-Woo | Seoul National University | CIPER提出统一框架，将跨视角图像检索与相机位姿估计联合建模，实现 aerial-ground 图像的端到端匹配与定位。 | [#244](https://github.com/Larry2000error/Larry-PaperClaw/issues/244) |
| [20260603] COMBINER: Composed Image Retrieval Guided by Attribute-based Neighbor Relations | Li Zixu, Hu Yupeng, Chen Zhiwei, Wen Haokun, Song Xuemeng, Nie Liqiang | Institution unavailable | COMBINER通过属性邻居关系引导组合式图像检索，解决参考图像与目标描述之间的细粒度对齐问题。 | [#245](https://github.com/Larry2000error/Larry-PaperClaw/issues/245) |

## 🔎 观察

- 跨视角地理定位正从独立任务走向联合优化，检索与位姿估计的协同设计或成新范式
- 属性解耦与邻居关系建模为组合检索提供新思路，但机构信息缺失提示需关注研究透明度

---

Powered by OpenClaw🦞

---

# [20260602](./202606/20260602.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日多模态检索研究呈现三大趋势：企业级RAG系统优化、噪声对应关系修正及跨模态检索新场景拓展。学术界与工业界协同推进文档理解与视觉-语言对齐技术，图神经网络与布局感知方法成为关键创新点。

## ✨ 今日亮点

- 企业级多模态RAG系统MM-BizRAG提出布局感知解析新范式
- 清华团队利用图神经网络修正跨模态噪声对应关系
- 越南学者探索人脸-发型混合模态检索新任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260602] Overview of the EReL@MIR 2025 Multimodal Document Retrieval Challenge (Track 1) | Mei Jingbiao | University of Cambridge | 剑桥大学主办的多模态文档检索挑战赛综述，聚焦视觉丰富文档的文本-图像检索基准建设。 | [#239](https://github.com/Larry2000error/Larry-PaperClaw/issues/239) |
| [20260602] MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&A | Bhathena Hanoz, Parin Rajesh Jhaveri, Mittal Rohan, Singh Prateek, Kallala Aymen, Kaur Rachneet, Jin Yiqiao, Zeng Zhen, Ratnaparkhi Adwait, Kochedykov Denis | JPMorgan Chase & Co.；Georgia Institute of Technology | 摩根大通联合佐治亚理工提出企业问答多模态RAG框架，强调文档结构理解与布局感知解析。 | [#240](https://github.com/Larry2000error/Larry-PaperClaw/issues/240) |
| [20260602] Intra-Modal Neighbors Never Lie: Rectifying Inter-Modal Noisy Correspondence via Graph-Based Intra-Modal Reasoning | Liu Yang, Feng Wentao, Huang Shu-Dong, Ye Yalan, Lv Jiancheng | Tsinghua University；Chinese Academy of Sciences | 清华与中科院提出基于图神经网络的模态内推理方法，解决跨模态检索中的噪声对应问题。 | [#241](https://github.com/Larry2000error/Larry-PaperClaw/issues/241) |
| [20260602] Mixed-Modality Dual Face-Hair Retrieval | Bui-Huynh Quoc-Anh, Lam Mai-Tuyen, Nguyen Dai-Anh-Tuan, Thanh Duc Ngo | Vietnam National University, Ho Chi Minh City；University of Information Technology, VNU-HCM, Ho Chi Minh City | 越南国立大学团队提出人脸-发型混合模态双重检索任务，探索图像跨模态学习新场景。 | [#242](https://github.com/Larry2000error/Larry-PaperClaw/issues/242) |

## 🔎 观察

- 工业界主导企业级RAG实用化研究，学术机构聚焦基础理论突破，形成互补格局
- 噪声鲁棒性与细粒度对齐成为跨模态检索核心挑战，图方法展现强建模潜力

---

Powered by OpenClaw🦞

---
