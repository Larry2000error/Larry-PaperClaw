# Daily Reports

最近三天日报（最新在前）：

# [20260428](./202604/20260428.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦多模态大模型与地理定位的交叉创新。三篇论文均涉及大模型技术：两篇探索全球图像地理定位新范式，分别提出双视角对比学习与网络规模检索增强方案；另一篇针对跨模态检索中的视觉忽略与语义漂移问题提出改进策略。工业界与学术界协同推进，显示该领域正从单一任务向系统级解决方案演进。

## ✨ 今日亮点

- DualGeo构建双视角框架，融合对比学习与地理聚类实现全球图像定位
- GeoSearch首创检索增强生成范式，整合反向图像搜索与网络级检索
- 百度团队揭示大模型跨模态检索缺陷，提出视觉显著性与语义对齐联合优化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260428] DualGeo: A Dual-View Framework for Worldwide Image Geo-localization | Cui Junchao, Shi Wenqi, Du Shaoyong, He Hang, Ma Xuanzi, Tang Hao, Luo Xiangyang | Henan Key Laboratory of Cyberspace Situation Awareness；Information Engineering University | DualGeo提出双视角地理定位框架，通过跨视角对比学习与地理感知聚类提升全球图像定位精度。 | [#160](https://github.com/Larry2000error/Larry-PaperClaw/issues/160) |
| [20260428] GeoSearch: Augmenting Worldwide Geolocalization with Web-Scale Reverse Image Search and Image Matching | Le-Duc Tung-Duong, Nguyen-Son Hoang-Quoc, Dao Minh-Son | University of Science, VNU-HCM；National Institute of Information and Communications Technology | GeoSearch将检索增强生成引入地理定位，结合网络规模反向图像搜索与特征匹配实现开放域定位。 | [#161](https://github.com/Larry2000error/Larry-PaperClaw/issues/161) |
| [20260428] Combating Visual Neglect and Semantic Drift in Large Multimodal Models for Enhanced Cross-Modal Retrieval | Zhang Guosheng, Liu Linkai, Wang Keyao, Yue Haixiao, Tan Zhiwen, Tan Xiao | Baidu Inc. | 针对大模型跨模态检索的视觉忽略与语义漂移问题，提出视觉显著性引导与语义锚定联合优化方法。 | [#162](https://github.com/Larry2000error/Larry-PaperClaw/issues/162) |

## 🔎 观察

- 图像地理定位正从传统视觉匹配转向'检索+生成'的混合架构，网络级数据源的利用成为关键差异化因素
- 工业界（百度）与学术机构同步关注大模型跨模态缺陷，表明多模态对齐仍是尚未解决的底层瓶颈

---

Powered by OpenClaw🦞

---

# [20260427](./202604/20260427.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦自监督视觉表征的几何分析及其在语义图像检索中的应用。研究趋势显示，遥感领域对无监督/自监督学习方法的关注持续，但今日候选文献数量有限，难以形成完整趋势判断。

## ✨ 今日亮点

- 自监督视觉表征的几何特性分析
- 语义图像检索的向量搜索优化
- 最近邻搜索在遥感检索中的应用

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260427] Geometric Analysis of Self-Supervised Vision Representations for Semantic Image Retrieval | Rodríguez-Betancourt Esteban, Casasola-Murillo Edgar | Universidad de Costa Rica | 该研究从几何视角分析自监督视觉表征，为语义图像检索中的向量搜索与最近邻检索提供理论支撑。 | [#158](https://github.com/Larry2000error/Larry-PaperClaw/issues/158) |

## 🔎 观察

- 候选文献仅1篇，且非传统遥感期刊来源，需警惕领域相关性偏差。
- 自监督学习+图像检索的组合符合当前AI趋势，但缺乏多源数据验证。

---

Powered by OpenClaw🦞

---

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
