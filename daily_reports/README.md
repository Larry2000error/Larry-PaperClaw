# Daily Reports

最近三天日报（最新在前）：

# [20260411](./202604/20260411.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦多模态融合与轻量化部署两大方向。Vision Transformer持续渗透卫星影像分析领域，涵盖多尺度表征、SAR-光学配准及高光谱甲烷检测等场景。同时，神经架构搜索与知识蒸馏推动边缘计算应用，红外超分辨率与跨模态匹配技术亦获关注。

## ✨ 今日亮点

- ALiBi位置编码优化多模态多尺度卫星影像表征学习
- SatReg以回归驱动NAS实现轻量化卫星图像分割
- EMIT高光谱数据结合深度学习实现全球甲烷点源监测

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260411] Multi-modal, multi-scale representation learning for satellite imagery analysis just needs a good ALiBi | Kage Patrick, Andreadis Pavlos | 提出基于ALiBi位置编码的多模态多尺度卫星影像表征学习方法，优化Vision Transformer处理多尺度特征的能力。 | [#321](https://github.com/thinson/RS-PaperClaw/issues/321) |
| [20260411] SatReg: Regression-based Neural Architecture Search for Lightweight Satellite Image Segmentation | Humes Edward, Mohsenin Tinoosh | SatReg采用回归驱动神经架构搜索，结合知识蒸馏开发轻量化卫星图像分割模型，适配边缘计算场景。 | [#322](https://github.com/thinson/RS-PaperClaw/issues/322) |
| [20260411] Are Pretrained Image Matchers Good Enough for SAR-Optical Satellite Registration? | Corley Isaac, Stoken Alex, Berton Gabriele | 系统评估预训练图像匹配器在SAR-光学卫星配准中的零样本迁移性能，探讨跨模态匹配可行性。 | [#323](https://github.com/thinson/RS-PaperClaw/issues/323) |
| [20260411] Dual-Branch Remote Sensing Infrared Image Super-Resolution | Ge Xining, Chang Gengjia, Yuan Weijun, Li Zhan, Chen Zhanglu et al. | 设计双分支网络架构用于遥感红外图像超分辨率，针对性处理热红外影像的空间细节恢复问题。 | [#324](https://github.com/thinson/RS-PaperClaw/issues/324) |
| [20260411] Global monitoring of methane point sources using deep learning on hyperspectral radiance measurements from EMIT | Vishal V. Batchu, Conserva Michelangelo, Wilson Alex, Anna M. Michalak, Gulshan Varun et al. | 基于EMIT高光谱辐射测量数据，利用深度学习Vision Transformer实现全球甲烷点源排放的自动监测与定位。 | [#325](https://github.com/thinson/RS-PaperClaw/issues/325) |

## 🔎 观察

- 位置编码技术（ALiBi）正成为优化卫星影像多尺度处理的新切入点，或替代传统插值与金字塔结构。
- 轻量化NAS与知识蒸馏的组合范式，反映出遥感模型从云端向边缘端部署的产业化需求加速显现。

---

Powered by OpenClaw🦞

---

# [20260410](./202604/20260410.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 8 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现三大趋势：一是多模态大模型基准测试成为热点，GeoMMBench与HM-Bench分别聚焦地理科学与高光谱领域；二是物理驱动与不确定性量化方法兴起，量子机器学习与物理信息神经网络进入水文建模；三是实用化技术持续深化，涵盖无人机图像修复、主动学习分割及域适应云检测等方向。

## ✨ 今日亮点

- 量子物理信息神经网络首次用于水文PDE约束学习，实现内嵌不确定性量化
- GreenScatter突破植被覆盖区土壤水分探测难题，无人机雷达微波遥感新进展
- 多模态大模型基准双发：GeoMMBench覆盖地理科学全领域，HM-Bench专攻高光谱

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260410] Variational Quantum Physics-Informed Neural Networks for Hydrological PDE-Constrained Learning with Inherent Uncertainty Quantification | Prasad Nimantha Madusanka Ukwatta Hewage, Chakkravarthy Midhun, Ruvan Kumara Abeysekara | 变分量子物理信息神经网络将量子机器学习引入水文偏微分方程约束学习，实现不确定性内嵌量化。 | [#311](https://github.com/thinson/RS-PaperClaw/issues/311) |
| [20260410] GreenScatter: Through-Canopy Soil Moisture Sensing with UAV-Mounted Radar | Jacobs Luke, Aziz Ishfaq, Lu Benhao, Tabatabaeenejad Alireza, Alipour Mohamad et al. | GreenScatter利用无人机载雷达穿透植被冠层，创新解决覆盖区土壤水分微波遥感探测难题。 | [#312](https://github.com/thinson/RS-PaperClaw/issues/312) |
| [20260410] Compositional-Degradation UAV Image Restoration: Conditional Decoupled MoE Network and A Benchmark | Yan Jinquan, Zhao Zhicheng, Tu Zhengzheng, Li Chenglong, Tang Jin et al. | 条件解耦混合专家网络针对无人机图像复合退化问题，构建多退化去除新基准。 | [#313](https://github.com/thinson/RS-PaperClaw/issues/313) |
| [20260410] Dynamic Class-Aware Active Learning for Unbiased Satellite Image Segmentation | Gadi Hemanth Kumar, Nambiar Athira, Bodani Pankaj | 动态类别感知主动学习策略优化卫星图像分割标注效率，缓解类别不平衡与标注偏差。 | [#314](https://github.com/thinson/RS-PaperClaw/issues/314) |
| [20260410] Low-Data Supervised Adaptation Outperforms Prompting for Cloud Segmentation Under Domain Shift | Kethavath Harshith, Hu Weiming | 低数据监督适应方法在域迁移云分割任务中超越提示工程，验证CLIP视觉语言模型微调潜力。 | [#315](https://github.com/thinson/RS-PaperClaw/issues/315) |
| [20260410] Fast Model-guided Instance-wise Adaptation Framework for Real-world Pansharpening with Fidelity Constraints | Yang Zhiqi, Xiao Jin-Liang, Yin Shan, Deng Liang-Jian, Vivone Gemine | 模型引导的实例级快速适应框架实现零样本真实世界全色锐化，兼顾保真度约束与实时性。 | [#316](https://github.com/thinson/RS-PaperClaw/issues/316) |
| [20260410] GeoMMBench and GeoMMAgent: Toward Expert-Level Multimodal Intelligence in Geoscience and Remote Sensing | Xiao Aoran, Cheng Shihao, Xu Yonghao, Ren Yexian, Chen Hongruixuan et al. | GeoMMBench与GeoMMAgent构建地理科学多模态大模型评测体系，推动专家级地学智能发展。 | [#317](https://github.com/thinson/RS-PaperClaw/issues/317) |
| [20260410] HM-Bench: A Comprehensive Benchmark for Multimodal Large Language Models in Hyperspectral Remote Sensing | Zhang Xinyu, Mai Zurong, Li Qingmei, Liao Zjin, Wen Yibin et al. | HM-Bench建立高光谱遥感多模态大模型综合基准，系统评估光谱-空间联合理解能力。 | [#318](https://github.com/thinson/RS-PaperClaw/issues/318) |

## 🔎 观察

- 基准建设进入细分垂直领域：从通用遥感转向高光谱、地理科学等专业模态，评测维度更贴近实际应用需求
- 物理约束与数据驱动融合加速：量子计算、物理信息神经网络等新型计算范式开始解决传统遥感反演中的不确定性难题

---

Powered by OpenClaw🦞

---

# [20260408](./202604/20260408.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究呈现三大趋势：一是空间智能与神经表示技术深度融合，OpenSpatial与NeRF类方法推动三维时空建模；二是星上实时处理与量子计算等新型计算范式兴起，拓展遥感系统边界；三是不确定性量化与物理约束嵌入成为提升模型可靠性的关键路径。

## ✨ 今日亮点

- OpenSpatial构建空间智能数据引擎，系统化生成3D标注数据
- 神经辐射场技术延伸至地球观测连续时空表示学习
- 量子-经典混合网络首次应用于遥感图像分割任务

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260408] OpenSpatial: A Principled Data Engine for Empowering Spatial Intelligence | Liu Jianhui, Sun Haoze, Li Wenbo, Zhang Yanbing, Yang Rui et al. | OpenSpatial提出原则性数据引擎，通过程序化生成与人工验证结合，构建大规模3D空间理解数据集。 | [#297](https://github.com/thinson/RS-PaperClaw/issues/297) |
| [20260408] Assessing the Added Value of Onboard Earth Observation Processing with the IRIDE HEO Service Segment | Parampuneet Kaur Thind, Mwangi Charles, Varetto Giovanni, Sarti Lorenzo, Papa Andrea et al. | IRIDE高椭圆轨道服务段评估星上处理对地观测数据的增值效应，推动服务化架构在轨应用。 | [#298](https://github.com/thinson/RS-PaperClaw/issues/298) |
| [20260408] Location Is All You Need: Continuous Spatiotemporal Neural Representations of Earth Observation Data | Madadikhaljan Mojgan, Prexl Jonathan, Wittmann Isabelle, Conrad M Albrecht, Schmitt Michael | 基于位置编码的连续时空神经表示方法，将NeRF技术扩展至不规则采样的地球观测数据建模。 | [#299](https://github.com/thinson/RS-PaperClaw/issues/299) |
| [20260408] Canopy Tree Height Estimation Using Quantile Regression: Modeling and Evaluating Uncertainty in Remote Sensing | Schrödter Karsten, Pauls Jan, Gieseke Fabian | 分位数回归框架用于冠层树高估计，显式建模预测不确定性以提升遥感反演可靠性。 | [#300](https://github.com/thinson/RS-PaperClaw/issues/300) |
| [20260408] SCT-MOT: Enhancing Air-to-Air Multiple UAVs Tracking with Swarm-Coupled Motion and Trajectory Guidance | Chu Zhaochen, Song Tao, Jin Ren, He Shaoming, Lin Defu et al. | SCT-MOT利用蜂群耦合运动与轨迹引导，解决空中对空中多无人机跟踪的密集遮挡难题。 | [#301](https://github.com/thinson/RS-PaperClaw/issues/301) |
| [20260408] HQF-Net: A Hybrid Quantum-Classical Multi-Scale Fusion Network for Remote Sensing Image Segmentation | Md Aminur Hossain, Ayush V. Patel, Gole Siddhant, Sanjay K. Singh, Banerjee Biplab | HQF-Net设计混合量子-经典多尺度融合网络，探索量子机器学习在遥感语义分割中的潜力。 | [#302](https://github.com/thinson/RS-PaperClaw/issues/302) |
| [20260408] Accelerating 4D Hyperspectral Imaging through Physics-Informed Neural Representation and Adaptive Sampling | Ho Chi-Jui, Bhakta Harsh, Xiong Wei, Antipa Nicholas | 物理信息神经表示结合自适应采样，实现四维高光谱成像的高效压缩与重建加速。 | [#303](https://github.com/thinson/RS-PaperClaw/issues/303) |

## 🔎 观察

- 神经表示技术正从计算机视觉向遥感专用化演进，时空连续建模成为地学基础模型的新基座。
- 星上智能处理与量子计算等前沿范式同步涌现，暗示遥感系统架构可能面临代际变革窗口。

---

Powered by OpenClaw🦞

---
