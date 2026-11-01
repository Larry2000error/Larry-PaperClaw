# Daily Reports

最近三天日报（最新在前）：

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
