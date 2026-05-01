# Daily Reports

最近三天日报（最新在前）：

# [20260429](./202604/20260429.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦行人重识别(Re-ID)技术突破，涵盖属性表达量化、文本引导部件匹配、三维视角合成及联邦域泛化四大方向。研究呈现多模态融合与可解释性增强趋势，特别关注跨视角、跨域场景下的模型鲁棒性与公平性问题。

## ✨ 今日亮点

- AttriBE首次量化属性表达性，提升Re-ID公平性与识别精度
- InterPartAbility引入文本引导部件匹配，增强模型可解释性
- 3D-LENS实现单视图三维提升合成，解决空中-地面跨视角难题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260429] AttriBE: Quantifying Attribute Expressivity in Body Embeddings for Recognition and Identification | Pal Basudha, Huang Siyuan, Nanduri Anirudh, Wang Zhaoyang, Chellappa Rama | Institution unavailable | AttriBE通过量化身体嵌入中的属性表达性，优化行人重识别的公平性与识别性能。 | [#164](https://github.com/Larry2000error/Larry-PaperClaw/issues/164) |
| [20260429] InterPartAbility: Text-Guided Part Matching for Interpretable Person Re-Identification | Murtaza Shakeeb, Shukla Aryan, Bhattacharya Rajarshi, Heritier Maguelonne, Granger Eric | LIVIA, Dept. of Systems Engineering, ETS Montreal；Genetec Inc. | InterPartAbility利用视觉-语言模型实现文本引导的部件匹配，提升Re-ID可解释性与检索精度。 | [#165](https://github.com/Larry2000error/Larry-PaperClaw/issues/165) |
| [20260429] 3D-LENS: A 3D Lifting-based Elevated Novel-view Synthesis method for Single-View Aerial-Ground Re-Identification | Grolleau William, Sabourin Astrid, Lapouge Guillaume, Achard Catherine | Université Paris-Saclay, CEA, List；Sorbonne University, CNRS, Institute of Intelligent Systems and Robotics (ISIR) | 3D-LENS基于三维提升合成新视角，解决单视图空中-地面行人重识别的跨域泛化问题。 | [#166](https://github.com/Larry2000error/Larry-PaperClaw/issues/166) |
| [20260429] CO-EVO: Co-evolving Semantic Anchoring and Style Diversification for Federated DG-ReID | Zhang Fengchun, Ma Qiang, Xiang Liuyu, Lai Jinshan, Huang Tingxuan, Hu Jianwei | School of Information and Software Engineering, University of Electronic Science and Technology of China；QiYuan Lab；School of Artificial Intelligence, Beijing University of Posts and Telecommunications；School of Software, Tsinghua University | CO-EVO通过语义锚定与风格多样化协同进化，实现联邦学习场景下的域泛化Re-ID。 | [#167](https://github.com/Larry2000error/Larry-PaperClaw/issues/167) |

## 🔎 观察

- 多模态融合成为Re-ID主流范式，文本与三维几何信息正逐步替代单一视觉特征
- 联邦学习与域泛化结合反映隐私保护需求上升，实际部署场景的技术适配性成为研究焦点

---

Powered by OpenClaw🦞

---

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
