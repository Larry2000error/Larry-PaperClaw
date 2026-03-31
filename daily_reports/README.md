# Daily Reports

最近三天日报（最新在前）：

# [20260330](./202603/20260330.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多模态融合与生成模型深化趋势。显著性检测引入矫正流与扩散模型，图像-文本检索聚焦噪声鲁棒性，合成数据集构建与物理模型结合更紧密。同时，无人机平台创新与跨域应用（无线通信信道推断）拓展了遥感技术的边界。

## ✨ 今日亮点

- ORSIFlow将矫正流与显著性引导结合，提升光学遥感显著目标检测精度
- 自旋三旋翼无人机通过模型预测控制实现视场扩展与自主飞行
- SVH-BD基于PROSAIL模型构建合成植被高光谱基准数据集

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260330] ORSIFlow: Saliency-Guided Rectified Flow for Optical Remote Sensing Salient Object Detection | Chen Haojing, Li Yutong, Liu Zhihang, Tan Tao, Bian Haoyu et al. | ORSIFlow提出显著性引导的矫正流框架，将潜在扩散模型引入光学遥感显著目标检测任务。 | [#225](https://github.com/thinson/RS-PaperClaw/issues/225) |
| [20260330] A Self-Rotating Tri-Rotor UAV for Field of View Expansion and Autonomous Flight | Zhou Xiaobin, Zheng Zihao, Jin Aoxu, Qiang Lei, Zhu Bo | 自旋三旋翼无人机采用非线性动态逆与模型预测控制，实现360度视场扩展与稳定自主飞行。 | [#226](https://github.com/thinson/RS-PaperClaw/issues/226) |
| [20260330] SVH-BD : Synthetic Vegetation Hyperspectral Benchmark Dataset for Emulation of Remote Sensing Images | Chedly Ben Azizi, Guilloteau Claire, Roussel Gilles, Puigt Matthieu | SVH-BD基于PROSAIL辐射传输模型合成植被高光谱数据，为遥感反演算法提供可控基准。 | [#227](https://github.com/thinson/RS-PaperClaw/issues/227) |
| [20260330] Robust Remote Sensing Image-Text Retrieval with Noisy Correspondence | Song Qiya, Xie Yiqiang, Sun Yuan, Dian Renwei, Kang Xudong | 针对遥感图文检索中的噪声对应问题，提出自步学习策略提升跨模态检索鲁棒性。 | [#228](https://github.com/thinson/RS-PaperClaw/issues/228) |
| [20260330] Deep Learning Based Site-Specific Channel Inference Using Satellite Images | Song Junzhe, He Ruisi, Yang Mi, Zhang Zhengyu, Gao Shuaiqi et al. | 利用卫星图像与深度学习进行站点级无线信道推断，支撑通信网络规划。 | [#229](https://github.com/thinson/RS-PaperClaw/issues/229) |

## 🔎 观察

- 生成式模型正从数据增强工具转向遥感解译核心架构，矫正流等新型扩散变体开始落地
- 遥感与垂直领域交叉加速，无线通信信道推断表明卫星图像正成为新型地理信息基础设施

---

Powered by OpenClaw🦞

---

# [20260329](./202603/20260329.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现两大主线：一是大语言模型深度渗透，从导航指令解析、物理先验知识嵌入到开放词汇变化检测，LLM正成为连接高层语义与底层视觉的关键桥梁；二是具身智能与能效优化并重，无人机导航与跟踪系统在神经形态计算加持下向低功耗、高鲁棒方向演进。

## ✨ 今日亮点

- 跨视角地理定位引入OpenStreetMap度量信息，实现全景图像的鲁棒 holistic 定位
- 扩散模型引导的原型检索机制，支撑遥感开放词汇变化检测新范式
- 脉冲神经网络首次系统应用于无人机目标跟踪，显著降低能耗同时保持精度

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260329] RHO: Robust Holistic OSM-Based Metric Cross-View Geo-Localization | Zheng Junwei, Dai Ruize, Liu Ruiping, Zeng Zichao, Chen Yufan et al. | RHO提出基于OSM的鲁棒整体度量跨视角地理定位方法，融合全景图像与地图度量信息提升定位精度。 | [#219](https://github.com/thinson/RS-PaperClaw/issues/219) |
| [20260329] OpenDPR: Open-Vocabulary Change Detection via Vision-Centric Diffusion-Guided Prototype Retrieval for Remote Sensing Imagery | Guo Qi, Wang Jue, Liu Yinhe, Zhong Yanfei | OpenDPR构建以视觉为中心的扩散引导原型检索框架，实现遥感影像的开放词汇变化检测。 | [#220](https://github.com/thinson/RS-PaperClaw/issues/220) |
| [20260329] LLM-Enabled Low-Altitude UAV Natural Language Navigation via Signal Temporal Logic Specification Translation and Repair | Ping Yuqi, Ding Huahao, Liang Tianhao, Zhou Longyu, Lei Guangyu et al. | 该方法将大语言模型与信号时序逻辑结合，完成低空无人机自然语言导航指令的形式化转换与修复。 | [#221](https://github.com/thinson/RS-PaperClaw/issues/221) |
| [20260329] Transferring Physical Priors into Remote Sensing Segmentation via Large Language Models | Lu Yuxi, Li Kunqi, Li Zhidong, Su Xiaohan, Wu Biao et al. | 研究通过大语言模型将物理先验知识编码为知识图谱，迁移至遥感语义分割任务以增强可解释性。 | [#222](https://github.com/thinson/RS-PaperClaw/issues/222) |
| [20260329] Fully Spiking Neural Networks with Target Awareness for Energy-Efficient UAV Tracking | Zhong Pengzhi, Mo Jiwei, Zeng Dan, He Feixiang, Li Shuiwang | 该工作设计目标感知的全脉冲神经网络，在无人机跟踪任务中实现能效与精度的协同优化。 | [#232](https://github.com/thinson/RS-PaperClaw/issues/232) |

## 🔎 观察

- LLM正从'工具调用'转向'知识内化'，物理规律与逻辑约束的显式嵌入成为提升遥感模型可信度的关键路径
- 神经形态计算与无人机平台的结合预示边缘智能新趋势，能效约束下的算法-硬件协同设计将成竞争焦点

---

Powered by OpenClaw🦞

---

# [20260328](./202603/20260328.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦智能感知与自主导航两大方向。成像领域探索无透镜偏振重建与多模态融合；定位导航方向关注跨视角地理定位与无人机避障控制，视觉-语言模型与事件相机等新型传感器成为技术热点。

## ✨ 今日亮点

- 无透镜偏振成像突破传统光学限制，RGB引导重建降低硬件复杂度
- 零样本VL模型实现跨视角地理定位重排序，无需标注数据适配新场景
- 事件相机与深度融合赋能高速无人机端到端避障控制

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260328] Guided Lensless Polarization Imaging | Kraicer Noa, Yosef Erez, Giryes Raja | 提出RGB引导的无透镜偏振成像方法，通过计算重建实现紧凑光学系统下的偏振信息恢复。 | [#215](https://github.com/thinson/RS-PaperClaw/issues/215) |
| [20260328] Zero-shot Vision-Language Reranking for Cross-View Geolocalization | Yunus Talha Erzurumlu, John E. Anderson, William J. Shuart, Toth Charles, Yilmaz Alper | 利用LLaVA等视觉-语言模型进行零样本重排序，提升跨视角地理定位的泛化能力与检索精度。 | [#216](https://github.com/thinson/RS-PaperClaw/issues/216) |
| [20260328] An End-to-end Flight Control Network for High-speed UAV Obstacle Avoidance based on Event-Depth Fusion | Shang Dikai, Zhao Jingyue, Xu Shi, Ye Nanyang, Wang Lei | 基于事件相机与深度融合构建端到端飞行控制网络，采用模仿学习实现高速无人机实时避障。 | [#217](https://github.com/thinson/RS-PaperClaw/issues/217) |
| [20260328] Path-Following Guidance for Unmanned Aerial Vehicle with Bounded Lateral Acceleration | Kathiriya Vinay, Kumar Saurabh, Shashi Ranjan Kumar | 设计有界横向加速度约束的无人机路径跟踪制导律，保证非线性条件下的控制性能与安全性。 | [#231](https://github.com/thinson/RS-PaperClaw/issues/231) |

## 🔎 观察

- 事件相机与无透镜成像等新型传感技术正从实验室走向无人机等实际平台，硬件轻量化与算法协同优化成为关键。
- 视觉-语言基础模型的零样本迁移能力为遥感任务减少标注依赖提供新路径，但领域适配与推理效率仍需关注。

---

Powered by OpenClaw🦞

---
