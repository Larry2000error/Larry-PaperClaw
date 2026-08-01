# Daily Reports

最近三天日报（最新在前）：

# [20260722](./202607/20260722.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日研究聚焦跨模态检索与异构视觉对齐，涵盖边缘计算优化、多轮交互检索及跨视角地理定位。可见光-红外预训练采样策略与无人机-卫星大偏角定位成为遥感感知关键方向，体现多传感器融合与极端视角鲁棒性的技术趋势。

## ✨ 今日亮点

- PolySim提出确定性多项式替代方案，解决边缘设备概率嵌入计算瓶颈
- OffNadirLoc构建大偏角无人机-卫星定位基准，应对透视畸变挑战
- 可见光-红外预训练引入重要性采样，突破跨模态表征对齐效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260722] PolySim: Deterministic Polynomial Surrogates for Cross-Modal Retrieval on CiM | Li Xinzhao, Power Charles, Ren Pengyu, Won Jongun, Pei Likai, Hu Yuting, Xiong Jinjun, Vardar Alptekin, Cao Ningyuan, Xiaobo Sharon Hu, Kämpfe Thomas, Ni Kai, Qin Ruiyang | Villanova University；University of Notre Dame；University at Buffalo；Fraunhofer IPMS；TU Braunschweig | PolySim设计确定性多项式代理模型，在存内计算架构上实现高效跨模态检索，规避概率嵌入的硬件开销。 | [#357](https://github.com/Larry2000error/Larry-PaperClaw/issues/357) |
| [20260722] Diverse-Intent Multi-Turn Fashion Image Retrieval | Tang Mingqiang, Wen Haokun, Liu Meng, Hu Yupeng, Guan Weili, Song Xuemeng | Southern University of Science and Technology；Harbin Institute of Technology (Shenzhen)；Shandong University；Shenzhen Loop Area Institute | Diverse-Intent框架支持多轮时尚图像检索，通过视觉-语言预训练捕捉用户意图演化，提升交互式搜索体验。 | [#358](https://github.com/Larry2000error/Larry-PaperClaw/issues/358) |
| [20260722] Not All Patches are Equal: Sampling Matters for Visible-Infrared Pre-Training | Ma Qiwei, Deng Bin, Zhu Junjie, Huang Qiangjuan, Duan Puhong, Yang Ke, Kang Xudong, Li Shutao | School of Artificial Intelligence and Robotics, Hunan University；Yuelushan Center for Industrial Innovation；Intelligent Game and Decision Lab | 提出非均匀 patch 采样策略用于可见光-红外预训练，依据信息重要性加权优化跨模态表征学习效率。 | [#359](https://github.com/Larry2000error/Larry-PaperClaw/issues/359) |
| [20260722] OffNadirLoc: Benchmark and Framework for Challenging UAV-to-Satellite Geo-Localization under Large Off-Nadir Views | Qiao Qian, Liu Wenye, Liu Ting, Shu Jiuhe, Wang Peng | Northwestern Polytechnical University | OffNadirLoc建立大偏角无人机-卫星地理定位基准，结合结构感知学习缓解极端视角下的透视畸变问题。 | [#360](https://github.com/Larry2000error/Larry-PaperClaw/issues/360) |

## 🔎 观察

- 跨模态检索正向边缘端迁移，存内计算与确定性近似成为硬件协同设计新焦点
- 遥感定位从正射视角扩展至大偏角场景，透视畸变建模能力或成下一代算法核心竞争力

---

Powered by OpenClaw🦞

---

# [20260721](./202607/20260721.md)
## 📌 今日概况

今日共检索候选论文 10 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日研究呈现多模态对齐与跨模态检索的集中趋势。视觉-语言模型在病理学基准测试、大规模稳定对齐及统一嵌入空间构建方面取得进展；同时，3D场景检索、无人机拒止环境定位及行人重识别等应用方向亦有新成果，体现出从基础模型优化到垂直场景落地的完整链条。

## ✨ 今日亮点

- PathAgentBench构建病理全切片图像证据检索基准，推动医学VLM临床可用性评估
- KALE提出核对齐与损失均衡方法，解决CLIP-DINOv2网络规模对齐稳定性问题
- NGPS融合深度卫星匹配与多速率传感，实现GPS拒止环境下无人机地理定位

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260721] PathAgentBench: Benchmarking Evidence-Seeking Vision-Language Models on Whole-Slide Pathology Image | Liao Dankai, Zhang Tianyi, Wu Yufeng, Zhang Xinyue, Xue Qiaochu, Liu Zeyu, Zhao Dachun, Cai Linghan, Jin Yueming | National University of Singapore；National University Hospital；Singapore | PathAgentBench针对全切片病理图像构建证据检索基准，系统评估视觉-语言模型的临床推理能力。 | [#349](https://github.com/Larry2000error/Larry-PaperClaw/issues/349) |
| [20260721] CR-Refiner: An Object-Centric Optimal Transport Reranker for Edit-Conditioned 3D Scene Retrieval | Wu Hao, Zhu Jinjing, Wu Nanyu, Cai Qianyi, Lin Heyi, Wang Hao, Xiong Hui | Hong Kong University of Science and Technology；Hong Kong University of Science and Technology (Guangzhou) | CR-Refiner以对象为中心的最优传输重排序框架，提升编辑条件3D场景检索的精确性。 | [#350](https://github.com/Larry2000error/Larry-PaperClaw/issues/350) |
| [20260721] NGPS: GPS-Denied Aerial Geo-Localization and 2.5D Reconstruction via Deep Satellite Image Matching and Multi-Rate Sensor Fusion | Sharma Sanket | Institution unavailable | NGPS通过深度卫星图像匹配与多速率传感器融合，实现无GPS环境下的无人机地理定位与2.5D重建。 | [#351](https://github.com/Larry2000error/Larry-PaperClaw/issues/351) |
| [20260721] KALE: Kernel Alignment with Loss Equilibration for Stable CLIP-DINOv2 Alignment at Web Scale | Pawłowicz Michał | Institution unavailable | KALE采用核对齐与损失均衡策略，稳定CLIP-DINOv2在网页规模数据上的联合训练。 | [#352](https://github.com/Larry2000error/Larry-PaperClaw/issues/352) |
| [20260721] Reliability-Aware 3D Geometric Injection for Universal Person Re-identification | Su Bohan, Wang Jiashuo, Liu Fangyi, Ye Mang | National Engineering Research Center for Multimedia Software, School of Computer Science, Wuhan University | 可靠性感知3D几何注入方法增强单目深度估计，提升跨模态行人重识别的泛化性能。 | [#353](https://github.com/Larry2000error/Larry-PaperClaw/issues/353) |
| [20260727] Dual-Edged Homogeneous-Modality Similarity: Towards Visible-Infrared Modality-Incomplete Person Re-Identification with Modality Adaptive Matching | Xu Xin, Zhan Shuhao, Liu Wei, Wang Zheng, Jiang Kui, Lin Chia-Wen | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System, Wuhan University of Science and Technology；School of Computer Science, Wuhan University；Faculty of Computing, Harbin Institute of Technology；Department of Electrical Engineering and the Institute of Communications Engineering, National Tsing Hua University | 模态自适应匹配框架利用同质模态相似性，解决可见光-红外模态缺失场景下的行人重识别。 | [#354](https://github.com/Larry2000error/Larry-PaperClaw/issues/354) |
| [20260721] Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio | Abdul Basit Tonmoy, Kazi Fardinul Hoque, Md. Shahrier Islam Arham, Luthra Arman | Eximius Labs；Wabash College；Skop Intelligence Co. | Fusion Embedding构建统一嵌入空间，支持文本、图像、视频与音频的跨模态检索与表示。 | [#355](https://github.com/Larry2000error/Larry-PaperClaw/issues/355) |

## 🔎 观察

- 行人重识别领域同日出现两篇独立工作，分别聚焦3D几何注入与模态缺失问题，显示该方向研究热度持续攀升。
- 多模态统一嵌入成为新兴趋势，但病理、遥感等专业领域仍依赖领域特定基准，通用模型与垂直应用的鸿沟尚未弥合。

---

Powered by OpenClaw🦞

---

# [20260717](./202607/20260717.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日研究聚焦视觉Transformer效率优化与跨物种生物识别两大方向。前者探索视觉地点识别中的Token剪枝策略以降低推理成本，后者针对多物种动物重识别任务构建物种感知的图结构方法，均体现领域对计算效率与任务特异性的双重关注。

## ✨ 今日亮点

- 视觉地点识别领域首次系统验证Token剪枝对识别性能的影响边界
- 多物种动物重识别引入物种感知图构建，突破单一物种方法局限
- LightGlue与LightGBM组合优化生物特征匹配与聚类效率

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260717] Are All Tokens Necessary for Visual Place Recognition? An Empirical Study of Token Reduction for Efficient Inference | Jin Tong, Liu Yunpeng, Hu Shuyu, Zhang Qinghua, Han Ruize, Wang Song, Lu Feng | Shenyang Institute of Automation, Chinese Academy of Sciences；University of Chinese Academy of Sciences；Shenzhen University of Advanced Technology | 中科院团队实证研究视觉地点识别中Token剪枝策略，揭示非必要Token的识别冗余性，为高效推理提供优化路径。 | [#343](https://github.com/Larry2000error/Larry-PaperClaw/issues/343) |
| [20260717] DS@GT ARC at AnimalCLEF 2026: Species-Aware Graph Construction for Multi-Species Animal Re-Identification | Evan Sinclair Smith, Miyaguchi Anthony, Palamari Snigdha, Evangelista Danté | Georgia Institute of Technology | 佐治亚理工团队提出物种感知图构建方法，整合LightGlue与LightGBM实现多物种动物重识别的联合优化。 | [#345](https://github.com/Larry2000error/Larry-PaperClaw/issues/345) |

## 🔎 观察

- Token剪枝研究反映视觉Transformer在遥感定位任务中的部署瓶颈，边缘计算需求驱动效率导向的模型压缩研究。
- 多物种动物识别从单一物种向群落级扩展，生态监测场景的复杂度提升正重塑生物识别的方法论框架。

---

Powered by OpenClaw🦞

---
