# Daily Reports

最近三天日报（最新在前）：

# [20260402](./202604/20260402.md)
## 📌 今日概况

今日共检索候选论文 18 篇；关键词+LLM 智能匹配遥感交叉论文 13 篇；最终纳入日报 13 篇。

今日遥感AI研究呈现三大趋势：一是视觉-语言-动作模型（VLA）向无人机具身智能延伸，二是开放词汇学习持续渗透变化检测与分割任务，三是跨视角地理定位成为热点，UAV-卫星/无人机-地面视角对齐技术密集涌现。此外，KAN网络轻量化、扩散模型RFI抑制等方向亦有新进展。

## ✨ 今日亮点

- UAV-Track VLA首次将VLA模型引入无人机空中跟踪，实现语言指令驱动的具身飞行控制
- CoRegOVCD提出免训练一致性正则化策略，突破开放词汇变化检测的数据瓶颈
- LinkS²Bench构建首个UAV-卫星动态跨视角基准，系统评估VLM空间推理能力边界

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260402] UAV-Track VLA: Embodied Aerial Tracking via Vision-Language-Action Models | Zhang Qiyao, Zheng Shuhua, Sun Jianli, Li Chengxiang, Wu Xianke et al. | UAV-Track VLA：基于视觉-语言-动作模型的无人机具身空中跟踪框架。 | [#247](https://github.com/thinson/RS-PaperClaw/issues/247) |
| [20260402] CoRegOVCD: Consistency-Regularized Open-Vocabulary Change Detection | Tang Weidong, Sun Hanbin, Li Zihan, Wang Yikai, Zhang Feifan | CoRegOVCD：一致性正则化驱动的免训练开放词汇变化检测方法。 | [#248](https://github.com/thinson/RS-PaperClaw/issues/248) |
| [20260402] Are VLMs Lost Between Sky and Space? LinkS$^2$Bench for UAV-Satellite Dynamic Cross-View Spatial Intelligence | Liu Dian, Feng Jie, Li Di, Zheng Yuhui, Li Guanbin et al. | LinkS²Bench：面向无人机-卫星跨视角空间智能的VLM评测基准。 | [#249](https://github.com/thinson/RS-PaperClaw/issues/249) |
| [20260402] Decouple and Rectify: Semantics-Preserving Structural Enhancement for Open-Vocabulary Remote Sensing Segmentation | Feng Jie, Li Fengze, Zhang Junpeng, Chen Siyu, Liang Yuping et al. | 解耦-校正框架：面向开放词汇遥感分割的语义保持结构增强策略。 | [#250](https://github.com/thinson/RS-PaperClaw/issues/250) |
| [20260402] Test-Time Adaptation for Height Completion via Self-Supervised ViT Features and Monocular Foundation Models | Rafaeli Osher, Svoray Tal, Nahlieli Ariel | 基于自监督ViT特征与单目基础模型的高程补全测试时自适应方法。 | [#251](https://github.com/thinson/RS-PaperClaw/issues/251) |
| [20260402] Light-ResKAN: A Parameter-Sharing Lightweight KAN with Gram Polynomials for Efficient SAR Image Recognition | Yi Pan, Li Weijie, Chen Xiaodong, Zhang Jiehua, Liu Li et al. | Light-ResKAN：Gram多项式参数共享的轻量KAN网络用于SAR图像识别。 | [#252](https://github.com/thinson/RS-PaperClaw/issues/252) |
| [20260402] ProVG: Progressive Visual Grounding via Language Decoupling for Remote Sensing Imagery | Li Ke, Wang Ting, Wang Di, Zhu Yongshan, Zhang Yiming et al. | ProVG：语言解耦驱动的渐进式视觉定位方法用于遥感影像。 | [#253](https://github.com/thinson/RS-PaperClaw/issues/253) |
| [20260402] GeoAI Agency Primitives | Zaytar Akram, Sawahn Rohan, Robinson Caleb, Gilles Q. Hacheme, Girmaw A. Tadesse et al. | GeoAI智能体原语：面向地理空间基础模型的人机协同能力抽象框架。 | [#254](https://github.com/thinson/RS-PaperClaw/issues/254) |
| [20260402] Cosine-Normalized Attention for Hyperspectral Image Classification | Ahmad Muhammad, Mazzara Manuel | 余弦归一化注意力机制用于高光谱图像分类。 | [#255](https://github.com/thinson/RS-PaperClaw/issues/255) |
| [20260402] Unifying UAV Cross-View Geo-Localization via 3D Geometric Perception | Li Haoyuan, Yang Wen, Xu Fang, Tan Hong, Zhang Haijian et al. | 基于3D几何感知的无人机跨视角地理定位统一框架。 | [#256](https://github.com/thinson/RS-PaperClaw/issues/256) |
| [20260402] Satellite-Free Training for Drone-View Geo-Localization | Liu Tao, Zhang Yingzhi, Ren Kan, Zhao Xiaoqi | 无卫星训练的无人机视角地理定位：纯3D场景重建驱动的跨视角检索。 | [#257](https://github.com/thinson/RS-PaperClaw/issues/257) |
| [20260402] Prototype-Based Low Altitude UAV Semantic Segmentation | Zhang Da, Junyu Gao, Zhiyuan Zhao | 原型学习驱动的低空无人机语义分割方法。 | [#258](https://github.com/thinson/RS-PaperClaw/issues/258) |
| [20260402] A Conditional Denoising Diffusion Probabilistic Model for RFI Mitigation in Synthetic Aperture Interferometric Radiometer | Luo Yuankai, Zhou Han, Hao Jinlong, Zhu Dong, Hu Fei | 条件去噪扩散概率模型用于综合孔径干涉辐射计的射频干扰抑制。 | [#259](https://github.com/thinson/RS-PaperClaw/issues/259) |

## 🔎 观察

- 跨视角地理定位（UAV-卫星/地面）今日集中出现4项研究，显示该方向正从2D图像匹配向3D几何感知演进，卫星-free训练范式或降低数据依赖
- 开放词汇学习在遥感领域加速落地，但变化检测、分割等密集预测任务仍面临语义-空间对齐难题，一致性正则化与结构增强成为新解题思路

---

Powered by OpenClaw🦞

---

# [20260401](./202604/20260401.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与基础模型适配两大主线。高光谱非线性解混引入生成对抗框架，作物产量预测构建多模态基准，SAR对抗攻击探索物理层安全，全景视觉惯性SLAM拓展无人机感知边界，持续学习缓解视觉语言模型灾难性遗忘，SAM变体实现高分辨率道路交互分割。

## ✨ 今日亮点

- YieldSAT构建首个高分辨率作物产量预测多模态基准数据集
- PC-SAM提出补丁约束机制优化SAM在高分辨率遥感道路分割中的交互能力
- PanoAir发布跨时段真实世界无人机全景视觉惯性SLAM数据集

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260401] Looking into a Pixel by Nonlinear Unmixing -- A Generative Approach | Tang Maofeng, Qi Hairong | Tang等提出基于生成对抗网络与循环一致性的非线性高光谱解混方法，通过生成式建模实现像素级光谱分解。 | [#240](https://github.com/thinson/RS-PaperClaw/issues/240) |
| [20260401] YieldSAT: A Multimodal Benchmark Dataset for High-Resolution Crop Yield Prediction | Miranda Miro, Pathak Deepak, Helber Patrick, Bischke Benjamin, Najjar Hiba et al. | Miranda等发布YieldSAT数据集，融合卫星影像与多源农业数据，建立高分辨率作物产量预测的多模态评估基准。 | [#241](https://github.com/thinson/RS-PaperClaw/issues/241) |
| [20260401] Adversarial Attenuation Patch Attack for SAR Object Detection | Zhang Yiming, Qin Weibo, Wang Feng | Zhang等设计针对SAR目标检测的对抗衰减贴片攻击，模拟电子干扰场景下的物理层隐身攻击机制。 | [#242](https://github.com/thinson/RS-PaperClaw/issues/242) |
| [20260401] PanoAir: A Panoramic Visual-Inertial SLAM with Cross-Time Real-World UAV Dataset | Wu Yiyang, Zhang Xiaohu, Du Yanjin, Zhang Tongsu, Li Chujun et al. | Wu等构建PanoAir数据集，支持全景相机与IMU融合的无人机全向感知定位及跨时段SLAM研究。 | [#243](https://github.com/thinson/RS-PaperClaw/issues/243) |
| [20260401] Continual Vision-Language Learning for Remote Sensing: Benchmarking and Analysis | Weng Xingxing, Ni Ruifeng, Pang Chao, Hao XiangYu, Wang Yishan et al. | Weng等建立遥感视觉语言模型持续学习基准，系统分析增量训练中的灾难性遗忘问题与缓解策略。 | [#244](https://github.com/thinson/RS-PaperClaw/issues/244) |
| [20260401] PC-SAM: Patch-Constrained Fine-Grained Interactive Road Segmentation in High-Resolution Remote Sensing Images | Lv Chengcheng, Li Rushi, Wu Mincheng, Shi Xiufang, Wen Zhenyu et al. | Lv等提出PC-SAM框架，以补丁约束机制引导SAM实现高分辨率遥感影像的细粒度交互式道路提取。 | [#245](https://github.com/thinson/RS-PaperClaw/issues/245) |

## 🔎 观察

- SAM及其变体持续主导遥感交互式分割方向，但高分辨率适配与细粒度控制仍是待解难题
- 多模态基准数据集建设加速，反映出遥感AI从算法创新向系统评估与可重复性研究的范式转移

---

Powered by OpenClaw🦞

---

# [20260331](./202603/20260331.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多模态融合与基础模型应用深化趋势。视觉-语言模型持续向地球观测领域渗透，涵盖文本-图像数据集构建、跨模态检索及开放词汇分割等方向。同时，层次化分类、高光谱解混与单目高度估计等经典任务在方法论上均有创新，体现遥感专用模型与通用AI技术的双向融合。

## ✨ 今日亮点

- BigEarthNet.txt发布大规模多传感器图文数据集，填补遥感视觉-语言基准空白
- ConInfer提出无需训练的上下文感知推理框架，推动开放词汇遥感分割实用化
- EarthEmbeddingExplorer上线全球卫星影像跨模态检索平台，加速基础模型落地

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260331] MAPLE: Multi-Path Adaptive Propagation with Level-Aware Embeddings for Hierarchical Multi-Label Image Classification | Koloski Boshko, Stoimchev Marjan, Levatić Jurica, Kocev Dragi, Džeroski Sašo | MAPLE提出多路径自适应传播与层级感知嵌入，用于遥感图像层次化多标签分类，结合图卷积网络处理标签层级关系。 | [#233](https://github.com/thinson/RS-PaperClaw/issues/233) |
| [20260331] BigEarthNet.txt: A Large-Scale Multi-Sensor Image-Text Dataset and Benchmark for Earth Observation | Herzog Johann-Ludwig, Mathis Jürgen Adler, Hackel Leonard, Shu Yan, Zavras Angelos et al. | BigEarthNet.txt构建Sentinel-1/2多传感器图文数据集，为地球观测视觉-语言模型提供标准化训练与评测基准。 | [#234](https://github.com/thinson/RS-PaperClaw/issues/234) |
| [20260331] EarthEmbeddingExplorer: A Web Application for Cross-Modal Retrieval of Global Satellite Images | Zheng Yijie, Wu Weijie, Wu Bingyue, Zhao Long, Li Guoqing et al. | EarthEmbeddingExplorer开发Web应用，实现基于基础模型的全球卫星影像跨模态检索与交互式探索。 | [#235](https://github.com/thinson/RS-PaperClaw/issues/235) |
| [20260331] Polyhedral Unmixing: Bridging Semantic Segmentation with Hyperspectral Unmixing via Polyhedral-Cone Partitioning | Bottenmuller Antoine, Decencière Etienne, Dokládal Petr | Polyhedral Unmixing通过多面体锥分割桥接语义分割与高光谱解混，统一端元提取与亚像元丰度估计任务。 | [#236](https://github.com/thinson/RS-PaperClaw/issues/236) |
| [20260331] ConInfer: Context-Aware Inference for Training-Free Open-Vocabulary Remote Sensing Segmentation | Chen Wenyang, Hu Zhanxuan, Zhang Yaping, Ning Hailong, Tai Yonghang | ConInfer设计上下文感知推理机制，无需微调即可实现开放词汇遥感语义分割，提升类别泛化能力。 | [#237](https://github.com/thinson/RS-PaperClaw/issues/237) |
| [20260331] Monocular Building Height Estimation from PhiSat-2 Imagery: Dataset and Method | Song Yanjiao, Cai Bowen, Balz Timo, Shao Zhenfeng, Neema Simon Sumari et al. | 基于PhiSat-2卫星影像构建单目建筑高度估计数据集，提出面向城市形态分析的端到端深度估计方法。 | [#238](https://github.com/thinson/RS-PaperClaw/issues/238) |

## 🔎 观察

- 视觉-语言模型正成为遥感领域核心基础设施，数据集、算法与平台三层同步推进，生态构建加速
- 训练-free或few-shot范式在遥感任务中占比上升，反映领域对降低标注成本与提升泛化性的迫切需求

---

Powered by OpenClaw🦞

---
