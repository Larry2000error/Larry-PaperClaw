# Daily Reports

最近三天日报（最新在前）：

# [20260326](./202603/20260326.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究呈现多维度技术突破：轻量化海洋语义分割、跨视角地理定位与自回归缩放、高程感知多模态推理等方向并进。神经隐式表示、量子深度学习与车机协同感知等前沿方法持续拓展遥感应用边界，体现算法效率与场景落地的双重追求。

## ✨ 今日亮点

- LEMMA提出拉普拉斯金字塔轻量架构，实现海洋环境高效边缘感知分割
- GeoHeight-Bench构建首个高程感知多模态基准，填补垂直维度推理空白
- V2U4Real发布大规模真实车机协同感知数据集，支撑空地联合3D检测

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260326] LEMMA: Laplacian pyramids for Efficient Marine SeMAntic Segmentation | Gakhar Ishaan, Srivastava Laven, Sagaram Sankarshanaa, Kasliwal Aditya, Verma Ujjwal | LEMMA利用拉普拉斯金字塔分解与轻量编码器，在海洋语义分割中平衡边缘检测精度与计算效率。 | [#203](https://github.com/thinson/RS-PaperClaw/issues/203) |
| [20260326] Just Zoom In: Cross-View Geo-Localization via Autoregressive Zooming | Yunus Talha Erzurumlu, Kwag Jiyong, Yilmaz Alper | Just Zoom In通过自回归渐进缩放机制，实现卫星图像与无人机视角的跨视图地理定位匹配。 | [#204](https://github.com/thinson/RS-PaperClaw/issues/204) |
| [20260326] GeoHeight-Bench: Towards Height-Aware Multimodal Reasoning in Remote Sensing | Hu Xuran, Xiong Zhitong, Hong Zhongcheng, Ban Yifang, Zhu Xiaoxiang et al. | GeoHeight-Bench建立高程感知多模态推理基准，评估大模型对遥感场景垂直维度的理解能力。 | [#205](https://github.com/thinson/RS-PaperClaw/issues/205) |
| [20260326] Underdetermined Blind Source Separation via Weighted Simplex Shrinkage Regularization and Quantum Deep Image Prior | Lin Chia-Hsiang, Young Si-Sheng | 该方法融合加权单纯形收缩正则化与量子深度图像先验，解决高光谱欠定盲源分离问题。 | [#206](https://github.com/thinson/RS-PaperClaw/issues/206) |
| [20260326] V2U4Real: A Real-world Large-scale Dataset for Vehicle-to-UAV Cooperative Perception | Li Weijia, Xiang Haoen, Wang Tianxu, Wu Shuaibing, Xia Qiming et al. | V2U4Real提供真实世界大规模车机协同感知数据，支持多模态3D目标检测与空地联合感知研究。 | [#207](https://github.com/thinson/RS-PaperClaw/issues/207) |
| [20260326] Robust Principal Component Completion | Wang Yinjian, Li Wei, Gui Yuanyuan, James E. Fowler, Vivone Gemine | 鲁棒主成分补全方法结合变分贝叶斯推断，实现张量数据的前景提取与稀疏恢复。 | [#208](https://github.com/thinson/RS-PaperClaw/issues/208) |
| [20260326] GeoNDC: A Queryable Neural Data Cube for Planetary-Scale Earth Observation | Qi Jianbo, Li Mengyao, Jiang Baogui, Chen Yidan, Wang Qiao | GeoNDC构建可查询神经数据立方体，以隐式神经表示支持行星尺度地球观测时空建模。 | [#209](https://github.com/thinson/RS-PaperClaw/issues/209) |

## 🔎 观察

- 神经隐式表示正从三维重建向行星尺度时空数据管理延伸，GeoNDC与GeoHeight-Bench共同指向垂直维度建模成为新焦点
- 轻量化设计与边缘感知需求驱动海洋、无人机等场景专用架构创新，LEMMA的拉普拉斯金字塔策略或成低算力部署范式

---

Powered by OpenClaw🦞

---

# [20260325](./202603/20260325.md)
## 📌 今日概况

今日共检索候选论文 9 篇；关键词+LLM 智能匹配遥感交叉论文 7 篇；最终纳入日报 7 篇。

今日遥感AI研究呈现多模态融合与可解释性并重的趋势。时序分析方面，Sentinel-2数据在农业监测与土地利用中的应用持续深化，Transformer架构及其变体（Swin、线性注意力）成为主流。高光谱成像在月球矿物制图与端元分解领域取得进展，不确定性量化和可解释AI方法受到关注。

## ✨ 今日亮点

- 多任务学习结合空间上下文提升有机/常规农田识别精度
- Aitchison几何引入贝叶斯高光谱解混实现不确定性量化
- 动态空间-光谱专家路由机制优化高光谱图像分类性能

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260325] The role of spatial context and multitask learning in the detection of organic and conventional farming systems based on Sentinel-2 time series | Hemmerling Jan, Schwieder Marcel, Rufin Philippe, Thomas Leon-Friedrich, Tulbure Mirela et al. | 利用Sentinel-2时序数据，通过空间上下文建模与多任务学习区分有机与常规农业系统。 | [#195](https://github.com/thinson/RS-PaperClaw/issues/195) |
| [20260325] Connecting Meteorite Spectra to Lunar Surface Composition Using Hyperspectral Imaging and Machine Learning | Fatemeh Fazel Hesar, Raouf Mojtaba, Chegeni Amirmohammad, Soltani Peyman, Foing Bernard et al. | 基于高光谱成像与机器学习建立陨石光谱与月球表面成分的关联映射。 | [#196](https://github.com/thinson/RS-PaperClaw/issues/196) |
| [20260325] Combi-CAM: A Novel Multi-Layer Approach for Explainable Image Geolocalization | Faget David, José Luis Lisani, Colom Miguel | 提出Combi-CAM多层可解释方法，增强卷积神经网络图像地理定位的透明度。 | [#197](https://github.com/thinson/RS-PaperClaw/issues/197) |
| [20260325] Comparative analysis of dual-form networks for live land monitoring using multi-modal satellite image time series | Dumeur Iris, Anger Jérémy, Facciolo Gabriele | 对比分析双形式网络架构，用于多模态卫星图像时序的实时土地监测。 | [#198](https://github.com/thinson/RS-PaperClaw/issues/198) |
| [20260325] LGEST: Dynamic Spatial-Spectral Expert Routing for Hyperspectral Image Classification | Wen Jiawen, Qiu Suixuan, Luo Zihang, Yang Xiaofei, Shi Haotian | 设计动态空间-光谱专家路由机制LGEST，提升高光谱图像分类效率与精度。 | [#199](https://github.com/thinson/RS-PaperClaw/issues/199) |
| [20260325] DB SwinT: A Dual-Branch Swin Transformer Network for Road Extraction in Optical Remote Sensing Imagery | He Zongyang, Yang Xiangli, Gao Xian, Wang Zhiguo | 构建双分支Swin Transformer网络DB SwinT，优化光学遥感影像道路提取任务。 | [#200](https://github.com/thinson/RS-PaperClaw/issues/200) |
| [20260325] Aitchison Geometry on the Simplex for Uncertainty Quantification in Bayesian Hyperspectral Image Unmixing | Blondel Hector, Drumetz Lucas, Chonavel Thierry | 将Aitchison单形几何引入贝叶斯框架，实现高光谱图像解混的不确定性量化。 | [#201](https://github.com/thinson/RS-PaperClaw/issues/201) |

## 🔎 观察

- Transformer架构持续主导遥感时序与空间建模，但线性注意力等效率优化方案开始涌现
- 可解释AI与不确定性量化方法逐步从辅助工具转向核心研究议题，反映领域对模型可信度的需求提升

---

Powered by OpenClaw🦞

---

# [20260324](./202603/20260324.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多技术路线并进态势：基础模型层面探索模型权重融合而非数据驱动学习；应用层面覆盖光伏设施普查、雪崩灾害监测等垂直场景；方法层面持续深化对比学习、LSTM时序建模与不确定性量化等核心技术。

## ✨ 今日亮点

- GeoSANE开创性地从神经网络权重空间学习地理表征，突破传统数据驱动范式
- 检索增强生成技术首次应用于卫星影像光伏设施清单估算，支撑配电网规划
- SAR影像深度学习变化检测实现大规模雪崩制图，拓展灾害遥感监测能力

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260324] GeoSANE: Learning Geospatial Representations from Models, Not Data | Hanna Joelle, Falk Damian, Stella X. Yu, Borth Damian | GeoSANE提出从模型权重而非原始数据学习地理空间表征的新范式，为地理基础模型训练开辟替代路径。 | [#188](https://github.com/thinson/RS-PaperClaw/issues/188) |
| [20260324] Dual Contrastive Network for Few-Shot Remote Sensing Image Scene Classification | Ji Zhong, Hou Liyuan, Wang Xuan, Wang Gang, Pang Yanwei | 双对比网络通过全局-局部特征协同对比学习，提升小样本遥感场景分类的泛化性能。 | [#189](https://github.com/thinson/RS-PaperClaw/issues/189) |
| [20260324] Retrieval-Guided Photovoltaic Inventory Estimation from Satellite Imagery for Distribution Grid Planning | Guo Muhao, Mai Lihao, Blasch Erik, Parol Jafarali, Rakan Turki et al. | 检索增强生成框架结合卫星影像与外部知识库，实现分布式光伏设施的精准清估算。 | [#190](https://github.com/thinson/RS-PaperClaw/issues/190) |
| [20260324] L-UNet: An LSTM Network for Remote Sensing Image Change Detection | Sun Shuting, Mu Lin, Wang Lizhe, Liu Peng | L-UNet将LSTM嵌入UNet架构，强化遥感影像变化检测的时序特征建模能力。 | [#191](https://github.com/thinson/RS-PaperClaw/issues/191) |
| [20260324] Predictive Photometric Uncertainty in Gaussian Splatting for Novel View Synthesis | Chamuditha Jayanga Galappaththige, Gottwald Thomas, Stehr Peter, Heinert Edgar, Suenderhauf Niko et al. | 高斯溅射光度不确定性预测方法，为神经辐射场新视角合成提供可靠性量化。 | [#192](https://github.com/thinson/RS-PaperClaw/issues/192) |
| [20260324] Large-Scale Avalanche Mapping from SAR Images with Deep Learning-based Change Detection | Gatti Mattia, Mariani Alberto, Gallo Ignazio, Monti Fabiano | 基于SAR影像与深度学习的多时相变化检测，实现山区大范围雪崩事件的自动化制图。 | [#193](https://github.com/thinson/RS-PaperClaw/issues/193) |

## 🔎 观察

- 模型权重空间学习（GeoSANE）代表基础模型训练的新方向，可能降低对海量标注数据的依赖
- 检索增强生成与遥感结合尚处早期，光伏设施估算案例显示其在结构化知识融合方面的潜力

---

Powered by OpenClaw🦞

---
