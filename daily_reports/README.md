# Daily Reports

最近三天日报（最新在前）：

# [20260528](./202605/20260528.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 4 篇。

今日研究聚焦视觉-语言模型的检索与推理能力提升。多模态检索领域探索单向量模型的潜力重估，第一人称视角视频分析关注零样本物体再识别，地理定位任务引入智能体推理与证据验证机制，同时多轮对话式图像检索获得新的基准数据集支持。

## ✨ 今日亮点

- 单向量嵌入模型通过后期交互机制挑战多向量检索范式
- SAM3特征融合实现厨房场景零样本物体再识别
- 智能体推理框架强化图像地理定位的证据验证能力

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260528] Your Embedding Model is SMARTer Than You Think | Zhang Jianrui, Hyun Jung Lee, Ganguly Sukanta, Kam Tae-Eui, Kim Donghyun, Yong Jae Lee | UW-Madison；Korea University；NetApp, Inc. | 该研究提出SMART方法，通过后期交互机制激活单向量模型的多向量检索能力，无需训练即可匹敌专用多向量模型。 | [#220](https://github.com/Larry2000error/Larry-PaperClaw/issues/220) |
| [20260528] Zero-Shot Object Re-Identification in Egocentric Kitchen Videos via Multi-Stage SAM3 Feature Fusion | Klepachevskyi Dmytro, Wong Alexander, Rambhatla Sirisha, Chen Yuhao | University of Waterloo | 论文提出多阶段SAM3特征融合框架，在 egocentric 厨房视频中实现零样本物体再识别，无需目标域训练数据。 | [#221](https://github.com/Larry2000error/Larry-PaperClaw/issues/221) |
| [20260528] REVERSE: Reinforcing Evidence Verification and Search for Agentic Image geo-localization | Li Yong, Jia Furong, Yin Dacheng, Rong Kang, Rao Fengyun, LYU Jing, Zhang Fan | Peking University；The Hong Kong University of Science and Technology；WeChat Vision, Tencent Inc | REVERSE框架引入智能体推理机制，通过多轮证据验证与搜索迭代提升图像地理定位的准确性与可解释性。 | [#222](https://github.com/Larry2000error/Larry-PaperClaw/issues/222) |
| [20260528] CIRCLED: A Multi-turn CIR Dataset with Consistent Dialogues across Domains | Takeda Tomohisa, Lin Yu-Chieh, Nozawa Yuji, Ng Youyang, Torii Osamu, Matsui Yusuke | Graduate School of Information Science and Technology, The University of Tokyo；Kioxia Corporation | CIRCLED数据集构建跨领域一致的多轮对话式图像检索基准，支持时尚域的组合图像检索研究。 | [#223](https://github.com/Larry2000error/Larry-PaperClaw/issues/223) |

## 🔎 观察

- 检索架构呈现'轻量单向量+复杂交互'新趋势，平衡效率与表达能力
- 第一人称视觉与地理定位任务加速融入大模型智能体范式，推理可解释性成为关键诉求

---

Powered by OpenClaw🦞

---

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
