# Daily Reports

最近三天日报（最新在前）：

# [20260430](./202604/20260430.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦行人重识别领域的域适应技术。研究提出自适应中间域适应方法，解决源数据缺失场景下的模型泛化问题，体现无源学习在隐私敏感应用中的发展趋势。

## ✨ 今日亮点

- 提出AIDA-ReID框架，实现无源数据下的域适应
- 构建自适应中间域，桥接多源域与目标域差异
- 面向隐私保护场景，推动Re-ID实用化部署

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260430] AIDA-ReID: Adaptive Intermediate Domain Adaptation for Generalizable and Source-Free Person Re-Identification | Iqbal Sundas, Tian Qing, Ali Danish, Gou Jianping, Oue Weihua | School of Software, Nanjing University of Information Science and Technology；Wuxi Institute of Technology, Nanjing University of Information Science and Technology；School of Computer Science, Wuhan University；School of Computer and Information Science, Southwest University；School of Big Data and Computer Science, Guizhou Normal University | AIDA-ReID提出自适应中间域适应方法，在无需源数据条件下实现可泛化的行人重识别，解决多源域适应中的隐私与迁移难题。 | [#171](https://github.com/Larry2000error/Larry-PaperClaw/issues/171) |

## 🔎 观察

- 无源学习成为Re-ID领域重要方向，反映数据隐私合规需求对技术路线的直接影响
- 中间域构建策略或可为其他跨域遥感任务（如跨传感器场景识别）提供迁移思路

---

Powered by OpenClaw🦞

---

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
