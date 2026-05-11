# Daily Reports

最近三天日报（最新在前）：

# [20260507](./202605/20260507.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI领域聚焦智能视觉识别技术，两篇论文分别针对遮挡行人重识别与文本-图像车辆检索任务，核心趋势为细粒度特征学习与跨模态对齐，通过动态掩码学习和部件级感知提升复杂场景下的检索鲁棒性。

## ✨ 今日亮点

- DPM++提出动态掩码度量学习，解决遮挡行人重识别中的特征对齐难题
- T2I-VeRW实现部件级细粒度感知，推动文本到图像车辆检索精度提升
- 两篇工作均强调局部特征与全局语义的联合建模，反映当前研究热点

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260507] DPM++: Dynamic Masked Metric Learning for Occluded Person Re-identification | Tan Lei, Luan Yingshi, Zou Pincong, Dai Pingyang, Cao Liujuan | Institution unavailable | DPM++通过动态掩码度量学习策略，有效缓解遮挡干扰，提升行人重识别在复杂场景下的准确性。 | [#184](https://github.com/Larry2000error/Larry-PaperClaw/issues/184) |
| [20260507] T2I-VeRW: Part-level Fine-grained Perception for Text-to-Image Vehicle Retrieval | Wang Xiao, Wang Ziwen, Kong Weizhe, Wu Wentao, Li Yuehang, Zheng Aihua, Li Chenglong, Tang Jin | Institution unavailable | T2I-VeRW构建部件级细粒度跨模态对齐框架，实现文本描述与车辆图像的精准检索匹配。 | [#185](https://github.com/Larry2000error/Larry-PaperClaw/issues/185) |

## 🔎 观察

- 遮挡处理与细粒度感知成为视觉检索的关键技术方向，局部特征学习的重要性持续凸显
- 跨模态检索任务从粗粒度向部件级演进，对多源数据对齐精度提出更高要求

---

Powered by OpenClaw🦞

---

# [20260506](./202605/20260506.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦视觉-语言模型在卫星图像检索中的创新应用，两篇论文分别探索零样本检索与开放词汇检索。同时，目标重识别领域持续活跃，涵盖行人终身学习、隐私保护及热成像车辆识别等方向，跨模态与跨域泛化成为共性技术诉求。

## ✨ 今日亮点

- 零样本卫星图像检索：联合嵌入与对比学习实现危机响应场景下的无需训练检索
- LLM引导的查询嵌入优化：Open-SAT框架突破卫星图像开放词汇对象检索瓶颈
- 提示锚定视觉-文本蒸馏：终身行人重识别的新范式，缓解跨域遗忘问题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260506] Zero-Shot Satellite Image Retrieval through Joint Embeddings: Application to Crisis Response | Walsh James, Fawcett William, Colvard Grace, Ramos-Pollán Raúl | University of Cambridge；Universidad de Antioquia | 剑桥大学团队提出零样本卫星图像检索方法，通过联合嵌入与对比学习实现危机响应场景下无需训练的图像检索。 | [#178](https://github.com/Larry2000error/Larry-PaperClaw/issues/178) |
| [20260506] Open-SAT: LLM-Guided Query Embedding Refinement for Open-Vocabulary Object Retrieval in Satellite Imagery | Md Adnan Arefeen, Debnath Biplob, Ravi K. Rajendran, Sankaradas Murugan, Srimat T. Chakradhar | North South University；NEC Laboratories America | Open-SAT框架利用大语言模型引导查询嵌入优化，解决卫星图像开放词汇对象检索中的语义对齐难题。 | [#179](https://github.com/Larry2000error/Larry-PaperClaw/issues/179) |
| [20260506] Prompt-Anchored Vision-Text Distillation for Lifelong Person Re-identification | Wen Wen, Chen Hao, Zhang Shiliang | University of Electronic Science and Technology of China；Harbin Institute of Technology, Shenzhen；Peking University | 提示锚定视觉-文本蒸馏方法用于终身行人重识别，通过知识蒸馏缓解跨域场景下的模型遗忘问题。 | [#180](https://github.com/Larry2000error/Larry-PaperClaw/issues/180) |
| [20260506] ICPR 2026 Competition on Privacy-Preserving Person Re-Identification from Top-View RGB-Depth Camera (TVRID) | Delécluse Raphaël, Wannous Hazem, Guimas Laurent | IMT Nord Europe, University of Lille, CNRS UMR 9189 - CRIStAL；Explain | ICPR 2026竞赛发布顶视RGB-D相机隐私保护行人重识别基准，推动跨模态检索与隐私计算技术融合。 | [#181](https://github.com/Larry2000error/Larry-PaperClaw/issues/181) |
| [20260506] VC-FeS: Viewpoint-Conditioned Feature Selection for Vehicle Re-identification in Thermal Vision | Ginige Yasod, Gunasekara Ransika, Hewavitharana Darsha, Ariyarathne Manjula, Jayasekara Peshala, Rodrigo Ranga | School of Computer Science, University of Sydney；Department of Electronics and Telecommunication Engineering, University of Moratuwa | VC-FeS方法引入视角条件特征选择机制，提升热成像车辆重识别在复杂视角变化下的鲁棒性。 | [#182](https://github.com/Larry2000error/Larry-PaperClaw/issues/182) |

## 🔎 观察

- 视觉-语言模型正加速渗透遥感领域，从预训练对齐走向查询端动态优化，LLM的语义推理能力成为检索精度提升的新变量
- 重识别研究呈现多模态扩展态势：热成像、RGB-D、顶视视角等非常规传感数据的技术适配需求显著增长

---

Powered by OpenClaw🦞

---

# [20260504](./202605/20260504.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦视觉基础模型的专业化适配。KAIST团队系统对比了电光遥感专用模型与通用视觉基础模型的检索性能，为遥感领域模型选型提供实证依据。同时，个性化图像生成领域出现相册引导的推理检索新方法，强调身份一致性保持。

## ✨ 今日亮点

- 遥感检索领域首次开展专用VFM与通用VFM的受控对比实验
- 电光遥感视觉基础模型的跨场景泛化能力成为评估焦点
- 个性化图像补全引入相册级推理检索机制增强身份一致性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260504] AlbumFill: Album-Guided Reasoning and Retrieval for Personalized Image Completion | Tsai Yu-Ju, Price Brian, Liu Qing, Figueroa Luis, Pakhomov Daniil, Ding Zhihong, Cohen Scott, Yang Ming-Hsuan | University of California, Merced；Adobe Research | 提出AlbumFill框架，通过相册引导推理与检索实现个性化图像补全，解决参考图像选择与身份一致性问题。 | [#175](https://github.com/Larry2000error/Larry-PaperClaw/issues/175) |
| [20260504] Rethinking Electro-Optical Vision Foundation Models for Remote Sensing Retrieval: A Controlled Comparison with Generalist VFM | Park Hyobin, Seo Minseok, Choi Dong-Geol | Korea Advanced Institute of Science and Technology (KAIST)；Hanbat National University | 系统比较电光遥感专用视觉基础模型与通用VFM在遥感检索任务中的性能差异，揭示领域适配的关键设计选择。 | [#176](https://github.com/Larry2000error/Larry-PaperClaw/issues/176) |

## 🔎 观察

- 遥感领域正从'自研专用模型'向'评估适配通用模型'转变，反映基础模型生态成熟。
- 个性化生成任务中'参考检索+推理'的范式可能迁移至遥感目标识别等需先验引导的任务。

---

Powered by OpenClaw🦞

---
