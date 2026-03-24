# Daily Reports

最近三天日报（最新在前）：

# [20260323](./202603/20260323.md)
## 📌 今日概况

今日共检索候选论文 19 篇；关键词+LLM 智能匹配遥感交叉论文 13 篇；最终纳入日报 13 篇。

今日遥感AI研究呈现三大趋势：一是跨视角地理定位与UAV导航技术持续升温，多篇论文聚焦实时定位与无GPS环境应用；二是基础模型可信度与自监督学习成为热点，光谱掩码与物理约束方法受关注；三是三维重建与立体匹配技术深化，NeRF与深度学习融合卫星影像处理流程。智能体工具创建与扩散模型分辨率增强亦具亮点。

## ✨ 今日亮点

- 跨视角地理定位技术突破：两篇论文分别从迭代流预测与视觉导航角度推进实时精确定位
- 遥感智能体进化：OpenEarth-Agent实现从工具调用到工具创建的自主能力跃迁
- 光谱可信学习：SpecTM提出光谱靶向掩码策略，增强基础模型物理可信度

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260323] Riverine Land Cover Mapping through Semantic Segmentation of Multispectral Point Clouds | Thurachen Sopitta, Taher Josef, Lehtomäki Matti, Matikainen Leena, Blåfield Linnea et al. | 提出多光谱点云语义分割方法，实现河流沿岸土地覆盖精细制图 | [#174](https://github.com/thinson/RS-PaperClaw/issues/174) |
| [20260323] Beyond Matching to Tiles: Bridging Unaligned Aerial and Satellite Views for Vision-Only UAV Navigation | Liu Kejia, Zhou Haoyang, Xu Ruoyu, Wang Peicheng, Song Mingli et al. | 构建无需GPS的无人机视觉导航框架，桥接航拍与卫星影像视角差异 | [#175](https://github.com/thinson/RS-PaperClaw/issues/175) |
| [20260323] OpenEarth-Agent: From Tool Calling to Tool Creation for Open-Environment Earth Observation | Zhao Sijie, Liu Feng, Zhang Xueliang, Chen Hao, Gu Xinyu et al. | 开发开放环境地球观测智能体，支持自主工具创建与调用 | [#176](https://github.com/thinson/RS-PaperClaw/issues/176) |
| [20260323] SpecTM: Spectral Targeted Masking for Trustworthy Foundation Models | Syed Usama Imtiaz, Mitra Nasr Azadani, Alamdari Nasrin | 设计光谱靶向掩码策略，提升遥感基础模型可信度与物理一致性 | [#177](https://github.com/thinson/RS-PaperClaw/issues/177) |
| [20260323] GeoFlow: Real-Time Fine-Grained Cross-View Geolocalization via Iterative Flow Prediction | Ayesh Abu Lehyeh, Zhang Xiaohan, Arrabi Ahmad, Sultani Waqas, Chen Chen et al. | 通过迭代流预测实现实时细粒度跨视角地理定位，适用于拒止环境 | [#178](https://github.com/thinson/RS-PaperClaw/issues/178) |
| [20260323] SatGeo-NeRF: Geometrically Regularized NeRF for Satellite Imagery | Wagner Valentin, Bullinger Sebastian, Arens Michael, Stiefelhagen Rainer | 引入几何正则化约束，改进卫星影像NeRF三维重建与深度估计 | [#179](https://github.com/thinson/RS-PaperClaw/issues/179) |
| [20260323] A Latent Representation Learning Framework for Hyperspectral Image Emulation in Remote Sensing | Chedly Ben Azizi, Guilloteau Claire, Roussel Gilles, Puigt Matthieu | 基于变分自编码器学习潜层表示，实现高光谱图像仿真生成 | [#180](https://github.com/thinson/RS-PaperClaw/issues/180) |
| [20260323] Deep S2P: Integrating Learning Based Stereo Matching Into the Satellite Stereo Pipeline | Masquil Elías, Ehret Thibaud, Musé Pablo, Facciolo Gabriele | 将深度学习立体匹配集成至卫星立体处理流程，优化数字表面模型生产 | [#181](https://github.com/thinson/RS-PaperClaw/issues/181) |
| [20260323] SHARP: Spectrum-aware Highly-dynamic Adaptation for Resolution Promotion in Remote Sensing Synthesis | Zhao Bingxuan, Zhou Qing, Yang Chuang, Wang Qi | 提出频谱感知动态适配机制，结合旋转位置编码提升遥感图像分辨率 | [#182](https://github.com/thinson/RS-PaperClaw/issues/182) |
| [20260323] Rethinking SAR ATR: A Target-Aware Frequency-Spatial Enhancement Framework with Noise-Resilient Knowledge Guidance | Lin Yansong, Cheng Zihan, Wang Jielei, Lua Guoming, Cui Zongyong | 构建频域-空域联合增强框架，引入噪声鲁棒知识蒸馏改进SAR目标识别 | [#183](https://github.com/thinson/RS-PaperClaw/issues/183) |
| [20260323] Evolutionary Biparty Multiobjective UAV Path Planning: Problems and Empirical Comparisons | Chen Kesheng, Luo Wenjian, Lin Xin, Song Zhen, Chang Yatong | 设计进化双目标优化算法，解决多目标无人机路径规划问题 | [#184](https://github.com/thinson/RS-PaperClaw/issues/184) |
| [20260323] Unregistered Spectral Image Fusion: Unmixing, Adversarial Learning, and Recoverability | Song Jiahui, Shrestha Sagar, Fu Xiao | 融合解混与对抗学习，实现未配准多光谱与高光谱图像融合超分 | [#185](https://github.com/thinson/RS-PaperClaw/issues/185) |
| [20260323] EpiMask: Leveraging Epipolar Distance Based Masks in Cross-Attention for Satellite Image Matching | Deshmukh Rahul, Chauhan Aditya, Kak Avinash | 利用极线距离掩码改进交叉注意力机制，提升卫星影像匹配精度 | [#186](https://github.com/thinson/RS-PaperClaw/issues/186) |

## 🔎 观察

- 跨视角地理定位研究密集涌现，反映无人机自主导航与拒止环境应用的迫切需求，技术路线从特征匹配向端到端流预测演进
- 基础模型研究开始关注光谱物理约束与可信度问题，标志着遥感AI从性能优先向可解释、可信赖方向转型

---

Powered by OpenClaw🦞

---

# [20260322](./202603/20260322.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦视觉语言模型与空间智能的深度融合。道路提取任务引入细粒度层级分类与VLM技术，无人机导航则探索几何引导的跨模态表征对齐，体现从静态地物识别向动态环境理解的范式演进。

## ✨ 今日亮点

- 大规模道路数据集支撑VLM细粒度层级分类，提升路网语义理解能力
- 几何引导的表征对齐机制优化无人机视觉语言导航性能
- 跨模态空间推理成为城市环境智能体研究的核心方向

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260322] A Large-Scale Remote Sensing Dataset and VLM-based Algorithm for Fine-Grained Road Hierarchy Classification | Han Ting, Xie Xiangyi, Chen Yiping, Du Yumeng, Ma Jin et al. | 论文构建大规模遥感数据集，提出基于视觉语言模型的道路细粒度层级分类方法，实现路网语义层次化解析。 | [#171](https://github.com/thinson/RS-PaperClaw/issues/171) |
| [20260322] SpatialFly: Geometry-Guided Representation Alignment for UAV Vision-and-Language Navigation in Urban Environments | Jiang Wen, Huang Kangyao, Wang Li, Xu Wang, Fan Wei et al. | 论文提出SpatialFly框架，通过几何引导的表征对齐机制，增强无人机在城市环境中的视觉语言导航能力。 | [#172](https://github.com/thinson/RS-PaperClaw/issues/172) |

## 🔎 观察

- VLM正从通用视觉任务向遥感垂直领域渗透，层级化语义标注或成为下一代道路数据集标配
- 无人机导航研究从端到端感知转向显式空间推理，几何先验与语言指令的联合建模值得持续关注

---

Powered by OpenClaw🦞

---

# [20260321](./202603/20260321.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究呈现多模态融合与智能应用的深化趋势。研究涵盖AI数据中心热岛效应量化、光学-SAR高效融合、无人机神经定位、跨模态行人检索及灾后街景生成等方向，体现遥感技术向精细化、实时化及灾害应急响应领域的拓展。

## ✨ 今日亮点

- AI数据中心热岛效应研究揭示数字基础设施对城市热环境的量化影响
- 光学-SAR融合实现云遮挡条件下的轻量化语义分割
- 跨模态模糊对齐网络推动无人机视角下行人检索精度提升

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260321] The data heat island effect: quantifying the impact of AI data centers in a warming world | Marinoni Andrea, Lio&#39; Pietro, Cambria Erik, Luca Dal Zilio, Lin Weisi et al. | 研究量化AI数据中心引发的'数据热岛'效应，拓展传统城市热岛理论至数字基础设施领域。 | [#165](https://github.com/thinson/RS-PaperClaw/issues/165) |
| [20260321] Lean Learning Beyond Clouds: Efficient Discrepancy-Conditioned Optical-SAR Fusion for Semantic Segmentation | Meng Chenxing, Quan Wuzhou, Cai Yingjie, Cao Liqun, Zhang Liyan et al. | 提出差异条件驱动的光学-SAR融合框架，以精简学习策略解决云遮挡下的高效语义分割问题。 | [#166](https://github.com/thinson/RS-PaperClaw/issues/166) |
| [20260321] PiLoT: Neural Pixel-to-3D Registration for UAV-based Ego and Target Geo-localization | Cheng Xiaoya, Wang Long, Liu Yan, Liu Xinyi, Tan Hanlin et al. | PiLoT方法通过神经像素到三维配准，实现无人机自身与目标的同时地理定位。 | [#167](https://github.com/thinson/RS-PaperClaw/issues/167) |
| [20260321] Cross-modal Fuzzy Alignment Network for Text-Aerial Person Retrieval and A Large-scale Benchmark | Deng Yifei, Li Chenglong, Zhang Yuyang, Hu Guyue, Tang Jin | 构建跨模态模糊对齐网络及大规模基准，处理文本与无人机图像间细粒度语义对齐难题。 | [#168](https://github.com/thinson/RS-PaperClaw/issues/168) |
| [20260321] Satellite-to-Street: Synthesizing Post-Disaster Views from Satellite Imagery via Generative Vision Models | Yang Yifan, Zou Lei, Jepson Wendy | 利用生成式视觉模型从卫星影像合成灾后街景视图，辅助灾害响应决策。 | [#169](https://github.com/thinson/RS-PaperClaw/issues/169) |

## 🔎 观察

- 遥感AI正从单一模态分析转向多源数据协同，SAR与光学融合、卫星到街景生成等方向凸显数据互补价值
- 无人机平台成为研究热点，定位精度与跨模态检索能力提升将推动低空经济应用场景落地

---

Powered by OpenClaw🦞

---
