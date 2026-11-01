# Daily Reports

最近三天日报（最新在前）：

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

# [20261024](./202610/20261024.md)
## 📌 今日概况

今日共检索候选论文 18 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦视觉-语言检索与行人属性识别两大方向。研究趋势显示，推理时证据聚合与跨域泛化成为核心挑战，越南AI团队表现活跃，在域泛化行人检索与多编码器融合方面贡献显著。

## ✨ 今日亮点

- 提出标题共识作为推理时证据，革新视觉-语言检索范式
- LENS方法结合似然评估与邻域平滑，解决跨相机行人检索域泛化难题
- UniQuery统一视觉模型查询头，实现跨域行人属性识别

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261024] Whispers from the Neighbors: Rethinking Caption Consensus as Inference-Time Evidence for Vision-Language Retrieval | Khang Nhat Hoang Vo, Shoer Belal, Abhirama Subramanyam Penamakuri | Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) | 该研究将标题共识重新定义为推理时证据，通过邻居样本的语义一致性优化双编码器视觉-语言检索。 | [#663](https://github.com/Larry2000error/Larry-PaperClaw/issues/663) |
| [20261024] LENS: Likelihood Evaluation and Neighbor Smoothing for Attribute-Based Person Retrieval on Unseen Cameras | Nguyen Dang Duy Tan, Vo Thanh Nguyen, Linh T. T. Tran, Huynh Nguyen Phat | AI VIET NAM；Ho Chi Minh City University of Technology and Engineering；University of Information Technology, VNU-HCM；University of Science, VNU-HCM | LENS方法融合对数似然评分与邻域平滑技术，提升未见相机场景下基于属性的行人检索泛化能力。 | [#664](https://github.com/Larry2000error/Larry-PaperClaw/issues/664) |
| [20261024] UniQuery: Unifying Vision Models with a Joint Query Head for Cross-Domain Pedestrian Attribute Recognition | Nguyen Dang Duy Tan, Linh T. T. Tran, Huynh Nguyen Phat, Vo Thanh Nguyen | AI VIET NAM；University of Information Technology, VNU-HCM；University of Science, VNU-HCM；Ho Chi Minh City University of Technology and Engineering | UniQuery设计联合查询头统一多视觉基础模型，以查询驱动机制实现跨域行人属性识别的特征融合。 | [#665](https://github.com/Larry2000error/Larry-PaperClaw/issues/665) |

## 🔎 观察

- 越南高校与AI VIET NAM机构在行人分析领域形成研究集群，两篇工作均聚焦跨域泛化，显示该区域计算机视觉研究实力提升。
- 推理时优化（Inference-Time）成为视觉-语言模型新热点，从训练时对齐转向测试时证据聚合，反映对开放场景鲁棒性的迫切需求。

---

Powered by OpenClaw🦞

---

# [20261023](./202610/20261023.md)
## 📌 今日概况

今日共检索候选论文 31 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多模态融合与几何表征两大主线。GeoLEON-CLIP将图神经网络与对比学习结合用于地理区域表示；同时，超几何空间（双曲空间）在视频时序建模中的创新应用值得关注。视觉编码器的稀疏优化与跨模态行人重识别亦体现表征学习的精细化趋势。

## ✨ 今日亮点

- GeoLEON-CLIP提出图锚定多模态对比学习，融合遥感图像与地理文本实现区域级表示
- SPOOK通过稀疏像素优化挖掘视觉编码器的流形外知识，提升自监督表征质量
- 双曲空间视频时刻检索方法，以庞加莱球组织时序证据优化视频-文本对齐

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20261023] Are Textual Residuals Truly Complementary? Learning Visual Complements under Semantic Superposition for Visible-Infrared Person Re-Identification | Li Xiaoyang, Lu Mingming, Zhou Wei, Li Hao, Zhang Canhui | School of Computer Science and Engineering, Central South University | 该文质疑文本残差在可见光-红外行人重识别中的互补性，提出语义叠加下的视觉补全学习框架。 | [#616](https://github.com/Larry2000error/Larry-PaperClaw/issues/616) |
| [20261023] SPOOK: Sparse Pixel Optimization for Off-Manifold Knowledge in Vision Encoders | Gupta Ankit, Pandya Akshat, Adami Christoph, Dolson Emily | Department of Computer Science & Engineering；Coco Robotics；Program in Evolution, Ecology, & Behavior；Department of Physics & Astronomy；Department of Microbiology, Genetics, & Immunology；Michigan State University | SPOOK通过稀疏像素优化策略，显式挖掘视觉编码器中分布于数据流形之外的知识。 | [#658](https://github.com/Larry2000error/Larry-PaperClaw/issues/658) |
| [20261023] Organizing Temporal Evidence in Hyperbolic Space for Video Moment Retrieval | Liu Mengnan, Zhou Sanping, Xia Kun, Lin Jiaxuan, Hua Gang, Wang Le | Institution unavailable | 将视频时刻检索的时序证据组织嵌入双曲空间，利用庞加莱球层次特性优化长视频理解。 | [#659](https://github.com/Larry2000error/Larry-PaperClaw/issues/659) |
| [20261023] GeoLEON-CLIP: Graph-Anchored Multimodal Contrastive Learning for Geographic Region Representation | Malek Radoslaw, Soltysiak Szymon, Kawala-Sterniuk Aleksandra, Szymanski Piotr | Wrocław University of Science and Technology | GeoLEON-CLIP以图神经网络锚定地理实体，通过多模态对比学习构建可迁移的区域表征。 | [#660](https://github.com/Larry2000error/Larry-PaperClaw/issues/660) |
| [20261023] Beyond Post-Hoc Rewards: Privileged Reasoning Exploration for Multimodal Embeddings | Yang Tianyu, Tian Yijun, Lars Benedikt Kaesberg, Jan Philip Wahle, Gipp Bela, Ruas Terry, Kurzawe Daniel | University of Göttingen；University of Notre Dame；State and University Library of Göttingen | 针对多模态嵌入的特权推理探索框架，突破事后奖励机制以优化检索增强生成任务。 | [#661](https://github.com/Larry2000error/Larry-PaperClaw/issues/661) |

## 🔎 观察

- 双曲几何正从NLP向视觉-语言任务渗透，其层次化特性对遥感地物尺度差异建模具潜在价值
- 稀疏表征与流形外知识挖掘成为视觉编码器优化新方向，或推动遥感预训练模型效率提升

---

Powered by OpenClaw🦞

---
