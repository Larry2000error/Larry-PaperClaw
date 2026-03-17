# Daily Reports

最近三天日报（最新在前）：

# [20260316](./202603/20260316.md)
## 📌 今日概况

今日共检索候选论文 40 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 1 篇。

今日仅收录1篇论文，聚焦时间序列分析领域。研究提出弹性相似性度量的新下界范式，通过二分图建模优化相似性搜索效率，为时序数据挖掘提供理论支撑与算法加速思路。

## ✨ 今日亮点

- 提出弹性相似性度量新下界范式，突破传统方法局限
- 构建二分图模型优化时序相似性搜索计算效率
- 给出更紧致的下界理论结果，提升算法可扩展性

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260316] A New Lower Bounding Paradigm and Tighter Lower Bounds for Elastic Similarity Measures | Chao Zemin, Xiao Boyu, Li Zitong, Qi Zhixin, Liu Xianglong et al. | 提出弹性相似性度量的新下界范式，通过二分图建模获得更紧致下界，优化时序相似性搜索效率。 | [#84](https://github.com/thinson/RS-PaperClaw/issues/84) |

## 🔎 观察

- 时序分析仍是遥感数据处理的底层技术需求，下界优化对大规模卫星时序检索具有潜在价值
- 理论型工作占比偏低，需关注后续是否开源验证及在遥感场景的实际迁移效果

---

Powered by OpenClaw🦞

---

# [20260315](./202603/20260315.md)
## 📌 今日概况

今日共检索候选论文 25 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦泛化性学习范式，零样本全色锐化成为热点。G-ZAP框架通过隐式神经表示实现任意尺度融合，突破传统方法对配对训练数据的依赖，推动遥感图像超分辨率向实用化场景迁移。

## ✨ 今日亮点

- 零样本学习首次系统应用于全色锐化任务，解决跨传感器泛化难题
- 隐式神经表示实现连续尺度建模，支持任意分辨率提升需求
- 多尺度融合机制兼顾空间细节与光谱保真，无需重新训练即可适配新数据

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260315] G-ZAP: A Generalizable Zero-Shot Framework for Arbitrary-Scale Pansharpening | Yang Zhiqi, Yin Shan, Liang Jingze, Deng Liang-Jian | G-ZAP提出可泛化的零样本全色锐化框架，利用隐式神经表示实现任意尺度图像融合，摆脱配对数据约束。 | [#82](https://github.com/thinson/RS-PaperClaw/issues/82) |

## 🔎 观察

- 零样本范式正从自然图像向遥感专用任务渗透，数据获取瓶颈驱动方法论革新
- 隐式神经表示的连续建模能力，或成为下一代多分辨率遥感分析的基础组件

---

Powered by OpenClaw🦞

---

# [20260314](./202603/20260314.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现多技术路线并进态势：目标检测持续优化YOLO系列架构，视觉基础模型与跨视角地理定位成为热点，自监督学习与扩散模型深度融合趋势明显，量子计算开始介入灾害监测领域，空地协同感知与文本引导编辑等应用方向亦有新进展。

## ✨ 今日亮点

- YOLOv11n双策略改进提升遥感多尺度小目标检测性能
- 量子增强视觉Transformer首次应用于遥感洪水检测任务
- 视觉基础模型实现零样本跨视角地理定位新突破

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260314] Dual-Strategy Improvement of YOLOv11n for Multi-Scale Object Detection in Remote Sensing Images | Zhu Shuaiyu, Ablameyko Sergey | 提出YOLOv11n双策略改进方案，针对遥感图像多尺度目标检测中的微小目标识别难题进行架构优化。 | [#75](https://github.com/thinson/RS-PaperClaw/issues/75) |
| [20260314] Quantum-Enhanced Vision Transformer for Flood Detection using Remote Sensing Imagery | Maity Soumyajit, Ghanbarian Behzad | 构建量子增强型视觉Transformer混合架构，将量子计算优势引入遥感影像洪水灾害自动检测。 | [#76](https://github.com/thinson/RS-PaperClaw/issues/76) |
| [20260314] Self-Supervised Uncertainty Estimation For Super-Resolution of Satellite Images | Zheng Zhe, Dewil Valéry, Arias Pablo | 开发自监督卫星图像超分辨率框架，集成不确定性估计机制提升重建结果可靠性。 | [#78](https://github.com/thinson/RS-PaperClaw/issues/78) |
| [20260314] OpenCOOD-Air: Prompting Heterogeneous Ground-Air Collaborative Perception with Spatial Conversion and Offset Prediction | Wu Xianke, Bai Songlin, Li Chengxiang, Luo Zhiyao, Tian Yulin et al. | OpenCOOD-Air通过空间转换与偏移预测实现空地异构协同感知，支持提示驱动的跨域迁移。 | [#79](https://github.com/thinson/RS-PaperClaw/issues/79) |
| [20260314] VFM-Loc: Zero-Shot Cross-View Geo-Localization via Aligning Discriminative Visual Hierarchies | Lu Jun, Sang Zehao, Wei Haoqi, Liu Xiangyun, Zhu Kun et al. | VFM-Loc对齐判别性视觉层次结构，使视觉基础模型具备零样本跨视角地理定位能力。 | [#80](https://github.com/thinson/RS-PaperClaw/issues/80) |
| [20260314] RSEdit: Text-Guided Image Editing for Remote Sensing | Zhenyuan Chen, Zechuan Zhang, Feng Zhang | RSEdit基于扩散模型实现文本引导的遥感图像编辑，支持双时相场景理解与可控生成。 | [#85](https://github.com/thinson/RS-PaperClaw/issues/85) |
| [20260314] Sat-JEPA-Diff: Bridging Self-Supervised Learning and Generative Diffusion for Remote Sensing | Komurcu Kursat, Petkevicius Linas | Sat-JEPA-Diff架接自监督学习与生成扩散模型，统一遥感卫星影像预测与表征学习范式。 | [#94](https://github.com/thinson/RS-PaperClaw/issues/94) |
| [20260314] MOGeo: Beyond One-to-One Cross-View Object Geo-localization | Lv Bo, Zhang Qingwang, Wu Le, Li Yuanyuan, Zhu Yingying | MOGeo突破一对一匹配限制，实现多对象跨视角地理定位的联合推理与精确定位。 | [#95](https://github.com/thinson/RS-PaperClaw/issues/95) |

## 🔎 观察

- 视觉基础模型与跨视角地理定位形成技术共振，零样本与多对象扩展正重塑该领域研究范式
- 自监督学习与生成模型的双向融合加速，扩散架构已成为遥感图像编辑与预测的主流选择

---

Powered by OpenClaw🦞

---
