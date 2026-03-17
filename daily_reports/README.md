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

今日共检索候选论文 26 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多维度创新态势：目标检测领域持续优化YOLO系列架构以应对多尺度挑战；量子计算与视觉Transformer的融合探索为灾害监测开辟新路径；自监督学习与不确定性量化成为卫星影像超分辨率研究热点；空地协同感知、跨视角地理定位及多高度场景建模等方向亦取得显著进展。

## ✨ 今日亮点

- 量子增强视觉Transformer首次应用于遥感洪水检测，开创量子-经典混合架构新范式
- YOLOv11n双策略改进方案针对性解决遥感影像多尺度与小目标检测难题
- 视觉基础模型实现零样本跨视角地理定位，突破传统方法对标注数据的依赖

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260314] Dual-Strategy Improvement of YOLOv11n for Multi-Scale Object Detection in Remote Sensing Images | Zhu Shuaiyu, Ablameyko Sergey | 提出YOLOv11n双策略改进方法，通过优化网络结构提升遥感影像多尺度目标检测性能。 | [#75](https://github.com/thinson/RS-PaperClaw/issues/75) |
| [20260314] Quantum-Enhanced Vision Transformer for Flood Detection using Remote Sensing Imagery | Maity Soumyajit, Ghanbarian Behzad | 构建量子增强视觉Transformer混合架构，探索量子计算在遥感洪水检测中的应用潜力。 | [#76](https://github.com/thinson/RS-PaperClaw/issues/76) |
| [20260314] Self-Supervised Uncertainty Estimation For Super-Resolution of Satellite Images | Zheng Zhe, Dewil Valéry, Arias Pablo | 开发自监督不确定性估计框架，为卫星影像超分辨率重建提供可靠性度量。 | [#78](https://github.com/thinson/RS-PaperClaw/issues/78) |
| [20260314] OpenCOOD-Air: Prompting Heterogeneous Ground-Air Collaborative Perception with Spatial Conversion and Offset Prediction | Wu Xianke, Bai Songlin, Li Chengxiang, Luo Zhiyao, Tian Yulin et al. | 设计空地协同感知系统OpenCOOD-Air，实现异构无人机与地面车辆的空间转换与偏移预测。 | [#79](https://github.com/thinson/RS-PaperClaw/issues/79) |
| [20260314] VFM-Loc: Zero-Shot Cross-View Geo-Localization via Aligning Discriminative Visual Hierarchies | Lu Jun, Sang Zehao, Wei Haoqi, Liu Xiangyun, Zhu Kun et al. | 提出VFM-Loc零样本跨视角地理定位方法，通过对齐判别性视觉层次实现无需训练的地理定位。 | [#80](https://github.com/thinson/RS-PaperClaw/issues/80) |
| [20260314] Sky2Ground: A Benchmark for Site Modeling under Varying Altitude | Wang Zengyan, Mitra Sirshapan, Modi Rajat, Lim Grace, Rawat Yogesh | 发布Sky2Ground基准数据集，支持变高度条件下的航拍、卫星与地面影像联合场景建模。 | [#81](https://github.com/thinson/RS-PaperClaw/issues/81) |

## 🔎 观察

- 量子计算与遥感AI的交叉研究尚处早期探索阶段，其实际算力优势与工程化落地路径仍需验证
- 零样本学习与视觉基础模型的结合正重塑遥感下游任务范式，数据效率与泛化能力成为核心竞争点

---

Powered by OpenClaw🦞

---
