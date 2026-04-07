# Daily Reports

最近三天日报（最新在前）：

# [20260406](./202604/20260406.md)
## 📌 今日概况

今日共检索候选论文 7 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦空天信息智能处理与传输优化。三篇论文分别覆盖无人机实时深度估计、低轨卫星协同大模型推理及卫星移动性驱动的遥感数据分发，体现遥感AI向边缘智能、星上计算与高效通信融合发展的趋势。

## ✨ 今日亮点

- ZeD-MAP实现零样本深度估计与光束法平差结合，支撑无人机实时三维重建
- 面向LEO星座的LLM协同推理框架，通过模型分割与流水线并行降低通信开销
- OrbitTransit利用卫星轨道移动性优化遥感数据扩散，提升全球观测覆盖效率

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260406] ZeD-MAP: Bundle Adjustment Guided Zero-Shot Depth Maps for Real-Time Aerial Imaging | Selim Ahmet Iz, Nex Francesco, Kerle Norman, Meissner Henry, Berger Ralf | ZeD-MAP提出光束法平差引导的零样本深度估计方法，无需训练数据即可实现无人机实时 aerial imaging 三维建图。 | [#282](https://github.com/thinson/RS-PaperClaw/issues/282) |
| [20260406] Communication-Efficient Collaborative LLM Inference over LEO Satellite Networks | Zhang Songge, Wu Wen, Li Liang, Wang Ye, Xuemin et al. | 该研究设计通信高效的协同LLM推理架构，通过模型切分与流水线并行适配低轨卫星网络带宽受限场景。 | [#283](https://github.com/thinson/RS-PaperClaw/issues/283) |
| [20260406] OrbitTransit: Traffic Delivery and Diffusion for Earth Observation via Satellite Mobility | Zhao Haoyuan, Chen Long, Yi Ching Chou, Fang Hao, Liu Jiangchuan | OrbitTransit利用低轨卫星轨道移动性构建动态流量交付网络，优化地球观测数据的全球扩散与时效性。 | [#284](https://github.com/thinson/RS-PaperClaw/issues/284) |

## 🔎 观察

- 星载智能计算成为热点，LLM推理与深度估计等重型任务正向卫星边缘迁移，需平衡算力与能耗约束
- 卫星网络研究从静态拓扑转向动态移动性利用，轨道预测驱动的数据路由或成下一代天基基础设施关键

---

Powered by OpenClaw🦞

---

# [20260405](./202604/20260405.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多模态融合与专业化模型并进的趋势。基础模型建设向高频时序数据延伸，视觉语言模型拓展至能源预测领域，SAR目标检测引入稀疏专家混合架构，同时低空经济基础设施研究关注通信控制协同设计。不确定性量化与跨域泛化成为时空融合任务的关键技术方向。

## ✨ 今日亮点

- HighFM构建面向高频地球观测数据的基础模型，强化时空表征学习能力
- Solar-VLM将多模态视觉语言模型引入光伏功率预测，实现跨模态能源时序建模
- SARES-DEIM在SAR舰船检测中融合稀疏混合专家与DETR架构，提升复杂场景鲁棒性

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260405] HighFM: Towards a Foundation Model for Learning Representations from High-Frequency Earth Observation Data | Girtsou Stella, Alexis Konstantinos, Giannopoulos Giorgos, Kontoes Harris | HighFM针对高频卫星观测数据设计基础模型，学习细粒度时空表征以支撑下游遥感任务。 | [#276](https://github.com/thinson/RS-PaperClaw/issues/276) |
| [20260405] Uncertainty-Aware Test-Time Adaptation for Cross-Region Spatio-Temporal Fusion of Land Surface Temperature | Bouaziz Sofiane, Hafiane Adel, Canals Raphael, Nedjai Rachid | 该研究提出不确定性感知的测试时自适应方法，解决地表温度跨区域时空融合中的域迁移问题。 | [#277](https://github.com/thinson/RS-PaperClaw/issues/277) |
| [20260405] Solar-VLM: Multimodal Vision-Language Models for Augmented Solar Power Forecasting | Fan Hang, Pei Haoran, Liang Runze, Liu Weican, Cheng Long et al. | Solar-VLM整合视觉语言模型与多模态学习，增强光伏发电预测对气象条件的语义理解能力。 | [#278](https://github.com/thinson/RS-PaperClaw/issues/278) |
| [20260405] SARES-DEIM: Sparse Mixture-of-Experts Meets DETR for Robust SAR Ship Detection | Song Fenghao, Yang Shaojing, Zhou Xi | SARES-DEIM将稀疏混合专家机制嵌入DETR检测框架，优化SAR图像舰船目标的复杂背景识别。 | [#279](https://github.com/thinson/RS-PaperClaw/issues/279) |
| [20260405] UAV Control and Communication Enabled Low-Altitude Economy: Challenges, Resilient Architecture and Co-design Strategies | Liang Tianhao, Su Nanchi, Ping Yuqi, Lei Guangyu, Chen Xinglin et al. | 该综述探讨低空经济中无人机通信控制协同设计，提出韧性架构应对城市复杂环境挑战。 | [#280](https://github.com/thinson/RS-PaperClaw/issues/280) |

## 🔎 观察

- 遥感基础模型正从静态图像向高频时序数据演进，时序分辨率成为新的技术竞争维度
- 视觉语言模型的跨域迁移能力使其成为连接遥感数据与专业应用（如能源、交通）的桥梁

---

Powered by OpenClaw🦞

---

# [20260404](./202604/20260404.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究聚焦三大方向：表征学习、高效计算与物理驱动成像。多任务表征学习通过互信息优化提升泛化能力；SAR成像借助Apple Silicon架构实现数量级加速；物理约束的无监督网络为单像素高光谱超分辨开辟新路径。

## ✨ 今日亮点

- 多标注三元组学习框架，以任务导向互信息最大化实现遥感表征自适应优化
- Apple Silicon单调度FFT流水线，将SAR成像从8秒压缩至370毫秒
- 物理信息无训练网络，RGB引导实现单像素高光谱超分辨重建

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260404] Task-Guided Multi-Annotation Triplet Learning for Remote Sensing Representations | Zhou Meilun, Zare Alina | 提出任务引导多标注三元组学习，通过互信息最大化优化遥感表征的多任务适应性。 | [#272](https://github.com/thinson/RS-PaperClaw/issues/272) |
| [20260404] From 8 Seconds to 370ms: Kernel-Fused SAR Imaging on Apple Silicon via Single-Dispatch FFT Pipelines | Mohamed Amine Bergach | 设计核融合SAR成像方案，利用Apple Silicon统一内存架构与单调度FFT流水线实现22倍加速。 | [#273](https://github.com/thinson/RS-PaperClaw/issues/273) |
| [20260404] Physics-Informed Untrained Learning for RGB-Guided Superresolution Single-Pixel Hyperspectral Imaging | Zhang Hao, Xu Bilige, Wei Lichen, Ma Xu, Ren Wenyi | 构建物理信息无训练神经网络，以RGB先验引导单像素高光谱成像的超分辨重建。 | [#274](https://github.com/thinson/RS-PaperClaw/issues/274) |

## 🔎 观察

- 边缘计算硬件优化正成为遥感实时处理的关键突破口，Apple Silicon等异构架构值得持续关注
- 物理约束与无训练学习的结合，为数据稀缺场景下的高光谱成像提供了可解释性新范式

---

Powered by OpenClaw🦞

---
