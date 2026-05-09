# Daily Reports

最近三天日报（最新在前）：

# [20260507](./202605/20260507.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦视觉识别中的细粒度感知与遮挡鲁棒性问题。两篇论文分别针对行人重识别中的遮挡挑战和车辆跨模态检索中的部件级对齐，体现了从粗粒度到细粒度、从单模态到跨模态的技术演进趋势，核心方法均涉及动态掩码学习与局部特征增强。

## ✨ 今日亮点

- DPM++提出动态掩码度量学习，解决遮挡行人重识别中的特征对齐难题
- T2I-VeRW构建部件级细粒度感知框架，实现文本到图像的车辆精准检索
- 两篇工作均强调局部部件建模，反映视觉识别向精细化理解发展

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260507] DPM++: Dynamic Masked Metric Learning for Occluded Person Re-identification | Tan Lei, Luan Yingshi, Zou Pincong, Dai Pingyang, Cao Liujuan | Institution unavailable | DPM++通过动态掩码度量学习，在遮挡场景下实现行人重识别的鲁棒特征匹配。 | [#184](https://github.com/Larry2000error/Larry-PaperClaw/issues/184) |
| [20260507] T2I-VeRW: Part-level Fine-grained Perception for Text-to-Image Vehicle Retrieval | Wang Xiao, Wang Ziwen, Kong Weizhe, Wu Wentao, Li Yuehang, Zheng Aihua, Li Chenglong, Tang Jin | Institution unavailable | T2I-VeRW提出部件级细粒度感知方法，提升文本到图像车辆跨模态检索精度。 | [#185](https://github.com/Larry2000error/Larry-PaperClaw/issues/185) |

## 🔎 观察

- 遮挡处理与细粒度对齐成为重识别领域的关键技术方向，掩码学习策略应用日趋深入
- 跨模态检索正从全局特征向局部部件级对齐演进，文本描述与视觉区域的细粒度关联成为研究重点

---

Powered by OpenClaw🦞

---

# [20260506](./202605/20260506.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日研究聚焦视觉-语言模型在遥感与监控场景的检索应用。卫星图像零样本检索与开放词汇检索成为热点，结合对比学习与LLM引导的查询优化；同时，多模态重识别技术向终身学习、隐私保护及热成像等方向延伸，体现跨域泛化与实用部署的双重诉求。

## ✨ 今日亮点

- 零样本卫星图像检索通过联合嵌入实现危机响应场景的快速图像定位
- LLM引导的查询嵌入优化支持卫星影像开放词汇目标检索
- 热成像车辆重识别引入视角条件特征选择以应对跨视角挑战

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260506] Zero-Shot Satellite Image Retrieval through Joint Embeddings: Application to Crisis Response | Walsh James, Fawcett William, Colvard Grace, Ramos-Pollán Raúl | University of Cambridge；Universidad de Antioquia | 提出零样本卫星图像检索方法，通过联合嵌入与对比学习实现危机响应场景下的快速图像定位。 | [#178](https://github.com/Larry2000error/Larry-PaperClaw/issues/178) |
| [20260506] Open-SAT: LLM-Guided Query Embedding Refinement for Open-Vocabulary Object Retrieval in Satellite Imagery | Md Adnan Arefeen, Debnath Biplob, Ravi K. Rajendran, Sankaradas Murugan, Srimat T. Chakradhar | North South University；NEC Laboratories America | 设计LLM引导的查询嵌入精化框架，提升卫星影像开放词汇目标检索的语义对齐能力。 | [#179](https://github.com/Larry2000error/Larry-PaperClaw/issues/179) |
| [20260506] Prompt-Anchored Vision-Text Distillation for Lifelong Person Re-identification | Wen Wen, Chen Hao, Zhang Shiliang | University of Electronic Science and Technology of China；Harbin Institute of Technology, Shenzhen；Peking University | 提出提示锚定的视觉-文本蒸馏方法，解决终身行人重识别中的跨域泛化与知识迁移问题。 | [#180](https://github.com/Larry2000error/Larry-PaperClaw/issues/180) |
| [20260506] ICPR 2026 Competition on Privacy-Preserving Person Re-Identification from Top-View RGB-Depth Camera (TVRID) | Delécluse Raphaël, Wannous Hazem, Guimas Laurent | IMT Nord Europe, University of Lille, CNRS UMR 9189 - CRIStAL；Explain | 发起顶视RGB-深度相机的隐私保护行人重识别竞赛，推动多模态隐私感知识别技术发展。 | [#181](https://github.com/Larry2000error/Larry-PaperClaw/issues/181) |
| [20260506] VC-FeS: Viewpoint-Conditioned Feature Selection for Vehicle Re-identification in Thermal Vision | Ginige Yasod, Gunasekara Ransika, Hewavitharana Darsha, Ariyarathne Manjula, Jayasekara Peshala, Rodrigo Ranga | School of Computer Science, University of Sydney；Department of Electronics and Telecommunication Engineering, University of Moratuwa | 针对热成像车辆重识别任务，引入视角条件特征选择机制以增强跨视角特征判别性。 | [#182](https://github.com/Larry2000error/Larry-PaperClaw/issues/182) |

## 🔎 观察

- 遥感检索正从封闭集向开放词汇演进，LLM与视觉-语言模型的融合成为突破语义鸿沟的关键路径
- 重识别研究呈现多模态扩展趋势，热成像、深度图与隐私保护技术的引入反映真实部署场景的复杂需求

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
