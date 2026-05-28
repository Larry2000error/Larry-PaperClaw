# Daily Reports

最近三天日报（最新在前）：

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

# [20260519](./202605/20260519.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI领域研究聚焦于视觉-语言模型与3D点云理解两大方向。CLIP架构持续演进，通过双提示学习与混合编码器提升遮挡场景下的行人重识别性能；同时，2D-3D跨模态对齐取得进展，Tango3D在全局检索与局部密集匹配上实现统一，为3D基础模型发展提供新思路。

## ✨ 今日亮点

- CLIP双提示机制结合混合视觉编码器，有效缓解遮挡行人重识别中的特征混淆问题
- Tango3D提出全局-局部联合对齐框架，突破2D-3D对应关系中尺度不一致的瓶颈
- 高校与产业界协同创新，腾讯混元团队参与3D基础模型关键技术攻关

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260519] Dual-Prompt CLIP with Hybrid Visual Encoders for Occluded Person Re-Identification | Ji Zhangjian, Qiao Shaotong, Feng Kai, Wei Wei | School of Computer & Information Technology, Shanxi University；Key Laboratory of Computational Intelligence and Chinese Information Processing of Ministry of Education | 山西大学团队提出双提示CLIP架构，以混合视觉编码器与可学习提示优化遮挡行人重识别，实现视觉-语言特征协同对齐。 | [#207](https://github.com/Larry2000error/Larry-PaperClaw/issues/207) |
| [20260519] Tango3D: Towards Alignment for Global and Local 2D-3D Correspondence | He Zebin, Yang Mingxin, Yang Shuhui, Sun Hanxiao, Han Xintong, Guo Chunchao, Luo Wenhan | HKUST；Tencent Hunyuan | 港科大与腾讯混元联合发布Tango3D，通过全局-局部联合对齐机制统一2D-3D对应任务，提升点云理解与跨模态检索性能。 | [#209](https://github.com/Larry2000error/Larry-PaperClaw/issues/209) |

## 🔎 观察

- 提示学习正成为CLIP下游适配的主流范式，但双提示设计对计算开销的影响需进一步验证
- 2D-3D对齐从分离式走向统一框架，或加速3D基础模型在开放场景中的实用化部署

---

Powered by OpenClaw🦞

---
