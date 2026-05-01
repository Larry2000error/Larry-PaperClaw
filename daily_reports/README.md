# Daily Reports

最近三天日报（最新在前）：

# [20260428](./202604/20260428.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦图像地理定位与多模态检索两大方向。图像地理定位领域呈现双路径演进：DualGeo提出双视图对比学习框架，GeoSearch探索网络规模检索增强；多模态领域则关注大模型的视觉注意力缺失与语义漂移问题，三篇均涉及大语言模型技术融合。

## ✨ 今日亮点

- DualGeo构建双视图地理定位框架，结合对比学习与地理聚类提升全球定位精度
- GeoSearch首创网络规模反向图像检索增强，突破传统地理定位数据瓶颈
- 百度团队针对大模型视觉忽略与语义漂移，提出跨模态检索优化新策略

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260428] DualGeo: A Dual-View Framework for Worldwide Image Geo-localization | Cui Junchao, Shi Wenqi, Du Shaoyong, He Hang, Ma Xuanzi, Tang Hao, Luo Xiangyang | Henan Key Laboratory of Cyberspace Situation Awareness；Information Engineering University | DualGeo通过双视图对比学习与跨注意力机制，实现粗到细粒度的全球图像地理定位。 | [#160](https://github.com/Larry2000error/Larry-PaperClaw/issues/160) |
| [20260428] GeoSearch: Augmenting Worldwide Geolocalization with Web-Scale Reverse Image Search and Image Matching | Le-Duc Tung-Duong, Nguyen-Son Hoang-Quoc, Dao Minh-Son | University of Science, VNU-HCM；National Institute of Information and Communications Technology | GeoSearch融合网络规模反向图像搜索与图像匹配，构建检索增强的地理定位新范式。 | [#161](https://github.com/Larry2000error/Larry-PaperClaw/issues/161) |
| [20260428] Combating Visual Neglect and Semantic Drift in Large Multimodal Models for Enhanced Cross-Modal Retrieval | Zhang Guosheng, Liu Linkai, Wang Keyao, Yue Haixiao, Tan Zhiwen, Tan Xiao | Baidu Inc. | 该工作诊断大模型视觉忽略与语义漂移缺陷，提出增强跨模态检索的对齐方法。 | [#162](https://github.com/Larry2000error/Larry-PaperClaw/issues/162) |

## 🔎 观察

- 图像地理定位正从单一模型预测转向'检索+匹配+生成'的混合增强架构，数据规模成为关键变量
- 多模态大模型的视觉感知短板日益凸显，工业界开始系统性研究跨模态对齐的失效模式

---

Powered by OpenClaw🦞

---

# [20260427](./202604/20260427.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦自监督视觉表征的几何分析及其在语义图像检索中的应用。研究趋势显示，遥感领域对自监督学习与向量检索技术的结合持续保持关注，但当日新成果产出有限。

## ✨ 今日亮点

- 自监督视觉表征的几何特性分析
- 语义图像检索的向量搜索优化
- 最近邻搜索在遥感检索中的应用

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260427] Geometric Analysis of Self-Supervised Vision Representations for Semantic Image Retrieval | Rodríguez-Betancourt Esteban, Casasola-Murillo Edgar | Universidad de Costa Rica | 该研究从几何视角分析自监督视觉表征，为语义图像检索中的向量搜索与最近邻检索提供理论支撑。 | [#158](https://github.com/Larry2000error/Larry-PaperClaw/issues/158) |

## 🔎 观察

- 当日候选论文数量偏少，可能反映遥感AI领域投稿或收录的周期性波动。
- 研究主题偏向基础表征学习，未见典型遥感数据源（卫星/无人机影像）的明确标注，需关注其跨领域迁移价值。

---

Powered by OpenClaw🦞

---

# [20260424](./202604/20260424.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦多模态学习与视觉-语言模型的优化应用。联邦学习框架下的跨模态检索解决数据孤岛与模态缺失问题，CLIP特征聚合策略的重新设计则提升行人重识别在遮挡场景下的鲁棒性。两项工作均体现从全局表征向局部精细化建模的演进趋势。

## ✨ 今日亮点

- 联邦跨模态检索通过语义路由与个性化适配器解决模态缺失难题
- CLIP特征聚合从全局平均转向局部感知，增强遮挡行人重识别性能
- 视觉-语言预训练模型在下游任务的特征提取策略持续优化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260424] Federated Cross-Modal Retrieval with Missing Modalities via Semantic Routing and Adapter Personalization | Zhou Hefeng, Liu Xuan, Chen Sicheng, Zhang Wutong, Yan Wu, Lou Jiong, Wu Chentao, Xue Guangtao, Zhao Wei, Li Jie | Shanghai Jiao Tong University；Shenzhen Univ of Advanced Technology；Hohai University | 提出语义路由与适配器个性化方法，实现联邦场景下缺失模态的跨模态检索，平衡全局知识共享与本地数据异质性。 | [#156](https://github.com/Larry2000error/Larry-PaperClaw/issues/156) |
| [20260424] From Global to Local: Rethinking CLIP Feature Aggregation for Person Re-Identification | Zheng Aotian, Sun Winston, Alattar Bahaa, Ablavsky Vitaly, Hwang Jenq-Neng | Department of Electrical and Computer Engineering, University of Washington；Applied Physics Laboratory, University of Washington | 重新设计CLIP特征聚合策略，从全局平均池化转向局部细粒度建模，提升遮挡条件下行人重识别的判别能力。 | [#157](https://github.com/Larry2000error/Larry-PaperClaw/issues/157) |

## 🔎 观察

- 多模态联邦学习正从模态对齐走向模态缺失的容错机制设计，实际落地价值显著提升
- CLIP等视觉-语言模型的下游适配研究，正从直接迁移进入结构层面的针对性改造阶段

---

Powered by OpenClaw🦞

---
