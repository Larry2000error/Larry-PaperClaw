# Daily Reports

最近三天日报（最新在前）：

# [20260903](./202609/20260903.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究呈现跨模态检索与农业智能监测两大主线。跨模态生成式检索通过动态扩展机制突破信息不对称为核心创新；畜禽精准养殖领域则聚焦侧视相机下的个体再识别技术，体现AI向垂直场景的深度渗透。

## ✨ 今日亮点

- 跨模态生成式检索引入动态通配符推理，缓解自回归解码中的信息不对称为题
- 生猪个体追踪创新采用背部标记分类，解决侧视相机视角下的再识别难题
- 农业计算机视觉研究凸显产学研医跨界协作，覆盖从算法到动物福利全链条

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260903] WIDE: Wildcard Inference with Dynamic Expansion for Cross-Modal Generative Retrieval | Guo Teng, Wang Xin, Xu Jiayou, Zhou Keying, Shen Jifeng, Ruan Haoxin | Jilin University；Jiangsu University | WIDE提出动态扩展的通配符推理机制，优化跨模态生成式检索中的束搜索策略，应对自回归解码的信息不对称瓶颈。 | [#471](https://github.com/Larry2000error/Larry-PaperClaw/issues/471) |
| [20260905] BMCTrack-d: Pig re-identification and tracking via back marks in challenging camera settings | Brunner David, Oczak Maciej, Bordes Marie, Rault Jean-Loup, Stephan M. Winkler, Dorfer Viktoria | Bioinformatics Research Group, PLFDoc, University of Applied Sciences Upper Austria；Computer Vision Lab, TU Wien；Precision Livestock Farming Hub, The University of Veterinary Medicine Vienna；Animal Welfare Science Unit, The University of Veterinary Medicine Vienna | BMCTrack-d开发基于背部标记分类的生猪再识别与跟踪系统，专为侧视相机等挑战性养殖场景设计。 | [#472](https://github.com/Larry2000error/Larry-PaperClaw/issues/472) |

## 🔎 观察

- 生成式检索正从静态编码向动态推理演进，WIDE的通配符扩展机制或成跨模态对齐新范式
- 农业AI研究呈现精细化转向，畜禽个体识别从群体监测下沉至标记级特征，技术落地性显著增强

---

Powered by OpenClaw🦞

---

# [20260902](./202609/20260902.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦视觉-语言模型优化与地理空间智能两大方向。一方面，学者致力于缓解大模型视觉幻觉问题，并改进图像检索的流形学习方法；另一方面，面向实际应用场景，出现了细粒度POI定位的新基准数据集，体现遥感与地理信息领域对高精度、实用化技术的持续追求。

## ✨ 今日亮点

- 稀疏解码机制有效抑制大视觉语言模型的视觉幻觉现象
- 邻居嵌入投影与秩聚合结合提升流形学习图像检索性能
- 全球-局部非对称匹配实现大规模街景中细粒度店铺定位

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260902] RVSD: Retrieval Vision Sparse Decoding for Mitigating Visual Hallucinations in Large Vision-Language Models | Liu Canjie, Kang Jiawen, Wen Jinbo, Zhong Zishao | School of Automation, Guangdong University of Technology；Department of Computer Science, City University of Hong Kong；The Second Affiliated Hospital of Guangzhou University of Chinese Medicine | RVSD提出检索视觉稀疏解码方法，通过跨模态检索引导稀疏解码以缓解大视觉语言模型的视觉幻觉。 | [#468](https://github.com/Larry2000error/Larry-PaperClaw/issues/468) |
| [20260902] Aggregating Neighbor Embedding Projection and Rank-Based Manifold Learning for Image Retrieval | Vinicius Atsushi Sato Kawai, Gustavo Rosseto Leticio, Lucas Pascotti Valem, Daniel Carlos Guimarães Pedronette | São Paulo State University (UNESP)；University of São Paulo (USP) | ANEPR融合邻居嵌入投影与基于秩的流形学习，优化内容图像检索中的相似度传播与结构保持。 | [#469](https://github.com/Larry2000error/Larry-PaperClaw/issues/469) |
| [20260902] GeoStore: Finding Small Storefronts in Large Scenes -- A Fine-Grained POI Localization Benchmark with Global-to-Local Asymmetric Matching | Han Lu, Sun Xiting, Wang Hao, Cao Zhiqiang, Du Ruihuan, Zeng Ziquan, Lv Chunlong | Amap, Alibaba Group | GeoStore构建细粒度POI定位基准，采用全局到局部非对称匹配解决大场景中小目标检索难题。 | [#484](https://github.com/Larry2000error/Larry-PaperClaw/issues/484) |

## 🔎 观察

- 视觉-语言模型幻觉问题仍是研究热点，稀疏解码与检索增强结合成为新思路，但工程落地复杂度需关注。
- 地理空间AI从粗粒度场景识别向细粒度POI定位演进，非对称匹配设计反映实际应用中视角与尺度差异的建模需求。

---

Powered by OpenClaw🦞

---

# [20260901](./202609/20260901.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦视觉检索与表征学习两大方向。组合图像检索、自监督学习与细粒度视觉理解成为热点，跨域监控场景下的车辆属性分类获得新基准支持，语义图结构方法推动多实体检索发展。

## ✨ 今日亮点

- AutoConcept提出无训练概念引导重排序，突破组合图像检索依赖训练数据瓶颈
- ViTAMINS系统研究合成难负样本对自监督ViT表征学习的影响机制
- SAGE构建语义属性图实现多实体视觉检索，拓展文档理解应用场景

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260901] AutoConcept: Training-Free Concept-Guided Reranking for Metadata-Available Composed Image Retrieval | Wang Tianyu, Wu Tianjiao | School of Computer Science and Technology, Soochow University；INSTITUT NATIONAL DES SCIENCES APPLIQUEES DE LYON | AutoConcept提出无需训练的概念引导重排序框架，利用元数据实现组合图像检索的零样本优化。 | [#465](https://github.com/Larry2000error/Larry-PaperClaw/issues/465) |
| [20260901] ViTAMINS: An Empirical Study of Training Self-Supervised Vision Transformers with Synthetic Hard Negatives | Giakoumoglou Nikos, Floros Andreas, Papadopoulos Kleanthis-Marios, Stathaki Tania | Imperial College London | ViTAMINS通过合成难负样本实证研究自监督Vision Transformer的训练特性与表征质量。 | [#466](https://github.com/Larry2000error/Larry-PaperClaw/issues/466) |
| [20260901] A Benchmark for Vehicle Attribute Classification in Cross-Domain Surveillance Scenarios | Sergio M. Silva, Otavio T. Remer, Gabriel E. Lima, Wojcik Lucas, Laroca Rayson, Menotti David | Department of Informatics, Federal University of Paraná；Graduate Program in Informatics, Pontifical Catholic University of Paraná | 发布跨域监控场景车辆属性分类基准，为智能交通系统提供标准化评估体系。 | [#482](https://github.com/Larry2000error/Larry-PaperClaw/issues/482) |
| [20260901] SAGE: Semantic Attribute Graphs for Multi-Entity Visual Retrieval | Kim Yongjoo, Kwon Mincheol, Choi Seonga, Lee Minseung, Oh Kyeong-Jin, Lee Hyunyoung, Choi Yunsu, Lee Jungbeom | Korea University；KT Corporation | SAGE引入语义属性图结构，解决多实体视觉检索中的细粒度匹配与文档理解难题。 | [#483](https://github.com/Larry2000error/Larry-PaperClaw/issues/483) |

## 🔎 观察

- 无训练/零样本方法在检索任务中持续受到关注，反映领域对数据效率与部署成本的现实考量
- 自监督学习与难样本挖掘的结合仍是表征学习核心议题，合成数据策略或成降低标注依赖的关键路径

---

Powered by OpenClaw🦞

---
