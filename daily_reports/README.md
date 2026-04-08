# Daily Reports

最近三天日报（最新在前）：

# [20260407](./202604/20260407.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现多模态融合与基础模型双主线并进态势。SAR-光学异构数据融合持续深化，Vision Transformers与Mamba架构在滑坡检测、变化检测等任务中广泛应用。边缘智能与近实时监测推动星上处理落地，3D Gaussian Splatting与视觉语言模型拓展UAV应用边界，大语言模型开始介入遥感任务评估环节。

## ✨ 今日亮点

- 多模态基础模型统一框架：单模型实现遥感图像修复、融合等多任务，支持语言提示引导
- Mamba架构入侵高光谱领域：物理对齐频谱Mamba实现小样本目标检测，解耦语义与动态信息
- LLM-as-Judge范式落地：大语言模型首次用于无人机电力线分割的语义质量评判

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260407] Multi-Modal Landslide Detection from Sentinel-1 SAR and Sentinel-2 Optical Imagery Using Multi-Encoder Vision Transformers and Ensemble Learning | Nasios Ioannis | 提出多编码器Vision Transformers融合Sentinel-1 SAR与Sentinel-2光学影像，集成学习提升滑坡检测精度。 | [#286](https://github.com/thinson/RS-PaperClaw/issues/286) |
| [20260407] Edge Intelligence for Satellite-based Earth Observation: Scheduling Image Acquisition and Processing | Soret Beatriz, Antonio M. Mercado-Martínez, Jurado-Navas Antonio, Nicolai D. Lyholm, Moretti Marco et al. | 构建卫星对地观测边缘智能框架，联合优化星上图像获取调度与在轨处理资源分配。 | [#287](https://github.com/thinson/RS-PaperClaw/issues/287) |
| [20260407] ASSR-Net: Anisotropic Structure-Aware and Spectrally Recalibrated Network for Hyperspectral Image Fusion | Song Qiya, Zhou Hongzhi, Tan Lishan, Dian Renwei, Li Shutao | ASSR-Net通过各向异性结构感知与光谱重校准模块，增强高光谱图像融合的空间-光谱一致性。 | [#288](https://github.com/thinson/RS-PaperClaw/issues/288) |
| [20260407] A Unified Foundation Model for All-in-One Multi-Modal Remote Sensing Image Restoration and Fusion with Language Prompting | Cui Yongchuan, Liu Peng | 统一基础模型以语言提示驱动，实现多模态遥感图像修复与融合的全任务覆盖。 | [#289](https://github.com/thinson/RS-PaperClaw/issues/289) |
| [20260407] Physics-Aligned Spectral Mamba: Decoupling Semantics and Dynamics for Few-Shot Hyperspectral Target Detection | Gong Luqi, Xie Qixin, Chen Yue, Chen Ziqiang, Fan Fanda et al. | 物理对齐频谱Mamba解耦语义与动态特征，支撑高光谱小样本目标检测的元学习范式。 | [#290](https://github.com/thinson/RS-PaperClaw/issues/290) |
| [20260407] Prior-guided Fusion of Multimodal Features for Change Detection from Optical-SAR Images | Liu Xuanguang, Ding Lei, Li Yujie, Dai Chenguang, Zhang Zhenchao et al. | 先验引导的多模态特征融合网络，挖掘光学-SAR影像的模态特异性与时序变化信息。 | [#291](https://github.com/thinson/RS-PaperClaw/issues/291) |
| [20260407] LSGS-Loc: Towards Robust 3DGS-Based Visual Localization for Large-Scale UAV Scenarios | Zhang Xiang, Wang Tengfei, Xu Fang, Wang Xin, Zhan Zongqian | LSGS-Loc面向大规模无人机场景，基于3D高斯溅射实现尺度感知的鲁棒视觉定位。 | [#292](https://github.com/thinson/RS-PaperClaw/issues/292) |
| [20260407] Near real-time monitoring of global land-ocean cover dynamics | Wang Lixing, Li Tao, Dou Xinyu, Liu Zhu | 全球陆海覆盖近实时监测系统，同步追踪陆地覆盖与海冰动态变化。 | [#293](https://github.com/thinson/RS-PaperClaw/issues/293) |
| [20260407] UAVReason: A Unified, Large-Scale Benchmark for Multimodal Aerial Scene Reasoning and Generation | Sun Jintao, Zhang Hu, Di Donglin, Ding Gangyi, Zheng Zhedong | UAVReason构建首个大规模无人机多模态场景推理与生成基准，覆盖视觉问答与图像生成任务。 | [#294](https://github.com/thinson/RS-PaperClaw/issues/294) |
| [20260407] LLM-as-Judge for Semantic Judging of Powerline Segmentation in UAV Inspection | Hossain Akram, Abdelfattah Rabab, Wang Xiaofeng, Abdelfatah Kareem | LLM-as-Judge框架替代传统指标，对无人机巡检中的电力线分割结果进行语义级质量评估。 | [#295](https://github.com/thinson/RS-PaperClaw/issues/295) |

## 🔎 观察

- Mamba与Transformer形成架构竞争：Mamba凭借线性复杂度优势开始渗透高光谱时序建模，但Transformer在多模态融合中仍占主导。
- 遥感评估范式面临变革：LLM-as-Judge的出现暗示像素级指标可能向语义级评判演进，但计算开销与可解释性仍是落地瓶颈。

---

Powered by OpenClaw🦞

---

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
