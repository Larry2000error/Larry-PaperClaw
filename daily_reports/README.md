# Daily Reports

最近三天日报（最新在前）：

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

今日研究聚焦视觉Transformer效率优化与跨物种生物识别两大方向。前者探索视觉地点识别中的Token剪枝策略，以降低推理成本；后者针对多物种动物重识别任务，提出物种感知的图构建方法。两工作均体现领域对计算效率与任务特异性的双重关注。

## ✨ 今日亮点

- Token剪枝实证研究揭示视觉地点识别中冗余Token的识别规律
- 物种感知图构建方法突破多物种动物重识别的跨类干扰难题
- LightGlue与LightGBM组合实现高效特征匹配与分类

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260717] Are All Tokens Necessary for Visual Place Recognition? An Empirical Study of Token Reduction for Efficient Inference | Jin Tong, Liu Yunpeng, Hu Shuyu, Zhang Qinghua, Han Ruize, Wang Song, Lu Feng | Shenyang Institute of Automation, Chinese Academy of Sciences；University of Chinese Academy of Sciences；Shenzhen University of Advanced Technology | 该研究系统评估Token剪枝策略在视觉地点识别中的有效性，为高效推理提供实证依据。 | [#343](https://github.com/Larry2000error/Larry-PaperClaw/issues/343) |
| [20260717] DS@GT ARC at AnimalCLEF 2026: Species-Aware Graph Construction for Multi-Species Animal Re-Identification | Evan Sinclair Smith, Miyaguchi Anthony, Palamari Snigdha, Evangelista Danté | Georgia Institute of Technology | DS@GT团队提出物种感知的图构建方法，结合LightGlue与LightGBM实现多物种动物重识别。 | [#345](https://github.com/Larry2000error/Larry-PaperClaw/issues/345) |

## 🔎 观察

- Token剪枝正从通用视觉任务向地理定位等垂直领域渗透，效率优化进入精细化阶段
- 动物重识别任务呈现多物种联合建模趋势，物种先验知识的显式引入成为关键设计

---

Powered by OpenClaw🦞

---

# [20260716](./202607/20260716.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦跨模态定位与行人重识别两大方向。地理定位领域关注证据推理与轨迹序列建模，以缓解地标偏差并提升连续观测下的定位精度。行人重识别研究呈现多模态融合趋势，可见光-红外跨模态学习与无监督方法成为热点，同时出现系统性综述梳理单模态到多模态的技术演进。

## ✨ 今日亮点

- HoloGeo提出证据驱动推理框架，缓解视觉地理定位中的地标偏差问题
- AlphaWiSE设计自适应权重插值策略，实现持续多模态表征学习
- 轨迹感知跨视角地理定位利用序列观测，提升视频-文本-卫星匹配精度

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260716] HoloGeo: Mitigating Landmark Bias in Geo-localization via Evidence-Driven Reasoning | Zhou Pengcheng, Liu Xuanyu, Yin Yanchen, Li Bobo, Wu Shengqiong, Lee Mong-Li, Hsu Wynne | National University of Singapore；Shandong University of Science and Technology；University of Oxford | HoloGeo通过证据驱动推理机制识别并抑制地标偏差，提升视觉地理定位的泛化能力。 | [#337](https://github.com/Larry2000error/Larry-PaperClaw/issues/337) |
| [20260716] Structural-Semantic Reciprocal Learning for Unsupervised Visible-Infrared Person Re-Identification | Tian Moyao, Liu Shijia, Yang Yan, Yuan Xin, Chen Minshi, Wang Wei, Wang Xiao | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-Time Industrial System, Wuhan University of Science and Technology；State Key Laboratory of Robotics and Intelligent Systems, Shenyang Institute of Automation, Chinese Academy of Sciences；China University of Chinese Academy of Sciences | 提出结构-语义互惠学习框架，在无监督设定下实现可见光-红外行人重识别。 | [#338](https://github.com/Larry2000error/Larry-PaperClaw/issues/338) |
| [20260716] AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation Learning | Jain Sarthak, Hu Qiran, Zhu Zhen, Liu Yaoyao | University of Illinois Urbana-Champaign；Google DeepMind | AlphaWiSE采用自适应权重插值实现持续多模态学习，缓解跨模态检索中的灾难性遗忘。 | [#339](https://github.com/Larry2000error/Larry-PaperClaw/issues/339) |
| [20260716] Blurring Modal Boundaries: A Unified Survey from Single- to Multi-Modal Person Re-ldentification | Wang Xiao, Wang Bing, Yang Bin, Chen Cuiqun, Xu Xin, Ye Mang | School of Computer Science and Technology, Wuhan University of Science and Technology；Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System, Wuhan University of Science and Technology；School of Computer, Wuhan University；School of Computer, Anhui University | 系统综述单模态到多模态行人重识别技术，涵盖文本-图像检索与可见光-红外匹配方法。 | [#340](https://github.com/Larry2000error/Larry-PaperClaw/issues/340) |
| [20260716] Trajectory-aware Cross-view Geo-localization with Sequential Observations | Gao Tianyi, Lin Jiayu, Beaulieu Danielle, Jacobs Nathan | Washington University in St. Louis | 利用轨迹序列建模实现跨视角地理定位，整合视频、文本描述与卫星图像进行路径匹配。 | [#342](https://github.com/Larry2000error/Larry-PaperClaw/issues/342) |

## 🔎 观察

- 地理定位研究正从静态图像匹配向动态序列推理演进，轨迹感知与证据推理成为提升鲁棒性的关键路径。
- 行人重识别领域多模态融合趋势显著，武汉科技大学团队在同日贡献两篇相关成果，显示该机构在此方向的集中布局。

---

Powered by OpenClaw🦞

---
