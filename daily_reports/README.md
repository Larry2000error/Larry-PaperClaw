# Daily Reports

最近三天日报（最新在前）：

# [20261029](./202610/20261029.md)
## 📌 今日概况

今日共检索候选论文 34 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日研究呈现多场景视觉智能深化趋势：航空-地面跨视角感知、水下生物识别、医学影像重建等垂直领域持续突破；自监督学习与度量学习成为共性技术路径；同时视觉-语言模型的检索能力评估引发方法论反思。

## ✨ 今日亮点

- KITScenes数据集填补航空增强自动驾驶基准空白，支持跨视角定位与高精地图构建
- 海马开集重识别研究拓展水下多视角生物监测技术边界
- 无标注息肉检索方法降低结肠镜视频分析对医学标注的依赖

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261029] Luggage re-identification: A study of strategies towards a real-world application | Dhôte Quentin, Audigier Romaric | Université Paris-Saclay；CEA；List | 针对行李重识别任务，研究面向真实视频监控场景的多相机跟踪策略优化。 | [#681](https://github.com/Larry2000error/Larry-PaperClaw/issues/681) |
| [20261029] A Unified Benchmark for Aerial-Enhanced Autonomous Driving: The KITScenes Aerial Dataset | Lengerer Daniel, Schwarzkopf Richard, Merkert Jonas, Immel Fabian, Polley Rupert, Bieder Frank, Pauls Jan-Hendrik, J. Marius Zöllner, Bogenberger Klaus, Stiller Christoph, Markgraf Carsten | Technical University of Applied Sciences Augsburg；FZI Research Center for Information Technology；Karlsruhe Institute of Technology (KIT)；Technical University of Munich；Parallel Domain | 发布KITScenes航空数据集，统一基准推动航空图像增强的自动驾驶感知研究。 | [#682](https://github.com/Larry2000error/Larry-PaperClaw/issues/682) |
| [20261029] It Takes Two to Probe, Thousands to Retrieve: Putting Vision--Language Probes to the Retrieval Test | Beňová Ivana, Gregor Michal, Šimko Marián | Kempelen Institute of Intelligentz Technologies | 系统检验视觉-语言探针在图像-文本检索任务中的实际效能与负采样影响。 | [#683](https://github.com/Larry2000error/Larry-PaperClaw/issues/683) |
| [20261029] Open-set multi-view seahorse re-identification from underwater photograph sequences | Fauvel Tristan, Louisy Sylvie, Louisy Patrick, Fauvel Thomas | Baysic Labs；Association Peau-Bleue；UMR BOREA；Parc Naturel Marin du Bassin d'Arcachon；Office Français de la Biodiversité | 提出开集多视角海马重识别方法，基于水下照片序列实现海洋生物个体追踪。 | [#684](https://github.com/Larry2000error/Larry-PaperClaw/issues/684) |
| [20261029] Annotation-Free Representation Learning for Polyp Retrieval in Colonoscopy Videos | Parolari Luca, Ballan Lamberto, Biffi Carlo, Loic Le Folgoc | University of Padova；Cosmo Intelligent Medical Devices；LTCI, Telecom Paris, Institut Polytechnique de Paris | 开发无需标注的息肉表示学习方法，支持结肠镜视频中病变片段的高效检索。 | [#685](https://github.com/Larry2000error/Larry-PaperClaw/issues/685) |
| [20261029] FFAI: Flow Matching with Feedback Training and Adaptive Initialization for CT Reconstruction | Duan Jigang, Wang Heran, Ma Genwei, Zhao Xing | Institution unavailable | 引入反馈训练与自适应初始化的流匹配框架，提升低剂量与稀疏视角CT重建质量。 | [#686](https://github.com/Larry2000error/Larry-PaperClaw/issues/686) |
| [20261029] FDSML: Formula-Driven Supervised Metric Learning with Parameter-Aware Triplet Loss | Otake Hina, Arakawa Shinei, Tanaka Keitaro, Fukuhara Yoshihiro, Kataoka Hirokatsu, Morishima Shigeo | Waseda University；Waseda Research Institute for Science and Engineering；National Institute of Advanced Industrial Science and Technology；University of Oxford | 提出公式驱动监督度量学习框架，利用分形图像与参数感知三元组损失优化图像检索。 | [#687](https://github.com/Larry2000error/Larry-PaperClaw/issues/687) |

## 🔎 观察

- 航空-地面跨视角融合正成为自动驾驶感知的新方向，但传感器时空配准与数据规模仍是瓶颈
- 自监督学习在医学影像领域加速渗透，然而临床验证标准与泛化性评估体系尚未同步建立

---

Powered by OpenClaw🦞

---

# [20261027](./202610/20261027.md)
## 📌 今日概况

今日共检索候选论文 36 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦跨模态检索与生成式模型优化。遥感领域关注高效图文检索架构，电商场景探索端到端多模态搜索规模化。视频扩散模型被重新用于跨视角时序目标关联，而梯度冲突缓解技术则推动文本驱动的人物异常检索。整体呈现效率优先、多模态融合与任务迁移三大趋势。

## ✨ 今日亮点

- 遥感图文检索提出无交互召回+文本引导重排的两阶段高效架构
- 视频扩散Transformer迁移至跨视角时序目标关联任务
- 电商生成式检索通过语义ID实现端到端多模态搜索规模化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261027] GradCO: Behavior-Aware Gradient-Conflict Offloading for Text-Based Person Anomaly Search | Fu Zhiheng, Li Zixu, Chen Zhiwei, Huang Jiale, Liu Fangxu, Bi Jinhe, Hu Yupeng | Shandong University；National University of Singapore | GradCO提出行为感知梯度冲突卸载框架，通过混合专家模型优化文本驱动的人物异常检索训练稳定性。 | [#673](https://github.com/Larry2000error/Larry-PaperClaw/issues/673) |
| [20261027] Efficient Remote Sensing Image-Text Retrieval via Interaction-Free Recall and Text-Guided Reranking | Chen Xi, Chen Xu, Jia Xiamgyang, Wang Wei, Zhang Xu, Shun Zhenyuan | Wuhan University；Beijing Institute for General Artificial Intelligence (BIGAI) | 该工作设计无交互召回与文本引导重排两阶段策略，降低遥感图文检索计算开销同时保持精度。 | [#674](https://github.com/Larry2000error/Larry-PaperClaw/issues/674) |
| [20261027] Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence | Jin Siyoon, Chung Dahyun, An Honggyu, Lim Sangbeom, Nam Wonjin, Jung Jaewoo, Moon WonJun, Kim Seungryong | KAIST AI；Korea University | 研究将视频扩散Transformer重新用于跨视角时序目标对应任务，利用预训练时序建模能力实现多视图匹配。 | [#675](https://github.com/Larry2000error/Larry-PaperClaw/issues/675) |
| [20261027] PailitaoMMSearch2.0 Technical Report: Scaling Generative Retrieval to Unified End-to-End Multimodal Search | Ye Xiaohan, Gong Zihan, Zhao Jingqian, Du Lianyu, Shu Yunmeng, Chen Xu, Zhou Zesheng, You Renchun, Chen Bocheng, Lan Jinsong, Tang Haihong, Zheng Bo | Taobao & Tmall Group of Alibaba | 技术报告披露拍立淘多模态搜索2.0系统，通过生成式检索与语义ID统一处理文本、图像、视频查询。 | [#678](https://github.com/Larry2000error/Larry-PaperClaw/issues/678) |

## 🔎 观察

- 遥感视觉-语言检索正从精度竞争转向效率优化，两阶段解耦设计成为降低推理成本的主流思路。
- 视频基础模型的跨任务迁移价值凸显，扩散Transformer的时序建模能力可扩展至静态图像的多视角分析场景。

---

Powered by OpenClaw🦞

---

# [20261026](./202610/20261026.md)
## 📌 今日概况

今日共检索候选论文 36 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究呈现多模态融合与空间智能两大主线。三篇论文分别探索渐进式多模态表征学习、脑电信号驱动的视觉注意力预测，以及生成式AI辅助历史地图语义重建，体现出从通用多模态技术向垂直领域（地理空间、认知科学）深度渗透的趋势。

## ✨ 今日亮点

- 多模态融合顺序研究揭示渐进式表征学习对跨模态检索的关键影响
- 脑电-眼动联合建模开辟视觉注意力预测的神经生理新路径
- 生成式空间知识框架实现历史地图的自动化语义重建与矢量化

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261026] When Fusion Order Matters: Insights on Progressive Multimodal Representation Learning for Cross-modal Retrieval | Zhao Haoxiang, Wang Bin, Wang Yaofei, Lan Xiao, Diao Yunfeng, Wang Xu | University of Science and Technology of China；Hefei University of Technology；Sichuan University | 中国科学技术大学团队提出渐进式多模态表征学习方法，系统论证融合顺序对跨模态视频检索性能具有显著影响。 | [#668](https://github.com/Larry2000error/Larry-PaperClaw/issues/668) |
| [20261026] EEGaze: Multimodal Attention Prediction in Visual Search via EEG-Based Saliency Refinement | Sharma Mansi, Orazgaliyev Dinar, Krüger Antonio, Müller Philipp | Max-Planck-Institute for Intelligent Systems；Saarland University；DFKI | 德国研究团队构建EEGaze数据集，通过脑电信号细化显著性预测，实现视觉搜索任务中多模态注意力机制的神经级建模。 | [#669](https://github.com/Larry2000error/Larry-PaperClaw/issues/669) |
| [20261026] ArchiveLens: A Generative Spatial Knowledge Framework for Semantic Reconstruction of Historical Maps | Wu Yanan, Yang Yalin, Deng Chengbin | Department of Geography, The University of Central Arkansas；Department of Geology and Geography, West Virginia University；Center for Spatial Analysis；Department of Geography and Environmental Sustainability, University of Oklahoma | 美国地理学界联合开发ArchiveLens生成式框架，整合空间知识实现历史地图的语义重建与建筑物轮廓自动提取。 | [#670](https://github.com/Larry2000error/Larry-PaperClaw/issues/670) |

## 🔎 观察

- 多模态学习正从简单特征拼接转向时序化、渐进式的深度融合策略，融合顺序成为新的优化维度。
- 历史地图数字化需求推动生成式AI与空间知识图谱结合，地理人文领域成为遥感AI落地的新蓝海。

---

Powered by OpenClaw🦞

---
