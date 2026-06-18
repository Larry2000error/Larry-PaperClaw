# Daily Reports

最近三天日报（最新在前）：

# [20260610](./202606/20260610.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感AI研究聚焦跨模态检索与重识别技术，涵盖法医图像、昼夜场景、可见光-红外及换装场景等复杂应用。低秩结构学习与提示学习成为主流技术路线，多专家网络与正交子空间方法受到关注，显示领域对鲁棒特征表示的持续探索。

## ✨ 今日亮点

- 跨域重识别研究活跃，昼夜场景与换装问题各有一篇工作
- 低秩结构学习成为热点，两篇论文分别应用于组合检索与换装重识别
- 多专家网络架构首次引入可见光-红外行人重识别任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260610] Bridging the Modality Gap in Forensic Image Retrieval | González-Gazapo Ricardo, Morales-González Annette, Martínez-Díaz Yoanna, Méndez-Vázquez Heydi, García-Borroto Milton | Advanced Technologies Application Center (CENATAV)；Centro de Sistemas Complejos, Facultad de Física, Universidad de La Habana | 提出跨模态法医图像检索框架，整合纹身与素描检索任务，探索大语言模型在取证场景的应用潜力。 | [#261](https://github.com/Larry2000error/Larry-PaperClaw/issues/261) |
| [20260610] Bridging Day and Night: Unsupervised Cross-Domain Re-Identification with Synergistic Prompt and Prototype Learning | Xu Jiyang, Liu Rui, Dai Hang | School of Computer Science, Wuhan University | 设计协同提示与原型学习机制，实现无监督昼夜跨域行人重识别，缓解域间分布差异。 | [#262](https://github.com/Larry2000error/Larry-PaperClaw/issues/262) |
| [20260610] MFEN:Multi-Frequency Expert Network for Visible-Infrared Person Re-ID | Li Xulin, Lu Yan, Liu Bin, Yang Qinhong, Chu Qi, Gong Tao, Yu Nenghai | University of Science and Technology of China；Anhui Province Key Laboratory of Digital Security；The Chinese University of Hong Kong | 构建多频率专家网络，通过频域学习与混合专家架构，有效缩小可见光-红外模态差异。 | [#263](https://github.com/Larry2000error/Larry-PaperClaw/issues/263) |
| [20260610] RankVR: Low-Rank Structure Perception and Value Recalibration for Robust Composed Image Retrieval | Huang Jiale, Li Zixu, Fu Zhiheng, Chen Zhiwei, Huang Qinlei, Hu Yupeng | Shandong University | 提出低秩结构感知与价值重校准方法，增强组合图像检索的全局结构一致性与噪声鲁棒性。 | [#264](https://github.com/Larry2000error/Larry-PaperClaw/issues/264) |
| [20260610] Learning Instance-Adaptive Low-Rank Orthogonal Subspaces for Clothes-Changing Person Re-Identification | Kim Dong-Woo, Kim Tae-Kyun | Imperial College London | 学习实例自适应低秩正交子空间，利用视觉-语言模型解决换装场景下行人重识别的表观变化难题。 | [#265](https://github.com/Larry2000error/Larry-PaperClaw/issues/265) |

## 🔎 观察

- 低秩表示学习成为本日最突出技术趋势，在检索与重识别两类任务中均获应用，反映领域对高效降维表征的共识
- 视觉-语言模型向 specialized 下游任务渗透加速，提示学习与原型学习结合成为跨域迁移的标准范式

---

Powered by OpenClaw🦞

---

# [20260608](./202606/20260608.md)
## 📌 今日概况

今日共检索候选论文 5 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 3 篇。

今日研究聚焦视觉-语言模型在遥感与地理空间任务中的创新应用。三项工作分别探索零样本语义重识别、多模态生成式检索优化及全球图像地理定位，体现大模型时代下语义理解与空间推理的深度融合趋势。

## ✨ 今日亮点

- VLM首次用于自动驾驶零样本语义重识别，突破传统监督学习局限
- 提出前缀保留优化策略，显著缩小多模态生成检索的索引-解码差距
- 结合位置注意力机制与大模型，实现全球范围图像地理定位

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260608] Zero-Shot Semantic Re-Identification for Autonomous Driving: A VLM Baseline Study | Borges Eduardo, Abreu Manuel, Garrote Luís, Urbano J. Nunes | Institute of Systems and Robotics, University of Coimbra | 提出VLM基线方法，通过语义匹配实现自动驾驶场景零样本行人车辆重识别。 | [#256](https://github.com/Larry2000error/Larry-PaperClaw/issues/256) |
| [20260608] Closing the Indexing-Decoding Gap in Multimodal Generative Retrieval via Prefix Retention Optimization | Chen Yufei, Wang Zihan, Tang Yubao, Zhao Yukun, Maarten de Rijke, Ren Zhaochun | Shandong University；CISPA Helmholtz Center for Information Security；University of Amsterdam；Leiden University | 针对多模态生成检索，设计前缀保留优化机制改进残差量化与束搜索过程。 | [#257](https://github.com/Larry2000error/Larry-PaperClaw/issues/257) |
| [20260608] When Vision Misleads, Let Location Speak: A Worldwide Image Geo-Localization Method via Location Attention Mechanism and Large Multimodal Models | Cui Junchao, Shi Wenqi, Ma Xuanzi, Wu Nan, Du Shaoyong, Luo Xiangyang | Institution unavailable | 构建位置注意力机制，融合CLIP与大模型解决视觉歧义下的全球图像地理定位。 | [#258](https://github.com/Larry2000error/Larry-PaperClaw/issues/258) |

## 🔎 观察

- 地理定位任务正从纯视觉判别转向视觉-地理语义联合推理，位置编码成为关键创新点
- 生成式检索的瓶颈已从表征学习转向索引-解码协同优化，量化策略研究价值凸显

---

Powered by OpenClaw🦞

---

# [20260606](./202606/20260606.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 2 篇；最终纳入日报 2 篇。

今日遥感AI研究呈现跨模态智能与时空图神经网络两大主线。GeoGNN聚焦时序地理定位，通过双塔图神经网络融合时空表征；IMAGINE则探索自适应图式-意象增强的组合视频检索，推动跨模态语义对齐技术发展。

## ✨ 今日亮点

- GeoGNN提出双塔图神经网络架构，实现时序数据与地理空间的联合嵌入学习
- IMAGINE创新引入图式-意象增强机制，提升组合视频检索的语义理解能力
- 两研究分别来自Emory-橡树岭-南加大联盟与山东大学团队，体现产学研协同

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260606] GeoGNN: Time Series Geo-Localization using Two-Tower Graph Neural Networks | Tran Toan, Abebe Waqwoya, Potnis Abhishek, Chinthavali Supriya, Shahabi Cyrus, Xiong Li, Lunga Dalton | Emory University；Oak Ridge National Laboratory；University of Southern California | GeoGNN构建双塔图神经网络，联合学习时序数据的空间嵌入与时间表示，用于精确地理定位任务。 | [#253](https://github.com/Larry2000error/Larry-PaperClaw/issues/253) |
| [20260606] IMAGINE: Adaptive Schema-Imagery Enhanced Composition for Composed Video Retrieval | Huang Jiale, Li Zixu, Chen Zhiwei, Fu Zhiheng, Wang Chunxiao, Hu Yupeng | Shandong University；Qilu University of Technology (Shandong Academy of Sciences) | IMAGINE提出自适应图式-意象增强组合框架，通过多模态原型学习实现复杂视频语义检索。 | [#254](https://github.com/Larry2000error/Larry-PaperClaw/issues/254) |

## 🔎 观察

- 图神经网络正成为遥感时空建模的核心工具，双塔架构设计或成地理定位新范式
- 跨模态检索从简单对齐迈向深层语义组合，图式认知理论的引入值得关注

---

Powered by OpenClaw🦞

---
