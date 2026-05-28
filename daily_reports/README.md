# Daily Reports

最近三天日报（最新在前）：

# [20260523](./202605/20260523.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦组合图像检索（CIR）技术，涵盖不确定性量化与地球观测应用两大方向。清华团队引入共形预测解决检索歧义问题，希腊-捷克联合团队则首次系统评估CIR在卫星影像中的实际表现，推动视觉语言模型向遥感专用场景落地。

## ✨ 今日亮点

- 共形预测校准交互不确定性，提升零样本组合图像检索可靠性
- 首份遥感CIR基准测试揭示视觉语言模型在卫星影像应用中的性能差距
- 多机构跨国合作推动组合检索技术从通用视觉向地球观测迁移

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260523] Resolving Ambiguity in Composed Image Retrieval via Calibrated Interaction | Tran Amsisan, Le Baogh, Tuan Kiet Pham, Sui Yang Guang | Tsinghua University；Chinese Academy of Sciences | 提出基于共形预测的校准交互框架，通过量化不确定性解决组合图像检索中的意图歧义问题。 | [#217](https://github.com/Larry2000error/Larry-PaperClaw/issues/217) |
| [20260523] Benchmarking Composed Image Retrieval for Applied Earth Observation | Psomas Bill, Christopoulos Dionysis, Petropoulos Thanasis, Efthymiadis Nikos, Kakogeorgiou Ioannis, Chum Ondřej, Avrithis Yannis, Tolias Giorgos, Karantzalos Konstantinos | Visual Recognition Group, Department of Cybernetics, Czech Technical University in Prague；Remote Sensing Laboratory, School of Rural, Surveying and Geoinformatics Engineering, National Technical University of Athens；Institute of Informatics & Telecommunications, National Centre for Scientific Research "Demokritos"；Department of Informatics and Telecommunications, National and Kapodistrian University of Athens | 构建首个面向地球观测的组合图像检索基准，系统评估CLIP等视觉语言模型在卫星影像检索任务中的适用性。 | [#218](https://github.com/Larry2000error/Larry-PaperClaw/issues/218) |

## 🔎 观察

- 组合图像检索正从通用视觉向垂直领域渗透，遥感场景的特殊性（如光谱特征、地理尺度）对现有VLMs构成挑战
- 不确定性量化方法（如共形预测）与检索任务的结合，反映出社区对模型可靠性而非单纯精度的关注转向

---

Powered by OpenClaw🦞

---

# [20260521](./202605/20260521.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦视觉-语言模型的跨模态对齐与检索优化。FashionLens探索任务自适应学习在时尚电商检索中的应用；Supervised Classification Heads提出权重回收机制实现语义原型对齐；DeliCIR则引入多智能体 deliberative 推理提升组合图像检索性能。整体趋势显示测试时扩展与模块化设计成为提升检索精度的关键路径。

## ✨ 今日亮点

- FashionLens构建任务自适应框架，缓解时尚检索中多任务冲突问题
- 权重回收策略将分类头转化为语义原型，实现零样本视觉-语言对齐
- DeliCIR采用分层多智能体 deliberative 进化，优化组合图像检索推理

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260521] FashionLens: Toward Versatile Fashion Image Retrieval via Task-Adaptive Learning | Wen Haokun, Song Xuemeng, Xie Xinghao, Chen Xiaolin, Zhao Xiangyu, Guan Weili | Institution unavailable | FashionLens提出任务自适应学习框架，通过动态路由与专用编码器解决时尚图像检索中的多任务干扰问题。 | [#212](https://github.com/Larry2000error/Larry-PaperClaw/issues/212) |
| [20260521] Supervised Classification Heads as Semantic Prototypes: Unlocking Vision-Language Alignment via Weight Recycling | Méndez David, Confalonieri Roberto, Natalia Díaz Rodríguez | Universidad de Granada；Università degli Studi di Milano | 该研究将预训练分类头的权重回收为语义原型，无需额外训练即可解锁视觉-语言模型的跨模态对齐能力。 | [#213](https://github.com/Larry2000error/Larry-PaperClaw/issues/213) |
| [20260521] DeliCIR: Deliberative Test-Time Evolutionary Hierarchical Multi-Agents for Composed Image Retrieval | Pei Xingtian, Song Yukun, Wang Changwei, Chen Shunpeng, Xu Rongtao, Xu Shengpeng, Xu Shibiao | Institution unavailable | DeliCIR设计 deliberative 测试时进化机制，利用分层多智能体协作优化组合图像检索的复杂推理过程。 | [#214](https://github.com/Larry2000error/Larry-PaperClaw/issues/214) |

## 🔎 观察

- 测试时计算扩展（Test-Time Scaling）正从语言模型向视觉-语言检索任务迁移，DeliCIR的进化推理机制印证了这一趋势
- 权重回收与参数重用成为高效对齐的新范式，或降低视觉-语言模型对大规模对比训练的依赖

---

Powered by OpenClaw🦞

---

# [20260520](./202605/20260520.md)
## 📌 今日概况

今日共检索候选论文 1 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI领域研究聚焦于视觉-语言模型的零样本推理能力，无需训练的组合图像检索成为热点。学者探索通过语义迁移与运输机制，实现文本-图像-图像三元组的高效对齐，降低模型部署成本。

## ✨ 今日亮点

- 提出训练自由的零样本组合图像检索框架，突破传统微调范式
- 创新语义迁移与运输机制，强化三元组间的细粒度语义对齐
- 融合大语言模型先验知识，提升复杂视觉概念的推理能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260520] STiTch: Semantic Transition and Transportation in Collaboration for Training-Free Zero-Shot Composed Image Retrieval | Li Miaoge, Wang Dongsheng, Sun Zening, Zhang Jinsen, Luo Wenhan, Guo Jingcai | The Hong Kong Polytechnic University；Shenzhen University；The Hong Kong University of Science and Technology | STiTch提出训练自由的零样本组合图像检索方法，通过语义迁移与运输机制实现文本-参考图像-目标图像的高效对齐。 | [#210](https://github.com/Larry2000error/Larry-PaperClaw/issues/210) |

## 🔎 观察

- 训练自由范式显著降低计算成本，但语义对齐精度仍是开放挑战
- 大语言模型先验的引入或成为视觉-语言任务的新标准配置

---

Powered by OpenClaw🦞

---
