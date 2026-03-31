# Daily Reports

最近三天日报（最新在前）：

# [20260330](./202603/20260330.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多维度交叉趋势：生成模型向显著性检测渗透，ORSIFlow将矫正流与潜扩散结合提升光学遥感目标检测精度；硬件层面，自旋三旋翼无人机通过非线性动态逆控制扩展视场；数据基建方面，PROSAIL驱动的合成高光谱植被数据集填补基准空白；多模态检索与无线通信信道推断则体现遥感向跨域应用的延伸。

## ✨ 今日亮点

- ORSIFlow首次将矫正流引入遥感显著性检测，以显著性引导生成机制优化边界感知
- 自旋三旋翼无人机采用模型预测控制与非线性动态逆，实现360°视场自主飞行
- SVH-BD基于PROSAIL辐射传输模型构建合成高光谱植被基准，支持遥感图像仿真

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260330] ORSIFlow: Saliency-Guided Rectified Flow for Optical Remote Sensing Salient Object Detection | Chen Haojing, Li Yutong, Liu Zhihang, Tan Tao, Bian Haoyu et al. | ORSIFlow提出显著性引导矫正流，结合潜扩散模型与边界感知损失，优化光学遥感显著目标检测的生成质量与效率。 | [#225](https://github.com/thinson/RS-PaperClaw/issues/225) |
| [20260330] A Self-Rotating Tri-Rotor UAV for Field of View Expansion and Autonomous Flight | Zhou Xiaobin, Zheng Zihao, Jin Aoxu, Qiang Lei, Zhu Bo | 自旋三旋翼无人机通过模型预测控制与非线性动态逆实现自主飞行，以机械旋转扩展视场突破固定相机视角限制。 | [#226](https://github.com/thinson/RS-PaperClaw/issues/226) |
| [20260330] SVH-BD : Synthetic Vegetation Hyperspectral Benchmark Dataset for Emulation of Remote Sensing Images | Chedly Ben Azizi, Guilloteau Claire, Roussel Gilles, Puigt Matthieu | SVH-BD基于PROSAIL辐射传输模型生成合成高光谱植被数据，为遥感图像仿真与植被性状反演提供标准化基准。 | [#227](https://github.com/thinson/RS-PaperClaw/issues/227) |
| [20260330] Robust Remote Sensing Image-Text Retrieval with Noisy Correspondence | Song Qiya, Xie Yiqiang, Sun Yuan, Dian Renwei, Kang Xudong | 针对遥感图文检索中的噪声对应问题，提出自步课程学习策略，逐步过滤噪声样本以提升跨模态检索鲁棒性。 | [#228](https://github.com/thinson/RS-PaperClaw/issues/228) |
| [20260330] Deep Learning Based Site-Specific Channel Inference Using Satellite Images | Song Junzhe, He Ruisi, Yang Mi, Zhang Zhengyu, Gao Shuaiqi et al. | 利用卫星图像与深度学习进行站点级无线信道推断，构建抽头延迟线模型辅助通信网络规划与频谱管理。 | [#229](https://github.com/thinson/RS-PaperClaw/issues/229) |

## 🔎 观察

- 生成式AI正从图像合成向判别任务回流，矫正流等高效生成模型开始服务于检测任务的特征增强与边界精细化
- 遥感硬件创新与算法研究呈现并行态势，无人机平台动力学控制与上层视觉任务形成系统级闭环，但跨层协同优化尚待深入

---

Powered by OpenClaw🦞

---

# [20260329](./202603/20260329.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多模态融合与智能体应用趋势。大语言模型成为核心驱动力，赋能地理定位、变化检测、语义分割及无人机导航等任务。物理知识嵌入与开放词汇学习成为新方向，同时深度学习结合卫星影像持续支撑社会经济分析应用。

## ✨ 今日亮点

- RHO提出基于OSM的全景图像度量级跨视角地理定位方法
- OpenDPR通过扩散引导原型检索实现遥感开放词汇变化检测
- LLM驱动无人机自然语言导航，结合时序逻辑规范翻译与修复

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260329] RHO: Robust Holistic OSM-Based Metric Cross-View Geo-Localization | Zheng Junwei, Dai Ruize, Liu Ruiping, Zeng Zichao, Chen Yufan et al. | RHO利用OpenStreetMap数据实现鲁棒的全景图像跨视角度量地理定位，提升视觉定位精度。 | [#219](https://github.com/thinson/RS-PaperClaw/issues/219) |
| [20260329] OpenDPR: Open-Vocabulary Change Detection via Vision-Centric Diffusion-Guided Prototype Retrieval for Remote Sensing Imagery | Guo Qi, Wang Jue, Liu Yinhe, Zhong Yanfei | OpenDPR提出以视觉为中心的扩散引导原型检索框架，支持遥感影像的开放词汇变化检测。 | [#220](https://github.com/thinson/RS-PaperClaw/issues/220) |
| [20260329] LLM-Enabled Low-Altitude UAV Natural Language Navigation via Signal Temporal Logic Specification Translation and Repair | Ping Yuqi, Ding Huahao, Liang Tianhao, Zhou Longyu, Lei Guangyu et al. | 该方法将大语言模型用于低空无人机自然语言导航指令的时序逻辑规范翻译与自动修复。 | [#221](https://github.com/thinson/RS-PaperClaw/issues/221) |
| [20260329] Transferring Physical Priors into Remote Sensing Segmentation via Large Language Models | Lu Yuxi, Li Kunqi, Li Zhidong, Su Xiaohan, Wu Biao et al. | 通过大语言模型将物理先验知识转化为知识图谱，增强遥感语义分割的物理可解释性。 | [#222](https://github.com/thinson/RS-PaperClaw/issues/222) |
| [20260329] Estimating the Impact of COVID-19 on Travel Demand in Houston Area Using Deep Learning and Satellite Imagery | Pachika Alekhya, Gao Lu, Song Lingguang, Lu Pan, Wang Xingju | 结合深度学习与卫星影像，量化评估COVID-19对休斯顿地区出行需求的影响。 | [#223](https://github.com/thinson/RS-PaperClaw/issues/223) |

## 🔎 观察

- 大语言模型正从通用工具向遥感专用智能体演进，覆盖感知-认知-决策全链条。
- 开放词汇与物理先验的结合，反映出遥感AI从数据驱动向知识增强的范式转变。

---

Powered by OpenClaw🦞

---

# [20260328](./202603/20260328.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日遥感AI研究呈现多模态融合与智能感知趋势：计算成像领域探索无透镜偏振成像新范式，视觉语言模型赋能跨视角地理定位，事件相机与深度融合推动高速无人机自主避障。三项研究均强调端到端学习与跨模态信息整合。

## ✨ 今日亮点

- 无透镜偏振成像突破传统光学限制，RGB引导重建降低硬件复杂度
- 零样本视觉语言重排序实现跨视角地理定位，无需任务特定训练
- 事件-深度融合网络以模仿学习实现高速无人机毫秒级避障响应

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260328] Guided Lensless Polarization Imaging | Kraicer Noa, Yosef Erez, Giryes Raja | 提出RGB引导的无透镜偏振成像方法，通过计算重建替代传统光学透镜，实现轻量化偏振信息采集。 | [#215](https://github.com/thinson/RS-PaperClaw/issues/215) |
| [20260328] Zero-shot Vision-Language Reranking for Cross-View Geolocalization | Yunus Talha Erzurumlu, John E. Anderson, William J. Shuart, Toth Charles, Yilmaz Alper | 利用LLaVA等视觉语言模型进行零样本重排序，提升跨视角地理定位的泛化能力与检索精度。 | [#216](https://github.com/thinson/RS-PaperClaw/issues/216) |
| [20260328] An End-to-end Flight Control Network for High-speed UAV Obstacle Avoidance based on Event-Depth Fusion | Shang Dikai, Zhao Jingyue, Xu Shi, Ye Nanyang, Wang Lei | 设计端到端飞行控制网络，融合事件相机与深度信息，基于模仿学习实现高速无人机实时避障。 | [#217](https://github.com/thinson/RS-PaperClaw/issues/217) |

## 🔎 观察

- 多模态融合成为核心趋势：三篇论文均涉及跨传感器或跨模态信息整合，反映遥感系统向异构数据协同演进
- 零样本与端到端范式加速落地：视觉语言模型和模仿学习降低领域适配成本，推动技术从实验室向实际平台迁移

---

Powered by OpenClaw🦞

---
