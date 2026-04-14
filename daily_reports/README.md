# Daily Reports

最近三天日报（最新在前）：

# [20260413](./202604/20260413.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现多模态融合与效率优化双主线。Mamba架构、扩散模型与联邦学习等新兴技术持续渗透，视觉语言模型在变化检测与跨模态任务中表现活跃。同时，成本感知学习、无训练压缩及低空经济基础设施等应用导向研究凸显行业对实用化部署的迫切需求。

## ✨ 今日亮点

- Mamba多模态网络实现爆炸载荷下结构损伤快速评估，兼顾多尺度特征融合
- HuiYanEarth-SAR基础模型以地理先验驱动高保真SAR图像低成本生成
- 语义-几何双压缩策略实现超高分辨率遥感图像的无训练视觉令牌精简

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260413] A Mamba-Based Multimodal Network for Multiscale Blast-Induced Rapid Structural Damage Assessment | Ma Wanli, Selvakumaran Sivasakthy, Dain G. Farrimond, Adam A. Dennis, Samuel E. Rigby | 基于Mamba的多模态网络融合多源数据，实现爆炸载荷下结构损伤的快速多尺度评估。 | [#331](https://github.com/thinson/RS-PaperClaw/issues/331) |
| [20260413] The Impact of Federated Learning on Distributed Remote Sensing Archives | Umashankar Anand, Tomotaki-Dawoud Karam, Schneider Nicolai | 探讨联邦学习在分布式遥感档案中的应用，针对Non-IID数据优化FedAvg与FedProx策略。 | [#332](https://github.com/thinson/RS-PaperClaw/issues/332) |
| [20260413] HuiYanEarth-SAR: A Foundation Model for High-Fidelity and Low-Cost Global Remote Sensing Imagery Generation | Liu Yongxiang, Zhou Jie, Song Yafei, Liu Tianpeng, Liu Li | HuiYanEarth-SAR基础模型整合地理先验与散射机制，实现高保真低成本全球SAR图像生成。 | [#333](https://github.com/thinson/RS-PaperClaw/issues/333) |
| [20260413] Observe Less, Understand More: Cost-aware Cross-scale Observation for Remote Sensing Understanding | Xie Zhenghao, Xiao Jing, Wang Zhenqi, Ma Kexin, Liao Liang et al. | 提出成本感知的跨尺度观测框架，以更少观测实现遥感理解任务的高效推理。 | [#334](https://github.com/thinson/RS-PaperClaw/issues/334) |
| [20260413] Beyond Reconstruction: Reconstruction-to-Vector Diffusion for Hyperspectral Anomaly Detection | Xiang Jijun, Wang Jiayi, Wang Pengxiang, Chen Cheng, Wang Nian et al. | 重构至向量扩散模型突破传统重建范式，通过流形净化提升高光谱亚像素异常检测精度。 | [#335](https://github.com/thinson/RS-PaperClaw/issues/335) |
| [20260413] Toward Environment-Aware LAE: SAR as a Shared Sensing Infrastructure | Zhang Xue, Huang Bang, Alouini Mohamed-Slim | 探讨SAR作为低空经济共享感知基础设施的环境感知潜力与应用架构。 | [#336](https://github.com/thinson/RS-PaperClaw/issues/336) |
| [20260413] A Deep Equilibrium Network for Hyperspectral Unmixing | Wang Chentong, Gao Jincheng, Zhu Fei, Chen Jie | 深度均衡网络以隐式微分求解高光谱解混，联合光谱-空间特征实现丰度估计。 | [#337](https://github.com/thinson/RS-PaperClaw/issues/337) |
| [20260413] Bridging the RGB-IR Gap: Consensus and Discrepancy Modeling for Text-Guided Multispectral Detection | Wu Jiaqi, Wang Zhen, Huang Enhao, Shen Kangqing, Wang Yulin et al. | 文本引导的多光谱检测框架建模RGB-IR共识与差异，弥合跨模态语义鸿沟。 | [#338](https://github.com/thinson/RS-PaperClaw/issues/338) |
| [20260413] Seg2Change: Adapting Open-Vocabulary Semantic Segmentation Model for Remote Sensing Change Detection | Su You, Song Yonghong, Chen Jingqi, Wen Zehan | Seg2Change将开放词汇语义分割模型适配至遥感变化检测，拓展视觉语言模型应用边界。 | [#339](https://github.com/thinson/RS-PaperClaw/issues/339) |
| [20260413] Semantic-Geometric Dual Compression: Training-Free Visual Token Reduction for Ultra-High-Resolution Remote Sensing Understanding | Li Yueying, Wang Fengxiang, Li Yan, Chen Mingshuo, Zhao Mengying et al. | 语义-几何双压缩策略无需训练即可削减超高分辨率遥感图像的视觉令牌，适配多模态大模型。 | [#340](https://github.com/thinson/RS-PaperClaw/issues/340) |

## 🔎 观察

- 视觉语言模型正从通用领域向遥感专用任务纵深渗透，开放词汇与变化检测的结合或成新范式。
- 效率优化研究呈现分层态势：既有数据层面的成本感知采样，也有模型层面的令牌压缩与隐式网络设计。

---

Powered by OpenClaw🦞

---

# [20260412](./202604/20260412.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究聚焦多模态大模型与基础模型创新。视觉语言模型在地理定位任务中实现生成器向检索器的范式转换，遥感基础模型探索语义 grounding 新路径。同时，多光谱融合与主动式激光雷达-惯性里程计等方向亦有进展，体现从数据融合到智能交互的技术纵深。

## ✨ 今日亮点

- MLLM解锁自然语言引导的地理定位，通过参数高效微调实现生成到检索的范式跃迁
- GeoMeld构建语义 grounded 的遥感基础模型，推进多模态对比学习与地理空间AI融合
- CoFusion提出光谱坐标注意力机制，实现多光谱与高光谱图像的高效融合

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260412] Turning Generators into Retrievers: Unlocking MLLMs for Natural Language-Guided Geo-Localization | Chen Yuqi, Zhang Xiaohan, Arrabi Ahmad, Sultani Waqas, Chen Chen et al. | Chen等提出将多模态大语言模型从生成器转化为检索器，通过参数高效微调实现自然语言引导的地理定位。 | [#327](https://github.com/thinson/RS-PaperClaw/issues/327) |
| [20260412] GeoMeld: Toward Semantically Grounded Foundation Models for Remote Sensing | Hasan Maram, Md Aminur Hossain, Roy Savitra, Bhowmik Souparna, Ayush V. Patel et al. | Hasan等构建GeoMeld框架，通过语义 grounding 与对比学习增强遥感基础模型的多模态表征能力。 | [#328](https://github.com/thinson/RS-PaperClaw/issues/328) |
| [20260412] CoFusion: Multispectral and Hyperspectral Image Fusion via Spectral Coordinate Attention | Li Baisong | Li提出CoFusion方法，利用光谱坐标注意力机制实现多光谱与高光谱图像的多尺度空谱协同融合。 | [#329](https://github.com/thinson/RS-PaperClaw/issues/329) |
| [20260412] AWARE: Adaptive Whole-body Active Rotating Control for Enhanced LiDAR-Inertial Odometry under Human-in-the-Loop Interaction | Zhang Yizhe, Li Jianping, Yin Liangliang, Dong Zhen, Yang Bisheng | Zhang等设计AWARE系统，通过人在回路交互实现无人机全身体主动旋转控制以增强激光雷达-惯性里程计。 | [#342](https://github.com/thinson/RS-PaperClaw/issues/342) |

## 🔎 观察

- 视觉语言模型正从通用领域向遥感专用场景深度渗透，生成-检索范式转换或重塑跨模态检索技术路线
- 主动感知与人机协同成为无人机导航新趋势，传统被动式状态估计向交互式智能控制演进

---

Powered by OpenClaw🦞

---

# [20260411](./202604/20260411.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦多模态融合与轻量化部署两大方向。Vision Transformer持续渗透卫星影像分析领域，涵盖多尺度表征、SAR-光学配准及高光谱甲烷检测等场景。同时，神经架构搜索与知识蒸馏推动边缘计算应用，红外超分辨率则关注双分支架构设计。

## ✨ 今日亮点

- ALiBi位置编码优化多模态多尺度卫星影像表征学习
- SatReg提出回归驱动NAS实现轻量化卫星图像分割
- EMIT高光谱数据结合深度学习实现全球甲烷点源监测

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260411] Multi-modal, multi-scale representation learning for satellite imagery analysis just needs a good ALiBi | Kage Patrick, Andreadis Pavlos | 论文提出基于ALiBi位置编码的多模态多尺度表征学习方法，优化卫星影像分析中的长距离依赖建模。 | [#321](https://github.com/thinson/RS-PaperClaw/issues/321) |
| [20260411] SatReg: Regression-based Neural Architecture Search for Lightweight Satellite Image Segmentation | Humes Edward, Mohsenin Tinoosh | SatReg采用回归策略引导神经架构搜索，结合知识蒸馏构建面向边缘计算的轻量级卫星图像分割模型。 | [#322](https://github.com/thinson/RS-PaperClaw/issues/322) |
| [20260411] Are Pretrained Image Matchers Good Enough for SAR-Optical Satellite Registration? | Corley Isaac, Stoken Alex, Berton Gabriele | 研究系统评估预训练图像匹配器在SAR-光学卫星配准中的零样本迁移能力，探讨跨模态匹配瓶颈。 | [#323](https://github.com/thinson/RS-PaperClaw/issues/323) |
| [20260411] Dual-Branch Remote Sensing Infrared Image Super-Resolution | Ge Xining, Chang Gengjia, Yuan Weijun, Li Zhan, Chen Zhanglu et al. | 双分支网络架构针对遥感红外图像超分辨率任务，分别处理空间细节与热辐射特征以重建高分辨率影像。 | [#324](https://github.com/thinson/RS-PaperClaw/issues/324) |
| [20260411] Global monitoring of methane point sources using deep learning on hyperspectral radiance measurements from EMIT | Vishal V. Batchu, Conserva Michelangelo, Wilson Alex, Anna M. Michalak, Gulshan Varun et al. | 基于EMIT传感器高光谱辐射测量数据，构建深度学习模型实现全球范围内甲烷点源排放的自动识别与量化。 | [#325](https://github.com/thinson/RS-PaperClaw/issues/325) |

## 🔎 观察

- 位置编码技术正成为提升卫星影像Transformer性能的关键切入点，ALiBi的外推特性或缓解多尺度训练-推理不一致问题。
- 遥感模型轻量化从单纯压缩向自动化架构设计演进，NAS与任务特定回归目标结合可能重塑边缘部署范式。

---

Powered by OpenClaw🦞

---
