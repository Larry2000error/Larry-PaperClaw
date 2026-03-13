# Daily Reports

最近三天日报（最新在前）：

# [20260312](./202603/20260312.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 4 篇；最终纳入日报 4 篇。

今日遥感AI研究呈现基础模型与语义通信双轨并进态势。SAR领域推出十亿级参数基础模型CrossEarth-SAR，探索Mixture-of-Experts架构的领域泛化能力；视觉语言模型引入OpenStreetMap地理信息辅助领域适应；多标签分类结合层次标签建模与图神经网络提升精度。语义通信方向，LEO卫星地球观测任务中联合JSCC与资源分配优化QoS，反映遥感数据链路端到端智能化趋势。

## ✨ 今日亮点

- CrossEarth-SAR构建十亿级SAR基础模型，融合MoE实现跨域语义分割泛化
- LEO卫星EO任务引入语义通信，JSCC与资源分配联合优化QoS
- 遥感VLMs结合OpenStreetMap地理信息突破领域适应瓶颈

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260312] CrossEarth-SAR: A SAR-Centric and Billion-Scale Geospatial Foundation Model for Domain Generalizable Semantic Segmentation | Ye Ziqi, Gong Ziyang, Liao Ning, Hu Xiaoxing, Wang Di et al. | CrossEarth-SAR提出以SAR为中心的十亿级地理空间基础模型，采用Mixture-of-Experts实现领域可泛化语义分割 | [#58](https://github.com/thinson/RS-PaperClaw/issues/58) |
| [20260312] A Joint JSCC-Resource Allocation Framework for QoS-Aware Semantic Communication in LEO Satellite-based EO Missions | Nguyen-Kha Hung, Ti Ti Nguyen, Vu Nguyen Ha, Lagunas Eva, Chatzinotas Symeon et al. | 联合JSCC与资源分配框架优化LEO卫星地球观测任务中的语义通信质量，满足QoS需求 | [#59](https://github.com/thinson/RS-PaperClaw/issues/59) |
| [20260312] OSM-based Domain Adaptation for Remote Sensing VLMs | Stefan Maria Ailuro, Markov Mario, Mahdi Mohammad, Boychev Delyan, Luc Van Gool et al. | OSM-based方法利用OpenStreetMap数据辅助遥感视觉语言模型进行领域适应，提升跨域性能 | [#60](https://github.com/thinson/RS-PaperClaw/issues/60) |
| [20260312] HELM: Hierarchical and Explicit Label Modeling with Graph Learning for Multi-Label Image Classification | Stoimchev Marjan, Koloski Boshko, Levatić Jurica, Kocev Dragi, Džeroski Sašo | HELM通过层次化显式标签建模与图学习结合，提升多标签遥感图像分类效果 | [#61](https://github.com/thinson/RS-PaperClaw/issues/61) |

## 🔎 观察

- 遥感基础模型向十亿级参数与领域泛化演进，SAR数据处理能力显著提升但部署成本挑战增大
- 语义通信从传统传输向语义层优化转型，LEO星座场景下的端到端联合设计成为新增长点

---

Powered by OpenClaw🦞

---

# [20260311](./202603/20260311.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 0 篇。

当日未检索到符合条件并纳入日报的论文。

## ✨ 今日亮点

- 当日暂无新增亮点。

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| - | - | 当日无纳入论文 | - |

## 🔎 观察

- 当日暂无可统计的论文样本，建议次日继续观察趋势变化。
- 统计口径已统一为候选数、LLM匹配数与纳入数三项。

---

Powered by OpenClaw🦞

---

# [20260310](./202603/20260310.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 15 篇；最终纳入日报 15 篇。

今日遥感研究聚焦于视觉语言模型与多模态融合。SIGMAE提出光谱指数引导的多光谱基础模型，GeoAlignCLIP和GeoSolver分别从细粒度对齐和推理过程监督提升VLMs在遥感任务上的表现。CarbonBench建立碳通量零样本学习的全球基准，BuildMamba将状态空间模型引入建筑分割与高度估计，OmniEarth提供遥感VLMs综合评测基准。

## ✨ 今日亮点

- SIGMAE利用光谱指数引导的MAE框架构建多光谱遥感基础模型，提升下游任务迁移能力
- GeoSolver引入细粒度过程监督强化遥感VLMs的推理能力，实现测试时链式思考
- CarbonBench发布碳通量零样本学习全球基准，推动遥感在全球碳循环估算中的应用

## 🗂 今日文章列表

| 标题 | 作者 | 一句话概括 | Issue |
|---|---|---|---|
| [20260310] BuildMamba: A Visual State-Space Based Model for Multi-Task Building Segmentation and Height Estimation from Satellite Images | Sinan U. Ulu, A. Enes Doruk, I. Can Yagmur, Bahadir K. Gunturk, Oguz Hanoglu, Hasan F. Ates | BuildMamba将状态空间模型Mamba应用于卫星图像建筑分割与高度估计多任务学习。 | [#3](https://github.com/thinson/RS-PaperClaw/issues/3) |
| [20260310] SIGMAE: A Spectral-Index-Guided Foundation Model for Multispectral Remote Sensing | Xiaokang Zhang, Bo Li, Chufeng Zhou et al. | SIGMAE提出光谱指数引导的多光谱遥感MAE基础模型，融合光谱信息提升特征表示。 | [#4](https://github.com/thinson/RS-PaperClaw/issues/4) |
| [20260310] CarbonBench: A Global Benchmark for Upscaling of Carbon Fluxes Using Zero-Shot Learning | Rozanov Aleksei, Renganathan Arvind, Zhang Yimeng, Kumar Vipin | CarbonBench发布碳通量零样本学习与空间迁移的全球基准数据集与评测方法。 | [#24](https://github.com/thinson/RS-PaperClaw/issues/24) |
| [20260310] TIMID: Time-Dependent Mistake Detection in Videos of Robot Executions | Gallego Nerea, Salanova Fernando, Mannarano Claudio, Mahulea Cristian, Montijano Eduardo | 聚焦Video Anomaly Detection、Robot Execution，给出可复现的模型与评测方案。 | [#25](https://github.com/thinson/RS-PaperClaw/issues/25) |
| [20260310] CLIOPATRA: Extracting Private Information from LLM Insights | Meenatchi Sundaram Muthu Selva Annamalai, Emiliano De Cristofaro, Kairouz Peter | 聚焦Privacy Attack、LLM Security，给出可复现的模型与评测方案。 | [#26](https://github.com/thinson/RS-PaperClaw/issues/26) |
| [20260310] Well Log-Guided Synthesis of Subsurface Images from Sparse Petrography Data Using cGANs | Sadeghkhani Ali, Assadi A., Bennett B., Rabbani A. | 研究利用cGANs结合测井数据合成稀疏岩相数据的地下孔隙图像。 | [#27](https://github.com/thinson/RS-PaperClaw/issues/27) |
| [20260310] PRECEPT: Planning Resilience via Experience, Context Engineering &amp; Probing Trajectories A Unified Framework for Test-Time Adaptation with Compositional Rule Learning and Pareto-Guided Prompt Evolution | Shahmansoori Arash | 聚焦遥感AI方法，给出可复现的模型与评测方案。 | [#28](https://github.com/thinson/RS-PaperClaw/issues/28) |
| [20260310] Grounding Synthetic Data Generation With Vision and Language Models | Ümit Mert Çağlar, Temizel Alptekin | 提出基于视觉语言模型的遥感合成数据生成方法，增强语义分割数据增广。 | [#29](https://github.com/thinson/RS-PaperClaw/issues/29) |
| [20260310] GeoAlignCLIP: Enhancing Fine-Grained Vision-Language Alignment in Remote Sensing via Multi-Granular Consistency Learning | Yang Xiao, Fu Ronghao, Duan Zhuoran, Lin Zhiwen, Liu Xueyan et al. | GeoAlignCLIP通过多粒度一致性学习提升遥感图像与文本的细粒度对齐。 | [#30](https://github.com/thinson/RS-PaperClaw/issues/30) |
| [20260310] GeoSolver: Scaling Test-Time Reasoning in Remote Sensing with Fine-Grained Process Supervision | Sun Lang, Fu Ronghao, Duan Zhuoran, Liu Haoran, Liu Xueyan et al. | GeoSolver引入过程监督与强化学习实现遥感VLMs的细粒度推理能力。 | [#31](https://github.com/thinson/RS-PaperClaw/issues/31) |
| [20260310] RESBev: Making BEV Perception More Robust | Zhuo Lifeng, Jin Kefan, Liu Zhe, Wang Hesheng | 聚焦BEV Perception、Autonomous Driving，给出可复现的模型与评测方案。 | [#32](https://github.com/thinson/RS-PaperClaw/issues/32) |
| [20260310] Probing the Reliability of Driving VLMs: From Inconsistent Responses to Grounded Temporal Reasoning | Chang Chun-Peng, Wang Chen-Yu, Caesar Holger, Pagani Alain | 聚焦Vision-Language Models、Autonomous Driving，给出可复现的模型与评测方案。 | [#33](https://github.com/thinson/RS-PaperClaw/issues/33) |
| [20260310] Component-Aware Sketch-to-Image Generation Using Self-Attention Encoding and Coordinate-Preserving Fusion | Zia Ali, Muhammad Umer Ramzan, Ali Usman, Faheem Muhammad, Khamis Abdelwahed et al. | 聚焦Sketch-to-Image Generation、Self-Attention，给出可复现的模型与评测方案。 | [#34](https://github.com/thinson/RS-PaperClaw/issues/34) |
| [20260310] Telogenesis: Goal Is All U Need | Deng Zhuoran, Zhang Yizhi, Zhang Ziyi, Shen Wan | 聚焦Goal Conditioning、Attention Allocation，给出可复现的模型与评测方案。 | [#35](https://github.com/thinson/RS-PaperClaw/issues/35) |
| [20260310] OmniEarth: A Benchmark for Evaluating Vision-Language Models in Geospatial Tasks | Fu Ronghao, Liu Haoran, Zhang Weijie, Lin Zhiwen, Yang Xiao et al. | OmniEarth发布遥感视觉语言模型综合评测基准，覆盖多模态地理空间任务。 | [#36](https://github.com/thinson/RS-PaperClaw/issues/36) |

## 🔎 观察

- 视觉语言模型正成为遥感领域研究热点，多篇论文从不同角度提升VLMs在遥感场景下的细粒度理解与推理能力。
- 基础模型与基准数据集的构建持续推进，MAE框架与多光谱融合成为遥感预训练新方向。

---

Powered by OpenClaw🦞

---
